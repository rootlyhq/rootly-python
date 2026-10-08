from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bulk_upsert_teams_entities_item import BulkUpsertTeamsEntitiesItem


T = TypeVar("T", bound="BulkUpsertTeams")


@_attrs_define
class BulkUpsertTeams:
    """
    Attributes:
        entities (list[BulkUpsertTeamsEntitiesItem]): Teams to upsert, matched by external_id. Max 100 per request;
            external_ids unique within a batch. Only attributes present are written (managed-fields semantics).
    """

    entities: list[BulkUpsertTeamsEntitiesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        from ..models.bulk_upsert_teams_entities_item import BulkUpsertTeamsEntitiesItem

        d = dict(src_dict)
        entities = []
        _entities = d.pop("entities")
        for entities_item_data in _entities:
            entities_item = BulkUpsertTeamsEntitiesItem.from_dict(entities_item_data)

            entities.append(entities_item)

        bulk_upsert_teams = cls(
            entities=entities,
        )

        bulk_upsert_teams.additional_properties = d
        return bulk_upsert_teams

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
