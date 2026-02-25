from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_catalog_entity_data_attributes_fields_item import UpdateCatalogEntityDataAttributesFieldsItem


T = TypeVar("T", bound="UpdateCatalogEntityDataAttributes")


@_attrs_define
class UpdateCatalogEntityDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[None, Unset, str]):
        position (Union[None, Unset, int]): Default position of the item when displayed in a list.
        fields (Union[Unset, list['UpdateCatalogEntityDataAttributesFieldsItem']]): Array of field values for this
            catalog entity
    """

    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    position: None | Unset | int = UNSET
    fields: Unset | list["UpdateCatalogEntityDataAttributesFieldsItem"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        position: None | Unset | int
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        fields: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_catalog_entity_data_attributes_fields_item import (
            UpdateCatalogEntityDataAttributesFieldsItem,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = UpdateCatalogEntityDataAttributesFieldsItem.from_dict(fields_item_data)

            fields.append(fields_item)

        update_catalog_entity_data_attributes = cls(
            name=name,
            description=description,
            position=position,
            fields=fields,
        )

        return update_catalog_entity_data_attributes
