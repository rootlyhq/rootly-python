from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_entity_property_response_data import CatalogEntityPropertyResponseData


T = TypeVar("T", bound="CatalogEntityPropertyResponse")


@_attrs_define
class CatalogEntityPropertyResponse:
    """**Deprecated:** This endpoint is deprecated, please use `include=fields` on catalog entities or native catalog
    endpoints (teams, services, functionalities, incident_types, causes, environments) to retrieve field values instead.

        Attributes:
            data (CatalogEntityPropertyResponseData):
    """

    data: "CatalogEntityPropertyResponseData"
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
        from ..models.catalog_entity_property_response_data import CatalogEntityPropertyResponseData

        d = dict(src_dict)
        data = CatalogEntityPropertyResponseData.from_dict(d.pop("data"))

        catalog_entity_property_response = cls(
            data=data,
        )

        catalog_entity_property_response.additional_properties = d
        return catalog_entity_property_response

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
