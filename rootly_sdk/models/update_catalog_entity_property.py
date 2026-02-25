from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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

    data: "UpdateCatalogEntityPropertyData"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        update_catalog_entity_property.additional_properties = d
        return update_catalog_entity_property

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
