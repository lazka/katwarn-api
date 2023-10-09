# SPDX-License-Identifier: MIT

from urllib.parse import quote

from .models import (Alert, Incident, Incidents, ServiceArea, ServiceAreaInfos,
                     ServiceAreas, Topic, TopicAlert, TopicDescription, Topics)
from .utils import Service


class KatWarnApi:
    def get_incident(self, incident_id: str) -> Incident:
        service = Service.create("content")
        r = service.get(f"{service.url}/incidents/{quote(incident_id)}")
        r.raise_for_status()
        return Incident.parse_raw(r.content)

    def get_alert(self, incident_id: str, alert_id: str) -> Alert:
        service = Service.create("content")
        r = service.get(
            f"{service.url}/incidents/{quote(incident_id)}/{quote(alert_id)}"
        )
        r.raise_for_status()
        return Alert.parse_raw(r.content)

    def get_topic_alert(self, incident_id: str, alert_id: str) -> TopicAlert:
        service = Service.create("content")
        r = service.get(
            f"{service.url}/incidents/{quote(incident_id)}/{quote(alert_id)}"
        )
        r.raise_for_status()
        return TopicAlert.parse_raw(r.content)

    def get_topics(self) -> Topics:
        service = Service.create("content")
        r = service.get(f"{service.url}/topics")
        r.raise_for_status()
        return Topics.parse_raw(r.content)

    def get_topic(self, topic_id: str) -> Topic:
        service = Service.create("content")
        r = service.get(f"{service.url}/topics/{quote(topic_id)}")
        r.raise_for_status()
        return Topic.parse_raw(r.content)

    def get_topic_description(self, topic_id: str) -> TopicDescription:
        service = Service.create("content")
        r = service.get(f"{service.url}/topics/{quote(topic_id)}/description")
        r.raise_for_status()
        return TopicDescription.parse_raw(r.content)

    def get_incidents(self) -> Incidents:
        service = Service.create("content")
        r = service.get(f"{service.url}/incidents")
        r.raise_for_status()
        return Incidents.parse_raw(r.content)

    def get_service_areas(self) -> ServiceAreas:
        service = Service.create("servicearea")
        r = service.get(f"{service.url}/service_areas")
        r.raise_for_status()
        return ServiceAreas.parse_raw(r.content)

    def get_service_area(self, provider_id: str) -> ServiceArea:
        service = Service.create("servicearea")
        r = service.get(f"{service.url}/service_areas/{quote(provider_id)}")
        r.raise_for_status()
        return ServiceArea.parse_raw(r.content)

    def get_service_area_infos(self, provider_id: str) -> ServiceAreaInfos:
        service = Service.create("servicearea")
        r = service.get(f"{service.url}/service_areas/{quote(provider_id)}/infos")
        r.raise_for_status()
        return ServiceAreaInfos.parse_raw(r.content)

    def get_service_area_info(self, info_id) -> dict:
        # I've never seen this one in the wild, so I don't know what it looks like
        service = Service.create("servicearea")
        r = service.get(f"{service.url}/service_areas/infos/{quote(info_id)}")
        r.raise_for_status()
        return r.json()
