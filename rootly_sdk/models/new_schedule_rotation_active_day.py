from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_schedule_rotation_active_day_data import NewScheduleRotationActiveDayData


T = TypeVar("T", bound="NewScheduleRotationActiveDay")


@_attrs_define
class NewScheduleRotationActiveDay:
    """
    Attributes:
        data (NewScheduleRotationActiveDayData):
    """

    data: NewScheduleRotationActiveDayData

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_schedule_rotation_active_day_data import NewScheduleRotationActiveDayData

        d = dict(src_dict)
        data = NewScheduleRotationActiveDayData.from_dict(d.pop("data"))

        new_schedule_rotation_active_day = cls(
            data=data,
        )

        return new_schedule_rotation_active_day
