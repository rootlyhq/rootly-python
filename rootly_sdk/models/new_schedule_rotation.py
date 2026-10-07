from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_schedule_rotation_data import NewScheduleRotationData


T = TypeVar("T", bound="NewScheduleRotation")


@_attrs_define
class NewScheduleRotation:
    """
    Attributes:
        data (NewScheduleRotationData):
    """

    data: NewScheduleRotationData

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
        from ..models.new_schedule_rotation_data import NewScheduleRotationData

        d = dict(src_dict)
        data = NewScheduleRotationData.from_dict(d.pop("data"))

        new_schedule_rotation = cls(
            data=data,
        )

        return new_schedule_rotation
