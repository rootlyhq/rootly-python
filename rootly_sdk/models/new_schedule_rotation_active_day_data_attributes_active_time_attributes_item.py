from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewScheduleRotationActiveDayDataAttributesActiveTimeAttributesItem")


@_attrs_define
class NewScheduleRotationActiveDayDataAttributesActiveTimeAttributesItem:
    """
    Attributes:
        start_time (str | Unset): Start time for schedule rotation active time
        end_time (str | Unset): End time for schedule rotation active time
    """

    start_time: str | Unset = UNSET
    end_time: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time

        end_time = self.end_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        new_schedule_rotation_active_day_data_attributes_active_time_attributes_item = cls(
            start_time=start_time,
            end_time=end_time,
        )

        return new_schedule_rotation_active_day_data_attributes_active_time_attributes_item
