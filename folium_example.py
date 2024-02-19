#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

import argparse
import json

import folium
from requests import HTTPError
import requests_mock
from jinja2 import Template

from katwarn_api import KatWarnApi


def mock_requests(dump_path: str) -> None:

    with open(dump_path, "r") as f:
        dump = json.load(f)

    def text_callback(request, context):
        if request.url in dump:
            context.status_code = 200
            return dump[request.url]
        else:
            context.status_code = 404
            return ""

    import re
    adapter = requests_mock.Adapter()
    adapter.register_uri('GET', re.compile('.*'), text=text_callback)
    mocker = requests_mock.Mocker(adapter=adapter)
    mocker.start()


def main():
    parser = argparse.ArgumentParser(description="Create a map with Folium")
    parser.add_argument(
        "-o",
        "--output",
        metavar="PATH",
        type=str,
        default="map.html",
        help="Output file",
    )
    parser.add_argument(
        "-d",
        "--from-dump",
        metavar="PATH",
        type=str,
        help="Load data from dump instead of the web API",
    )
    args = parser.parse_args()

    if args.from_dump is not None:
        mock_requests(args.from_dump)

    api = KatWarnApi()
    map = folium.Map()
    boxes = []

    def get_bounds():
        ymin = min([b.ymin for b in boxes])
        ymax = max([b.ymax for b in boxes])
        xmin = min([b.xmin for b in boxes])
        xmax = max([b.xmax for b in boxes])
        return [(ymin, xmax), (ymax, xmin)]

    for entry in api.get_service_areas().index:
        boxes.append(entry.bbox)
        service_area = api.get_service_area(entry.provider_id)

        service_area_map = folium.FeatureGroup(
            name=f"Service Area: {entry.provider_id}"
        )
        service_area_map.add_to(map)

        def fixup_topo_json_for_folium(topo_json: dict):
            # Folium only supports TopoJSON with GeometryCollection, so hack it together
            # https://github.com/python-visualization/folium/issues/1816
            for key in topo_json["objects"].keys():
                orig = topo_json["objects"][key]
                new = {"type": "GeometryCollection", "geometries": [orig]}
                topo_json["objects"][key] = new

        topo_json = service_area.service_area
        fixup_topo_json_for_folium(topo_json)
        for key in topo_json["objects"].keys():
            tooltip = folium.GeoJsonTooltip(fields=["longhand"], aliases=["Name"])
            folium.TopoJson(
                topo_json, "objects." + key, tooltip=tooltip, name=key
            ).add_to(service_area_map)

    alert_map = folium.FeatureGroup(name="Alerts")
    alert_map.add_to(map)
    map.keep_in_front(alert_map)

    for entry in api.get_incidents().incidents:
        try:
            incident = api.get_incident(entry.id)
        except HTTPError as e:
            if e.response.status_code == 404:
                # XXX: some incidents are broken
                continue
            raise
        boxes.append(incident.bbox)
        for alert_id in incident.alerts:
            alert = api.get_alert(incident.id, alert_id)

            def style_function(x, alert=alert):
                if alert.severity == 'minor':
                    return {"color": "#edd400"}
                elif alert.severity == 'moderate':
                    return {"color": "#f57900"}
                elif alert.severity == 'severe':
                    return {"color": "#cc0000"}
                elif alert.severity == 'extreme':
                    return {"color": "#a40000"}
                else:
                    return {}

            def highlight_function(x):
                return {"weight": 5, "color": "#333"}

            template = Template("""
<div style="width: 85vw; max-width: 500px">
    <h4>{{ alert.headline }}</h4>
    <dl>
        <dt>Beschreibung</dt>
        <dd>{{ alert.description }}</dd>
        <dt>Schwere</dt>
        <dd>{{ alert.severity.value }}</dd>
        {% if alert.web %}
            <dt>Web</dt>
            <dd><a href="{{ alert.web }}" target="_blank">{{ alert.web }}</a></dd>
        {% endif %}
    </dl>
</div>
            """)
            popup = folium.Popup(template.render(alert=alert))
            folium.GeoJson(
                alert.geometry,
                name=alert.headline,
                tooltip=alert.headline,
                popup=popup,
                highlight_function=highlight_function,
                style_function=style_function,
            ).add_to(alert_map)

    folium.LayerControl().add_to(map)
    map.fit_bounds(get_bounds())
    map.save(args.output)


if __name__ == "__main__":
    main()
