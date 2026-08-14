from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
        name (Union[Unset, str]): Required for new entities. Optional for updates (managed-fields: omitted attributes
            are preserved).
        description (Union[None, Unset, str]):
        public_description (Union[None, Unset, str]):
        backstage_id (Union[None, Unset, str]):
        fields (Union[Unset, list['BulkUpsertCatalogEntitiesEntitiesItemFieldsItem']]): Property values for this entity.
            Only mentioned fields are written; unmentioned fields are preserved.
    """

    external_id: str
    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    public_description: Union[None, Unset, str] = UNSET
    backstage_id: Union[None, Unset, str] = UNSET
    fields: Union[Unset, list["BulkUpsertCatalogEntitiesEntitiesItemFieldsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        public_description: Union[None, Unset, str]
        if isinstance(self.public_description, Unset):
            public_description = UNSET
        else:
            public_description = self.public_description

        backstage_id: Union[None, Unset, str]
        if isinstance(self.backstage_id, Unset):
            backstage_id = UNSET
        else:
            backstage_id = self.backstage_id

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
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

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_public_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        public_description = _parse_public_description(d.pop("public_description", UNSET))

        def _parse_backstage_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backstage_id = _parse_backstage_id(d.pop("backstage_id", UNSET))

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
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
