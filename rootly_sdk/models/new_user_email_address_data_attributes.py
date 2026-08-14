from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="NewUserEmailAddressDataAttributes")


@_attrs_define
class NewUserEmailAddressDataAttributes:
    """
    Attributes:
        email (str): Email address
    """

    email: str

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        new_user_email_address_data_attributes = cls(
            email=email,
        )

        return new_user_email_address_data_attributes
