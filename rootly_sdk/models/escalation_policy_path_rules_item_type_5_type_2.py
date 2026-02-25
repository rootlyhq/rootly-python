from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_policy_path_rules_item_type_5_type_2_operator import (
    EscalationPolicyPathRulesItemType5Type2Operator,
    check_escalation_policy_path_rules_item_type_5_type_2_operator,
)
from ..models.escalation_policy_path_rules_item_type_5_type_2_rule_type import (
    EscalationPolicyPathRulesItemType5Type2RuleType,
    check_escalation_policy_path_rules_item_type_5_type_2_rule_type,
)

T = TypeVar("T", bound="EscalationPolicyPathRulesItemType5Type2")


@_attrs_define
class EscalationPolicyPathRulesItemType5Type2:
    """
    Attributes:
        rule_type (EscalationPolicyPathRulesItemType5Type2RuleType): The type of the escalation path rule
        json_path (str): JSON path to extract value from payload
        operator (EscalationPolicyPathRulesItemType5Type2Operator): How JSON path value should be matched
        value (str): Value with which JSON path value should be matched
    """

    rule_type: EscalationPolicyPathRulesItemType5Type2RuleType
    json_path: str
    operator: EscalationPolicyPathRulesItemType5Type2Operator
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_type: str = self.rule_type

        json_path = self.json_path

        operator: str = self.operator

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_type": rule_type,
                "json_path": json_path,
                "operator": operator,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_type = check_escalation_policy_path_rules_item_type_5_type_2_rule_type(d.pop("rule_type"))

        json_path = d.pop("json_path")

        operator = check_escalation_policy_path_rules_item_type_5_type_2_operator(d.pop("operator"))

        value = d.pop("value")

        escalation_policy_path_rules_item_type_5_type_2 = cls(
            rule_type=rule_type,
            json_path=json_path,
            operator=operator,
            value=value,
        )

        escalation_policy_path_rules_item_type_5_type_2.additional_properties = d
        return escalation_policy_path_rules_item_type_5_type_2

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
