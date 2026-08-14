from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserPhoneNumberDataAttributes")


@_attrs_define
class UpdateUserPhoneNumberDataAttributes:
    """
    Attributes:
        phone (Union[Unset, str]): Phone number in international format
    """

    phone: Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phone = d.pop("phone", UNSET)

        update_user_phone_number_data_attributes = cls(
            phone=phone,
        )

        return update_user_phone_number_data_attributes
