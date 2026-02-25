from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.update_catalog_field_data_attributes_catalog_type import (
    UpdateCatalogFieldDataAttributesCatalogType,
    check_update_catalog_field_data_attributes_catalog_type,
)
from ..models.update_catalog_field_data_attributes_kind import (
    UpdateCatalogFieldDataAttributesKind,
    check_update_catalog_field_data_attributes_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCatalogFieldDataAttributes")


@_attrs_define
class UpdateCatalogFieldDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]):
        kind (Union[Unset, UpdateCatalogFieldDataAttributesKind]):
        kind_catalog_id (Union[None, Unset, str]): Restricts values to items of specified catalog.
        position (Union[None, Unset, int]): Default position of the item when displayed in a list.
        required (Union[Unset, bool]): Whether the field is required.
        catalog_type (Union[Unset, UpdateCatalogFieldDataAttributesCatalogType]): The type of catalog the field belongs
            to.
    """

    name: Union[Unset, str] = UNSET
    kind: Union[Unset, UpdateCatalogFieldDataAttributesKind] = UNSET
    kind_catalog_id: Union[None, Unset, str] = UNSET
    position: Union[None, Unset, int] = UNSET
    required: Union[Unset, bool] = UNSET
    catalog_type: Union[Unset, UpdateCatalogFieldDataAttributesCatalogType] = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, UpdateCatalogFieldDataAttributesKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_update_catalog_field_data_attributes_kind(_kind)

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
        catalog_type: Union[Unset, UpdateCatalogFieldDataAttributesCatalogType]
        if isinstance(_catalog_type, Unset):
            catalog_type = UNSET
        else:
            catalog_type = check_update_catalog_field_data_attributes_catalog_type(_catalog_type)

        update_catalog_field_data_attributes = cls(
            name=name,
            kind=kind,
            kind_catalog_id=kind_catalog_id,
            position=position,
            required=required,
            catalog_type=catalog_type,
        )

        return update_catalog_field_data_attributes
