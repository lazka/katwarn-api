# SPDX-License-Identifier: MIT

import json
from urllib.parse import quote

from .utils import Service


def dump_all() -> dict[str, str]:
    """Dump all data from the API to an URL -> JSON mapping"""

    results = {}

    def dump(service: Service, url: str):
        print(f"GET {url}")
        r = service.get(url)
        if r.status_code == 404:
            print(f"{url} not found")
            return None
        r.raise_for_status()
        result = r.json()
        # re-dump to ensure consistent formatting/ordering
        results[url] = json.dumps(result, ensure_ascii=False, sort_keys=True)
        return result

    service = Service.create("servicearea")
    for entry in dump(service, f"{service.url}/service_areas")["index"]:
        provider_id = entry["provider_id"]
        dump(service, f"{service.url}/service_areas/{quote(provider_id)}")
        infos = dump(service, f"{service.url}/service_areas/{quote(provider_id)}/infos")
        for entry in infos["infos"]:
            entry_id = entry["id"]
            dump(service, f"{service.url}/service_areas/infos/{quote(entry_id)}")

    service = Service.create("content")
    for entry in dump(service, f"{service.url}/incidents")["incidents"]:
        incident_id = entry["id"]
        incident = dump(service, f"{service.url}/incidents/{quote(incident_id)}")
        if incident is None:
            continue
        for alert_id in incident["alerts"]:
            dump(
                service,
                f"{service.url}/incidents/{quote(incident_id)}/{quote(alert_id)}",
            )

    service = Service.create("content")
    for topic_id in dump(service, f"{service.url}/topics")["topics"]:
        dump(service, f"{service.url}/topics/{quote(topic_id)}/description")
        topic = dump(service, f"{service.url}/topics/{quote(topic_id)}")
        for incident in topic["incidents"]:
            for alert in incident["alerts"]:
                dump(
                    service,
                    f"{service.url}/incidents/{quote(incident['id'])}/{quote(alert)}",
                )

    return results
