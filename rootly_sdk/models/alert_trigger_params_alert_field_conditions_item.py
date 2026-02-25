from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_trigger_params_alert_field_conditions_item_condition_type import (
    AlertTriggerParamsAlertFieldConditionsItemConditionType,
    check_alert_trigger_params_alert_field_conditions_item_condition_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertTriggerParamsAlertFieldConditionsItem")


@_attrs_define
class AlertTriggerParamsAlertFieldConditionsItem:
    """
    Attributes:
        alert_field_id (str):
        condition_type (AlertTriggerParamsAlertFieldConditionsItemConditionType):
        values (Union[Unset, list[str]]):
    """

    alert_field_id: str
    condition_type: AlertTriggerParamsAlertFieldConditionsItemConditionType
    values: Unset | list[str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_field_id = self.alert_field_id

        condition_type: str = self.condition_type

        values: Unset | list[str] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_field_id": alert_field_id,
                "condition_type": condition_type,
            }
        )
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alert_field_id = d.pop("alert_field_id")

        condition_type = check_alert_trigger_params_alert_field_conditions_item_condition_type(d.pop("condition_type"))

        values = cast(list[str], d.pop("values", UNSET))

        alert_trigger_params_alert_field_conditions_item = cls(
            alert_field_id=alert_field_id,
            condition_type=condition_type,
            values=values,
        )

        alert_trigger_params_alert_field_conditions_item.additional_properties = d
        return alert_trigger_params_alert_field_conditions_item

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
