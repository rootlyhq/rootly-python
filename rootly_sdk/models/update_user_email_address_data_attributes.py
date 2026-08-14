from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserEmailAddressDataAttributes")


@_attrs_define
class UpdateUserEmailAddressDataAttributes:
    """
    Attributes:
        email (Union[Unset, str]): Email address
    """

    email: Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        update_user_email_address_data_attributes = cls(
            email=email,
        )

        return update_user_email_address_data_attributes
