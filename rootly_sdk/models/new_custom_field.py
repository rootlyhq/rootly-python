from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_custom_field_data import NewCustomFieldData


T = TypeVar("T", bound="NewCustomField")


@_attrs_define
class NewCustomField:
    """
    Attributes:
        data (NewCustomFieldData):
    """

    data: NewCustomFieldData

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
        from ..models.new_custom_field_data import NewCustomFieldData

        d = dict(src_dict)
        data = NewCustomFieldData.from_dict(d.pop("data"))

        new_custom_field = cls(
            data=data,
        )

        return new_custom_field
