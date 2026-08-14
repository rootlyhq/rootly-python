from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NewAlertDataAttributesAlertFieldValuesAttributesItemType0")


@_attrs_define
class NewAlertDataAttributesAlertFieldValuesAttributesItemType0:
    """
    Attributes:
        alert_field_id (str): ID of the custom alert field
        value (str): Value for the alert field
    """

    alert_field_id: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_field_id = self.alert_field_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        new_alert_data_attributes_alert_field_values_attributes_item_type_0 = cls(
            alert_field_id=alert_field_id,
            value=value,
        )

        new_alert_data_attributes_alert_field_values_attributes_item_type_0.additional_properties = d
        return new_alert_data_attributes_alert_field_values_attributes_item_type_0

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
