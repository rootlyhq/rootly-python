from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_policy_path_rules_item_type_3_operator import (
    EscalationPolicyPathRulesItemType3Operator,
    check_escalation_policy_path_rules_item_type_3_operator,
)
from ..models.escalation_policy_path_rules_item_type_3_rule_type import (
    EscalationPolicyPathRulesItemType3RuleType,
    check_escalation_policy_path_rules_item_type_3_rule_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EscalationPolicyPathRulesItemType3")


@_attrs_define
class EscalationPolicyPathRulesItemType3:
    """
    Attributes:
        rule_type (EscalationPolicyPathRulesItemType3RuleType): The type of the escalation path rule
        fieldable_type (str): The type of the fieldable (e.g., AlertField)
        fieldable_id (str): The ID of the alert field
        operator (EscalationPolicyPathRulesItemType3Operator): How the alert field value should be matched
        values (Union[Unset, list[str]]): Values to match against
    """

    rule_type: EscalationPolicyPathRulesItemType3RuleType
    fieldable_type: str
    fieldable_id: str
    operator: EscalationPolicyPathRulesItemType3Operator
    values: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_type: str = self.rule_type

        fieldable_type = self.fieldable_type

        fieldable_id = self.fieldable_id

        operator: str = self.operator

        values: Union[Unset, list[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_type": rule_type,
                "fieldable_type": fieldable_type,
                "fieldable_id": fieldable_id,
                "operator": operator,
            }
        )
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_type = check_escalation_policy_path_rules_item_type_3_rule_type(d.pop("rule_type"))

        fieldable_type = d.pop("fieldable_type")

        fieldable_id = d.pop("fieldable_id")

        operator = check_escalation_policy_path_rules_item_type_3_operator(d.pop("operator"))

        values = cast(list[str], d.pop("values", UNSET))

        escalation_policy_path_rules_item_type_3 = cls(
            rule_type=rule_type,
            fieldable_type=fieldable_type,
            fieldable_id=fieldable_id,
            operator=operator,
            values=values,
        )

        escalation_policy_path_rules_item_type_3.additional_properties = d
        return escalation_policy_path_rules_item_type_3

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
