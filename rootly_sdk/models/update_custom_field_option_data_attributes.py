from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCustomFieldOptionDataAttributes")


@_attrs_define
class UpdateCustomFieldOptionDataAttributes:
    """
    Attributes:
        value (Union[Unset, str]): The value of the custom_field_option
        color (Union[Unset, str]): The hex color of the custom_field_option
        default (Union[Unset, bool]):
        position (Union[Unset, int]): The position of the custom_field_option
    """

    value: Unset | str = UNSET
    color: Unset | str = UNSET
    default: Unset | bool = UNSET
    position: Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        color = self.color

        default = self.default

        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if color is not UNSET:
            field_dict["color"] = color
        if default is not UNSET:
            field_dict["default"] = default
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        color = d.pop("color", UNSET)

        default = d.pop("default", UNSET)

        position = d.pop("position", UNSET)

        update_custom_field_option_data_attributes = cls(
            value=value,
            color=color,
            default=default,
            position=position,
        )

        return update_custom_field_option_data_attributes
