from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.schedule_rotation_schedule_rotationable_attributes_type_2_handoff_day import (
    ScheduleRotationScheduleRotationableAttributesType2HandoffDay,
)

T = TypeVar("T", bound="ScheduleRotationScheduleRotationableAttributesType2")


@_attrs_define
class ScheduleRotationScheduleRotationableAttributesType2:
    """
    Attributes:
        handoff_time (str): Hand off time for monthly rotation
        handoff_day (ScheduleRotationScheduleRotationableAttributesType2HandoffDay): Hand off day for monthly rotation
    """

    handoff_time: str
    handoff_day: ScheduleRotationScheduleRotationableAttributesType2HandoffDay

    def to_dict(self) -> dict[str, Any]:
        handoff_time = self.handoff_time

        handoff_day = self.handoff_day.value

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "handoff_time": handoff_time,
                "handoff_day": handoff_day,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        handoff_time = d.pop("handoff_time")

        handoff_day = ScheduleRotationScheduleRotationableAttributesType2HandoffDay(d.pop("handoff_day"))

        schedule_rotation_schedule_rotationable_attributes_type_2 = cls(
            handoff_time=handoff_time,
            handoff_day=handoff_day,
        )

        return schedule_rotation_schedule_rotationable_attributes_type_2
