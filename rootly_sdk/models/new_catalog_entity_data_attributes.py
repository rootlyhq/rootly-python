from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewCatalogEntityDataAttributes")


@_attrs_define
class NewCatalogEntityDataAttributes:
    """
    Attributes:
        name (str):
        description (Union[None, Unset, str]):
        position (Union[None, Unset, int]): Default position of the item when displayed in a list.
    """

    name: str
    description: Union[None, Unset, str] = UNSET
    position: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        position: Union[None, Unset, int]
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_position(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position = _parse_position(d.pop("position", UNSET))

        new_catalog_entity_data_attributes = cls(
            name=name,
            description=description,
            position=position,
        )

        return new_catalog_entity_data_attributes
