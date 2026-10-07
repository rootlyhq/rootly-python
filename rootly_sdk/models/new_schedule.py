from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_schedule_data import NewScheduleData


T = TypeVar("T", bound="NewSchedule")


@_attrs_define
class NewSchedule:
    """
    Attributes:
        data (NewScheduleData):
    """

    data: NewScheduleData

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
        from ..models.new_schedule_data import NewScheduleData

        d = dict(src_dict)
        data = NewScheduleData.from_dict(d.pop("data"))

        new_schedule = cls(
            data=data,
        )

        return new_schedule
