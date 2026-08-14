from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_catalog_data_attributes_icon import (
    NewCatalogDataAttributesIcon,
    check_new_catalog_data_attributes_icon,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewCatalogDataAttributes")


@_attrs_define
class NewCatalogDataAttributes:
    """
    Attributes:
        name (str):
        slug (Union[None, Unset, str]): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        description (Union[None, Unset, str]):
        icon (Union[Unset, NewCatalogDataAttributesIcon]):
        position (Union[None, Unset, int]): Default position of the catalog when displayed in a list.
        external_id (Union[None, Unset, str]): An external identifier for this catalog. Must be unique within the team.
    """

    name: str
    slug: None | Unset | str = UNSET
    description: None | Unset | str = UNSET
    icon: Unset | NewCatalogDataAttributesIcon = UNSET
    position: None | Unset | int = UNSET
    external_id: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

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

        icon: Unset | str = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon

        position: None | Unset | int
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        external_id: None | Unset | str
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

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
        name = d.pop("name")

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

        _icon = d.pop("icon", UNSET)
        icon: Unset | NewCatalogDataAttributesIcon
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = check_new_catalog_data_attributes_icon(_icon)

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_external_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        new_catalog_data_attributes = cls(
            name=name,
            slug=slug,
            description=description,
            icon=icon,
            position=position,
            external_id=external_id,
        )

        return new_catalog_data_attributes
