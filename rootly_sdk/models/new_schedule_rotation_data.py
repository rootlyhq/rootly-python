from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_schedule_rotation_data_type import NewScheduleRotationDataType, check_new_schedule_rotation_data_type

if TYPE_CHECKING:
    from ..models.new_schedule_rotation_data_attributes import NewScheduleRotationDataAttributes


T = TypeVar("T", bound="NewScheduleRotationData")


@_attrs_define
class NewScheduleRotationData:
    """
    Attributes:
        type_ (NewScheduleRotationDataType):
        attributes (NewScheduleRotationDataAttributes):
    """

    type_: NewScheduleRotationDataType
    attributes: NewScheduleRotationDataAttributes

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
        from ..models.new_schedule_rotation_data_attributes import NewScheduleRotationDataAttributes

        d = dict(src_dict)
        type_ = check_new_schedule_rotation_data_type(d.pop("type"))

        attributes = NewScheduleRotationDataAttributes.from_dict(d.pop("attributes"))

        new_schedule_rotation_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return new_schedule_rotation_data
