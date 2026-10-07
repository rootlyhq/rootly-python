from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="NewAlertDataAttributesLabelsItemType0")


@_attrs_define
class NewAlertDataAttributesLabelsItemType0:
    """
    Attributes:
        key (str): Key of the tag
        value (bool | float | str): Value of the tag
    """

    key: str
    value: bool | float | str

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value: bool | float | str
        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        def _parse_value(data: object) -> bool | float | str:
            return cast(bool | float | str, data)

        value = _parse_value(d.pop("value"))

        new_alert_data_attributes_labels_item_type_0 = cls(
            key=key,
            value=value,
        )

        return new_alert_data_attributes_labels_item_type_0
