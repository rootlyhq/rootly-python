from __future__ import annotations

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
        kind_catalog_id (None | str | Unset): Restricts values to items of specified catalog.
        multiple (bool | Unset): Whether the attribute accepts multiple values.
        position (int | None | Unset): Default position of the item when displayed in a list.
        required (bool | Unset): Whether the property is required.
        catalog_type (NewCatalogPropertyDataAttributesCatalogType | Unset): The type of catalog the property belongs to.
    """

    name: str
    kind: NewCatalogPropertyDataAttributesKind
    kind_catalog_id: None | str | Unset = UNSET
    multiple: bool | Unset = UNSET
    position: int | None | Unset = UNSET
    required: bool | Unset = UNSET
    catalog_type: NewCatalogPropertyDataAttributesCatalogType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind: str = self.kind

        kind_catalog_id: None | str | Unset
        if isinstance(self.kind_catalog_id, Unset):
            kind_catalog_id = UNSET
        else:
            kind_catalog_id = self.kind_catalog_id

        multiple = self.multiple

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        required = self.required

        catalog_type: str | Unset = UNSET
        if not isinstance(self.catalog_type, Unset):
            catalog_type = self.catalog_type

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "kind": kind,
            }
        )
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        kind = check_new_catalog_property_data_attributes_kind(d.pop("kind"))

        def _parse_kind_catalog_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind_catalog_id = _parse_kind_catalog_id(d.pop("kind_catalog_id", UNSET))

        multiple = d.pop("multiple", UNSET)

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        required = d.pop("required", UNSET)

        _catalog_type = d.pop("catalog_type", UNSET)
        catalog_type: NewCatalogPropertyDataAttributesCatalogType | Unset
        if isinstance(_catalog_type, Unset):
            catalog_type = UNSET
        else:
            catalog_type = check_new_catalog_property_data_attributes_catalog_type(_catalog_type)

        new_catalog_property_data_attributes = cls(
            name=name,
            kind=kind,
            kind_catalog_id=kind_catalog_id,
            multiple=multiple,
            position=position,
            required=required,
            catalog_type=catalog_type,
        )

        return new_catalog_property_data_attributes
