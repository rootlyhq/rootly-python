from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="UpdateScheduleRotationUserDataAttributes")


@_attrs_define
class UpdateScheduleRotationUserDataAttributes:
    """
    Attributes:
        user_id (int | Unset): Schedule rotation user
        position (int | Unset): Position of the user inside rotation
    """

    user_id: int | Unset = UNSET
    position: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id", UNSET)

        position = d.pop("position", UNSET)

        update_schedule_rotation_user_data_attributes = cls(
            user_id=user_id,
            position=position,
        )

        return update_schedule_rotation_user_data_attributes
