from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AlertGroupConditionsItemValuesItemType0")


@_attrs_define
class AlertGroupConditionsItemValuesItemType0:
    """
    Attributes:
        record_id (str): ID of the Alert Urgency to set.
        record_type (str): Should be "AlertUrgency".
    """

    record_id: str
    record_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_id = self.record_id

        record_type = self.record_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "record_id": record_id,
                "record_type": record_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        record_id = d.pop("record_id")

        record_type = d.pop("record_type")

        alert_group_conditions_item_values_item_type_0 = cls(
            record_id=record_id,
            record_type=record_type,
        )

        alert_group_conditions_item_values_item_type_0.additional_properties = d
        return alert_group_conditions_item_values_item_type_0

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
