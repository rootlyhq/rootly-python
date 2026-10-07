from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_policy_path_notification_type_rules_item_alert_urgency_operator import (
    EscalationPolicyPathNotificationTypeRulesItemAlertUrgencyOperator,
    check_escalation_policy_path_notification_type_rules_item_alert_urgency_operator,
)
from ..models.escalation_policy_path_notification_type_rules_item_alert_urgency_rule_type import (
    EscalationPolicyPathNotificationTypeRulesItemAlertUrgencyRuleType,
    check_escalation_policy_path_notification_type_rules_item_alert_urgency_rule_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EscalationPolicyPathNotificationTypeRulesItemAlertUrgency")


@_attrs_define
class EscalationPolicyPathNotificationTypeRulesItemAlertUrgency:
    """
    Attributes:
        rule_type (EscalationPolicyPathNotificationTypeRulesItemAlertUrgencyRuleType): The type of the escalation path
            rule
        urgency_ids (list[str]): Alert urgency ids for which this escalation path should be used
        operator (EscalationPolicyPathNotificationTypeRulesItemAlertUrgencyOperator | Unset): How the alert's urgency
            should be matched. is and is_not take exactly one id Default: 'is_one_of'.
    """

    rule_type: EscalationPolicyPathNotificationTypeRulesItemAlertUrgencyRuleType
    urgency_ids: list[str]
    operator: EscalationPolicyPathNotificationTypeRulesItemAlertUrgencyOperator | Unset = "is_one_of"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_type: str = self.rule_type

        urgency_ids = self.urgency_ids

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_type": rule_type,
                "urgency_ids": urgency_ids,
            }
        )
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_type = check_escalation_policy_path_notification_type_rules_item_alert_urgency_rule_type(
            d.pop("rule_type")
        )

        urgency_ids = cast(list[str], d.pop("urgency_ids"))

        _operator = d.pop("operator", UNSET)
        operator: EscalationPolicyPathNotificationTypeRulesItemAlertUrgencyOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = check_escalation_policy_path_notification_type_rules_item_alert_urgency_operator(_operator)

        escalation_policy_path_notification_type_rules_item_alert_urgency = cls(
            rule_type=rule_type,
            urgency_ids=urgency_ids,
            operator=operator,
        )

        escalation_policy_path_notification_type_rules_item_alert_urgency.additional_properties = d
        return escalation_policy_path_notification_type_rules_item_alert_urgency

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
