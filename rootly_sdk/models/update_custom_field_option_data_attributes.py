from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="UpdateCustomFieldOptionDataAttributes")


@_attrs_define
class UpdateCustomFieldOptionDataAttributes:
    """
    Attributes:
        value (str | Unset): The value of the custom_field_option
        color (str | Unset): The hex color of the custom_field_option
        default (bool | Unset):
        position (int | Unset): The position of the custom_field_option
    """

    value: str | Unset = UNSET
    color: str | Unset = UNSET
    default: bool | Unset = UNSET
    position: int | Unset = UNSET

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
