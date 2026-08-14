from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

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
        id (Union[Unset, str]): Unique ID of the alert urgency
        retrigger_timeout_minutes (Union[None, Unset, int]): Re-trigger acknowledged alerts of this urgency after N
            minutes; null inherits the workspace default, negative = never.
        urgency (Union[None, Unset, str]): The urgency level
        color (Union[None, Unset, str]): The color associated with this urgency level
        team_id (Union[Unset, int]): The ID of the team this urgency belongs to
        deleted_at (Union[None, Unset, str]): Date of deletion
    """

    name: str
    description: str
    position: int
    created_at: str
    updated_at: str
    id: Union[Unset, str] = UNSET
    retrigger_timeout_minutes: Union[None, Unset, int] = UNSET
    urgency: Union[None, Unset, str] = UNSET
    color: Union[None, Unset, str] = UNSET
    team_id: Union[Unset, int] = UNSET
    deleted_at: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        id = self.id

        retrigger_timeout_minutes: Union[None, Unset, int]
        if isinstance(self.retrigger_timeout_minutes, Unset):
            retrigger_timeout_minutes = UNSET
        else:
            retrigger_timeout_minutes = self.retrigger_timeout_minutes

        urgency: Union[None, Unset, str]
        if isinstance(self.urgency, Unset):
            urgency = UNSET
        else:
            urgency = self.urgency

        color: Union[None, Unset, str]
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        team_id = self.team_id

        deleted_at: Union[None, Unset, str]
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
        if retrigger_timeout_minutes is not UNSET:
            field_dict["retrigger_timeout_minutes"] = retrigger_timeout_minutes
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

        def _parse_retrigger_timeout_minutes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        retrigger_timeout_minutes = _parse_retrigger_timeout_minutes(d.pop("retrigger_timeout_minutes", UNSET))

        def _parse_urgency(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        urgency = _parse_urgency(d.pop("urgency", UNSET))

        def _parse_color(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        color = _parse_color(d.pop("color", UNSET))

        team_id = d.pop("team_id", UNSET)

        def _parse_deleted_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        alert_urgency = cls(
            name=name,
            description=description,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            retrigger_timeout_minutes=retrigger_timeout_minutes,
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
