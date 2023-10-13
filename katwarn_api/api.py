# SPDX-License-Identifier: MIT

from urllib.parse import quote

from .models import (Alert, Incident, Incidents, ServiceArea, ServiceAreaInfo,
                     ServiceAreaInfos, ServiceAreaObjectProperties,
                     ServiceAreaProperties, ServiceAreas, Topic, TopicAlert,
                     TopicDescription, Topics)
from .utils import Service


class KatWarnApi:
    def get_incident(self, incident_id: str) -> Incident:
        service = Service.create("content")
        r = service.get(f"{service.url}/incidents/{quote(incident_id)}")
        r.raise_for_status()
        return Incident.model_validate_json(r.content)

    def get_alert(self, incident_id: str, alert_id: str) -> Alert:
        service = Service.create("content")
        r = service.get(
            f"{service.url}/incidents/{quote(incident_id)}/{quote(alert_id)}"
        )
        r.raise_for_status()
        return Alert.model_validate_json(r.content)

    def get_topic_alert(self, incident_id: str, alert_id: str) -> TopicAlert:
        service = Service.create("content")
        r = service.get(
            f"{service.url}/incidents/{quote(incident_id)}/{quote(alert_id)}"
        )
        r.raise_for_status()
        return TopicAlert.model_validate_json(r.content)

    def get_topics(self) -> Topics:
        service = Service.create("content")
        r = service.get(f"{service.url}/topics")
        r.raise_for_status()
        return Topics.model_validate_json(r.content)

    def get_topic(self, topic_id: str) -> Topic:
        service = Service.create("content")
        r = service.get(f"{service.url}/topics/{quote(topic_id)}")
        r.raise_for_status()
        return Topic.model_validate_json(r.content)

    def get_topic_description(self, topic_id: str) -> TopicDescription:
        service = Service.create("content")
        r = service.get(f"{service.url}/topics/{quote(topic_id)}/description")
        r.raise_for_status()
        return TopicDescription.model_validate_json(r.content)

    def get_incidents(self) -> Incidents:
        service = Service.create("content")
        r = service.get(f"{service.url}/incidents")
        r.raise_for_status()
        return Incidents.model_validate_json(r.content)

    def get_service_areas(self) -> ServiceAreas:
        service = Service.create("servicearea")
        r = service.get(f"{service.url}/service_areas")
        r.raise_for_status()
        return ServiceAreas.model_validate_json(r.content)

    def get_service_area(self, provider_id: str) -> ServiceArea:
        service = Service.create("servicearea")
        r = service.get(f"{service.url}/service_areas/{quote(provider_id)}")
        r.raise_for_status()
        return ServiceArea.model_validate_json(r.content)

    def get_service_area_properties(
        self, service_area: ServiceArea
    ) -> ServiceAreaProperties:
        return ServiceAreaProperties.parse_obj(service_area.service_area["properties"])

    def get_service_area_objects(
        self, service_area: ServiceArea
    ) -> dict[str, ServiceAreaObjectProperties]:
        objects = service_area.service_area["objects"]
        results = {}
        for key, obj in objects.items():
            results[key] = ServiceAreaObjectProperties.parse_obj(obj["properties"])
        return results

    def get_service_area_infos(self, provider_id: str) -> ServiceAreaInfos:
        service = Service.create("servicearea")
        r = service.get(f"{service.url}/service_areas/{quote(provider_id)}/infos")
        r.raise_for_status()
        return ServiceAreaInfos.model_validate_json(r.content)

    def get_service_area_info(self, info_id) -> ServiceAreaInfo:
        # I've never seen this one in the wild, so I don't know what it looks like
        service = Service.create("servicearea")
        r = service.get(f"{service.url}/service_areas/infos/{quote(info_id)}")
        r.raise_for_status()
        return ServiceAreaInfo.model_validate_json(r.content)
