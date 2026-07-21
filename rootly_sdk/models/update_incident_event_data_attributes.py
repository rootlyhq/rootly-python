from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_incident_event_data_attributes_visibility import (
    check_update_incident_event_data_attributes_visibility,
)
from ..models.update_incident_event_data_attributes_visibility import UpdateIncidentEventDataAttributesVisibility
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="UpdateIncidentEventDataAttributes")


@_attrs_define
class UpdateIncidentEventDataAttributes:
    """
    Attributes:
        event (str | Unset): The summary of the incident event
        visibility (UpdateIncidentEventDataAttributesVisibility | Unset): The visibility of the incident action item
    """

    event: str | Unset = UNSET
    visibility: UpdateIncidentEventDataAttributesVisibility | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        visibility: str | Unset = UNSET
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
        visibility: UpdateIncidentEventDataAttributesVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = check_update_incident_event_data_attributes_visibility(_visibility)

        update_incident_event_data_attributes = cls(
            event=event,
            visibility=visibility,
        )

        return update_incident_event_data_attributes
