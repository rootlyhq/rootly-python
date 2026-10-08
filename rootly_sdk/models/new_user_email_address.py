from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_user_email_address_data import NewUserEmailAddressData


T = TypeVar("T", bound="NewUserEmailAddress")


@_attrs_define
class NewUserEmailAddress:
    """
    Attributes:
        data (NewUserEmailAddressData):
    """

    data: NewUserEmailAddressData

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
        from ..models.new_user_email_address_data import NewUserEmailAddressData

        d = dict(src_dict)
        data = NewUserEmailAddressData.from_dict(d.pop("data"))

        new_user_email_address = cls(
            data=data,
        )

        return new_user_email_address
