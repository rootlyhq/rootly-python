from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlertGroupDataAttributesAttributesItem")


@_attrs_define
class UpdateAlertGroupDataAttributesAttributesItem:
    """
    Attributes:
        json_path (str | Unset): The JSON path to the value to group by.
    """

    json_path: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        json_path = self.json_path

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if json_path is not UNSET:
            field_dict["json_path"] = json_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        json_path = d.pop("json_path", UNSET)

        update_alert_group_data_attributes_attributes_item = cls(
            json_path=json_path,
        )

        return update_alert_group_data_attributes_attributes_item
