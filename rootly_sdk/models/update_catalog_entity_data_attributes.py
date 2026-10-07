from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_catalog_entity_data_attributes_properties_item import (
        UpdateCatalogEntityDataAttributesPropertiesItem,
    )


T = TypeVar("T", bound="UpdateCatalogEntityDataAttributes")


@_attrs_define
class UpdateCatalogEntityDataAttributes:
    """
    Attributes:
        slug (None | str | Unset): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        name (str | Unset):
        description (None | str | Unset):
        public_description (None | str | Unset): The status page description of the catalog entity
        position (int | None | Unset): Default position of the item when displayed in a list.
        backstage_id (None | str | Unset): The Backstage entity ID this catalog entity is linked to.
        external_id (None | str | Unset): An external identifier for this catalog entity. Must be unique within the
            catalog.
        properties (list[UpdateCatalogEntityDataAttributesPropertiesItem] | Unset): Array of property values for this
            catalog entity
    """

    slug: None | str | Unset = UNSET
    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    public_description: None | str | Unset = UNSET
    position: int | None | Unset = UNSET
    backstage_id: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    properties: list[UpdateCatalogEntityDataAttributesPropertiesItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        public_description: None | str | Unset
        if isinstance(self.public_description, Unset):
            public_description = UNSET
        else:
            public_description = self.public_description

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        backstage_id: None | str | Unset
        if isinstance(self.backstage_id, Unset):
            backstage_id = UNSET
        else:
            backstage_id = self.backstage_id

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
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
        from ..models.update_catalog_entity_data_attributes_properties_item import (
            UpdateCatalogEntityDataAttributesPropertiesItem,
        )

        d = dict(src_dict)

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_public_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_description = _parse_public_description(d.pop("public_description", UNSET))

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_backstage_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backstage_id = _parse_backstage_id(d.pop("backstage_id", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        _properties = d.pop("properties", UNSET)
        properties: list[UpdateCatalogEntityDataAttributesPropertiesItem] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = UpdateCatalogEntityDataAttributesPropertiesItem.from_dict(properties_item_data)

                properties.append(properties_item)

        update_catalog_entity_data_attributes = cls(
            slug=slug,
            name=name,
            description=description,
            public_description=public_description,
            position=position,
            backstage_id=backstage_id,
            external_id=external_id,
            properties=properties,
        )

        return update_catalog_entity_data_attributes
