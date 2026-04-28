from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_checklist_template_catalog_type import (
    CatalogChecklistTemplateCatalogType,
    check_catalog_checklist_template_catalog_type,
)
from ..models.catalog_checklist_template_scope_type import (
    CatalogChecklistTemplateScopeType,
    check_catalog_checklist_template_scope_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_checklist_template_fields_type_0_item import CatalogChecklistTemplateFieldsType0Item
    from ..models.catalog_checklist_template_owners_type_0_item import CatalogChecklistTemplateOwnersType0Item


T = TypeVar("T", bound="CatalogChecklistTemplate")


@_attrs_define
class CatalogChecklistTemplate:
    """
    Attributes:
        name (str): The name of the checklist template
        catalog_type (CatalogChecklistTemplateCatalogType): The catalog type
        scope_type (CatalogChecklistTemplateScopeType): The scope type
        scope_id (str): The scope ID
        created_at (str): Date of creation
        updated_at (str): Date of last update
        slug (str | Unset): The slug of the checklist template
        description (None | str | Unset): The description of the checklist template
        fields (list[CatalogChecklistTemplateFieldsType0Item] | None | Unset): Template fields in position order
        owners (list[CatalogChecklistTemplateOwnersType0Item] | None | Unset): Template owners
    """

    name: str
    catalog_type: CatalogChecklistTemplateCatalogType
    scope_type: CatalogChecklistTemplateScopeType
    scope_id: str
    created_at: str
    updated_at: str
    slug: str | Unset = UNSET
    description: None | str | Unset = UNSET
    fields: list[CatalogChecklistTemplateFieldsType0Item] | None | Unset = UNSET
    owners: list[CatalogChecklistTemplateOwnersType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        catalog_type: str = self.catalog_type

        scope_type: str = self.scope_type

        scope_id = self.scope_id

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = []
            for fields_type_0_item_data in self.fields:
                fields_type_0_item = fields_type_0_item_data.to_dict()
                fields.append(fields_type_0_item)

        else:
            fields = self.fields

        owners: list[dict[str, Any]] | None | Unset
        if isinstance(self.owners, Unset):
            owners = UNSET
        elif isinstance(self.owners, list):
            owners = []
            for owners_type_0_item_data in self.owners:
                owners_type_0_item = owners_type_0_item_data.to_dict()
                owners.append(owners_type_0_item)

        else:
            owners = self.owners

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "catalog_type": catalog_type,
                "scope_type": scope_type,
                "scope_id": scope_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if fields is not UNSET:
            field_dict["fields"] = fields
        if owners is not UNSET:
            field_dict["owners"] = owners

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_checklist_template_fields_type_0_item import CatalogChecklistTemplateFieldsType0Item
        from ..models.catalog_checklist_template_owners_type_0_item import CatalogChecklistTemplateOwnersType0Item

        d = dict(src_dict)
        name = d.pop("name")

        catalog_type = check_catalog_checklist_template_catalog_type(d.pop("catalog_type"))

        scope_type = check_catalog_checklist_template_scope_type(d.pop("scope_type"))

        scope_id = d.pop("scope_id")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_fields(data: object) -> list[CatalogChecklistTemplateFieldsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_0 = []
                _fields_type_0 = data
                for fields_type_0_item_data in _fields_type_0:
                    fields_type_0_item = CatalogChecklistTemplateFieldsType0Item.from_dict(fields_type_0_item_data)

                    fields_type_0.append(fields_type_0_item)

                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CatalogChecklistTemplateFieldsType0Item] | None | Unset, data)

        fields = _parse_fields(d.pop("fields", UNSET))

        def _parse_owners(data: object) -> list[CatalogChecklistTemplateOwnersType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owners_type_0 = []
                _owners_type_0 = data
                for owners_type_0_item_data in _owners_type_0:
                    owners_type_0_item = CatalogChecklistTemplateOwnersType0Item.from_dict(owners_type_0_item_data)

                    owners_type_0.append(owners_type_0_item)

                return owners_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CatalogChecklistTemplateOwnersType0Item] | None | Unset, data)

        owners = _parse_owners(d.pop("owners", UNSET))

        catalog_checklist_template = cls(
            name=name,
            catalog_type=catalog_type,
            scope_type=scope_type,
            scope_id=scope_id,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            description=description,
            fields=fields,
            owners=owners,
        )

        catalog_checklist_template.additional_properties = d
        return catalog_checklist_template

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
