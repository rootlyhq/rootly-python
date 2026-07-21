from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

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
        id (str | Unset): Unique ID of the alert urgency
        urgency (None | str | Unset): The urgency level
        color (None | str | Unset): The color associated with this urgency level
        team_id (int | Unset): The ID of the team this urgency belongs to
        deleted_at (None | str | Unset): Date of deletion
    """

    name: str
    description: str
    position: int
    created_at: str
    updated_at: str
    id: str | Unset = UNSET
    urgency: None | str | Unset = UNSET
    color: None | str | Unset = UNSET
    team_id: int | Unset = UNSET
    deleted_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        id = self.id

        urgency: None | str | Unset
        if isinstance(self.urgency, Unset):
            urgency = UNSET
        else:
            urgency = self.urgency

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        team_id = self.team_id

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = self.deleted_at

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
        if id is not UNSET:
            field_dict["id"] = id
        if urgency is not UNSET:
            field_dict["urgency"] = urgency
        if color is not UNSET:
            field_dict["color"] = color
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        position = d.pop("position")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        id = d.pop("id", UNSET)

        def _parse_urgency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        urgency = _parse_urgency(d.pop("urgency", UNSET))

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        team_id = d.pop("team_id", UNSET)

        def _parse_deleted_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        alert_urgency = cls(
            name=name,
            description=description,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            urgency=urgency,
            color=color,
            team_id=team_id,
            deleted_at=deleted_at,
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
