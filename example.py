#!/usr/bin/env python3
# SPDX-License-Identifier: MIT

from katwarn_api import KatWarnApi


def main():
    api = KatWarnApi()

    # All alerts
    print("=== All alerts ===")
    for entry in api.get_incidents().incidents:
        incident = api.get_incident(entry.id)
        for alert_id in incident.alerts:
            alert = api.get_alert(incident.id, alert_id)
            print(f"{entry.provider_id}: [{alert.event_code.value}] {alert.headline}")

    # All service areas
    print("=== All service areas ===")
    for entry in api.get_service_areas().index:
        service_area = api.get_service_area(entry.provider_id)
        props = api.get_service_area_properties(service_area)
        print(f"{entry.provider_id}: {props.longhand}")
        for key, obj_props in api.get_service_area_objects(service_area).items():
            print(f"  - [{key}] {obj_props.longhand}")

    # All alerts for topics
    print("=== All alerts for topics ===")
    for topic_id in api.get_topics().topics:
        description = api.get_topic_description(topic_id)
        print(f"{description.provider_id}: {description.sublabel}")
        topic = api.get_topic(topic_id)
        for incident in topic.incidents:
            for alert_id in incident.alerts:
                alert = api.get_topic_alert(incident.id, alert_id)
                print(f"  - [{alert.event_code.value}] {alert.headline}")


if __name__ == "__main__":
    main()
