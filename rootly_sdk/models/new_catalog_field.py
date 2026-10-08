from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_catalog_field_data import NewCatalogFieldData


T = TypeVar("T", bound="NewCatalogField")


@_attrs_define
class NewCatalogField:
    """A catalog can have a maximum of 50 fields.

    Attributes:
        data (NewCatalogFieldData):
    """

    data: NewCatalogFieldData

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
        from ..models.new_catalog_field_data import NewCatalogFieldData

        d = dict(src_dict)
        data = NewCatalogFieldData.from_dict(d.pop("data"))

        new_catalog_field = cls(
            data=data,
        )

        return new_catalog_field
