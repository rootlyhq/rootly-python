from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_catalog_entity_data_attributes_properties_item import NewCatalogEntityDataAttributesPropertiesItem


T = TypeVar("T", bound="NewCatalogEntityDataAttributes")


@_attrs_define
class NewCatalogEntityDataAttributes:
    """
    Attributes:
        name (str):
        slug (Union[None, Unset, str]): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        description (Union[None, Unset, str]):
        public_description (Union[None, Unset, str]): The status page description of the catalog entity
        position (Union[None, Unset, int]): Default position of the item when displayed in a list.
        backstage_id (Union[None, Unset, str]): The Backstage entity ID this catalog entity is linked to.
        external_id (Union[None, Unset, str]): An external identifier for this catalog entity. Must be unique within the
            catalog.
        properties (Union[Unset, list['NewCatalogEntityDataAttributesPropertiesItem']]): Array of property values for
            this catalog entity
    """

    name: str
    slug: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    public_description: Union[None, Unset, str] = UNSET
    position: Union[None, Unset, int] = UNSET
    backstage_id: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    properties: Union[Unset, list["NewCatalogEntityDataAttributesPropertiesItem"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
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

        position: Union[None, Unset, int]
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

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

        properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if public_description is not UNSET:
            field_dict["public_description"] = public_description
        if position is not UNSET:
            field_dict["position"] = position
        if backstage_id is not UNSET:
            field_dict["backstage_id"] = backstage_id
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_catalog_entity_data_attributes_properties_item import (
            NewCatalogEntityDataAttributesPropertiesItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

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

        def _parse_position(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position = _parse_position(d.pop("position", UNSET))

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

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = NewCatalogEntityDataAttributesPropertiesItem.from_dict(properties_item_data)

            properties.append(properties_item)

        new_catalog_entity_data_attributes = cls(
            name=name,
            slug=slug,
            description=description,
            public_description=public_description,
            position=position,
            backstage_id=backstage_id,
            external_id=external_id,
            properties=properties,
        )

        return new_catalog_entity_data_attributes
