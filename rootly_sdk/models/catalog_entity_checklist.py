from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_entity_checklist_auditable_type import (
    CatalogEntityChecklistAuditableType,
    check_catalog_entity_checklist_auditable_type,
)
from ..models.catalog_entity_checklist_status import CatalogEntityChecklistStatus, check_catalog_entity_checklist_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_entity_checklist_checklist_fields_type_0_item import (
        CatalogEntityChecklistChecklistFieldsType0Item,
    )
    from ..models.catalog_entity_checklist_checklist_owners_type_0_item import (
        CatalogEntityChecklistChecklistOwnersType0Item,
    )


T = TypeVar("T", bound="CatalogEntityChecklist")


@_attrs_define
class CatalogEntityChecklist:
    """
    Attributes:
        catalog_checklist_template_id (str): The ID of the checklist template
        auditable_type (CatalogEntityChecklistAuditableType): The type of the auditable entity
        auditable_id (str): The ID of the auditable entity
        status (CatalogEntityChecklistStatus): The status of the checklist
        created_at (str): Date of creation
        updated_at (str): Date of last update
        started_at (None | str | Unset): When the checklist was started
        completed_at (None | str | Unset): When the checklist was completed
        completed_by_user_id (None | str | Unset): The ID of the user who completed the checklist
        checklist_fields (list[CatalogEntityChecklistChecklistFieldsType0Item] | None | Unset): Checklist fields
        checklist_owners (list[CatalogEntityChecklistChecklistOwnersType0Item] | None | Unset): Checklist owners
    """

    catalog_checklist_template_id: str
    auditable_type: CatalogEntityChecklistAuditableType
    auditable_id: str
    status: CatalogEntityChecklistStatus
    created_at: str
    updated_at: str
    started_at: None | str | Unset = UNSET
    completed_at: None | str | Unset = UNSET
    completed_by_user_id: None | str | Unset = UNSET
    checklist_fields: list[CatalogEntityChecklistChecklistFieldsType0Item] | None | Unset = UNSET
    checklist_owners: list[CatalogEntityChecklistChecklistOwnersType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_checklist_template_id = self.catalog_checklist_template_id

        auditable_type: str = self.auditable_type

        auditable_id = self.auditable_id

        status: str = self.status

        created_at = self.created_at

        updated_at = self.updated_at

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = self.completed_at

        completed_by_user_id: None | str | Unset
        if isinstance(self.completed_by_user_id, Unset):
            completed_by_user_id = UNSET
        else:
            completed_by_user_id = self.completed_by_user_id

        checklist_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.checklist_fields, Unset):
            checklist_fields = UNSET
        elif isinstance(self.checklist_fields, list):
            checklist_fields = []
            for checklist_fields_type_0_item_data in self.checklist_fields:
                checklist_fields_type_0_item = checklist_fields_type_0_item_data.to_dict()
                checklist_fields.append(checklist_fields_type_0_item)

        else:
            checklist_fields = self.checklist_fields

        checklist_owners: list[dict[str, Any]] | None | Unset
        if isinstance(self.checklist_owners, Unset):
            checklist_owners = UNSET
        elif isinstance(self.checklist_owners, list):
            checklist_owners = []
            for checklist_owners_type_0_item_data in self.checklist_owners:
                checklist_owners_type_0_item = checklist_owners_type_0_item_data.to_dict()
                checklist_owners.append(checklist_owners_type_0_item)

        else:
            checklist_owners = self.checklist_owners

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_checklist_template_id": catalog_checklist_template_id,
                "auditable_type": auditable_type,
                "auditable_id": auditable_id,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if completed_by_user_id is not UNSET:
            field_dict["completed_by_user_id"] = completed_by_user_id
        if checklist_fields is not UNSET:
            field_dict["checklist_fields"] = checklist_fields
        if checklist_owners is not UNSET:
            field_dict["checklist_owners"] = checklist_owners

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_entity_checklist_checklist_fields_type_0_item import (
            CatalogEntityChecklistChecklistFieldsType0Item,
        )
        from ..models.catalog_entity_checklist_checklist_owners_type_0_item import (
            CatalogEntityChecklistChecklistOwnersType0Item,
        )

        d = dict(src_dict)
        catalog_checklist_template_id = d.pop("catalog_checklist_template_id")

        auditable_type = check_catalog_entity_checklist_auditable_type(d.pop("auditable_type"))

        auditable_id = d.pop("auditable_id")

        status = check_catalog_entity_checklist_status(d.pop("status"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_started_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_completed_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        def _parse_completed_by_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completed_by_user_id = _parse_completed_by_user_id(d.pop("completed_by_user_id", UNSET))

        def _parse_checklist_fields(
            data: object,
        ) -> list[CatalogEntityChecklistChecklistFieldsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                checklist_fields_type_0 = []
                _checklist_fields_type_0 = data
                for checklist_fields_type_0_item_data in _checklist_fields_type_0:
                    checklist_fields_type_0_item = CatalogEntityChecklistChecklistFieldsType0Item.from_dict(
                        checklist_fields_type_0_item_data
                    )

                    checklist_fields_type_0.append(checklist_fields_type_0_item)

                return checklist_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CatalogEntityChecklistChecklistFieldsType0Item] | None | Unset, data)

        checklist_fields = _parse_checklist_fields(d.pop("checklist_fields", UNSET))

        def _parse_checklist_owners(
            data: object,
        ) -> list[CatalogEntityChecklistChecklistOwnersType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                checklist_owners_type_0 = []
                _checklist_owners_type_0 = data
                for checklist_owners_type_0_item_data in _checklist_owners_type_0:
                    checklist_owners_type_0_item = CatalogEntityChecklistChecklistOwnersType0Item.from_dict(
                        checklist_owners_type_0_item_data
                    )

                    checklist_owners_type_0.append(checklist_owners_type_0_item)

                return checklist_owners_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CatalogEntityChecklistChecklistOwnersType0Item] | None | Unset, data)

        checklist_owners = _parse_checklist_owners(d.pop("checklist_owners", UNSET))

        catalog_entity_checklist = cls(
            catalog_checklist_template_id=catalog_checklist_template_id,
            auditable_type=auditable_type,
            auditable_id=auditable_id,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            started_at=started_at,
            completed_at=completed_at,
            completed_by_user_id=completed_by_user_id,
            checklist_fields=checklist_fields,
            checklist_owners=checklist_owners,
        )

        catalog_entity_checklist.additional_properties = d
        return catalog_entity_checklist

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
