from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_trigger_params_alert_payload_conditions_logic import (
    AlertTriggerParamsAlertPayloadConditionsLogic,
    check_alert_trigger_params_alert_payload_conditions_logic,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_trigger_params_alert_payload_conditions_conditions_item import (
        AlertTriggerParamsAlertPayloadConditionsConditionsItem,
    )


T = TypeVar("T", bound="AlertTriggerParamsAlertPayloadConditions")


@_attrs_define
class AlertTriggerParamsAlertPayloadConditions:
    """
    Attributes:
        logic (Union[Unset, AlertTriggerParamsAlertPayloadConditionsLogic]):
        conditions (Union[Unset, list['AlertTriggerParamsAlertPayloadConditionsConditionsItem']]):
    """

    logic: Unset | AlertTriggerParamsAlertPayloadConditionsLogic = UNSET
    conditions: Unset | list["AlertTriggerParamsAlertPayloadConditionsConditionsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logic: Unset | str = UNSET
        if not isinstance(self.logic, Unset):
            logic = self.logic

        conditions: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logic is not UNSET:
            field_dict["logic"] = logic
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_trigger_params_alert_payload_conditions_conditions_item import (
            AlertTriggerParamsAlertPayloadConditionsConditionsItem,
        )

        d = dict(src_dict)
        _logic = d.pop("logic", UNSET)
        logic: Unset | AlertTriggerParamsAlertPayloadConditionsLogic
        if isinstance(_logic, Unset):
            logic = UNSET
        else:
            logic = check_alert_trigger_params_alert_payload_conditions_logic(_logic)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = AlertTriggerParamsAlertPayloadConditionsConditionsItem.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        alert_trigger_params_alert_payload_conditions = cls(
            logic=logic,
            conditions=conditions,
        )

        alert_trigger_params_alert_payload_conditions.additional_properties = d
        return alert_trigger_params_alert_payload_conditions

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
