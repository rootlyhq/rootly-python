from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.escalation_policy_path_rules_item_type_9_type_6_operator import (
    check_escalation_policy_path_rules_item_type_9_type_6_operator,
)
from ..models.escalation_policy_path_rules_item_type_9_type_6_operator import (
    EscalationPolicyPathRulesItemType9Type6Operator,
)
from ..models.escalation_policy_path_rules_item_type_9_type_6_rule_type import (
    check_escalation_policy_path_rules_item_type_9_type_6_rule_type,
)
from ..models.escalation_policy_path_rules_item_type_9_type_6_rule_type import (
    EscalationPolicyPathRulesItemType9Type6RuleType,
)
from typing import cast


T = TypeVar("T", bound="EscalationPolicyPathRulesItemType9Type6")


@_attrs_define
class EscalationPolicyPathRulesItemType9Type6:
    """
    Attributes:
        rule_type (EscalationPolicyPathRulesItemType9Type6RuleType): The type of the escalation path rule
        operator (EscalationPolicyPathRulesItemType9Type6Operator): How the alert source should be matched
        values (list[str]): Alert source values to match against (e.g., manual, datadog)
    """

    rule_type: EscalationPolicyPathRulesItemType9Type6RuleType
    operator: EscalationPolicyPathRulesItemType9Type6Operator
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
        rule_type = check_escalation_policy_path_rules_item_type_9_type_6_rule_type(d.pop("rule_type"))

        operator = check_escalation_policy_path_rules_item_type_9_type_6_operator(d.pop("operator"))

        values = cast(list[str], d.pop("values"))

        escalation_policy_path_rules_item_type_9_type_6 = cls(
            rule_type=rule_type,
            operator=operator,
            values=values,
        )

        escalation_policy_path_rules_item_type_9_type_6.additional_properties = d
        return escalation_policy_path_rules_item_type_9_type_6

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
