from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1_handoff_day import (
    NewScheduleRotationDataAttributesScheduleRotationableAttributesType1HandoffDay,
    check_new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1_handoff_day,
)

T = TypeVar("T", bound="NewScheduleRotationDataAttributesScheduleRotationableAttributesType1")


@_attrs_define
class NewScheduleRotationDataAttributesScheduleRotationableAttributesType1:
    """
    Attributes:
        handoff_time (str): Hand off time for weekly/biweekly rotation
        handoff_day (NewScheduleRotationDataAttributesScheduleRotationableAttributesType1HandoffDay): Hand off day for
            weekly/biweekly rotation
    """

    handoff_time: str
    handoff_day: NewScheduleRotationDataAttributesScheduleRotationableAttributesType1HandoffDay

    def to_dict(self) -> dict[str, Any]:
        handoff_time = self.handoff_time

        handoff_day: str = self.handoff_day

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "handoff_time": handoff_time,
                "handoff_day": handoff_day,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        handoff_time = d.pop("handoff_time")

        handoff_day = check_new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1_handoff_day(
            d.pop("handoff_day")
        )

        new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1 = cls(
            handoff_time=handoff_time,
            handoff_day=handoff_day,
        )

        return new_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1
