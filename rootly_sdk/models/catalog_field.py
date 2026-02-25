from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_field_catalog_type import CatalogFieldCatalogType, check_catalog_field_catalog_type
from ..models.catalog_field_kind import CatalogFieldKind, check_catalog_field_kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogField")


@_attrs_define
class CatalogField:
    """
    Attributes:
        catalog_id (Union[None, str]):
        name (str):
        kind (CatalogFieldKind):
        multiple (bool): Whether the attribute accepts multiple values.
        position (Union[None, int]): Default position of the item when displayed in a list.
        created_at (str):
        updated_at (str):
        slug (Union[Unset, str]):
        kind_catalog_id (Union[None, Unset, str]): Restricts values to items of specified catalog.
        required (Union[Unset, bool]): Whether the field is required.
        catalog_type (Union[Unset, CatalogFieldCatalogType]): The type of catalog the field belongs to.
    """

    catalog_id: None | str
    name: str
    kind: CatalogFieldKind
    multiple: bool
    position: None | int
    created_at: str
    updated_at: str
    slug: Unset | str = UNSET
    kind_catalog_id: None | Unset | str = UNSET
    required: Unset | bool = UNSET
    catalog_type: Unset | CatalogFieldCatalogType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_id: None | str
        catalog_id = self.catalog_id

        name = self.name

        kind: str = self.kind

        multiple = self.multiple

        position: None | int
        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        kind_catalog_id: None | Unset | str
        if isinstance(self.kind_catalog_id, Unset):
            kind_catalog_id = UNSET
        else:
            kind_catalog_id = self.kind_catalog_id

        required = self.required

        catalog_type: Unset | str = UNSET
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

        kind = check_catalog_field_kind(d.pop("kind"))

        multiple = d.pop("multiple")

        def _parse_position(data: object) -> None | int:
            if data is None:
                return data
            return cast(None | int, data)

        position = _parse_position(d.pop("position"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        def _parse_kind_catalog_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        kind_catalog_id = _parse_kind_catalog_id(d.pop("kind_catalog_id", UNSET))

        required = d.pop("required", UNSET)

        _catalog_type = d.pop("catalog_type", UNSET)
        catalog_type: Unset | CatalogFieldCatalogType
        if isinstance(_catalog_type, Unset):
            catalog_type = UNSET
        else:
            catalog_type = check_catalog_field_catalog_type(_catalog_type)

        catalog_field = cls(
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

        catalog_field.additional_properties = d
        return catalog_field

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
