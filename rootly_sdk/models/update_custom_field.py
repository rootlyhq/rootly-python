from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_custom_field_data import UpdateCustomFieldData


T = TypeVar("T", bound="UpdateCustomField")


@_attrs_define
class UpdateCustomField:
    """
    Attributes:
        data (UpdateCustomFieldData):
    """

    data: UpdateCustomFieldData

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
        from ..models.update_custom_field_data import UpdateCustomFieldData

        d = dict(src_dict)
        data = UpdateCustomFieldData.from_dict(d.pop("data"))

        update_custom_field = cls(
            data=data,
        )

        return update_custom_field
