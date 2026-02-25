from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_icon import CatalogIcon, check_catalog_icon
from ..types import UNSET, Unset

T = TypeVar("T", bound="Catalog")


@_attrs_define
class Catalog:
    """
    Attributes:
        name (str):
        icon (CatalogIcon):
        position (Union[None, int]): Default position of the catalog when displayed in a list.
        created_at (str):
        updated_at (str):
        description (Union[None, Unset, str]):
    """

    name: str
    icon: CatalogIcon
    position: None | int
    created_at: str
    updated_at: str
    description: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        icon: str = self.icon

        position: None | int
        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "icon": icon,
                "position": position,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        icon = check_catalog_icon(d.pop("icon"))

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

        catalog = cls(
            name=name,
            icon=icon,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
        )

        catalog.additional_properties = d
        return catalog

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
