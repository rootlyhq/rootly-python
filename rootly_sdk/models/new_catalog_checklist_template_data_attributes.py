from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_catalog_checklist_template_data_attributes_catalog_type import (
    NewCatalogChecklistTemplateDataAttributesCatalogType,
    check_new_catalog_checklist_template_data_attributes_catalog_type,
)
from ..models.new_catalog_checklist_template_data_attributes_scope_type import (
    NewCatalogChecklistTemplateDataAttributesScopeType,
    check_new_catalog_checklist_template_data_attributes_scope_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_catalog_checklist_template_data_attributes_builtin_field import (
        NewCatalogChecklistTemplateDataAttributesBuiltinField,
    )
    from ..models.new_catalog_checklist_template_data_attributes_custom_field import (
        NewCatalogChecklistTemplateDataAttributesCustomField,
    )
    from ..models.new_catalog_checklist_template_data_attributes_owners_type_0_item import (
        NewCatalogChecklistTemplateDataAttributesOwnersType0Item,
    )


T = TypeVar("T", bound="NewCatalogChecklistTemplateDataAttributes")


@_attrs_define
class NewCatalogChecklistTemplateDataAttributes:
    """
    Attributes:
        name (str): The name of the checklist template
        catalog_type (NewCatalogChecklistTemplateDataAttributesCatalogType): The catalog type
        scope_type (NewCatalogChecklistTemplateDataAttributesScopeType): The scope type
        description (None | str | Unset): The description of the checklist template
        scope_id (str | Unset): The scope ID (team or catalog UUID)
        fields (list[NewCatalogChecklistTemplateDataAttributesBuiltinField |
            NewCatalogChecklistTemplateDataAttributesCustomField] | None | Unset): Template fields. Position is determined
            by array order.
        owners (list[NewCatalogChecklistTemplateDataAttributesOwnersType0Item] | None | Unset): Template owners
    """

    name: str
    catalog_type: NewCatalogChecklistTemplateDataAttributesCatalogType
    scope_type: NewCatalogChecklistTemplateDataAttributesScopeType
    description: None | str | Unset = UNSET
    scope_id: str | Unset = UNSET
    fields: (
        list[
            NewCatalogChecklistTemplateDataAttributesBuiltinField | NewCatalogChecklistTemplateDataAttributesCustomField
        ]
        | None
        | Unset
    ) = UNSET
    owners: list[NewCatalogChecklistTemplateDataAttributesOwnersType0Item] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_catalog_checklist_template_data_attributes_builtin_field import (
            NewCatalogChecklistTemplateDataAttributesBuiltinField,
        )

        name = self.name

        catalog_type: str = self.catalog_type

        scope_type: str = self.scope_type

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        scope_id = self.scope_id

        fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = []
            for fields_type_0_item_data in self.fields:
                fields_type_0_item: dict[str, Any]
                if isinstance(fields_type_0_item_data, NewCatalogChecklistTemplateDataAttributesBuiltinField):
                    fields_type_0_item = fields_type_0_item_data.to_dict()
                else:
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

        field_dict.update(
            {
                "name": name,
                "catalog_type": catalog_type,
                "scope_type": scope_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if scope_id is not UNSET:
            field_dict["scope_id"] = scope_id
        if fields is not UNSET:
            field_dict["fields"] = fields
        if owners is not UNSET:
            field_dict["owners"] = owners

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_catalog_checklist_template_data_attributes_builtin_field import (
            NewCatalogChecklistTemplateDataAttributesBuiltinField,
        )
        from ..models.new_catalog_checklist_template_data_attributes_custom_field import (
            NewCatalogChecklistTemplateDataAttributesCustomField,
        )
        from ..models.new_catalog_checklist_template_data_attributes_owners_type_0_item import (
            NewCatalogChecklistTemplateDataAttributesOwnersType0Item,
        )

        d = dict(src_dict)
        name = d.pop("name")

        catalog_type = check_new_catalog_checklist_template_data_attributes_catalog_type(d.pop("catalog_type"))

        scope_type = check_new_catalog_checklist_template_data_attributes_scope_type(d.pop("scope_type"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        scope_id = d.pop("scope_id", UNSET)

        def _parse_fields(
            data: object,
        ) -> (
            list[
                NewCatalogChecklistTemplateDataAttributesBuiltinField
                | NewCatalogChecklistTemplateDataAttributesCustomField
            ]
            | None
            | Unset
        ):
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

                    def _parse_fields_type_0_item(
                        data: object,
                    ) -> (
                        NewCatalogChecklistTemplateDataAttributesBuiltinField
                        | NewCatalogChecklistTemplateDataAttributesCustomField
                    ):
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            fields_type_0_item_builtin_field = (
                                NewCatalogChecklistTemplateDataAttributesBuiltinField.from_dict(data)
                            )

                            return fields_type_0_item_builtin_field
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        fields_type_0_item_custom_field = (
                            NewCatalogChecklistTemplateDataAttributesCustomField.from_dict(data)
                        )

                        return fields_type_0_item_custom_field

                    fields_type_0_item = _parse_fields_type_0_item(fields_type_0_item_data)

                    fields_type_0.append(fields_type_0_item)

                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    NewCatalogChecklistTemplateDataAttributesBuiltinField
                    | NewCatalogChecklistTemplateDataAttributesCustomField
                ]
                | None
                | Unset,
                data,
            )

        fields = _parse_fields(d.pop("fields", UNSET))

        def _parse_owners(
            data: object,
        ) -> list[NewCatalogChecklistTemplateDataAttributesOwnersType0Item] | None | Unset:
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
                    owners_type_0_item = NewCatalogChecklistTemplateDataAttributesOwnersType0Item.from_dict(
                        owners_type_0_item_data
                    )

                    owners_type_0.append(owners_type_0_item)

                return owners_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NewCatalogChecklistTemplateDataAttributesOwnersType0Item] | None | Unset, data)

        owners = _parse_owners(d.pop("owners", UNSET))

        new_catalog_checklist_template_data_attributes = cls(
            name=name,
            catalog_type=catalog_type,
            scope_type=scope_type,
            description=description,
            scope_id=scope_id,
            fields=fields,
            owners=owners,
        )

        return new_catalog_checklist_template_data_attributes
