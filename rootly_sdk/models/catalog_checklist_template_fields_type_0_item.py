from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_checklist_template_fields_type_0_item_field_source import (
    CatalogChecklistTemplateFieldsType0ItemFieldSource,
    check_catalog_checklist_template_fields_type_0_item_field_source,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogChecklistTemplateFieldsType0Item")


@_attrs_define
class CatalogChecklistTemplateFieldsType0Item:
    """
    Attributes:
        field_source (CatalogChecklistTemplateFieldsType0ItemFieldSource | Unset): Source of the field
        field_key (str | Unset): Key identifying the field
        catalog_property_id (None | str | Unset): ID of the catalog property for custom fields
    """

    field_source: CatalogChecklistTemplateFieldsType0ItemFieldSource | Unset = UNSET
    field_key: str | Unset = UNSET
    catalog_property_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_source: str | Unset = UNSET
        if not isinstance(self.field_source, Unset):
            field_source = self.field_source

        field_key = self.field_key

        catalog_property_id: None | str | Unset
        if isinstance(self.catalog_property_id, Unset):
            catalog_property_id = UNSET
        else:
            catalog_property_id = self.catalog_property_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_source is not UNSET:
            field_dict["field_source"] = field_source
        if field_key is not UNSET:
            field_dict["field_key"] = field_key
        if catalog_property_id is not UNSET:
            field_dict["catalog_property_id"] = catalog_property_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _field_source = d.pop("field_source", UNSET)
        field_source: CatalogChecklistTemplateFieldsType0ItemFieldSource | Unset
        if isinstance(_field_source, Unset):
            field_source = UNSET
        else:
            field_source = check_catalog_checklist_template_fields_type_0_item_field_source(_field_source)

        field_key = d.pop("field_key", UNSET)

        def _parse_catalog_property_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        catalog_property_id = _parse_catalog_property_id(d.pop("catalog_property_id", UNSET))

        catalog_checklist_template_fields_type_0_item = cls(
            field_source=field_source,
            field_key=field_key,
            catalog_property_id=catalog_property_id,
        )

        catalog_checklist_template_fields_type_0_item.additional_properties = d
        return catalog_checklist_template_fields_type_0_item

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
