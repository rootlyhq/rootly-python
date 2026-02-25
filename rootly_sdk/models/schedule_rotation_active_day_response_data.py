from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_rotation_active_day_response_data_type import (
    ScheduleRotationActiveDayResponseDataType,
    check_schedule_rotation_active_day_response_data_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_rotation_active_day import ScheduleRotationActiveDay


T = TypeVar("T", bound="ScheduleRotationActiveDayResponseData")


@_attrs_define
class ScheduleRotationActiveDayResponseData:
    """
    Attributes:
        id (Union[Unset, str]): Unique ID of the schedule rotation active time
        type_ (Union[Unset, ScheduleRotationActiveDayResponseDataType]):
        attributes (Union[Unset, ScheduleRotationActiveDay]):
    """

    id: Unset | str = UNSET
    type_: Unset | ScheduleRotationActiveDayResponseDataType = UNSET
    attributes: Union[Unset, "ScheduleRotationActiveDay"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        attributes: Unset | dict[str, Any] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_rotation_active_day import ScheduleRotationActiveDay

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Unset | ScheduleRotationActiveDayResponseDataType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_schedule_rotation_active_day_response_data_type(_type_)

        _attributes = d.pop("attributes", UNSET)
        attributes: Unset | ScheduleRotationActiveDay
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ScheduleRotationActiveDay.from_dict(_attributes)

        schedule_rotation_active_day_response_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        schedule_rotation_active_day_response_data.additional_properties = d
        return schedule_rotation_active_day_response_data

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
