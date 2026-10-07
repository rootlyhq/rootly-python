from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_schedule_rotation_active_day_data_type import (
    NewScheduleRotationActiveDayDataType,
    check_new_schedule_rotation_active_day_data_type,
)

if TYPE_CHECKING:
    from ..models.new_schedule_rotation_active_day_data_attributes import NewScheduleRotationActiveDayDataAttributes


T = TypeVar("T", bound="NewScheduleRotationActiveDayData")


@_attrs_define
class NewScheduleRotationActiveDayData:
    """
    Attributes:
        type_ (NewScheduleRotationActiveDayDataType):
        attributes (NewScheduleRotationActiveDayDataAttributes):
    """

    type_: NewScheduleRotationActiveDayDataType
    attributes: NewScheduleRotationActiveDayDataAttributes

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_schedule_rotation_active_day_data_attributes import NewScheduleRotationActiveDayDataAttributes

        d = dict(src_dict)
        type_ = check_new_schedule_rotation_active_day_data_type(d.pop("type"))

        attributes = NewScheduleRotationActiveDayDataAttributes.from_dict(d.pop("attributes"))

        new_schedule_rotation_active_day_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return new_schedule_rotation_active_day_data
