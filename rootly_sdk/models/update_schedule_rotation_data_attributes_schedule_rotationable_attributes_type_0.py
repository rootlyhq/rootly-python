from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType0")


@_attrs_define
class UpdateScheduleRotationDataAttributesScheduleRotationableAttributesType0:
    """
    Attributes:
        handoff_time (str): Hand off time for daily rotation
    """

    handoff_time: str

    def to_dict(self) -> dict[str, Any]:
        handoff_time = self.handoff_time

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "handoff_time": handoff_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        handoff_time = d.pop("handoff_time")

        update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_0 = cls(
            handoff_time=handoff_time,
        )

        return update_schedule_rotation_data_attributes_schedule_rotationable_attributes_type_0
