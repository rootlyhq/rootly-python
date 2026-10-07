from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_match_mode import (
    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemMatchMode,
    check_update_escalation_policy_path_data_attributes_notification_type_rules_item_match_mode,
)
from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_notification_type import (
    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemNotificationType,
    check_update_escalation_policy_path_data_attributes_notification_type_rules_item_notification_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_alert_field import (
        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField,
    )
    from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source import (
        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource,
    )
    from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_alert_urgency import (
        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency,
    )
    from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window import (
        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow,
    )
    from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_json_path import (
        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath,
    )
    from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_related_incidents import (
        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidents,
    )
    from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_service import (
        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemService,
    )
    from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_working_hours import (
        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours,
    )


T = TypeVar("T", bound="UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItem")


@_attrs_define
class UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItem:
    """
    Attributes:
        conditions (list[UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField |
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource |
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency |
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow |
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath |
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidents |
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemService |
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours]): Conditions combined per
            match_mode, at least one per rule. A deferral_window condition matches when the alert falls inside its time
            blocks.
        notification_type (UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemNotificationType | Unset):
            Outcome when this rule matches Default: 'audible'.
        match_mode (UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemMatchMode | Unset): Whether all or
            any of the rule's conditions must match Default: 'match-all-rules'.
    """

    conditions: list[
        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField
        | UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource
        | UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency
        | UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow
        | UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath
        | UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidents
        | UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemService
        | UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours
    ]
    notification_type: UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemNotificationType | Unset = (
        "audible"
    )
    match_mode: UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemMatchMode | Unset = "match-all-rules"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_alert_field import (
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField,
        )
        from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source import (
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource,
        )
        from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_alert_urgency import (
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency,
        )
        from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window import (
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow,
        )
        from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_json_path import (
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath,
        )
        from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_service import (
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemService,
        )
        from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_working_hours import (
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours,
        )

        conditions = []
        for conditions_item_data in self.conditions:
            conditions_item: dict[str, Any]
            if isinstance(
                conditions_item_data, UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency
            ):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(
                conditions_item_data, UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours
            ):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(
                conditions_item_data, UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath
            ):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(
                conditions_item_data, UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField
            ):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(
                conditions_item_data, UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemService
            ):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(
                conditions_item_data, UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow
            ):
                conditions_item = conditions_item_data.to_dict()
            elif isinstance(
                conditions_item_data, UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource
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
        from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_alert_field import (
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField,
        )
        from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_alert_source import (
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource,
        )
        from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_alert_urgency import (
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency,
        )
        from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_deferral_window import (
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow,
        )
        from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_json_path import (
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath,
        )
        from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_related_incidents import (
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidents,
        )
        from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_service import (
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemService,
        )
        from ..models.update_escalation_policy_path_data_attributes_notification_type_rules_item_working_hours import (
            UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours,
        )

        d = dict(src_dict)
        conditions = []
        _conditions = d.pop("conditions")
        for conditions_item_data in _conditions:

            def _parse_conditions_item(
                data: object,
            ) -> (
                UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField
                | UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource
                | UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency
                | UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow
                | UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath
                | UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidents
                | UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemService
                | UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_alert_urgency = (
                        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertUrgency.from_dict(data)
                    )

                    return conditions_item_alert_urgency
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_working_hours = (
                        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemWorkingHours.from_dict(data)
                    )

                    return conditions_item_working_hours
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_json_path = (
                        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemJSONPath.from_dict(data)
                    )

                    return conditions_item_json_path
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_alert_field = (
                        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertField.from_dict(data)
                    )

                    return conditions_item_alert_field
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_service = (
                        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemService.from_dict(data)
                    )

                    return conditions_item_service
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_deferral_window = (
                        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemDeferralWindow.from_dict(data)
                    )

                    return conditions_item_deferral_window
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_alert_source = (
                        UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemAlertSource.from_dict(data)
                    )

                    return conditions_item_alert_source
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                conditions_item_related_incidents = (
                    UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemRelatedIncidents.from_dict(data)
                )

                return conditions_item_related_incidents

            conditions_item = _parse_conditions_item(conditions_item_data)

            conditions.append(conditions_item)

        _notification_type = d.pop("notification_type", UNSET)
        notification_type: UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemNotificationType | Unset
        if isinstance(_notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = (
                check_update_escalation_policy_path_data_attributes_notification_type_rules_item_notification_type(
                    _notification_type
                )
            )

        _match_mode = d.pop("match_mode", UNSET)
        match_mode: UpdateEscalationPolicyPathDataAttributesNotificationTypeRulesItemMatchMode | Unset
        if isinstance(_match_mode, Unset):
            match_mode = UNSET
        else:
            match_mode = check_update_escalation_policy_path_data_attributes_notification_type_rules_item_match_mode(
                _match_mode
            )

        update_escalation_policy_path_data_attributes_notification_type_rules_item = cls(
            conditions=conditions,
            notification_type=notification_type,
            match_mode=match_mode,
        )

        update_escalation_policy_path_data_attributes_notification_type_rules_item.additional_properties = d
        return update_escalation_policy_path_data_attributes_notification_type_rules_item

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
