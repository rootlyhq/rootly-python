from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_entity_managed_by import CatalogEntityManagedBy, check_catalog_entity_managed_by
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_entity_properties_item import CatalogEntityPropertiesItem


T = TypeVar("T", bound="CatalogEntity")


@_attrs_define
class CatalogEntity:
    """
    Attributes:
        name (str):
        position (Union[None, int]): Default position of the item when displayed in a list.
        created_at (str):
        updated_at (str):
        slug (Union[Unset, str]): The slug of the catalog entity. Derived from `name`.
        description (Union[None, Unset, str]):
        public_description (Union[None, Unset, str]): The status page description of the catalog entity
        backstage_id (Union[None, Unset, str]): The Backstage entity ID this catalog entity is linked to.
        external_id (Union[None, Unset, str]): An external identifier for this catalog entity. Must be unique within the
            catalog.
        managed_by (Union[Unset, CatalogEntityManagedBy]): Which source manages this resource (read-only).
        properties (Union[Unset, list['CatalogEntityPropertiesItem']]): Array of property values for this catalog entity
    """

    name: str
    position: Union[None, int]
    created_at: str
    updated_at: str
    slug: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    public_description: Union[None, Unset, str] = UNSET
    backstage_id: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    managed_by: Union[Unset, CatalogEntityManagedBy] = UNSET
    properties: Union[Unset, list["CatalogEntityPropertiesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        position: Union[None, int]
        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

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

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        managed_by: Union[Unset, str] = UNSET
        if not isinstance(self.managed_by, Unset):
            managed_by = self.managed_by

        properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "position": position,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if public_description is not UNSET:
            field_dict["public_description"] = public_description
        if backstage_id is not UNSET:
            field_dict["backstage_id"] = backstage_id
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if managed_by is not UNSET:
            field_dict["managed_by"] = managed_by
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_entity_properties_item import CatalogEntityPropertiesItem

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_position(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        position = _parse_position(d.pop("position"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

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

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        _managed_by = d.pop("managed_by", UNSET)
        managed_by: Union[Unset, CatalogEntityManagedBy]
        if isinstance(_managed_by, Unset):
            managed_by = UNSET
        else:
            managed_by = check_catalog_entity_managed_by(_managed_by)

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = CatalogEntityPropertiesItem.from_dict(properties_item_data)

            properties.append(properties_item)

        catalog_entity = cls(
            name=name,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            description=description,
            public_description=public_description,
            backstage_id=backstage_id,
            external_id=external_id,
            managed_by=managed_by,
            properties=properties,
        )

        catalog_entity.additional_properties = d
        return catalog_entity

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
