from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_policy_path_notification_type_rules_item_match_mode import (
    EscalationPolicyPathNotificationTypeRulesItemMatchMode,
    check_escalation_policy_path_notification_type_rules_item_match_mode,
)
from ..models.escalation_policy_path_notification_type_rules_item_notification_type import (
    EscalationPolicyPathNotificationTypeRulesItemNotificationType,
    check_escalation_policy_path_notification_type_rules_item_notification_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_policy_path_notification_type_rules_item_alert_field import (
        EscalationPolicyPathNotificationTypeRulesItemAlertField,
    )
    from ..models.escalation_policy_path_notification_type_rules_item_alert_source import (
        EscalationPolicyPathNotificationTypeRulesItemAlertSource,
    )
    from ..models.escalation_policy_path_notification_type_rules_item_alert_urgency import (
        EscalationPolicyPathNotificationTypeRulesItemAlertUrgency,
    )
    from ..models.escalation_policy_path_notification_type_rules_item_deferral_window import (
        EscalationPolicyPathNotificationTypeRulesItemDeferralWindow,
    )
    from ..models.escalation_policy_path_notification_type_rules_item_json_path import (
        EscalationPolicyPathNotificationTypeRulesItemJSONPath,
    )
    from ..models.escalation_policy_path_notification_type_rules_item_related_incidents import (
        EscalationPolicyPathNotificationTypeRulesItemRelatedIncidents,
    )
    from ..models.escalation_policy_path_notification_type_rules_item_service import (
        EscalationPolicyPathNotificationTypeRulesItemService,
    )
    from ..models.escalation_policy_path_notification_type_rules_item_working_hours import (
        EscalationPolicyPathNotificationTypeRulesItemWorkingHours,
    )


T = TypeVar("T", bound="EscalationPolicyPathNotificationTypeRulesItem")


@_attrs_define
class EscalationPolicyPathNotificationTypeRulesItem:
    """
    Attributes:
        conditions (list[EscalationPolicyPathNotificationTypeRulesItemAlertField |
            EscalationPolicyPathNotificationTypeRulesItemAlertSource |
            EscalationPolicyPathNotificationTypeRulesItemAlertUrgency |
            EscalationPolicyPathNotificationTypeRulesItemDeferralWindow |
            EscalationPolicyPathNotificationTypeRulesItemJSONPath |
            EscalationPolicyPathNotificationTypeRulesItemRelatedIncidents |
            EscalationPolicyPathNotificationTypeRulesItemService |
            EscalationPolicyPathNotificationTypeRulesItemWorkingHours]): Conditions combined per match_mode, at least one
            per rule. A deferral_window condition matches when the alert falls inside its time blocks.
        notification_type (EscalationPolicyPathNotificationTypeRulesItemNotificationType | Unset): Outcome when this
            rule matches Default: 'audible'.
        match_mode (EscalationPolicyPathNotificationTypeRulesItemMatchMode | Unset): Whether all or any of the rule's
            conditions must match Default: 'match-all-rules'.
    """

    conditions: list[
        EscalationPolicyPathNotificationTypeRulesItemAlertField
        | EscalationPolicyPathNotificationTypeRulesItemAlertSource
        | EscalationPolicyPathNotificationTypeRulesItemAlertUrgency
        | EscalationPolicyPathNotificationTypeRulesItemDeferralWindow
        | EscalationPolicyPathNotificationTypeRulesItemJSONPath
        | EscalationPolicyPathNotificationTypeRulesItemRelatedIncidents
        | EscalationPolicyPathNotificationTypeRulesItemService
        | EscalationPolicyPathNotificationTypeRulesItemWorkingHours
    ]
    notification_type: EscalationPolicyPathNotificationTypeRulesItemNotificationType | Unset = "audible"
    match_mode: EscalationPolicyPathNotificationTypeRulesItemMatchMode | Unset = "match-all-rules"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.escalation_policy_path_notification_type_rules_item_alert_field import (
            EscalationPolicyPathNotificationTypeRulesItemAlertField,
        )
        from ..models.escalation_policy_path_notification_type_rules_item_alert_source import (
            EscalationPolicyPathNotificationTypeRulesItemAlertSource,
        )
        from ..models.escalation_policy_path_notification_type_rules_item_alert_urgency import (
            EscalationPolicyPathNotificationTypeRulesItemAlertUrgency,
        )
        from ..models.escalation_policy_path_notification_type_rules_item_deferral_window import (
            EscalationPolicyPathNotificationTypeRulesItemDeferralWindow,
        )
        from ..models.escalation_policy_path_notification_type_rules_item_json_path import (
            EscalationPolicyPathNotificationTypeRulesItemJSONPath,
        )
        from ..models.escalation_policy_path_notification_type_rules_item_service import (
            EscalationPolicyPathNotificationTypeRulesItemService,
        )
        from ..models.escalation_policy_path_notification_type_rules_item_working_hours import (
            EscalationPolicyPathNotificationTypeRulesItemWorkingHours,
        )

        conditions = []
        for conditions_item_data in self.conditions:
            conditions_item: dict[str, Any]
            if isinstance(conditions_item_data, EscalationPolicyPathNotificationTypeRulesItemAlertUrgency):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(conditions_item_data, EscalationPolicyPathNotificationTypeRulesItemWorkingHours):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(conditions_item_data, EscalationPolicyPathNotificationTypeRulesItemJSONPath):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(conditions_item_data, EscalationPolicyPathNotificationTypeRulesItemAlertField):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(conditions_item_data, EscalationPolicyPathNotificationTypeRulesItemService):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(conditions_item_data, EscalationPolicyPathNotificationTypeRulesItemDeferralWindow):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(conditions_item_data, EscalationPolicyPathNotificationTypeRulesItemAlertSource):
                conditions_item = conditions_item_data.to_dict()
            else:
                conditions_item = conditions_item_data.to_dict()

            conditions.append(conditions_item)

        notification_type: str | Unset = UNSET
        if not isinstance(self.notification_type, Unset):
            notification_type = self.notification_type

        match_mode: str | Unset = UNSET
        if not isinstance(self.match_mode, Unset):
            match_mode = self.match_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conditions": conditions,
            }
        )
        if notification_type is not UNSET:
            field_dict["notification_type"] = notification_type
        if match_mode is not UNSET:
            field_dict["match_mode"] = match_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.escalation_policy_path_notification_type_rules_item_alert_field import (
            EscalationPolicyPathNotificationTypeRulesItemAlertField,
        )
        from ..models.escalation_policy_path_notification_type_rules_item_alert_source import (
            EscalationPolicyPathNotificationTypeRulesItemAlertSource,
        )
        from ..models.escalation_policy_path_notification_type_rules_item_alert_urgency import (
            EscalationPolicyPathNotificationTypeRulesItemAlertUrgency,
        )
        from ..models.escalation_policy_path_notification_type_rules_item_deferral_window import (
            EscalationPolicyPathNotificationTypeRulesItemDeferralWindow,
        )
        from ..models.escalation_policy_path_notification_type_rules_item_json_path import (
            EscalationPolicyPathNotificationTypeRulesItemJSONPath,
        )
        from ..models.escalation_policy_path_notification_type_rules_item_related_incidents import (
            EscalationPolicyPathNotificationTypeRulesItemRelatedIncidents,
        )
        from ..models.escalation_policy_path_notification_type_rules_item_service import (
            EscalationPolicyPathNotificationTypeRulesItemService,
        )
        from ..models.escalation_policy_path_notification_type_rules_item_working_hours import (
            EscalationPolicyPathNotificationTypeRulesItemWorkingHours,
        )

        d = dict(src_dict)
        conditions = []
        _conditions = d.pop("conditions")
        for conditions_item_data in _conditions:

            def _parse_conditions_item(
                data: object,
            ) -> (
                EscalationPolicyPathNotificationTypeRulesItemAlertField
                | EscalationPolicyPathNotificationTypeRulesItemAlertSource
                | EscalationPolicyPathNotificationTypeRulesItemAlertUrgency
                | EscalationPolicyPathNotificationTypeRulesItemDeferralWindow
                | EscalationPolicyPathNotificationTypeRulesItemJSONPath
                | EscalationPolicyPathNotificationTypeRulesItemRelatedIncidents
                | EscalationPolicyPathNotificationTypeRulesItemService
                | EscalationPolicyPathNotificationTypeRulesItemWorkingHours
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_alert_urgency = EscalationPolicyPathNotificationTypeRulesItemAlertUrgency.from_dict(
                        data
                    )

                    return conditions_item_alert_urgency
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_working_hours = EscalationPolicyPathNotificationTypeRulesItemWorkingHours.from_dict(
                        data
                    )

                    return conditions_item_working_hours
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_json_path = EscalationPolicyPathNotificationTypeRulesItemJSONPath.from_dict(data)

                    return conditions_item_json_path
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_alert_field = EscalationPolicyPathNotificationTypeRulesItemAlertField.from_dict(
                        data
                    )

                    return conditions_item_alert_field
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_service = EscalationPolicyPathNotificationTypeRulesItemService.from_dict(data)

                    return conditions_item_service
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_deferral_window = (
                        EscalationPolicyPathNotificationTypeRulesItemDeferralWindow.from_dict(data)
                    )

                    return conditions_item_deferral_window
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_alert_source = EscalationPolicyPathNotificationTypeRulesItemAlertSource.from_dict(
                        data
                    )

                    return conditions_item_alert_source
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                conditions_item_related_incidents = (
                    EscalationPolicyPathNotificationTypeRulesItemRelatedIncidents.from_dict(data)
                )

                return conditions_item_related_incidents

            conditions_item = _parse_conditions_item(conditions_item_data)

            conditions.append(conditions_item)

        _notification_type = d.pop("notification_type", UNSET)
        notification_type: EscalationPolicyPathNotificationTypeRulesItemNotificationType | Unset
        if isinstance(_notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = check_escalation_policy_path_notification_type_rules_item_notification_type(
                _notification_type
            )

        _match_mode = d.pop("match_mode", UNSET)
        match_mode: EscalationPolicyPathNotificationTypeRulesItemMatchMode | Unset
        if isinstance(_match_mode, Unset):
            match_mode = UNSET
        else:
            match_mode = check_escalation_policy_path_notification_type_rules_item_match_mode(_match_mode)

        escalation_policy_path_notification_type_rules_item = cls(
            conditions=conditions,
            notification_type=notification_type,
            match_mode=match_mode,
        )

        escalation_policy_path_notification_type_rules_item.additional_properties = d
        return escalation_policy_path_notification_type_rules_item

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
