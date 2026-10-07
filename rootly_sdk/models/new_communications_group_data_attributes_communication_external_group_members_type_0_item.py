from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewCommunicationsGroupDataAttributesCommunicationExternalGroupMembersType0Item")


@_attrs_define
class NewCommunicationsGroupDataAttributesCommunicationExternalGroupMembersType0Item:
    """
    Attributes:
        name (str | Unset): Name of the external member
        email (str | Unset): Email of the external member
        phone_number (str | Unset): Phone number of the external member
    """

    name: str | Unset = UNSET
    email: str | Unset = UNSET
    phone_number: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        phone_number = self.phone_number

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        new_communications_group_data_attributes_communication_external_group_members_type_0_item = cls(
            name=name,
            email=email,
            phone_number=phone_number,
        )

        return new_communications_group_data_attributes_communication_external_group_members_type_0_item
