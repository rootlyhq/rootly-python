from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_user_email_address_data import UpdateUserEmailAddressData


T = TypeVar("T", bound="UpdateUserEmailAddress")


@_attrs_define
class UpdateUserEmailAddress:
    """
    Attributes:
        data (UpdateUserEmailAddressData):
    """

    data: UpdateUserEmailAddressData

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
        from ..models.update_user_email_address_data import UpdateUserEmailAddressData

        d = dict(src_dict)
        data = UpdateUserEmailAddressData.from_dict(d.pop("data"))

        update_user_email_address = cls(
            data=data,
        )

        return update_user_email_address
