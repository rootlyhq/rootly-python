from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="ScheduleRotationScheduleRotationableAttributesType0")


@_attrs_define
class ScheduleRotationScheduleRotationableAttributesType0:
    """
    Attributes:
        handoff_time (str): Hand off time for daily rotation
    """

    handoff_time: str

    def to_dict(self) -> dict[str, Any]:
        handoff_time = self.handoff_time

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "handoff_time": handoff_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        handoff_time = d.pop("handoff_time")

        schedule_rotation_schedule_rotationable_attributes_type_0 = cls(
            handoff_time=handoff_time,
        )

        return schedule_rotation_schedule_rotationable_attributes_type_0
