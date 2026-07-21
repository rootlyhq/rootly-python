from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
    from ..models.bulk_upsert_catalog_entities_entities_item import BulkUpsertCatalogEntitiesEntitiesItem


T = TypeVar("T", bound="BulkUpsertCatalogEntities")


@_attrs_define
class BulkUpsertCatalogEntities:
    """
    Attributes:
        entities (list[BulkUpsertCatalogEntitiesEntitiesItem]): Array of catalog entities to upsert. Each must have an
            external_id. Max 100 per request. external_ids must be unique within a batch.
    """

    entities: list[BulkUpsertCatalogEntitiesEntitiesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_upsert_catalog_entities_entities_item import BulkUpsertCatalogEntitiesEntitiesItem

        entities = []
        for entities_item_data in self.entities:
            entities_item = entities_item_data.to_dict()
            entities.append(entities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entities": entities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_upsert_catalog_entities_entities_item import BulkUpsertCatalogEntitiesEntitiesItem

        d = dict(src_dict)
        entities = []
        _entities = d.pop("entities")
        for entities_item_data in _entities:
            entities_item = BulkUpsertCatalogEntitiesEntitiesItem.from_dict(entities_item_data)

            entities.append(entities_item)

        bulk_upsert_catalog_entities = cls(
            entities=entities,
        )

        bulk_upsert_catalog_entities.additional_properties = d
        return bulk_upsert_catalog_entities

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
