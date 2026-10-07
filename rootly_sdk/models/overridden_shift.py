from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OverriddenShift")


@_attrs_define
class OverriddenShift:
    """
    Attributes:
        starts_at (str): Start datetime of the overridden portion
        ends_at (str): End datetime of the overridden portion
        user_id (int | None | Unset): ID of the user whose shift was overridden
        rotation_id (None | str | Unset): ID of the rotation the overridden shift belongs to
        assignee_type (None | str | Unset): Type of the overridden assignee (User or Schedule)
        assignee_id (None | str | Unset): ID of the overridden assignee
    """

    starts_at: str
    ends_at: str
    user_id: int | None | Unset = UNSET
    rotation_id: None | str | Unset = UNSET
    assignee_type: None | str | Unset = UNSET
    assignee_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        starts_at = self.starts_at

        ends_at = self.ends_at

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        rotation_id: None | str | Unset
        if isinstance(self.rotation_id, Unset):
            rotation_id = UNSET
        else:
            rotation_id = self.rotation_id

        assignee_type: None | str | Unset
        if isinstance(self.assignee_type, Unset):
            assignee_type = UNSET
        else:
            assignee_type = self.assignee_type

        assignee_id: None | str | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        else:
            assignee_id = self.assignee_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "starts_at": starts_at,
                "ends_at": ends_at,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if rotation_id is not UNSET:
            field_dict["rotation_id"] = rotation_id
        if assignee_type is not UNSET:
            field_dict["assignee_type"] = assignee_type
        if assignee_id is not UNSET:
            field_dict["assignee_id"] = assignee_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        starts_at = d.pop("starts_at")

        ends_at = d.pop("ends_at")

        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_rotation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rotation_id = _parse_rotation_id(d.pop("rotation_id", UNSET))

        def _parse_assignee_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignee_type = _parse_assignee_type(d.pop("assignee_type", UNSET))

        def _parse_assignee_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignee_id = _parse_assignee_id(d.pop("assignee_id", UNSET))

        overridden_shift = cls(
            starts_at=starts_at,
            ends_at=ends_at,
            user_id=user_id,
            rotation_id=rotation_id,
            assignee_type=assignee_type,
            assignee_id=assignee_id,
        )

        overridden_shift.additional_properties = d
        return overridden_shift

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
