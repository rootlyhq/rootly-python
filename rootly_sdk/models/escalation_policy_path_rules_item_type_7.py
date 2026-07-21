from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.escalation_policy_path_rules_item_type_7_operator import (
    check_escalation_policy_path_rules_item_type_7_operator,
)
from ..models.escalation_policy_path_rules_item_type_7_operator import EscalationPolicyPathRulesItemType7Operator
from ..models.escalation_policy_path_rules_item_type_7_rule_type import (
    check_escalation_policy_path_rules_item_type_7_rule_type,
)
from ..models.escalation_policy_path_rules_item_type_7_rule_type import EscalationPolicyPathRulesItemType7RuleType
from typing import cast


T = TypeVar("T", bound="EscalationPolicyPathRulesItemType7")


@_attrs_define
class EscalationPolicyPathRulesItemType7:
    """
    Attributes:
        rule_type (EscalationPolicyPathRulesItemType7RuleType): The type of the escalation path rule
        operator (EscalationPolicyPathRulesItemType7Operator): Whether the alert must (or must not) have related
            incidents
    """

    rule_type: EscalationPolicyPathRulesItemType7RuleType
    operator: EscalationPolicyPathRulesItemType7Operator
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_type: str = self.rule_type

        operator: str = self.operator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_type": rule_type,
                "operator": operator,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_type = check_escalation_policy_path_rules_item_type_7_rule_type(d.pop("rule_type"))

        operator = check_escalation_policy_path_rules_item_type_7_operator(d.pop("operator"))

        escalation_policy_path_rules_item_type_7 = cls(
            rule_type=rule_type,
            operator=operator,
        )

        escalation_policy_path_rules_item_type_7.additional_properties = d
        return escalation_policy_path_rules_item_type_7

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
