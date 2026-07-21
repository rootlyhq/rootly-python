from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.new_incident_event_data_attributes_visibility import check_new_incident_event_data_attributes_visibility
from ..models.new_incident_event_data_attributes_visibility import NewIncidentEventDataAttributesVisibility
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="NewIncidentEventDataAttributes")


@_attrs_define
class NewIncidentEventDataAttributes:
    """
    Attributes:
        event (str): The summary of the incident event
        visibility (NewIncidentEventDataAttributesVisibility | Unset): The visibility of the incident action item
    """

    event: str
    visibility: NewIncidentEventDataAttributesVisibility | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        visibility: str | Unset = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "event": event,
            }
        )
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event = d.pop("event")

        _visibility = d.pop("visibility", UNSET)
        visibility: NewIncidentEventDataAttributesVisibility | Unset
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = check_new_incident_event_data_attributes_visibility(_visibility)

        new_incident_event_data_attributes = cls(
            event=event,
            visibility=visibility,
        )

        return new_incident_event_data_attributes
