from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.incident_event_service_status import IncidentEventServiceStatus, check_incident_event_service_status

T = TypeVar("T", bound="IncidentEventService")


@_attrs_define
class IncidentEventService:
    """
    Attributes:
        incident_event_id (str): The ID of the incident event.
        service_id (str): The ID of the service.
        status (IncidentEventServiceStatus): The status of the affected service
    """

    incident_event_id: str
    service_id: str
    status: IncidentEventServiceStatus

    def to_dict(self) -> dict[str, Any]:
        incident_event_id = self.incident_event_id

        service_id = self.service_id

        status: str = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "incident_event_id": incident_event_id,
                "service_id": service_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        incident_event_id = d.pop("incident_event_id")

        service_id = d.pop("service_id")

        status = check_incident_event_service_status(d.pop("status"))

        incident_event_service = cls(
            incident_event_id=incident_event_id,
            service_id=service_id,
            status=status,
        )

        return incident_event_service
