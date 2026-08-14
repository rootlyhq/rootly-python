from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_incident_status_page_event_data_attributes_status_page_components_type_0_item_status import (
    NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0ItemStatus,
    check_new_incident_status_page_event_data_attributes_status_page_components_type_0_item_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0Item")


@_attrs_define
class NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0Item:
    """
    Attributes:
        status_page_component_id (str): Unique ID of a component on the event's status page
        status (Union[Unset, NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0ItemStatus]): The status
            to record for the component
    """

    status_page_component_id: str
    status: Unset | NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0ItemStatus = UNSET

    def to_dict(self) -> dict[str, Any]:
        status_page_component_id = self.status_page_component_id

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status_page_component_id": status_page_component_id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status_page_component_id = d.pop("status_page_component_id")

        _status = d.pop("status", UNSET)
        status: Unset | NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0ItemStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_new_incident_status_page_event_data_attributes_status_page_components_type_0_item_status(
                _status
            )

        new_incident_status_page_event_data_attributes_status_page_components_type_0_item = cls(
            status_page_component_id=status_page_component_id,
            status=status,
        )

        return new_incident_status_page_event_data_attributes_status_page_components_type_0_item
