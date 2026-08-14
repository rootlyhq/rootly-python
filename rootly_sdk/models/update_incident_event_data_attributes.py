from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_incident_event_data_attributes_visibility import (
    UpdateIncidentEventDataAttributesVisibility,
    check_update_incident_event_data_attributes_visibility,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateIncidentEventDataAttributes")


@_attrs_define
class UpdateIncidentEventDataAttributes:
    """
    Attributes:
        event (Union[Unset, str]): The summary of the incident event
        visibility (Union[Unset, UpdateIncidentEventDataAttributesVisibility]): The visibility of the incident action
            item
    """

    event: Unset | str = UNSET
    visibility: Unset | UpdateIncidentEventDataAttributesVisibility = UNSET

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        visibility: Unset | str = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event = d.pop("event", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Unset | UpdateIncidentEventDataAttributesVisibility
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = check_update_incident_event_data_attributes_visibility(_visibility)

        update_incident_event_data_attributes = cls(
            event=event,
            visibility=visibility,
        )

        return update_incident_event_data_attributes
