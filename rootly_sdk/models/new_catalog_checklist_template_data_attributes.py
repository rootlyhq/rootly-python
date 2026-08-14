from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
        slug (Union[None, Unset, str]): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        description (Union[None, Unset, str]): The description of the checklist template
        scope_id (Union[Unset, str]): The scope ID (team or catalog UUID)
        fields (Union[None, Unset, list[Union['NewCatalogChecklistTemplateDataAttributesBuiltinField',
            'NewCatalogChecklistTemplateDataAttributesCustomField']]]): Template fields. Position is determined by array
            order.
        owners (Union[None, Unset, list['NewCatalogChecklistTemplateDataAttributesOwnersType0Item']]): Template owners
    """

    name: str
    catalog_type: NewCatalogChecklistTemplateDataAttributesCatalogType
    scope_type: NewCatalogChecklistTemplateDataAttributesScopeType
    slug: None | Unset | str = UNSET
    description: None | Unset | str = UNSET
    scope_id: Unset | str = UNSET
    fields: (
        None
        | Unset
        | list[
            Union[
                "NewCatalogChecklistTemplateDataAttributesBuiltinField",
                "NewCatalogChecklistTemplateDataAttributesCustomField",
            ]
        ]
    ) = UNSET
    owners: None | Unset | list["NewCatalogChecklistTemplateDataAttributesOwnersType0Item"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_catalog_checklist_template_data_attributes_builtin_field import (
            NewCatalogChecklistTemplateDataAttributesBuiltinField,
        )

        name = self.name

        catalog_type: str = self.catalog_type

        scope_type: str = self.scope_type

        slug: None | Unset | str
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        scope_id = self.scope_id

        fields: None | Unset | list[dict[str, Any]]
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

        owners: None | Unset | list[dict[str, Any]]
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
        if slug is not UNSET:
            field_dict["slug"] = slug
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

        def _parse_slug(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        scope_id = d.pop("scope_id", UNSET)

        def _parse_fields(
            data: object,
        ) -> (
            None
            | Unset
            | list[
                Union[
                    "NewCatalogChecklistTemplateDataAttributesBuiltinField",
                    "NewCatalogChecklistTemplateDataAttributesCustomField",
                ]
            ]
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
                    ) -> Union[
                        "NewCatalogChecklistTemplateDataAttributesBuiltinField",
                        "NewCatalogChecklistTemplateDataAttributesCustomField",
                    ]:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            fields_type_0_item_builtin_field = (
                                NewCatalogChecklistTemplateDataAttributesBuiltinField.from_dict(data)
                            )

                            return fields_type_0_item_builtin_field
                        except:  # noqa: E722
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
            except:  # noqa: E722
                pass
            return cast(
                None
                | Unset
                | list[
                    Union[
                        "NewCatalogChecklistTemplateDataAttributesBuiltinField",
                        "NewCatalogChecklistTemplateDataAttributesCustomField",
                    ]
                ],
                data,
            )

        fields = _parse_fields(d.pop("fields", UNSET))

        def _parse_owners(
            data: object,
        ) -> None | Unset | list["NewCatalogChecklistTemplateDataAttributesOwnersType0Item"]:
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
            except:  # noqa: E722
                pass
            return cast(None | Unset | list["NewCatalogChecklistTemplateDataAttributesOwnersType0Item"], data)

        owners = _parse_owners(d.pop("owners", UNSET))

        new_catalog_checklist_template_data_attributes = cls(
            name=name,
            catalog_type=catalog_type,
            scope_type=scope_type,
            slug=slug,
            description=description,
            scope_id=scope_id,
            fields=fields,
            owners=owners,
        )

        return new_catalog_checklist_template_data_attributes
