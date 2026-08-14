from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_incident_event_service_data_attributes_status import (
    NewIncidentEventServiceDataAttributesStatus,
    check_new_incident_event_service_data_attributes_status,
)

T = TypeVar("T", bound="NewIncidentEventServiceDataAttributes")


@_attrs_define
class NewIncidentEventServiceDataAttributes:
    """
    Attributes:
        incident_event_id (str): The ID of the incident event.
        service_id (str): The ID of the service.
        status (NewIncidentEventServiceDataAttributesStatus): The status of the affected service
    """

    incident_event_id: str
    service_id: str
    status: NewIncidentEventServiceDataAttributesStatus

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

        status = check_new_incident_event_service_data_attributes_status(d.pop("status"))

        new_incident_event_service_data_attributes = cls(
            incident_event_id=incident_event_id,
            service_id=service_id,
            status=status,
        )

        return new_incident_event_service_data_attributes
