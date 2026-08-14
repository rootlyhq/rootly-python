from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.update_catalog_property_data_attributes_catalog_type import (
    UpdateCatalogPropertyDataAttributesCatalogType,
    check_update_catalog_property_data_attributes_catalog_type,
)
from ..models.update_catalog_property_data_attributes_kind import (
    UpdateCatalogPropertyDataAttributesKind,
    check_update_catalog_property_data_attributes_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCatalogPropertyDataAttributes")


@_attrs_define
class UpdateCatalogPropertyDataAttributes:
    """
    Attributes:
        slug (Union[None, Unset, str]): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        name (Union[Unset, str]):
        kind (Union[Unset, UpdateCatalogPropertyDataAttributesKind]):
        kind_catalog_id (Union[None, Unset, str]): Restricts values to items of specified catalog.
        position (Union[None, Unset, int]): Default position of the item when displayed in a list.
        required (Union[Unset, bool]): Whether the property is required.
        catalog_type (Union[Unset, UpdateCatalogPropertyDataAttributesCatalogType]): The type of catalog the property
            belongs to.
        external_id (Union[None, Unset, str]): An external identifier for this catalog property. Must be unique within
            the scope.
    """

    slug: Union[None, Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    kind: Union[Unset, UpdateCatalogPropertyDataAttributesKind] = UNSET
    kind_catalog_id: Union[None, Unset, str] = UNSET
    position: Union[None, Unset, int] = UNSET
    required: Union[Unset, bool] = UNSET
    catalog_type: Union[Unset, UpdateCatalogPropertyDataAttributesCatalogType] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        name = self.name

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        kind_catalog_id: Union[None, Unset, str]
        if isinstance(self.kind_catalog_id, Unset):
            kind_catalog_id = UNSET
        else:
            kind_catalog_id = self.kind_catalog_id

        position: Union[None, Unset, int]
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        required = self.required

        catalog_type: Union[Unset, str] = UNSET
        if not isinstance(self.catalog_type, Unset):
            catalog_type = self.catalog_type

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
        if kind is not UNSET:
            field_dict["kind"] = kind
        if kind_catalog_id is not UNSET:
            field_dict["kind_catalog_id"] = kind_catalog_id
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

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

        name = d.pop("name", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, UpdateCatalogPropertyDataAttributesKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_update_catalog_property_data_attributes_kind(_kind)

        def _parse_kind_catalog_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        kind_catalog_id = _parse_kind_catalog_id(d.pop("kind_catalog_id", UNSET))

        def _parse_position(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position = _parse_position(d.pop("position", UNSET))

        required = d.pop("required", UNSET)

        _catalog_type = d.pop("catalog_type", UNSET)
        catalog_type: Union[Unset, UpdateCatalogPropertyDataAttributesCatalogType]
        if isinstance(_catalog_type, Unset):
            catalog_type = UNSET
        else:
            catalog_type = check_update_catalog_property_data_attributes_catalog_type(_catalog_type)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        update_catalog_property_data_attributes = cls(
            slug=slug,
            name=name,
            kind=kind,
            kind_catalog_id=kind_catalog_id,
            position=position,
            required=required,
            catalog_type=catalog_type,
            external_id=external_id,
        )

        return update_catalog_property_data_attributes
