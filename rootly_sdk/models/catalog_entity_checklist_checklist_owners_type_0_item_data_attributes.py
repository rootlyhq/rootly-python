from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogEntityChecklistChecklistOwnersType0ItemDataAttributes")


@_attrs_define
class CatalogEntityChecklistChecklistOwnersType0ItemDataAttributes:
    """
    Attributes:
        catalog_entity_checklist_id (str | Unset): The ID of the parent checklist
        owner_user_id (str | Unset): The ID of the owner user
        created_at (str | Unset): Date of creation
        updated_at (str | Unset): Date of last update
    """

    catalog_entity_checklist_id: str | Unset = UNSET
    owner_user_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_entity_checklist_id = self.catalog_entity_checklist_id

        owner_user_id = self.owner_user_id

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if catalog_entity_checklist_id is not UNSET:
            field_dict["catalog_entity_checklist_id"] = catalog_entity_checklist_id
        if owner_user_id is not UNSET:
            field_dict["owner_user_id"] = owner_user_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        catalog_entity_checklist_id = d.pop("catalog_entity_checklist_id", UNSET)

        owner_user_id = d.pop("owner_user_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        catalog_entity_checklist_checklist_owners_type_0_item_data_attributes = cls(
            catalog_entity_checklist_id=catalog_entity_checklist_id,
            owner_user_id=owner_user_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        catalog_entity_checklist_checklist_owners_type_0_item_data_attributes.additional_properties = d
        return catalog_entity_checklist_checklist_owners_type_0_item_data_attributes

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
