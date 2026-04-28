from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_escalation_policy_path_data_attributes_after_deferral_behavior import (
    NewEscalationPolicyPathDataAttributesAfterDeferralBehavior,
    check_new_escalation_policy_path_data_attributes_after_deferral_behavior,
)
from ..models.new_escalation_policy_path_data_attributes_match_mode import (
    NewEscalationPolicyPathDataAttributesMatchMode,
    check_new_escalation_policy_path_data_attributes_match_mode,
)
from ..models.new_escalation_policy_path_data_attributes_notification_type import (
    NewEscalationPolicyPathDataAttributesNotificationType,
    check_new_escalation_policy_path_data_attributes_notification_type,
)
from ..models.new_escalation_policy_path_data_attributes_path_type import (
    NewEscalationPolicyPathDataAttributesPathType,
    check_new_escalation_policy_path_data_attributes_path_type,
)
from ..models.new_escalation_policy_path_data_attributes_time_restriction_time_zone import (
    NewEscalationPolicyPathDataAttributesTimeRestrictionTimeZone,
    check_new_escalation_policy_path_data_attributes_time_restriction_time_zone,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_path_rule_alert_urgency import EscalationPathRuleAlertUrgency
    from ..models.escalation_path_rule_deferral_window import EscalationPathRuleDeferralWindow
    from ..models.escalation_path_rule_field import EscalationPathRuleField
    from ..models.escalation_path_rule_json_path import EscalationPathRuleJsonPath
    from ..models.escalation_path_rule_service import EscalationPathRuleService
    from ..models.escalation_path_rule_working_hour import EscalationPathRuleWorkingHour
    from ..models.new_escalation_policy_path_data_attributes_time_restrictions_item import (
        NewEscalationPolicyPathDataAttributesTimeRestrictionsItem,
    )


T = TypeVar("T", bound="NewEscalationPolicyPathDataAttributes")


@_attrs_define
class NewEscalationPolicyPathDataAttributes:
    """
    Attributes:
        name (str): The name of the escalation path
        notification_type (NewEscalationPolicyPathDataAttributesNotificationType | Unset): Notification rule type to be
            used Default: 'audible'.
        path_type (NewEscalationPolicyPathDataAttributesPathType | Unset): The type of escalation path to create
            Default: 'escalation'.
        after_deferral_behavior (NewEscalationPolicyPathDataAttributesAfterDeferralBehavior | Unset): What happens after
            a deferral path finishes. Required for deferral paths.
        after_deferral_path_id (None | str | Unset): The escalation path to execute after this deferral path when
            after_deferral_behavior is execute_path.
        default (bool | None | Unset): Whether this escalation path is the default path
        match_mode (NewEscalationPolicyPathDataAttributesMatchMode | Unset): How path rules are matched. Default:
            'match-all-rules'.
        position (int | Unset): The position of this path in the paths for this EP.
        repeat (bool | None | Unset): Whether this path should be repeated until someone acknowledges the alert
        repeat_count (int | None | Unset): The number of times this path will be executed until someone acknowledges the
            alert
        initial_delay (int | Unset): Initial delay for escalation path in minutes. Maximum 1 week (10080).
        rules (list[EscalationPathRuleAlertUrgency | EscalationPathRuleDeferralWindow | EscalationPathRuleField |
            EscalationPathRuleJsonPath | EscalationPathRuleService | EscalationPathRuleWorkingHour] | Unset): Escalation
            path conditions
        time_restriction_time_zone (NewEscalationPolicyPathDataAttributesTimeRestrictionTimeZone | Unset): Time zone
            used for time restrictions.
        time_restrictions (list[NewEscalationPolicyPathDataAttributesTimeRestrictionsItem] | Unset): If time
            restrictions are set, alerts will follow this path when they arrive within the specified time ranges and meet
            the rules.
    """

    name: str
    notification_type: NewEscalationPolicyPathDataAttributesNotificationType | Unset = "audible"
    path_type: NewEscalationPolicyPathDataAttributesPathType | Unset = "escalation"
    after_deferral_behavior: NewEscalationPolicyPathDataAttributesAfterDeferralBehavior | Unset = UNSET
    after_deferral_path_id: None | str | Unset = UNSET
    default: bool | None | Unset = UNSET
    match_mode: NewEscalationPolicyPathDataAttributesMatchMode | Unset = "match-all-rules"
    position: int | Unset = UNSET
    repeat: bool | None | Unset = UNSET
    repeat_count: int | None | Unset = UNSET
    initial_delay: int | Unset = UNSET
    rules: (
        list[
            EscalationPathRuleAlertUrgency
            | EscalationPathRuleDeferralWindow
            | EscalationPathRuleField
            | EscalationPathRuleJsonPath
            | EscalationPathRuleService
            | EscalationPathRuleWorkingHour
        ]
        | Unset
    ) = UNSET
    time_restriction_time_zone: NewEscalationPolicyPathDataAttributesTimeRestrictionTimeZone | Unset = UNSET
    time_restrictions: list[NewEscalationPolicyPathDataAttributesTimeRestrictionsItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.escalation_path_rule_alert_urgency import EscalationPathRuleAlertUrgency
        from ..models.escalation_path_rule_field import EscalationPathRuleField
        from ..models.escalation_path_rule_json_path import EscalationPathRuleJsonPath
        from ..models.escalation_path_rule_service import EscalationPathRuleService
        from ..models.escalation_path_rule_working_hour import EscalationPathRuleWorkingHour

        name = self.name

        notification_type: str | Unset = UNSET
        if not isinstance(self.notification_type, Unset):
            notification_type = self.notification_type

        path_type: str | Unset = UNSET
        if not isinstance(self.path_type, Unset):
            path_type = self.path_type

        after_deferral_behavior: str | Unset = UNSET
        if not isinstance(self.after_deferral_behavior, Unset):
            after_deferral_behavior = self.after_deferral_behavior

        after_deferral_path_id: None | str | Unset
        if isinstance(self.after_deferral_path_id, Unset):
            after_deferral_path_id = UNSET
        else:
            after_deferral_path_id = self.after_deferral_path_id

        default: bool | None | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        match_mode: str | Unset = UNSET
        if not isinstance(self.match_mode, Unset):
            match_mode = self.match_mode

        position = self.position

        repeat: bool | None | Unset
        if isinstance(self.repeat, Unset):
            repeat = UNSET
        else:
            repeat = self.repeat

        repeat_count: int | None | Unset
        if isinstance(self.repeat_count, Unset):
            repeat_count = UNSET
        else:
            repeat_count = self.repeat_count

        initial_delay = self.initial_delay

        rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item: dict[str, Any]
                if isinstance(rules_item_data, EscalationPathRuleAlertUrgency):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPathRuleWorkingHour):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPathRuleJsonPath):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPathRuleField):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPathRuleService):
                    rules_item = rules_item_data.to_dict()
                else:
                    rules_item = rules_item_data.to_dict()

                rules.append(rules_item)

        time_restriction_time_zone: str | Unset = UNSET
        if not isinstance(self.time_restriction_time_zone, Unset):
            time_restriction_time_zone = self.time_restriction_time_zone

        time_restrictions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.time_restrictions, Unset):
            time_restrictions = []
            for time_restrictions_item_data in self.time_restrictions:
                time_restrictions_item = time_restrictions_item_data.to_dict()
                time_restrictions.append(time_restrictions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if notification_type is not UNSET:
            field_dict["notification_type"] = notification_type
        if path_type is not UNSET:
            field_dict["path_type"] = path_type
        if after_deferral_behavior is not UNSET:
            field_dict["after_deferral_behavior"] = after_deferral_behavior
        if after_deferral_path_id is not UNSET:
            field_dict["after_deferral_path_id"] = after_deferral_path_id
        if default is not UNSET:
            field_dict["default"] = default
        if match_mode is not UNSET:
            field_dict["match_mode"] = match_mode
        if position is not UNSET:
            field_dict["position"] = position
        if repeat is not UNSET:
            field_dict["repeat"] = repeat
        if repeat_count is not UNSET:
            field_dict["repeat_count"] = repeat_count
        if initial_delay is not UNSET:
            field_dict["initial_delay"] = initial_delay
        if rules is not UNSET:
            field_dict["rules"] = rules
        if time_restriction_time_zone is not UNSET:
            field_dict["time_restriction_time_zone"] = time_restriction_time_zone
        if time_restrictions is not UNSET:
            field_dict["time_restrictions"] = time_restrictions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.escalation_path_rule_alert_urgency import EscalationPathRuleAlertUrgency
        from ..models.escalation_path_rule_deferral_window import EscalationPathRuleDeferralWindow
        from ..models.escalation_path_rule_field import EscalationPathRuleField
        from ..models.escalation_path_rule_json_path import EscalationPathRuleJsonPath
        from ..models.escalation_path_rule_service import EscalationPathRuleService
        from ..models.escalation_path_rule_working_hour import EscalationPathRuleWorkingHour
        from ..models.new_escalation_policy_path_data_attributes_time_restrictions_item import (
            NewEscalationPolicyPathDataAttributesTimeRestrictionsItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        _notification_type = d.pop("notification_type", UNSET)
        notification_type: NewEscalationPolicyPathDataAttributesNotificationType | Unset
        if isinstance(_notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = check_new_escalation_policy_path_data_attributes_notification_type(_notification_type)

        _path_type = d.pop("path_type", UNSET)
        path_type: NewEscalationPolicyPathDataAttributesPathType | Unset
        if isinstance(_path_type, Unset):
            path_type = UNSET
        else:
            path_type = check_new_escalation_policy_path_data_attributes_path_type(_path_type)

        _after_deferral_behavior = d.pop("after_deferral_behavior", UNSET)
        after_deferral_behavior: NewEscalationPolicyPathDataAttributesAfterDeferralBehavior | Unset
        if isinstance(_after_deferral_behavior, Unset):
            after_deferral_behavior = UNSET
        else:
            after_deferral_behavior = check_new_escalation_policy_path_data_attributes_after_deferral_behavior(
                _after_deferral_behavior
            )

        def _parse_after_deferral_path_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        after_deferral_path_id = _parse_after_deferral_path_id(d.pop("after_deferral_path_id", UNSET))

        def _parse_default(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        default = _parse_default(d.pop("default", UNSET))

        _match_mode = d.pop("match_mode", UNSET)
        match_mode: NewEscalationPolicyPathDataAttributesMatchMode | Unset
        if isinstance(_match_mode, Unset):
            match_mode = UNSET
        else:
            match_mode = check_new_escalation_policy_path_data_attributes_match_mode(_match_mode)

        position = d.pop("position", UNSET)

        def _parse_repeat(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        repeat = _parse_repeat(d.pop("repeat", UNSET))

        def _parse_repeat_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        repeat_count = _parse_repeat_count(d.pop("repeat_count", UNSET))

        initial_delay = d.pop("initial_delay", UNSET)

        _rules = d.pop("rules", UNSET)
        rules: (
            list[
                EscalationPathRuleAlertUrgency
                | EscalationPathRuleDeferralWindow
                | EscalationPathRuleField
                | EscalationPathRuleJsonPath
                | EscalationPathRuleService
                | EscalationPathRuleWorkingHour
            ]
            | Unset
        ) = UNSET
        if _rules is not UNSET:
            rules = []
            for rules_item_data in _rules:

                def _parse_rules_item(
                    data: object,
                ) -> (
                    EscalationPathRuleAlertUrgency
                    | EscalationPathRuleDeferralWindow
                    | EscalationPathRuleField
                    | EscalationPathRuleJsonPath
                    | EscalationPathRuleService
                    | EscalationPathRuleWorkingHour
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_0 = EscalationPathRuleAlertUrgency.from_dict(data)

                        return rules_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_1 = EscalationPathRuleWorkingHour.from_dict(data)

                        return rules_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_2 = EscalationPathRuleJsonPath.from_dict(data)

                        return rules_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_3 = EscalationPathRuleField.from_dict(data)

                        return rules_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_4 = EscalationPathRuleService.from_dict(data)

                        return rules_item_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_5 = EscalationPathRuleDeferralWindow.from_dict(data)

                    return rules_item_type_5

                rules_item = _parse_rules_item(rules_item_data)

                rules.append(rules_item)

        _time_restriction_time_zone = d.pop("time_restriction_time_zone", UNSET)
        time_restriction_time_zone: NewEscalationPolicyPathDataAttributesTimeRestrictionTimeZone | Unset
        if isinstance(_time_restriction_time_zone, Unset):
            time_restriction_time_zone = UNSET
        else:
            time_restriction_time_zone = check_new_escalation_policy_path_data_attributes_time_restriction_time_zone(
                _time_restriction_time_zone
            )

        _time_restrictions = d.pop("time_restrictions", UNSET)
        time_restrictions: list[NewEscalationPolicyPathDataAttributesTimeRestrictionsItem] | Unset = UNSET
        if _time_restrictions is not UNSET:
            time_restrictions = []
            for time_restrictions_item_data in _time_restrictions:
                time_restrictions_item = NewEscalationPolicyPathDataAttributesTimeRestrictionsItem.from_dict(
                    time_restrictions_item_data
                )

                time_restrictions.append(time_restrictions_item)

        new_escalation_policy_path_data_attributes = cls(
            name=name,
            notification_type=notification_type,
            path_type=path_type,
            after_deferral_behavior=after_deferral_behavior,
            after_deferral_path_id=after_deferral_path_id,
            default=default,
            match_mode=match_mode,
            position=position,
            repeat=repeat,
            repeat_count=repeat_count,
            initial_delay=initial_delay,
            rules=rules,
            time_restriction_time_zone=time_restriction_time_zone,
            time_restrictions=time_restrictions,
        )

        return new_escalation_policy_path_data_attributes
