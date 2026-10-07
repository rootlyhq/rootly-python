from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_catalog_checklist_template_data_attributes_builtin_field_field_source import (
    UpdateCatalogChecklistTemplateDataAttributesBuiltinFieldFieldSource,
    check_update_catalog_checklist_template_data_attributes_builtin_field_field_source,
)

T = TypeVar("T", bound="UpdateCatalogChecklistTemplateDataAttributesBuiltinField")


@_attrs_define
class UpdateCatalogChecklistTemplateDataAttributesBuiltinField:
    """
    Attributes:
        field_source (UpdateCatalogChecklistTemplateDataAttributesBuiltinFieldFieldSource):
        field_key (str): Key identifying the builtin field
    """

    field_source: UpdateCatalogChecklistTemplateDataAttributesBuiltinFieldFieldSource
    field_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_source: str = self.field_source

        field_key = self.field_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_source": field_source,
                "field_key": field_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_source = check_update_catalog_checklist_template_data_attributes_builtin_field_field_source(
            d.pop("field_source")
        )

        field_key = d.pop("field_key")

        update_catalog_checklist_template_data_attributes_builtin_field = cls(
            field_source=field_source,
            field_key=field_key,
        )

        update_catalog_checklist_template_data_attributes_builtin_field.additional_properties = d
        return update_catalog_checklist_template_data_attributes_builtin_field

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
