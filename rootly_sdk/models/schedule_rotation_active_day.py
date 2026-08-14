from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_rotation_active_day_day_name import (
    ScheduleRotationActiveDayDayName,
    check_schedule_rotation_active_day_day_name,
)

if TYPE_CHECKING:
    from ..models.schedule_rotation_active_day_active_time_attributes_item import (
        ScheduleRotationActiveDayActiveTimeAttributesItem,
    )


T = TypeVar("T", bound="ScheduleRotationActiveDay")


@_attrs_define
class ScheduleRotationActiveDay:
    """
    Attributes:
        schedule_rotation_id (str):
        day_name (ScheduleRotationActiveDayDayName): Schedule rotation day name for which active times to be created
        active_time_attributes (list['ScheduleRotationActiveDayActiveTimeAttributesItem']): Schedule rotation active
            times per day
        created_at (str): Date of creation
        updated_at (str): Date of last update
    """

    schedule_rotation_id: str
    day_name: ScheduleRotationActiveDayDayName
    active_time_attributes: list["ScheduleRotationActiveDayActiveTimeAttributesItem"]
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        schedule_rotation_id = self.schedule_rotation_id

        day_name: str = self.day_name

        active_time_attributes = []
        for active_time_attributes_item_data in self.active_time_attributes:
            active_time_attributes_item = active_time_attributes_item_data.to_dict()
            active_time_attributes.append(active_time_attributes_item)

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schedule_rotation_id": schedule_rotation_id,
                "day_name": day_name,
                "active_time_attributes": active_time_attributes,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_rotation_active_day_active_time_attributes_item import (
            ScheduleRotationActiveDayActiveTimeAttributesItem,
        )

        d = dict(src_dict)
        schedule_rotation_id = d.pop("schedule_rotation_id")

        day_name = check_schedule_rotation_active_day_day_name(d.pop("day_name"))

        active_time_attributes = []
        _active_time_attributes = d.pop("active_time_attributes")
        for active_time_attributes_item_data in _active_time_attributes:
            active_time_attributes_item = ScheduleRotationActiveDayActiveTimeAttributesItem.from_dict(
                active_time_attributes_item_data
            )

            active_time_attributes.append(active_time_attributes_item)

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        schedule_rotation_active_day = cls(
            schedule_rotation_id=schedule_rotation_id,
            day_name=day_name,
            active_time_attributes=active_time_attributes,
            created_at=created_at,
            updated_at=updated_at,
        )

        schedule_rotation_active_day.additional_properties = d
        return schedule_rotation_active_day

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
