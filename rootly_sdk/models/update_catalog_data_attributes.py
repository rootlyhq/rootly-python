from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.update_catalog_data_attributes_icon import (
    UpdateCatalogDataAttributesIcon,
    check_update_catalog_data_attributes_icon,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCatalogDataAttributes")


@_attrs_define
class UpdateCatalogDataAttributes:
    """
    Attributes:
        slug (Union[None, Unset, str]): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        icon (Union[Unset, UpdateCatalogDataAttributesIcon]):
        position (Union[None, Unset, int]): Default position of the catalog when displayed in a list.
        external_id (Union[None, Unset, str]): An external identifier for this catalog. Must be unique within the team.
    """

    slug: Union[None, Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    icon: Union[Unset, UpdateCatalogDataAttributesIcon] = UNSET
    position: Union[None, Unset, int] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        icon: Union[Unset, str] = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon

        position: Union[None, Unset, int]
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if icon is not UNSET:
            field_dict["icon"] = icon
        if position is not UNSET:
            field_dict["position"] = position
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _icon = d.pop("icon", UNSET)
        icon: Union[Unset, UpdateCatalogDataAttributesIcon]
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = check_update_catalog_data_attributes_icon(_icon)

        def _parse_position(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        update_catalog_data_attributes = cls(
            slug=slug,
            name=name,
            description=description,
            icon=icon,
            position=position,
            external_id=external_id,
        )

        return update_catalog_data_attributes
