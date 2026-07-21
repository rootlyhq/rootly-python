from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.escalation_policy_path_rules_item_type_8_type_3_operator import (
    check_escalation_policy_path_rules_item_type_8_type_3_operator,
)
from ..models.escalation_policy_path_rules_item_type_8_type_3_operator import (
    EscalationPolicyPathRulesItemType8Type3Operator,
)
from ..models.escalation_policy_path_rules_item_type_8_type_3_rule_type import (
    check_escalation_policy_path_rules_item_type_8_type_3_rule_type,
)
from ..models.escalation_policy_path_rules_item_type_8_type_3_rule_type import (
    EscalationPolicyPathRulesItemType8Type3RuleType,
)
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="EscalationPolicyPathRulesItemType8Type3")


@_attrs_define
class EscalationPolicyPathRulesItemType8Type3:
    """
    Attributes:
        rule_type (EscalationPolicyPathRulesItemType8Type3RuleType): The type of the escalation path rule
        fieldable_type (str): The type of the fieldable (e.g., AlertField)
        fieldable_id (str): The ID of the alert field
        operator (EscalationPolicyPathRulesItemType8Type3Operator): How the alert field value should be matched
        values (list[str] | Unset): Values to match against
    """

    rule_type: EscalationPolicyPathRulesItemType8Type3RuleType
    fieldable_type: str
    fieldable_id: str
    operator: EscalationPolicyPathRulesItemType8Type3Operator
    values: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_type: str = self.rule_type

        fieldable_type = self.fieldable_type

        fieldable_id = self.fieldable_id

        operator: str = self.operator

        values: list[str] | Unset = UNSET
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
        rule_type = check_escalation_policy_path_rules_item_type_8_type_3_rule_type(d.pop("rule_type"))

        fieldable_type = d.pop("fieldable_type")

        fieldable_id = d.pop("fieldable_id")

        operator = check_escalation_policy_path_rules_item_type_8_type_3_operator(d.pop("operator"))

        values = cast(list[str], d.pop("values", UNSET))

        escalation_policy_path_rules_item_type_8_type_3 = cls(
            rule_type=rule_type,
            fieldable_type=fieldable_type,
            fieldable_id=fieldable_id,
            operator=operator,
            values=values,
        )

        escalation_policy_path_rules_item_type_8_type_3.additional_properties = d
        return escalation_policy_path_rules_item_type_8_type_3

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
