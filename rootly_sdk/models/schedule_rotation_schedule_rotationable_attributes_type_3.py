from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.schedule_rotation_schedule_rotationable_attributes_type_3_shift_length_unit import (
    ScheduleRotationScheduleRotationableAttributesType3ShiftLengthUnit,
    check_schedule_rotation_schedule_rotationable_attributes_type_3_shift_length_unit,
)

T = TypeVar("T", bound="ScheduleRotationScheduleRotationableAttributesType3")


@_attrs_define
class ScheduleRotationScheduleRotationableAttributesType3:
    """
    Attributes:
        shift_length (int): Shift length for custom rotation
        shift_length_unit (ScheduleRotationScheduleRotationableAttributesType3ShiftLengthUnit): Shift length unit for
            custom rotation
        handoff_time (str): Hand off time for custom rotation. Use minutes for hourly rotation.
    """

    shift_length: int
    shift_length_unit: ScheduleRotationScheduleRotationableAttributesType3ShiftLengthUnit
    handoff_time: str

    def to_dict(self) -> dict[str, Any]:
        shift_length = self.shift_length

        shift_length_unit: str = self.shift_length_unit

        handoff_time = self.handoff_time

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "shift_length": shift_length,
                "shift_length_unit": shift_length_unit,
                "handoff_time": handoff_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shift_length = d.pop("shift_length")

        shift_length_unit = check_schedule_rotation_schedule_rotationable_attributes_type_3_shift_length_unit(
            d.pop("shift_length_unit")
        )

        handoff_time = d.pop("handoff_time")

        schedule_rotation_schedule_rotationable_attributes_type_3 = cls(
            shift_length=shift_length,
            shift_length_unit=shift_length_unit,
            handoff_time=handoff_time,
        )

        return schedule_rotation_schedule_rotationable_attributes_type_3
