from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_catalog_property_data_attributes_catalog_type import (
    NewCatalogPropertyDataAttributesCatalogType,
    check_new_catalog_property_data_attributes_catalog_type,
)
from ..models.new_catalog_property_data_attributes_kind import (
    NewCatalogPropertyDataAttributesKind,
    check_new_catalog_property_data_attributes_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewCatalogPropertyDataAttributes")


@_attrs_define
class NewCatalogPropertyDataAttributes:
    """
    Attributes:
        name (str):
        kind (NewCatalogPropertyDataAttributesKind):
        slug (Union[None, Unset, str]): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        kind_catalog_id (Union[None, Unset, str]): Restricts values to items of specified catalog.
        multiple (Union[Unset, bool]): Whether the attribute accepts multiple values.
        position (Union[None, Unset, int]): Default position of the item when displayed in a list.
        required (Union[Unset, bool]): Whether the property is required.
        catalog_type (Union[Unset, NewCatalogPropertyDataAttributesCatalogType]): The type of catalog the property
            belongs to.
        external_id (Union[None, Unset, str]): An external identifier for this catalog property. Must be unique within
            the scope.
    """

    name: str
    kind: NewCatalogPropertyDataAttributesKind
    slug: None | Unset | str = UNSET
    kind_catalog_id: None | Unset | str = UNSET
    multiple: Unset | bool = UNSET
    position: None | Unset | int = UNSET
    required: Unset | bool = UNSET
    catalog_type: Unset | NewCatalogPropertyDataAttributesCatalogType = UNSET
    external_id: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind: str = self.kind

        slug: None | Unset | str
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        kind_catalog_id: None | Unset | str
        if isinstance(self.kind_catalog_id, Unset):
            kind_catalog_id = UNSET
        else:
            kind_catalog_id = self.kind_catalog_id

        multiple = self.multiple

        position: None | Unset | int
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        required = self.required

        catalog_type: Unset | str = UNSET
        if not isinstance(self.catalog_type, Unset):
            catalog_type = self.catalog_type

        external_id: None | Unset | str
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "kind": kind,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if kind_catalog_id is not UNSET:
            field_dict["kind_catalog_id"] = kind_catalog_id
        if multiple is not UNSET:
            field_dict["multiple"] = multiple
        if position is not UNSET:
            field_dict["position"] = position
        if required is not UNSET:
            field_dict["required"] = required
        if catalog_type is not UNSET:
            field_dict["catalog_type"] = catalog_type
        if external_id is not UNSET:
            field_dict["external_id"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        kind = check_new_catalog_property_data_attributes_kind(d.pop("kind"))

        def _parse_slug(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_kind_catalog_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        kind_catalog_id = _parse_kind_catalog_id(d.pop("kind_catalog_id", UNSET))

        multiple = d.pop("multiple", UNSET)

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        required = d.pop("required", UNSET)

        _catalog_type = d.pop("catalog_type", UNSET)
        catalog_type: Unset | NewCatalogPropertyDataAttributesCatalogType
        if isinstance(_catalog_type, Unset):
            catalog_type = UNSET
        else:
            catalog_type = check_new_catalog_property_data_attributes_catalog_type(_catalog_type)

        def _parse_external_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        new_catalog_property_data_attributes = cls(
            name=name,
            kind=kind,
            slug=slug,
            kind_catalog_id=kind_catalog_id,
            multiple=multiple,
            position=position,
            required=required,
            catalog_type=catalog_type,
            external_id=external_id,
        )

        return new_catalog_property_data_attributes
