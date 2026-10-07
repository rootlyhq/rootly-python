from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0")


@_attrs_define
class UpdateAlertDataAttributesAlertFieldValuesAttributesItemType0:
    """
    Attributes:
        alert_field_id (str): ID of the custom alert field
        value (str): Value for the alert field
    """

    alert_field_id: str
    value: str

    def to_dict(self) -> dict[str, Any]:
        alert_field_id = self.alert_field_id

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "alert_field_id": alert_field_id,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alert_field_id = d.pop("alert_field_id")

        value = d.pop("value")

        update_alert_data_attributes_alert_field_values_attributes_item_type_0 = cls(
            alert_field_id=alert_field_id,
            value=value,
        )

        return update_alert_data_attributes_alert_field_values_attributes_item_type_0
