from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source_operator import (
    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSourceOperator,
    check_new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source_operator,
)
from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source_rule_type import (
    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSourceRuleType,
    check_new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source_rule_type,
)

T = TypeVar("T", bound="NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource")


@_attrs_define
class NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource:
    """
    Attributes:
        rule_type (NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSourceRuleType): The type of the
            escalation path rule
        operator (NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSourceOperator): How the alert
            source should be matched
        values (list[str]): Alert source values to match against (e.g., manual, datadog)
    """

    rule_type: NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSourceRuleType
    operator: NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSourceOperator
    values: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_type: str = self.rule_type

        operator: str = self.operator

        values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_type": rule_type,
                "operator": operator,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_type = (
            check_new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source_rule_type(
                d.pop("rule_type")
            )
        )

        operator = check_new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source_operator(
            d.pop("operator")
        )

        values = cast(list[str], d.pop("values"))

        new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source = cls(
            rule_type=rule_type,
            operator=operator,
            values=values,
        )

        new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source.additional_properties = d
        return new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source

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
