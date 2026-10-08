from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="NewScheduleRotationDataAttributesActiveTimeAttributesItem")


@_attrs_define
class NewScheduleRotationDataAttributesActiveTimeAttributesItem:
    """
    Attributes:
        start_time (str): Start time for schedule rotation active time
        end_time (str): End time for schedule rotation active time
    """

    start_time: str
    end_time: str

    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time

        end_time = self.end_time

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start_time": start_time,
                "end_time": end_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_time = d.pop("start_time")

        end_time = d.pop("end_time")

        new_schedule_rotation_data_attributes_active_time_attributes_item = cls(
            start_time=start_time,
            end_time=end_time,
        )

        return new_schedule_rotation_data_attributes_active_time_attributes_item
