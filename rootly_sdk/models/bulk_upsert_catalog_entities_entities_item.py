from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_upsert_catalog_entities_entities_item_fields_item import (
        BulkUpsertCatalogEntitiesEntitiesItemFieldsItem,
    )


T = TypeVar("T", bound="BulkUpsertCatalogEntitiesEntitiesItem")


@_attrs_define
class BulkUpsertCatalogEntitiesEntitiesItem:
    """
    Attributes:
        external_id (str): External identifier used as the upsert key. Must be unique within the catalog.
        name (str | Unset): Required for new entities. Optional for updates (managed-fields: omitted attributes are
            preserved).
        description (None | str | Unset):
        public_description (None | str | Unset):
        backstage_id (None | str | Unset):
        fields (list[BulkUpsertCatalogEntitiesEntitiesItemFieldsItem] | Unset): Property values for this entity. Only
            mentioned fields are written; unmentioned fields are preserved.
    """

    external_id: str
    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    public_description: None | str | Unset = UNSET
    backstage_id: None | str | Unset = UNSET
    fields: list[BulkUpsertCatalogEntitiesEntitiesItemFieldsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        public_description: None | str | Unset
        if isinstance(self.public_description, Unset):
            public_description = UNSET
        else:
            public_description = self.public_description

        backstage_id: None | str | Unset
        if isinstance(self.backstage_id, Unset):
            backstage_id = UNSET
        else:
            backstage_id = self.backstage_id

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if public_description is not UNSET:
            field_dict["public_description"] = public_description
        if backstage_id is not UNSET:
            field_dict["backstage_id"] = backstage_id
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_upsert_catalog_entities_entities_item_fields_item import (
            BulkUpsertCatalogEntitiesEntitiesItemFieldsItem,
        )

        d = dict(src_dict)
        external_id = d.pop("external_id")

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_public_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_description = _parse_public_description(d.pop("public_description", UNSET))

        def _parse_backstage_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backstage_id = _parse_backstage_id(d.pop("backstage_id", UNSET))

        _fields = d.pop("fields", UNSET)
        fields: list[BulkUpsertCatalogEntitiesEntitiesItemFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = BulkUpsertCatalogEntitiesEntitiesItemFieldsItem.from_dict(fields_item_data)

                fields.append(fields_item)

        bulk_upsert_catalog_entities_entities_item = cls(
            external_id=external_id,
            name=name,
            description=description,
            public_description=public_description,
            backstage_id=backstage_id,
            fields=fields,
        )

        bulk_upsert_catalog_entities_entities_item.additional_properties = d
        return bulk_upsert_catalog_entities_entities_item

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
