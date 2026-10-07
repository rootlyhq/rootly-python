from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_match_mode import (
    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemMatchMode,
    check_new_escalation_policy_path_data_attributes_notification_type_rules_item_match_mode,
)
from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_notification_type import (
    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemNotificationType,
    check_new_escalation_policy_path_data_attributes_notification_type_rules_item_notification_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_field import (
        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField,
    )
    from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source import (
        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource,
    )
    from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_urgency import (
        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency,
    )
    from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window import (
        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow,
    )
    from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_json_path import (
        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath,
    )
    from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_related_incidents import (
        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidents,
    )
    from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_service import (
        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemService,
    )
    from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_working_hours import (
        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours,
    )


T = TypeVar("T", bound="NewEscalationPolicyPathDataAttributesNotificationTypeRulesItem")


@_attrs_define
class NewEscalationPolicyPathDataAttributesNotificationTypeRulesItem:
    """
    Attributes:
        conditions (list[NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField |
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource |
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency |
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow |
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath |
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidents |
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemService |
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours]): Conditions combined per
            match_mode, at least one per rule. A deferral_window condition matches when the alert falls inside its time
            blocks.
        notification_type (NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemNotificationType | Unset):
            Outcome when this rule matches Default: 'audible'.
        match_mode (NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemMatchMode | Unset): Whether all or any
            of the rule's conditions must match Default: 'match-all-rules'.
    """

    conditions: list[
        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField
        | NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource
        | NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency
        | NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow
        | NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath
        | NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidents
        | NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemService
        | NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours
    ]
    notification_type: NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemNotificationType | Unset = (
        "audible"
    )
    match_mode: NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemMatchMode | Unset = "match-all-rules"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_field import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField,
        )
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource,
        )
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_urgency import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency,
        )
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow,
        )
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_json_path import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath,
        )
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_service import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemService,
        )
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_working_hours import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours,
        )

        conditions = []
        for conditions_item_data in self.conditions:
            conditions_item: dict[str, Any]
            if isinstance(
                conditions_item_data, NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency
            ):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(
                conditions_item_data, NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours
            ):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(
                conditions_item_data, NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath
            ):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(
                conditions_item_data, NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField
            ):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(
                conditions_item_data, NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemService
            ):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(
                conditions_item_data, NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow
            ):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(
                conditions_item_data, NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource
            ):
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
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_field import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField,
        )
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource,
        )
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_alert_urgency import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency,
        )
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow,
        )
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_json_path import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath,
        )
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_related_incidents import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidents,
        )
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_service import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemService,
        )
        from ..models.new_escalation_policy_path_data_attributes_notification_type_rules_item_working_hours import (
            NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours,
        )

        d = dict(src_dict)
        conditions = []
        _conditions = d.pop("conditions")
        for conditions_item_data in _conditions:

            def _parse_conditions_item(
                data: object,
            ) -> (
                NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField
                | NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource
                | NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency
                | NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow
                | NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath
                | NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidents
                | NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemService
                | NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_alert_urgency = (
                        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency.from_dict(data)
                    )

                    return conditions_item_alert_urgency
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_working_hours = (
                        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours.from_dict(data)
                    )

                    return conditions_item_working_hours
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_json_path = (
                        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath.from_dict(data)
                    )

                    return conditions_item_json_path
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_alert_field = (
                        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField.from_dict(data)
                    )

                    return conditions_item_alert_field
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_service = (
                        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemService.from_dict(data)
                    )

                    return conditions_item_service
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_deferral_window = (
                        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow.from_dict(data)
                    )

                    return conditions_item_deferral_window
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_alert_source = (
                        NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource.from_dict(data)
                    )

                    return conditions_item_alert_source
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                conditions_item_related_incidents = (
                    NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidents.from_dict(data)
                )

                return conditions_item_related_incidents

            conditions_item = _parse_conditions_item(conditions_item_data)

            conditions.append(conditions_item)

        _notification_type = d.pop("notification_type", UNSET)
        notification_type: NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemNotificationType | Unset
        if isinstance(_notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = (
                check_new_escalation_policy_path_data_attributes_notification_type_rules_item_notification_type(
                    _notification_type
                )
            )

        _match_mode = d.pop("match_mode", UNSET)
        match_mode: NewEscalationPolicyPathDataAttributesNotificationTypeRulesItemMatchMode | Unset
        if isinstance(_match_mode, Unset):
            match_mode = UNSET
        else:
            match_mode = check_new_escalation_policy_path_data_attributes_notification_type_rules_item_match_mode(
                _match_mode
            )

        new_escalation_policy_path_data_attributes_notification_type_rules_item = cls(
            conditions=conditions,
            notification_type=notification_type,
            match_mode=match_mode,
        )

        new_escalation_policy_path_data_attributes_notification_type_rules_item.additional_properties = d
        return new_escalation_policy_path_data_attributes_notification_type_rules_item

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
