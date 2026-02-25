from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewCommunicationsGroupDataAttributesCommunicationExternalGroupMembersType0Item")


@_attrs_define
class NewCommunicationsGroupDataAttributesCommunicationExternalGroupMembersType0Item:
    """
    Attributes:
        name (Union[Unset, str]): Name of the external member
        email (Union[Unset, str]): Email of the external member
        phone_number (Union[Unset, str]): Phone number of the external member
    """

    name: Unset | str = UNSET
    email: Unset | str = UNSET
    phone_number: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        phone_number = self.phone_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        new_communications_group_data_attributes_communication_external_group_members_type_0_item.additional_properties = d
        return new_communications_group_data_attributes_communication_external_group_members_type_0_item

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
