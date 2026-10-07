from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window_rule_type import (
    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindowRuleType,
    check_new_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window_rule_type,
)
from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window_time_zone import (
    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindowTimeZone,
    check_new_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window_time_zone,
)

if TYPE_CHECKING:
    from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window_time_blocks_item import (
        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindowTimeBlocksItem,
    )


T = TypeVar("T", bound="NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow")


@_attrs_define
class NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow:
    """
    Attributes:
        rule_type (NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindowRuleType): The type of
            the escalation path rule
        time_zone (NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindowTimeZone): Time zone for
            the deferral window
        time_blocks (list[NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindowTimeBlocksItem]):
            Time windows during which alerts are deferred
    """

    rule_type: NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindowRuleType
    time_zone: NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindowTimeZone
    time_blocks: list[NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindowTimeBlocksItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_type: str = self.rule_type

        time_zone: str = self.time_zone

        time_blocks = []
        for time_blocks_item_data in self.time_blocks:
            time_blocks_item = time_blocks_item_data.to_dict()
            time_blocks.append(time_blocks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rule_type": rule_type,
                "time_zone": time_zone,
                "time_blocks": time_blocks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window_time_blocks_item import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindowTimeBlocksItem,
        )

        d = dict(src_dict)
        rule_type = (
            check_new_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window_rule_type(
                d.pop("rule_type")
            )
        )

        time_zone = (
            check_new_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window_time_zone(
                d.pop("time_zone")
            )
        )

        time_blocks = []
        _time_blocks = d.pop("time_blocks")
        for time_blocks_item_data in _time_blocks:
            time_blocks_item = (
                NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindowTimeBlocksItem.from_dict(
                    time_blocks_item_data
                )
            )

            time_blocks.append(time_blocks_item)

        new_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window = cls(
            rule_type=rule_type,
            time_zone=time_zone,
            time_blocks=time_blocks,
        )

        new_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window.additional_properties = d
        return new_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window

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
