from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.new_alert_retrigger_rule_data_attributes_match_mode import (
    NewAlertRetriggerRuleDataAttributesMatchMode,
    check_new_alert_retrigger_rule_data_attributes_match_mode,
)
from ..models.new_alert_retrigger_rule_data_attributes_timeout_minutes import (
    NewAlertRetriggerRuleDataAttributesTimeoutMinutes,
    check_new_alert_retrigger_rule_data_attributes_timeout_minutes,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_alert_retrigger_rule_data_attributes_conditions_item import (
        NewAlertRetriggerRuleDataAttributesConditionsItem,
    )


T = TypeVar("T", bound="NewAlertRetriggerRuleDataAttributes")


@_attrs_define
class NewAlertRetriggerRuleDataAttributes:
    """
    Attributes:
        name (str): A human-readable name for the rule
        match_mode (Union[Unset, NewAlertRetriggerRuleDataAttributesMatchMode]): Whether all or any of the conditions
            must match
        timeout_minutes (Union[Unset, NewAlertRetriggerRuleDataAttributesTimeoutMinutes]): Re-trigger the alert this
            many minutes after acknowledgment. Null means never re-trigger.
        position (Union[Unset, int]): The position of the rule; the first matching rule (by position) decides the
            outcome
        conditions (Union[Unset, list['NewAlertRetriggerRuleDataAttributesConditionsItem']]): The conditions that
            determine which alerts this rule applies to. An empty array applies to every alert.
    """

    name: str
    match_mode: Union[Unset, NewAlertRetriggerRuleDataAttributesMatchMode] = UNSET
    timeout_minutes: Union[Unset, NewAlertRetriggerRuleDataAttributesTimeoutMinutes] = UNSET
    position: Union[Unset, int] = UNSET
    conditions: Union[Unset, list["NewAlertRetriggerRuleDataAttributesConditionsItem"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        match_mode: Union[Unset, str] = UNSET
        if not isinstance(self.match_mode, Unset):
            match_mode = self.match_mode

        timeout_minutes: Union[Unset, int] = UNSET
        if not isinstance(self.timeout_minutes, Unset):
            timeout_minutes = self.timeout_minutes

        position = self.position

        conditions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if match_mode is not UNSET:
            field_dict["match_mode"] = match_mode
        if timeout_minutes is not UNSET:
            field_dict["timeout_minutes"] = timeout_minutes
        if position is not UNSET:
            field_dict["position"] = position
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_alert_retrigger_rule_data_attributes_conditions_item import (
            NewAlertRetriggerRuleDataAttributesConditionsItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        _match_mode = d.pop("match_mode", UNSET)
        match_mode: Union[Unset, NewAlertRetriggerRuleDataAttributesMatchMode]
        if isinstance(_match_mode, Unset):
            match_mode = UNSET
        else:
            match_mode = check_new_alert_retrigger_rule_data_attributes_match_mode(_match_mode)

        _timeout_minutes = d.pop("timeout_minutes", UNSET)
        timeout_minutes: Union[Unset, NewAlertRetriggerRuleDataAttributesTimeoutMinutes]
        if isinstance(_timeout_minutes, Unset):
            timeout_minutes = UNSET
        else:
            timeout_minutes = check_new_alert_retrigger_rule_data_attributes_timeout_minutes(_timeout_minutes)

        position = d.pop("position", UNSET)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = NewAlertRetriggerRuleDataAttributesConditionsItem.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        new_alert_retrigger_rule_data_attributes = cls(
            name=name,
            match_mode=match_mode,
            timeout_minutes=timeout_minutes,
            position=position,
            conditions=conditions,
        )

        return new_alert_retrigger_rule_data_attributes
