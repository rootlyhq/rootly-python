from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="NewAlertFieldDataAttributes")


@_attrs_define
class NewAlertFieldDataAttributes:
    """
    Attributes:
        name (str): The name of the alert field
    """

    name: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        new_alert_field_data_attributes = cls(
            name=name,
        )

        return new_alert_field_data_attributes
