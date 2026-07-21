from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_catalog_checklist_template_data_attributes_builtin_field import (
        UpdateCatalogChecklistTemplateDataAttributesBuiltinField,
    )
    from ..models.update_catalog_checklist_template_data_attributes_custom_field import (
        UpdateCatalogChecklistTemplateDataAttributesCustomField,
    )
    from ..models.update_catalog_checklist_template_data_attributes_owners_type_0_item import (
        UpdateCatalogChecklistTemplateDataAttributesOwnersType0Item,
    )


T = TypeVar("T", bound="UpdateCatalogChecklistTemplateDataAttributes")


@_attrs_define
class UpdateCatalogChecklistTemplateDataAttributes:
    """
    Attributes:
        name (str | Unset): The name of the checklist template
        description (None | str | Unset): The description of the checklist template
        fields (list[UpdateCatalogChecklistTemplateDataAttributesBuiltinField |
            UpdateCatalogChecklistTemplateDataAttributesCustomField] | None | Unset): Template fields. Position is
            determined by array order. Replaces all existing fields.
        owners (list[UpdateCatalogChecklistTemplateDataAttributesOwnersType0Item] | None | Unset): Template owners.
            Replaces all existing owners.
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    fields: (
        list[
            UpdateCatalogChecklistTemplateDataAttributesBuiltinField
            | UpdateCatalogChecklistTemplateDataAttributesCustomField
        ]
        | None
        | Unset
    ) = UNSET
    owners: list[UpdateCatalogChecklistTemplateDataAttributesOwnersType0Item] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_catalog_checklist_template_data_attributes_builtin_field import (
            UpdateCatalogChecklistTemplateDataAttributesBuiltinField,
        )

        name = self.name

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
                fields_type_0_item: dict[str, Any]
                if isinstance(fields_type_0_item_data, UpdateCatalogChecklistTemplateDataAttributesBuiltinField):
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

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if fields is not UNSET:
            field_dict["fields"] = fields
        if owners is not UNSET:
            field_dict["owners"] = owners

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_catalog_checklist_template_data_attributes_builtin_field import (
            UpdateCatalogChecklistTemplateDataAttributesBuiltinField,
        )
        from ..models.update_catalog_checklist_template_data_attributes_custom_field import (
            UpdateCatalogChecklistTemplateDataAttributesCustomField,
        )
        from ..models.update_catalog_checklist_template_data_attributes_owners_type_0_item import (
            UpdateCatalogChecklistTemplateDataAttributesOwnersType0Item,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_fields(
            data: object,
        ) -> (
            list[
                UpdateCatalogChecklistTemplateDataAttributesBuiltinField
                | UpdateCatalogChecklistTemplateDataAttributesCustomField
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
                        UpdateCatalogChecklistTemplateDataAttributesBuiltinField
                        | UpdateCatalogChecklistTemplateDataAttributesCustomField
                    ):
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            fields_type_0_item_builtin_field = (
                                UpdateCatalogChecklistTemplateDataAttributesBuiltinField.from_dict(data)
                            )

                            return fields_type_0_item_builtin_field
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        fields_type_0_item_custom_field = (
                            UpdateCatalogChecklistTemplateDataAttributesCustomField.from_dict(data)
                        )

                        return fields_type_0_item_custom_field

                    fields_type_0_item = _parse_fields_type_0_item(fields_type_0_item_data)

                    fields_type_0.append(fields_type_0_item)

                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    UpdateCatalogChecklistTemplateDataAttributesBuiltinField
                    | UpdateCatalogChecklistTemplateDataAttributesCustomField
                ]
                | None
                | Unset,
                data,
            )

        fields = _parse_fields(d.pop("fields", UNSET))

        def _parse_owners(
            data: object,
        ) -> list[UpdateCatalogChecklistTemplateDataAttributesOwnersType0Item] | None | Unset:
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
                    owners_type_0_item = UpdateCatalogChecklistTemplateDataAttributesOwnersType0Item.from_dict(
                        owners_type_0_item_data
                    )

                    owners_type_0.append(owners_type_0_item)

                return owners_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UpdateCatalogChecklistTemplateDataAttributesOwnersType0Item] | None | Unset, data)

        owners = _parse_owners(d.pop("owners", UNSET))

        update_catalog_checklist_template_data_attributes = cls(
            name=name,
            description=description,
            fields=fields,
            owners=owners,
        )

        return update_catalog_checklist_template_data_attributes
