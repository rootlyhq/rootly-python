from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkUpsertTeamsEntitiesItemFieldsItem")


@_attrs_define
class BulkUpsertTeamsEntitiesItemFieldsItem:
    """Each field entry must include either catalog_field_id or catalog_property_id.

    Attributes:
        value (str): The value for this field
        catalog_field_id (str | Unset): UUID, slug, or external_id of the catalog field (required if catalog_property_id
            is absent)
        catalog_property_id (str | Unset): Alias for catalog_field_id (required if catalog_field_id is absent)
    """

    value: str
    catalog_field_id: str | Unset = UNSET
    catalog_property_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        catalog_field_id = self.catalog_field_id

        catalog_property_id = self.catalog_property_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
            }
        )
        if catalog_field_id is not UNSET:
            field_dict["catalog_field_id"] = catalog_field_id
        if catalog_property_id is not UNSET:
            field_dict["catalog_property_id"] = catalog_property_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        catalog_field_id = d.pop("catalog_field_id", UNSET)

        catalog_property_id = d.pop("catalog_property_id", UNSET)

        bulk_upsert_teams_entities_item_fields_item = cls(
            value=value,
            catalog_field_id=catalog_field_id,
            catalog_property_id=catalog_property_id,
        )

        bulk_upsert_teams_entities_item_fields_item.additional_properties = d
        return bulk_upsert_teams_entities_item_fields_item

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
