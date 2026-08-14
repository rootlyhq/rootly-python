from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_incident_event_functionality_data_attributes_status import (
    NewIncidentEventFunctionalityDataAttributesStatus,
    check_new_incident_event_functionality_data_attributes_status,
)

T = TypeVar("T", bound="NewIncidentEventFunctionalityDataAttributes")


@_attrs_define
class NewIncidentEventFunctionalityDataAttributes:
    """
    Attributes:
        incident_event_id (str): The ID of the incident event.
        functionality_id (str): The ID of the functionality.
        status (NewIncidentEventFunctionalityDataAttributesStatus): The status of the affected functionality
    """

    incident_event_id: str
    functionality_id: str
    status: NewIncidentEventFunctionalityDataAttributesStatus

    def to_dict(self) -> dict[str, Any]:
        incident_event_id = self.incident_event_id

        functionality_id = self.functionality_id

        status: str = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "incident_event_id": incident_event_id,
                "functionality_id": functionality_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        incident_event_id = d.pop("incident_event_id")

        functionality_id = d.pop("functionality_id")

        status = check_new_incident_event_functionality_data_attributes_status(d.pop("status"))

        new_incident_event_functionality_data_attributes = cls(
            incident_event_id=incident_event_id,
            functionality_id=functionality_id,
            status=status,
        )

        return new_incident_event_functionality_data_attributes
