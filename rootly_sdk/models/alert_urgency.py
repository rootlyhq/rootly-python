from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertUrgency")


@_attrs_define
class AlertUrgency:
    """
    Attributes:
        name (str): The name of the alert urgency
        description (str): The description of the alert urgency
        position (int): Position of the alert urgency
        created_at (str): Date of creation
        updated_at (str): Date of last update
    """

    name: str
    description: str
    position: int
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "position": position,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        position = d.pop("position")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        alert_urgency = cls(
            name=name,
            description=description,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
        )

        alert_urgency.additional_properties = d
        return alert_urgency

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
