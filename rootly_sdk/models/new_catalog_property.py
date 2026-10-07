from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_catalog_property_data import NewCatalogPropertyData


T = TypeVar("T", bound="NewCatalogProperty")


@_attrs_define
class NewCatalogProperty:
    """A catalog can have a maximum of 50 properties.

    Attributes:
        data (NewCatalogPropertyData):
    """

    data: NewCatalogPropertyData

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
        from ..models.new_catalog_property_data import NewCatalogPropertyData

        d = dict(src_dict)
        data = NewCatalogPropertyData.from_dict(d.pop("data"))

        new_catalog_property = cls(
            data=data,
        )

        return new_catalog_property
