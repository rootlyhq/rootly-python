from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_entity_fields_item import CatalogEntityFieldsItem


T = TypeVar("T", bound="CatalogEntity")


@_attrs_define
class CatalogEntity:
    """
    Attributes:
        name (str):
        position (Union[None, int]): Default position of the item when displayed in a list.
        created_at (str):
        updated_at (str):
        description (Union[None, Unset, str]):
        fields (Union[Unset, list['CatalogEntityFieldsItem']]): Array of field values for this catalog entity
    """

    name: str
    position: None | int
    created_at: str
    updated_at: str
    description: None | Unset | str = UNSET
    fields: Unset | list["CatalogEntityFieldsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        position: None | int
        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        fields: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "position": position,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_entity_fields_item import CatalogEntityFieldsItem

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_position(data: object) -> None | int:
            if data is None:
                return data
            return cast(None | int, data)

        position = _parse_position(d.pop("position"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = CatalogEntityFieldsItem.from_dict(fields_item_data)

            fields.append(fields_item)

        catalog_entity = cls(
            name=name,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            fields=fields,
        )

        catalog_entity.additional_properties = d
        return catalog_entity

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
