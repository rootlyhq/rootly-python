from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_catalog_data import UpdateCatalogData


T = TypeVar("T", bound="UpdateCatalog")


@_attrs_define
class UpdateCatalog:
    """
    Attributes:
        data (UpdateCatalogData):
    """

    data: UpdateCatalogData

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
        from ..models.update_catalog_data import UpdateCatalogData

        d = dict(src_dict)
        data = UpdateCatalogData.from_dict(d.pop("data"))

        update_catalog = cls(
            data=data,
        )

        return update_catalog
