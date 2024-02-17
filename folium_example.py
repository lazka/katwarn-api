#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

import argparse

import folium
from requests import HTTPError

from katwarn_api import KatWarnApi


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
    args = parser.parse_args()

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
            alert

            def style_function(x):
                return {"color": "red"}

            folium.GeoJson(
                alert.geometry,
                name=alert.headline,
                tooltip=alert.headline,
                style_function=style_function,
            ).add_to(alert_map)

    folium.LayerControl().add_to(map)
    map.fit_bounds(get_bounds())
    map.save(args.output)


if __name__ == "__main__":
    main()
