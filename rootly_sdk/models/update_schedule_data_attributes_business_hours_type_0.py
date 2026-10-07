from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpdateScheduleDataAttributesBusinessHoursType0")


@_attrs_define
class UpdateScheduleDataAttributesBusinessHoursType0:
    """Controls shadow paging on the schedule. Null disables shadow paging. start_time and end_time are HH:MM 24-hour
    format strings.

        Attributes:
            start_time (str):
            end_time (str):
            include_weekends (bool):
    """

    start_time: str
    end_time: str
    include_weekends: bool

    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time

        end_time = self.end_time

        include_weekends = self.include_weekends

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "start_time": start_time,
                "end_time": end_time,
                "include_weekends": include_weekends,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_time = d.pop("start_time")

        end_time = d.pop("end_time")

        include_weekends = d.pop("include_weekends")

        update_schedule_data_attributes_business_hours_type_0 = cls(
            start_time=start_time,
            end_time=end_time,
            include_weekends=include_weekends,
        )

        return update_schedule_data_attributes_business_hours_type_0
