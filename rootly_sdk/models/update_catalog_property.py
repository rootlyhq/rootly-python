from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_catalog_property_data import UpdateCatalogPropertyData


T = TypeVar("T", bound="UpdateCatalogProperty")


@_attrs_define
class UpdateCatalogProperty:
    """
    Attributes:
        data (UpdateCatalogPropertyData):
    """

    data: UpdateCatalogPropertyData

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
        from ..models.update_catalog_property_data import UpdateCatalogPropertyData

        d = dict(src_dict)
        data = UpdateCatalogPropertyData.from_dict(d.pop("data"))

        update_catalog_property = cls(
            data=data,
        )

        return update_catalog_property
