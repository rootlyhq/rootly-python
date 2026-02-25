from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_policy_path_rules_item_type_5_type_0_rule_type import (
    EscalationPolicyPathRulesItemType5Type0RuleType,
    check_escalation_policy_path_rules_item_type_5_type_0_rule_type,
)

T = TypeVar("T", bound="EscalationPolicyPathRulesItemType5Type0")


@_attrs_define
class EscalationPolicyPathRulesItemType5Type0:
    """
    Attributes:
        rule_type (EscalationPolicyPathRulesItemType5Type0RuleType): The type of the escalation path rule
        urgency_ids (list[str]): Alert urgency ids for which this escalation path should be used
    """

    rule_type: EscalationPolicyPathRulesItemType5Type0RuleType
    urgency_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_type: str = self.rule_type

        urgency_ids = self.urgency_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_type": rule_type,
                "urgency_ids": urgency_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_type = check_escalation_policy_path_rules_item_type_5_type_0_rule_type(d.pop("rule_type"))

        urgency_ids = cast(list[str], d.pop("urgency_ids"))

        escalation_policy_path_rules_item_type_5_type_0 = cls(
            rule_type=rule_type,
            urgency_ids=urgency_ids,
        )

        escalation_policy_path_rules_item_type_5_type_0.additional_properties = d
        return escalation_policy_path_rules_item_type_5_type_0

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
