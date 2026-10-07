from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_catalog_entity_property_data import NewCatalogEntityPropertyData


T = TypeVar("T", bound="NewCatalogEntityProperty")


@_attrs_define
class NewCatalogEntityProperty:
    """**Deprecated:** This endpoint is deprecated, please use the `fields` attribute on catalog entities or native catalog
    endpoints (teams, services, functionalities, incident_types, causes, environments) to set field values instead.

        Attributes:
            data (NewCatalogEntityPropertyData):
    """

    data: NewCatalogEntityPropertyData

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
        from ..models.new_catalog_entity_property_data import NewCatalogEntityPropertyData

        d = dict(src_dict)
        data = NewCatalogEntityPropertyData.from_dict(d.pop("data"))

        new_catalog_entity_property = cls(
            data=data,
        )

        return new_catalog_entity_property
