from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="NewUserPhoneNumberDataAttributes")


@_attrs_define
class NewUserPhoneNumberDataAttributes:
    """
    Attributes:
        phone (str): Phone number in international format
    """

    phone: str

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "phone": phone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phone = d.pop("phone")

        new_user_phone_number_data_attributes = cls(
            phone=phone,
        )

        return new_user_phone_number_data_attributes
