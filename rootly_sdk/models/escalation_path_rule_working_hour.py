from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_path_rule_working_hour_rule_type import (
    EscalationPathRuleWorkingHourRuleType,
    check_escalation_path_rule_working_hour_rule_type,
)

T = TypeVar("T", bound="EscalationPathRuleWorkingHour")


@_attrs_define
class EscalationPathRuleWorkingHour:
    """
    Attributes:
        rule_type (EscalationPathRuleWorkingHourRuleType): The type of the escalation path rule
        within_working_hour (bool): Whether the escalation path should be used within working hours
    """

    rule_type: EscalationPathRuleWorkingHourRuleType
    within_working_hour: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_type: str = self.rule_type

        within_working_hour = self.within_working_hour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_type": rule_type,
                "within_working_hour": within_working_hour,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_type = check_escalation_path_rule_working_hour_rule_type(d.pop("rule_type"))

        within_working_hour = d.pop("within_working_hour")

        escalation_path_rule_working_hour = cls(
            rule_type=rule_type,
            within_working_hour=within_working_hour,
        )

        escalation_path_rule_working_hour.additional_properties = d
        return escalation_path_rule_working_hour

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
