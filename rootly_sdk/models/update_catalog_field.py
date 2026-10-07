from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_catalog_field_data import UpdateCatalogFieldData


T = TypeVar("T", bound="UpdateCatalogField")


@_attrs_define
class UpdateCatalogField:
    """
    Attributes:
        data (UpdateCatalogFieldData):
    """

    data: UpdateCatalogFieldData

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
        from ..models.update_catalog_field_data import UpdateCatalogFieldData

        d = dict(src_dict)
        data = UpdateCatalogFieldData.from_dict(d.pop("data"))

        update_catalog_field = cls(
            data=data,
        )

        return update_catalog_field
