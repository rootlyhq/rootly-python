from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_catalog_checklist_template_data_attributes_custom_field_field_source import (
    UpdateCatalogChecklistTemplateDataAttributesCustomFieldFieldSource,
    check_update_catalog_checklist_template_data_attributes_custom_field_field_source,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCatalogChecklistTemplateDataAttributesCustomField")


@_attrs_define
class UpdateCatalogChecklistTemplateDataAttributesCustomField:
    """
    Attributes:
        field_source (UpdateCatalogChecklistTemplateDataAttributesCustomFieldFieldSource):
        catalog_property_id (str): ID of the catalog property
        field_key (str | Unset): Ignored for custom fields (auto-derived from catalog property)
    """

    field_source: UpdateCatalogChecklistTemplateDataAttributesCustomFieldFieldSource
    catalog_property_id: str
    field_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_source: str = self.field_source

        catalog_property_id = self.catalog_property_id

        field_key = self.field_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_source": field_source,
                "catalog_property_id": catalog_property_id,
            }
        )
        if field_key is not UNSET:
            field_dict["field_key"] = field_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_source = check_update_catalog_checklist_template_data_attributes_custom_field_field_source(
            d.pop("field_source")
        )

        catalog_property_id = d.pop("catalog_property_id")

        field_key = d.pop("field_key", UNSET)

        update_catalog_checklist_template_data_attributes_custom_field = cls(
            field_source=field_source,
            catalog_property_id=catalog_property_id,
            field_key=field_key,
        )

        update_catalog_checklist_template_data_attributes_custom_field.additional_properties = d
        return update_catalog_checklist_template_data_attributes_custom_field

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
