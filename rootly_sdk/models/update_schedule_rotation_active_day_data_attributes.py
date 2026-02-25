from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_schedule_rotation_active_day_data_attributes_day_name import (
    UpdateScheduleRotationActiveDayDataAttributesDayName,
    check_update_schedule_rotation_active_day_data_attributes_day_name,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_schedule_rotation_active_day_data_attributes_active_time_attributes_item import (
        UpdateScheduleRotationActiveDayDataAttributesActiveTimeAttributesItem,
    )


T = TypeVar("T", bound="UpdateScheduleRotationActiveDayDataAttributes")


@_attrs_define
class UpdateScheduleRotationActiveDayDataAttributes:
    """
    Attributes:
        day_name (Union[Unset, UpdateScheduleRotationActiveDayDataAttributesDayName]): Schedule rotation day name for
            which active times to be created
        active_time_attributes (Union[Unset,
            list['UpdateScheduleRotationActiveDayDataAttributesActiveTimeAttributesItem']]): Schedule rotation active times
            per day
    """

    day_name: Unset | UpdateScheduleRotationActiveDayDataAttributesDayName = UNSET
    active_time_attributes: Unset | list["UpdateScheduleRotationActiveDayDataAttributesActiveTimeAttributesItem"] = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        day_name: Unset | str = UNSET
        if not isinstance(self.day_name, Unset):
            day_name = self.day_name

        active_time_attributes: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.active_time_attributes, Unset):
            active_time_attributes = []
            for active_time_attributes_item_data in self.active_time_attributes:
                active_time_attributes_item = active_time_attributes_item_data.to_dict()
                active_time_attributes.append(active_time_attributes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if day_name is not UNSET:
            field_dict["day_name"] = day_name
        if active_time_attributes is not UNSET:
            field_dict["active_time_attributes"] = active_time_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_schedule_rotation_active_day_data_attributes_active_time_attributes_item import (
            UpdateScheduleRotationActiveDayDataAttributesActiveTimeAttributesItem,
        )

        d = dict(src_dict)
        _day_name = d.pop("day_name", UNSET)
        day_name: Unset | UpdateScheduleRotationActiveDayDataAttributesDayName
        if isinstance(_day_name, Unset):
            day_name = UNSET
        else:
            day_name = check_update_schedule_rotation_active_day_data_attributes_day_name(_day_name)

        active_time_attributes = []
        _active_time_attributes = d.pop("active_time_attributes", UNSET)
        for active_time_attributes_item_data in _active_time_attributes or []:
            active_time_attributes_item = (
                UpdateScheduleRotationActiveDayDataAttributesActiveTimeAttributesItem.from_dict(
                    active_time_attributes_item_data
                )
            )

            active_time_attributes.append(active_time_attributes_item)

        update_schedule_rotation_active_day_data_attributes = cls(
            day_name=day_name,
            active_time_attributes=active_time_attributes,
        )

        return update_schedule_rotation_active_day_data_attributes
