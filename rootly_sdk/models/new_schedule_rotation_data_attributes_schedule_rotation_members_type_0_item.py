from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_schedule_rotation_data_attributes_schedule_rotation_members_type_0_item_member_type import (
    NewScheduleRotationDataAttributesScheduleRotationMembersType0ItemMemberType,
    check_new_schedule_rotation_data_attributes_schedule_rotation_members_type_0_item_member_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewScheduleRotationDataAttributesScheduleRotationMembersType0Item")


@_attrs_define
class NewScheduleRotationDataAttributesScheduleRotationMembersType0Item:
    """
    Attributes:
        member_type (NewScheduleRotationDataAttributesScheduleRotationMembersType0ItemMemberType): Type of member
        member_id (str): ID of the member
        position (Union[Unset, int]): Position of the member in rotation
    """

    member_type: NewScheduleRotationDataAttributesScheduleRotationMembersType0ItemMemberType
    member_id: str
    position: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_type: str = self.member_type

        member_id = self.member_id

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "member_type": member_type,
                "member_id": member_id,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        member_type = check_new_schedule_rotation_data_attributes_schedule_rotation_members_type_0_item_member_type(
            d.pop("member_type")
        )

        member_id = d.pop("member_id")

        position = d.pop("position", UNSET)

        new_schedule_rotation_data_attributes_schedule_rotation_members_type_0_item = cls(
            member_type=member_type,
            member_id=member_id,
            position=position,
        )

        new_schedule_rotation_data_attributes_schedule_rotation_members_type_0_item.additional_properties = d
        return new_schedule_rotation_data_attributes_schedule_rotation_members_type_0_item

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
