from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_entity_checklist_checklist_fields_type_0_item_data_attributes_value_snapshot_type_0 import (
        CatalogEntityChecklistChecklistFieldsType0ItemDataAttributesValueSnapshotType0,
    )


T = TypeVar("T", bound="CatalogEntityChecklistChecklistFieldsType0ItemDataAttributes")


@_attrs_define
class CatalogEntityChecklistChecklistFieldsType0ItemDataAttributes:
    """
    Attributes:
        catalog_entity_checklist_id (str | Unset): The ID of the parent checklist
        catalog_checklist_template_field_id (None | str | Unset): The ID of the template field
        field_key (str | Unset): The field key
        checked (bool | Unset): Whether the field is checked
        value_snapshot (CatalogEntityChecklistChecklistFieldsType0ItemDataAttributesValueSnapshotType0 | None | Unset):
            The value snapshot at time of checking
        completed_by_user_id (None | str | Unset): The ID of the user who checked the field
        completed_at (None | str | Unset): When the field was checked
        created_at (str | Unset): Date of creation
        updated_at (str | Unset): Date of last update
    """

    catalog_entity_checklist_id: str | Unset = UNSET
    catalog_checklist_template_field_id: None | str | Unset = UNSET
    field_key: str | Unset = UNSET
    checked: bool | Unset = UNSET
    value_snapshot: CatalogEntityChecklistChecklistFieldsType0ItemDataAttributesValueSnapshotType0 | None | Unset = (
        UNSET
    )
    completed_by_user_id: None | str | Unset = UNSET
    completed_at: None | str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.catalog_entity_checklist_checklist_fields_type_0_item_data_attributes_value_snapshot_type_0 import (
            CatalogEntityChecklistChecklistFieldsType0ItemDataAttributesValueSnapshotType0,
        )

        catalog_entity_checklist_id = self.catalog_entity_checklist_id

        catalog_checklist_template_field_id: None | str | Unset
        if isinstance(self.catalog_checklist_template_field_id, Unset):
            catalog_checklist_template_field_id = UNSET
        else:
            catalog_checklist_template_field_id = self.catalog_checklist_template_field_id

        field_key = self.field_key

        checked = self.checked

        value_snapshot: dict[str, Any] | None | Unset
        if isinstance(self.value_snapshot, Unset):
            value_snapshot = UNSET
        elif isinstance(
            self.value_snapshot, CatalogEntityChecklistChecklistFieldsType0ItemDataAttributesValueSnapshotType0
        ):
            value_snapshot = self.value_snapshot.to_dict()
        else:
            value_snapshot = self.value_snapshot

        completed_by_user_id: None | str | Unset
        if isinstance(self.completed_by_user_id, Unset):
            completed_by_user_id = UNSET
        else:
            completed_by_user_id = self.completed_by_user_id

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = self.completed_at

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if catalog_entity_checklist_id is not UNSET:
            field_dict["catalog_entity_checklist_id"] = catalog_entity_checklist_id
        if catalog_checklist_template_field_id is not UNSET:
            field_dict["catalog_checklist_template_field_id"] = catalog_checklist_template_field_id
        if field_key is not UNSET:
            field_dict["field_key"] = field_key
        if checked is not UNSET:
            field_dict["checked"] = checked
        if value_snapshot is not UNSET:
            field_dict["value_snapshot"] = value_snapshot
        if completed_by_user_id is not UNSET:
            field_dict["completed_by_user_id"] = completed_by_user_id
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_entity_checklist_checklist_fields_type_0_item_data_attributes_value_snapshot_type_0 import (
            CatalogEntityChecklistChecklistFieldsType0ItemDataAttributesValueSnapshotType0,
        )

        d = dict(src_dict)
        catalog_entity_checklist_id = d.pop("catalog_entity_checklist_id", UNSET)

        def _parse_catalog_checklist_template_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        catalog_checklist_template_field_id = _parse_catalog_checklist_template_field_id(
            d.pop("catalog_checklist_template_field_id", UNSET)
        )

        field_key = d.pop("field_key", UNSET)

        checked = d.pop("checked", UNSET)

        def _parse_value_snapshot(
            data: object,
        ) -> CatalogEntityChecklistChecklistFieldsType0ItemDataAttributesValueSnapshotType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_snapshot_type_0 = (
                    CatalogEntityChecklistChecklistFieldsType0ItemDataAttributesValueSnapshotType0.from_dict(data)
                )

                return value_snapshot_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CatalogEntityChecklistChecklistFieldsType0ItemDataAttributesValueSnapshotType0 | None | Unset, data
            )

        value_snapshot = _parse_value_snapshot(d.pop("value_snapshot", UNSET))

        def _parse_completed_by_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completed_by_user_id = _parse_completed_by_user_id(d.pop("completed_by_user_id", UNSET))

        def _parse_completed_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        catalog_entity_checklist_checklist_fields_type_0_item_data_attributes = cls(
            catalog_entity_checklist_id=catalog_entity_checklist_id,
            catalog_checklist_template_field_id=catalog_checklist_template_field_id,
            field_key=field_key,
            checked=checked,
            value_snapshot=value_snapshot,
            completed_by_user_id=completed_by_user_id,
            completed_at=completed_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        catalog_entity_checklist_checklist_fields_type_0_item_data_attributes.additional_properties = d
        return catalog_entity_checklist_checklist_fields_type_0_item_data_attributes

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
