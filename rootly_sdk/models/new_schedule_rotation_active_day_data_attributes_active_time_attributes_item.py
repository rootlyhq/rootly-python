from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewScheduleRotationActiveDayDataAttributesActiveTimeAttributesItem")


@_attrs_define
class NewScheduleRotationActiveDayDataAttributesActiveTimeAttributesItem:
    """
    Attributes:
        start_time (Union[Unset, str]): Start time for schedule rotation active time
        end_time (Union[Unset, str]): End time for schedule rotation active time
    """

    start_time: Unset | str = UNSET
    end_time: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time

        end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        new_schedule_rotation_active_day_data_attributes_active_time_attributes_item = cls(
            start_time=start_time,
            end_time=end_time,
        )

        new_schedule_rotation_active_day_data_attributes_active_time_attributes_item.additional_properties = d
        return new_schedule_rotation_active_day_data_attributes_active_time_attributes_item

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
