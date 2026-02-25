from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewCommunicationsTypeDataAttributes")


@_attrs_define
class NewCommunicationsTypeDataAttributes:
    """
    Attributes:
        name (str): The name of the communications type
        color (Union[None, str]): The color of the communications type
        description (Union[None, Unset, str]): The description of the communications type
        position (Union[None, Unset, int]): Position of the communications type
    """

    name: str
    color: None | str
    description: None | Unset | str = UNSET
    position: None | Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        color: None | str
        color = self.color

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "color": color,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_color(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        color = _parse_color(d.pop("color"))

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

        new_communications_type_data_attributes = cls(
            name=name,
            color=color,
            description=description,
            position=position,
        )

        return new_communications_type_data_attributes
