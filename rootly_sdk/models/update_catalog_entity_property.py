from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_catalog_entity_property_data import UpdateCatalogEntityPropertyData


T = TypeVar("T", bound="UpdateCatalogEntityProperty")


@_attrs_define
class UpdateCatalogEntityProperty:
    """**Deprecated:** This endpoint is deprecated, please use the `fields` attribute on catalog entities or native catalog
    endpoints (teams, services, functionalities, incident_types, causes, environments) to set field values instead.

        Attributes:
            data (UpdateCatalogEntityPropertyData):
    """

    data: UpdateCatalogEntityPropertyData

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
        from ..models.update_catalog_entity_property_data import UpdateCatalogEntityPropertyData

        d = dict(src_dict)
        data = UpdateCatalogEntityPropertyData.from_dict(d.pop("data"))

        update_catalog_entity_property = cls(
            data=data,
        )

        return update_catalog_entity_property
