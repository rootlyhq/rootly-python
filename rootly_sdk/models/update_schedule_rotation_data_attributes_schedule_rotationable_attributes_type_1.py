from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1_handoff_day import (
    UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1HandoffDay,
)

T = TypeVar("T", bound="UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1")


@_attrs_define
class UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1:
    """
    Attributes:
        handoff_time (str): Hand off time for weekly/biweekly rotation
        handoff_day (UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1HandoffDay): Hand off day
            for weekly/biweekly rotation
    """

    handoff_time: str
    handoff_day: UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1HandoffDay

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

        handoff_day = UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType1HandoffDay(
            d.pop("handoff_day")
        )

        update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1 = cls(
            handoff_time=handoff_time,
            handoff_day=handoff_day,
        )

        return update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_1
