from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_schedule_rotation_user_data_type import (
    NewScheduleRotationUserDataType,
    check_new_schedule_rotation_user_data_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_schedule_rotation_user_data_attributes import NewScheduleRotationUserDataAttributes


T = TypeVar("T", bound="NewScheduleRotationUserData")


@_attrs_define
class NewScheduleRotationUserData:
    """
    Attributes:
        type_ (Union[Unset, NewScheduleRotationUserDataType]):
        attributes (Union[Unset, NewScheduleRotationUserDataAttributes]):
    """

    type_: Unset | NewScheduleRotationUserDataType = UNSET
    attributes: Union[Unset, "NewScheduleRotationUserDataAttributes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        attributes: Unset | dict[str, Any] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_schedule_rotation_user_data_attributes import NewScheduleRotationUserDataAttributes

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Unset | NewScheduleRotationUserDataType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_new_schedule_rotation_user_data_type(_type_)

        _attributes = d.pop("attributes", UNSET)
        attributes: Unset | NewScheduleRotationUserDataAttributes
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = NewScheduleRotationUserDataAttributes.from_dict(_attributes)

        new_schedule_rotation_user_data = cls(
            type_=type_,
            attributes=attributes,
        )

        new_schedule_rotation_user_data.additional_properties = d
        return new_schedule_rotation_user_data

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
