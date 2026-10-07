from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

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
        position (int | Unset): Position of the member in rotation
    """

    member_type: NewScheduleRotationDataAttributesScheduleRotationMembersType0ItemMemberType
    member_id: str
    position: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        member_type: str = self.member_type

        member_id = self.member_id

        position = self.position

        field_dict: dict[str, Any] = {}

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

        return new_schedule_rotation_data_attributes_schedule_rotation_members_type_0_item
