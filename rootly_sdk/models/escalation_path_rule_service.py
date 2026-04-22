from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_path_rule_service_rule_type import (
    EscalationPathRuleServiceRuleType,
    check_escalation_path_rule_service_rule_type,
)

T = TypeVar("T", bound="EscalationPathRuleService")


@_attrs_define
class EscalationPathRuleService:
    """
    Attributes:
        rule_type (EscalationPathRuleServiceRuleType): The type of the escalation path rule
        service_ids (list[str]): Service ids for which this escalation path should be used
    """

    rule_type: EscalationPathRuleServiceRuleType
    service_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_type: str = self.rule_type

        service_ids = self.service_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_type": rule_type,
                "service_ids": service_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_type = check_escalation_path_rule_service_rule_type(d.pop("rule_type"))

        service_ids = cast(list[str], d.pop("service_ids"))

        escalation_path_rule_service = cls(
            rule_type=rule_type,
            service_ids=service_ids,
        )

        escalation_path_rule_service.additional_properties = d
        return escalation_path_rule_service

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
