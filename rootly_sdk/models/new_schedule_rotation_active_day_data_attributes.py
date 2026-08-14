from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_schedule_rotation_active_day_data_attributes_day_name import (
    NewScheduleRotationActiveDayDataAttributesDayName,
    check_new_schedule_rotation_active_day_data_attributes_day_name,
)

if TYPE_CHECKING:
    from ..models.new_schedule_rotation_active_day_data_attributes_active_time_attributes_item import (
        NewScheduleRotationActiveDayDataAttributesActiveTimeAttributesItem,
    )


T = TypeVar("T", bound="NewScheduleRotationActiveDayDataAttributes")


@_attrs_define
class NewScheduleRotationActiveDayDataAttributes:
    """
    Attributes:
        day_name (NewScheduleRotationActiveDayDataAttributesDayName): Schedule rotation day name for which active times
            to be created
        active_time_attributes (list['NewScheduleRotationActiveDayDataAttributesActiveTimeAttributesItem']): Schedule
            rotation active times per day
    """

    day_name: NewScheduleRotationActiveDayDataAttributesDayName
    active_time_attributes: list["NewScheduleRotationActiveDayDataAttributesActiveTimeAttributesItem"]

    def to_dict(self) -> dict[str, Any]:
        day_name: str = self.day_name

        active_time_attributes = []
        for active_time_attributes_item_data in self.active_time_attributes:
            active_time_attributes_item = active_time_attributes_item_data.to_dict()
            active_time_attributes.append(active_time_attributes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "day_name": day_name,
                "active_time_attributes": active_time_attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_schedule_rotation_active_day_data_attributes_active_time_attributes_item import (
            NewScheduleRotationActiveDayDataAttributesActiveTimeAttributesItem,
        )

        d = dict(src_dict)
        day_name = check_new_schedule_rotation_active_day_data_attributes_day_name(d.pop("day_name"))

        active_time_attributes = []
        _active_time_attributes = d.pop("active_time_attributes")
        for active_time_attributes_item_data in _active_time_attributes:
            active_time_attributes_item = NewScheduleRotationActiveDayDataAttributesActiveTimeAttributesItem.from_dict(
                active_time_attributes_item_data
            )

            active_time_attributes.append(active_time_attributes_item)

        new_schedule_rotation_active_day_data_attributes = cls(
            day_name=day_name,
            active_time_attributes=active_time_attributes,
        )

        return new_schedule_rotation_active_day_data_attributes
