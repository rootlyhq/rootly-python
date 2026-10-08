from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertAlertFieldValuesType0Item")


@_attrs_define
class AlertAlertFieldValuesType0Item:
    """
    Attributes:
        id (str): Unique ID of the alert field value
        value (str): Value for the alert field
        alert_field_id (str): ID of the custom alert field
        alert_id (str): ID of the alert
        created_at (str): Date of creation
        updated_at (str): Date of last update
    """

    id: str
    value: str
    alert_field_id: str
    alert_id: str
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        value = self.value

        alert_field_id = self.alert_field_id

        alert_id = self.alert_id

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "value": value,
                "alert_field_id": alert_field_id,
                "alert_id": alert_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        value = d.pop("value")

        alert_field_id = d.pop("alert_field_id")

        alert_id = d.pop("alert_id")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        alert_alert_field_values_type_0_item = cls(
            id=id,
            value=value,
            alert_field_id=alert_field_id,
            alert_id=alert_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        alert_alert_field_values_type_0_item.additional_properties = d
        return alert_alert_field_values_type_0_item

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
