from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_user_phone_number_data import NewUserPhoneNumberData


T = TypeVar("T", bound="NewUserPhoneNumber")


@_attrs_define
class NewUserPhoneNumber:
    """
    Attributes:
        data (NewUserPhoneNumberData):
    """

    data: NewUserPhoneNumberData

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_user_phone_number_data import NewUserPhoneNumberData

        d = dict(src_dict)
        data = NewUserPhoneNumberData.from_dict(d.pop("data"))

        new_user_phone_number = cls(
            data=data,
        )

        return new_user_phone_number
