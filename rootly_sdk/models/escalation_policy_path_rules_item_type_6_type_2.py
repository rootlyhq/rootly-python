from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_policy_path_rules_item_type_6_type_2_operator import (
    EscalationPolicyPathRulesItemType6Type2Operator,
    check_escalation_policy_path_rules_item_type_6_type_2_operator,
)
from ..models.escalation_policy_path_rules_item_type_6_type_2_rule_type import (
    EscalationPolicyPathRulesItemType6Type2RuleType,
    check_escalation_policy_path_rules_item_type_6_type_2_rule_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EscalationPolicyPathRulesItemType6Type2")


@_attrs_define
class EscalationPolicyPathRulesItemType6Type2:
    """
    Attributes:
        rule_type (EscalationPolicyPathRulesItemType6Type2RuleType): The type of the escalation path rule
        json_path (str): JSON path to extract value from payload
        operator (EscalationPolicyPathRulesItemType6Type2Operator): How JSON path value should be matched
        value (None | str | Unset): Value with which JSON path value should be matched
        values (list[str] | Unset): Values to match against (for is_one_of / is_not_one_of operators)
    """

    rule_type: EscalationPolicyPathRulesItemType6Type2RuleType
    json_path: str
    operator: EscalationPolicyPathRulesItemType6Type2Operator
    value: None | str | Unset = UNSET
    values: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_type: str = self.rule_type

        json_path = self.json_path

        operator: str = self.operator

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        values: list[str] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_type": rule_type,
                "json_path": json_path,
                "operator": operator,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_type = check_escalation_policy_path_rules_item_type_6_type_2_rule_type(d.pop("rule_type"))

        json_path = d.pop("json_path")

        operator = check_escalation_policy_path_rules_item_type_6_type_2_operator(d.pop("operator"))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        values = cast(list[str], d.pop("values", UNSET))

        escalation_policy_path_rules_item_type_6_type_2 = cls(
            rule_type=rule_type,
            json_path=json_path,
            operator=operator,
            value=value,
            values=values,
        )

        escalation_policy_path_rules_item_type_6_type_2.additional_properties = d
        return escalation_policy_path_rules_item_type_6_type_2

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
