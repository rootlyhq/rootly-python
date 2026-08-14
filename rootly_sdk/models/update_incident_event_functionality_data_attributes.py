from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_incident_event_functionality_data_attributes_status import (
    UpdateIncidentEventFunctionalityDataAttributesStatus,
    check_update_incident_event_functionality_data_attributes_status,
)

T = TypeVar("T", bound="UpdateIncidentEventFunctionalityDataAttributes")


@_attrs_define
class UpdateIncidentEventFunctionalityDataAttributes:
    """
    Attributes:
        status (UpdateIncidentEventFunctionalityDataAttributesStatus): The status of the affected functionality
    """

    status: UpdateIncidentEventFunctionalityDataAttributesStatus

    def to_dict(self) -> dict[str, Any]:
        status: str = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = check_update_incident_event_functionality_data_attributes_status(d.pop("status"))

        update_incident_event_functionality_data_attributes = cls(
            status=status,
        )

        return update_incident_event_functionality_data_attributes
