from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_service_operator import (
    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemServiceOperator,
    check_update_escalation_policy_path_data_attributes_notification_type_rules_item_service_operator,
)
from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_service_rule_type import (
    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemServiceRuleType,
    check_update_escalation_policy_path_data_attributes_notification_type_rules_item_service_rule_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemService")


@_attrs_define
class UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemService:
    """
    Attributes:
        rule_type (UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemServiceRuleType): The type of the
            escalation path rule
        service_ids (list[str]): Service ids for which this escalation path should be used
        operator (UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemServiceOperator | Unset): How the
            alert's services should be matched. is and is_not take exactly one id Default: 'is_one_of'.
    """

    rule_type: UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemServiceRuleType
    service_ids: list[str]
    operator: UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemServiceOperator | Unset = "is_one_of"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_type: str = self.rule_type

        service_ids = self.service_ids

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_type": rule_type,
                "service_ids": service_ids,
            }
        )
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rule_type = check_update_escalation_policy_path_data_attributes_notification_type_rules_item_service_rule_type(
            d.pop("rule_type")
        )

        service_ids = cast(list[str], d.pop("service_ids"))

        _operator = d.pop("operator", UNSET)
        operator: UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemServiceOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = (
                check_update_escalation_policy_path_data_attributes_notification_type_rules_item_service_operator(
                    _operator
                )
            )

        update_escalation_policy_path_data_attributes_notification_type_rules_item_service = cls(
            rule_type=rule_type,
            service_ids=service_ids,
            operator=operator,
        )

        update_escalation_policy_path_data_attributes_notification_type_rules_item_service.additional_properties = d
        return update_escalation_policy_path_data_attributes_notification_type_rules_item_service

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
