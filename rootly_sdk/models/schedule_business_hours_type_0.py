from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ScheduleBusinessHoursType0")


@_attrs_define
class ScheduleBusinessHoursType0:
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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time

        end_time = self.end_time

        include_weekends = self.include_weekends

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        schedule_business_hours_type_0 = cls(
            start_time=start_time,
            end_time=end_time,
            include_weekends=include_weekends,
        )

        schedule_business_hours_type_0.additional_properties = d
        return schedule_business_hours_type_0

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
