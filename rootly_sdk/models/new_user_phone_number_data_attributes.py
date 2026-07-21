from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


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
