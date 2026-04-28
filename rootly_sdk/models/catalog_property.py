from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_property_catalog_type import CatalogPropertyCatalogType, check_catalog_property_catalog_type
from ..models.catalog_property_kind import CatalogPropertyKind, check_catalog_property_kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogProperty")


@_attrs_define
class CatalogProperty:
    """
    Attributes:
        catalog_id (None | str):
        name (str):
        kind (CatalogPropertyKind):
        multiple (bool): Whether the attribute accepts multiple values.
        position (int | None): Default position of the item when displayed in a list.
        created_at (str):
        updated_at (str):
        slug (str | Unset):
        kind_catalog_id (None | str | Unset): Restricts values to items of specified catalog.
        required (bool | Unset): Whether the property is required.
        catalog_type (CatalogPropertyCatalogType | Unset): The type of catalog the property belongs to.
    """

    catalog_id: None | str
    name: str
    kind: CatalogPropertyKind
    multiple: bool
    position: int | None
    created_at: str
    updated_at: str
    slug: str | Unset = UNSET
    kind_catalog_id: None | str | Unset = UNSET
    required: bool | Unset = UNSET
    catalog_type: CatalogPropertyCatalogType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_id: None | str
        catalog_id = self.catalog_id

        name = self.name

        kind: str = self.kind

        multiple = self.multiple

        position: int | None
        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        kind_catalog_id: None | str | Unset
        if isinstance(self.kind_catalog_id, Unset):
            kind_catalog_id = UNSET
        else:
            kind_catalog_id = self.kind_catalog_id

        required = self.required

        catalog_type: str | Unset = UNSET
        if not isinstance(self.catalog_type, Unset):
            catalog_type = self.catalog_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_id": catalog_id,
                "name": name,
                "kind": kind,
                "multiple": multiple,
                "position": position,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if kind_catalog_id is not UNSET:
            field_dict["kind_catalog_id"] = kind_catalog_id
        if required is not UNSET:
            field_dict["required"] = required
        if catalog_type is not UNSET:
            field_dict["catalog_type"] = catalog_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_catalog_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        catalog_id = _parse_catalog_id(d.pop("catalog_id"))

        name = d.pop("name")

        kind = check_catalog_property_kind(d.pop("kind"))

        multiple = d.pop("multiple")

        def _parse_position(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        position = _parse_position(d.pop("position"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        def _parse_kind_catalog_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind_catalog_id = _parse_kind_catalog_id(d.pop("kind_catalog_id", UNSET))

        required = d.pop("required", UNSET)

        _catalog_type = d.pop("catalog_type", UNSET)
        catalog_type: CatalogPropertyCatalogType | Unset
        if isinstance(_catalog_type, Unset):
            catalog_type = UNSET
        else:
            catalog_type = check_catalog_property_catalog_type(_catalog_type)

        catalog_property = cls(
            catalog_id=catalog_id,
            name=name,
            kind=kind,
            multiple=multiple,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            kind_catalog_id=kind_catalog_id,
            required=required,
            catalog_type=catalog_type,
        )

        catalog_property.additional_properties = d
        return catalog_property

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
