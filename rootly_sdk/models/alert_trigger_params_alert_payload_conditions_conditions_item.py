from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_trigger_params_alert_payload_conditions_conditions_item_operator import (
    AlertTriggerParamsAlertPayloadConditionsConditionsItemOperator,
    check_alert_trigger_params_alert_payload_conditions_conditions_item_operator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertTriggerParamsAlertPayloadConditionsConditionsItem")


@_attrs_define
class AlertTriggerParamsAlertPayloadConditionsConditionsItem:
    """
    Attributes:
        query (str):
        operator (AlertTriggerParamsAlertPayloadConditionsConditionsItemOperator):
        values (Union[Unset, list[str]]):
        use_regexp (Union[Unset, bool]):
    """

    query: str
    operator: AlertTriggerParamsAlertPayloadConditionsConditionsItemOperator
    values: Unset | list[str] = UNSET
    use_regexp: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        operator: str = self.operator

        values: Unset | list[str] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        use_regexp = self.use_regexp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "operator": operator,
            }
        )
        if values is not UNSET:
            field_dict["values"] = values
        if use_regexp is not UNSET:
            field_dict["use_regexp"] = use_regexp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        operator = check_alert_trigger_params_alert_payload_conditions_conditions_item_operator(d.pop("operator"))

        values = cast(list[str], d.pop("values", UNSET))

        use_regexp = d.pop("use_regexp", UNSET)

        alert_trigger_params_alert_payload_conditions_conditions_item = cls(
            query=query,
            operator=operator,
            values=values,
            use_regexp=use_regexp,
        )

        alert_trigger_params_alert_payload_conditions_conditions_item.additional_properties = d
        return alert_trigger_params_alert_payload_conditions_conditions_item

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
