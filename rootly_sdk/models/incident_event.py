from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_event_visibility import IncidentEventVisibility, check_incident_event_visibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentEvent")


@_attrs_define
class IncidentEvent:
    """
    Attributes:
        event (str): The summary of the incident event
        occurred_at (str): Date of occurence
        created_at (str): Date of creation
        updated_at (str): Date of last update
        visibility (Union[Unset, IncidentEventVisibility]): The visibility of the incident action item
    """

    event: str
    occurred_at: str
    created_at: str
    updated_at: str
    visibility: Unset | IncidentEventVisibility = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        occurred_at = self.occurred_at

        created_at = self.created_at

        updated_at = self.updated_at

        visibility: Unset | str = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
                "occurred_at": occurred_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event = d.pop("event")

        occurred_at = d.pop("occurred_at")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        _visibility = d.pop("visibility", UNSET)
        visibility: Unset | IncidentEventVisibility
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = check_incident_event_visibility(_visibility)

        incident_event = cls(
            event=event,
            occurred_at=occurred_at,
            created_at=created_at,
            updated_at=updated_at,
            visibility=visibility,
        )

        incident_event.additional_properties = d
        return incident_event

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
