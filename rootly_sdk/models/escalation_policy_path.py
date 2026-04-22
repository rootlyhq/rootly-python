from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_policy_path_after_deferral_behavior import (
    EscalationPolicyPathAfterDeferralBehavior,
    check_escalation_policy_path_after_deferral_behavior,
)
from ..models.escalation_policy_path_match_mode import (
    EscalationPolicyPathMatchMode,
    check_escalation_policy_path_match_mode,
)
from ..models.escalation_policy_path_path_type import (
    EscalationPolicyPathPathType,
    check_escalation_policy_path_path_type,
)
from ..models.escalation_policy_path_time_restriction_time_zone import (
    EscalationPolicyPathTimeRestrictionTimeZone,
    check_escalation_policy_path_time_restriction_time_zone,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_policy_path_rules_item_type_0 import EscalationPolicyPathRulesItemType0
    from ..models.escalation_policy_path_rules_item_type_1 import EscalationPolicyPathRulesItemType1
    from ..models.escalation_policy_path_rules_item_type_2 import EscalationPolicyPathRulesItemType2
    from ..models.escalation_policy_path_rules_item_type_3 import EscalationPolicyPathRulesItemType3
    from ..models.escalation_policy_path_rules_item_type_4 import EscalationPolicyPathRulesItemType4
    from ..models.escalation_policy_path_rules_item_type_5 import EscalationPolicyPathRulesItemType5
    from ..models.escalation_policy_path_rules_item_type_6_type_0 import EscalationPolicyPathRulesItemType6Type0
    from ..models.escalation_policy_path_rules_item_type_6_type_1 import EscalationPolicyPathRulesItemType6Type1
    from ..models.escalation_policy_path_rules_item_type_6_type_2 import EscalationPolicyPathRulesItemType6Type2
    from ..models.escalation_policy_path_rules_item_type_6_type_3 import EscalationPolicyPathRulesItemType6Type3
    from ..models.escalation_policy_path_rules_item_type_6_type_4 import EscalationPolicyPathRulesItemType6Type4
    from ..models.escalation_policy_path_rules_item_type_6_type_5 import EscalationPolicyPathRulesItemType6Type5
    from ..models.escalation_policy_path_rules_item_type_7_type_0 import EscalationPolicyPathRulesItemType7Type0
    from ..models.escalation_policy_path_rules_item_type_7_type_1 import EscalationPolicyPathRulesItemType7Type1
    from ..models.escalation_policy_path_rules_item_type_7_type_2 import EscalationPolicyPathRulesItemType7Type2
    from ..models.escalation_policy_path_rules_item_type_7_type_3 import EscalationPolicyPathRulesItemType7Type3
    from ..models.escalation_policy_path_rules_item_type_7_type_4 import EscalationPolicyPathRulesItemType7Type4
    from ..models.escalation_policy_path_rules_item_type_7_type_5 import EscalationPolicyPathRulesItemType7Type5
    from ..models.escalation_policy_path_time_restrictions_item import EscalationPolicyPathTimeRestrictionsItem


T = TypeVar("T", bound="EscalationPolicyPath")


@_attrs_define
class EscalationPolicyPath:
    """
    Attributes:
        name (str): The name of the escalation path
        default (bool): Whether this escalation path is the default path
        notification_type (str): Notification rule type
        escalation_policy_id (str): The ID of the escalation policy
        repeat (bool | None): Whether this path should be repeated until someone acknowledges the alert
        repeat_count (int | None): The number of times this path will be executed until someone acknowledges the alert
        path_type (EscalationPolicyPathPathType | Unset): The type of escalation path
        after_deferral_behavior (EscalationPolicyPathAfterDeferralBehavior | Unset): What happens after a deferral path
            finishes
        after_deferral_path_id (None | str | Unset): The escalation path to execute after this deferral path when
            after_deferral_behavior is execute_path
        match_mode (EscalationPolicyPathMatchMode | Unset): How path rules are matched.
        position (int | Unset): The position of this path in the paths for this EP.
        initial_delay (int | Unset): Initial delay for escalation path in minutes. Maximum 1 week (10080).
        created_at (str | Unset): Date of creation
        updated_at (str | Unset): Date of last update
        rules (list[EscalationPolicyPathRulesItemType0 | EscalationPolicyPathRulesItemType1 |
            EscalationPolicyPathRulesItemType2 | EscalationPolicyPathRulesItemType3 | EscalationPolicyPathRulesItemType4 |
            EscalationPolicyPathRulesItemType5 | EscalationPolicyPathRulesItemType6Type0 |
            EscalationPolicyPathRulesItemType6Type1 | EscalationPolicyPathRulesItemType6Type2 |
            EscalationPolicyPathRulesItemType6Type3 | EscalationPolicyPathRulesItemType6Type4 |
            EscalationPolicyPathRulesItemType6Type5 | EscalationPolicyPathRulesItemType7Type0 |
            EscalationPolicyPathRulesItemType7Type1 | EscalationPolicyPathRulesItemType7Type2 |
            EscalationPolicyPathRulesItemType7Type3 | EscalationPolicyPathRulesItemType7Type4 |
            EscalationPolicyPathRulesItemType7Type5] | Unset): Escalation path rules
        time_restriction_time_zone (EscalationPolicyPathTimeRestrictionTimeZone | Unset): Time zone used for time
            restrictions.
        time_restrictions (list[EscalationPolicyPathTimeRestrictionsItem] | Unset): If time restrictions are set, alerts
            will follow this path when they arrive within the specified time ranges and meet the rules.
    """

    name: str
    default: bool
    notification_type: str
    escalation_policy_id: str
    repeat: bool | None
    repeat_count: int | None
    path_type: EscalationPolicyPathPathType | Unset = UNSET
    after_deferral_behavior: EscalationPolicyPathAfterDeferralBehavior | Unset = UNSET
    after_deferral_path_id: None | str | Unset = UNSET
    match_mode: EscalationPolicyPathMatchMode | Unset = UNSET
    position: int | Unset = UNSET
    initial_delay: int | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    rules: (
        list[
            EscalationPolicyPathRulesItemType0
            | EscalationPolicyPathRulesItemType1
            | EscalationPolicyPathRulesItemType2
            | EscalationPolicyPathRulesItemType3
            | EscalationPolicyPathRulesItemType4
            | EscalationPolicyPathRulesItemType5
            | EscalationPolicyPathRulesItemType6Type0
            | EscalationPolicyPathRulesItemType6Type1
            | EscalationPolicyPathRulesItemType6Type2
            | EscalationPolicyPathRulesItemType6Type3
            | EscalationPolicyPathRulesItemType6Type4
            | EscalationPolicyPathRulesItemType6Type5
            | EscalationPolicyPathRulesItemType7Type0
            | EscalationPolicyPathRulesItemType7Type1
            | EscalationPolicyPathRulesItemType7Type2
            | EscalationPolicyPathRulesItemType7Type3
            | EscalationPolicyPathRulesItemType7Type4
            | EscalationPolicyPathRulesItemType7Type5
        ]
        | Unset
    ) = UNSET
    time_restriction_time_zone: EscalationPolicyPathTimeRestrictionTimeZone | Unset = UNSET
    time_restrictions: list[EscalationPolicyPathTimeRestrictionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.escalation_policy_path_rules_item_type_0 import EscalationPolicyPathRulesItemType0
        from ..models.escalation_policy_path_rules_item_type_1 import EscalationPolicyPathRulesItemType1
        from ..models.escalation_policy_path_rules_item_type_2 import EscalationPolicyPathRulesItemType2
        from ..models.escalation_policy_path_rules_item_type_3 import EscalationPolicyPathRulesItemType3
        from ..models.escalation_policy_path_rules_item_type_4 import EscalationPolicyPathRulesItemType4
        from ..models.escalation_policy_path_rules_item_type_5 import EscalationPolicyPathRulesItemType5
        from ..models.escalation_policy_path_rules_item_type_6_type_0 import EscalationPolicyPathRulesItemType6Type0
        from ..models.escalation_policy_path_rules_item_type_6_type_1 import EscalationPolicyPathRulesItemType6Type1
        from ..models.escalation_policy_path_rules_item_type_6_type_2 import EscalationPolicyPathRulesItemType6Type2
        from ..models.escalation_policy_path_rules_item_type_6_type_3 import EscalationPolicyPathRulesItemType6Type3
        from ..models.escalation_policy_path_rules_item_type_6_type_4 import EscalationPolicyPathRulesItemType6Type4
        from ..models.escalation_policy_path_rules_item_type_6_type_5 import EscalationPolicyPathRulesItemType6Type5
        from ..models.escalation_policy_path_rules_item_type_7_type_0 import EscalationPolicyPathRulesItemType7Type0
        from ..models.escalation_policy_path_rules_item_type_7_type_1 import EscalationPolicyPathRulesItemType7Type1
        from ..models.escalation_policy_path_rules_item_type_7_type_2 import EscalationPolicyPathRulesItemType7Type2
        from ..models.escalation_policy_path_rules_item_type_7_type_3 import EscalationPolicyPathRulesItemType7Type3
        from ..models.escalation_policy_path_rules_item_type_7_type_4 import EscalationPolicyPathRulesItemType7Type4

        name = self.name

        default = self.default

        notification_type = self.notification_type

        escalation_policy_id = self.escalation_policy_id

        repeat: bool | None
        repeat = self.repeat

        repeat_count: int | None
        repeat_count = self.repeat_count

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

        match_mode: str | Unset = UNSET
        if not isinstance(self.match_mode, Unset):
            match_mode = self.match_mode

        position = self.position

        initial_delay = self.initial_delay

        created_at = self.created_at

        updated_at = self.updated_at

        rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item: dict[str, Any]
                if isinstance(rules_item_data, EscalationPolicyPathRulesItemType0):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType1):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType2):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType3):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType4):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType5):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType6Type0):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType6Type1):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType6Type2):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType6Type3):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType6Type4):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType6Type5):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType7Type0):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType7Type1):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType7Type2):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType7Type3):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType7Type4):
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
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "default": default,
                "notification_type": notification_type,
                "escalation_policy_id": escalation_policy_id,
                "repeat": repeat,
                "repeat_count": repeat_count,
            }
        )
        if path_type is not UNSET:
            field_dict["path_type"] = path_type
        if after_deferral_behavior is not UNSET:
            field_dict["after_deferral_behavior"] = after_deferral_behavior
        if after_deferral_path_id is not UNSET:
            field_dict["after_deferral_path_id"] = after_deferral_path_id
        if match_mode is not UNSET:
            field_dict["match_mode"] = match_mode
        if position is not UNSET:
            field_dict["position"] = position
        if initial_delay is not UNSET:
            field_dict["initial_delay"] = initial_delay
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if rules is not UNSET:
            field_dict["rules"] = rules
        if time_restriction_time_zone is not UNSET:
            field_dict["time_restriction_time_zone"] = time_restriction_time_zone
        if time_restrictions is not UNSET:
            field_dict["time_restrictions"] = time_restrictions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.escalation_policy_path_rules_item_type_0 import EscalationPolicyPathRulesItemType0
        from ..models.escalation_policy_path_rules_item_type_1 import EscalationPolicyPathRulesItemType1
        from ..models.escalation_policy_path_rules_item_type_2 import EscalationPolicyPathRulesItemType2
        from ..models.escalation_policy_path_rules_item_type_3 import EscalationPolicyPathRulesItemType3
        from ..models.escalation_policy_path_rules_item_type_4 import EscalationPolicyPathRulesItemType4
        from ..models.escalation_policy_path_rules_item_type_5 import EscalationPolicyPathRulesItemType5
        from ..models.escalation_policy_path_rules_item_type_6_type_0 import EscalationPolicyPathRulesItemType6Type0
        from ..models.escalation_policy_path_rules_item_type_6_type_1 import EscalationPolicyPathRulesItemType6Type1
        from ..models.escalation_policy_path_rules_item_type_6_type_2 import EscalationPolicyPathRulesItemType6Type2
        from ..models.escalation_policy_path_rules_item_type_6_type_3 import EscalationPolicyPathRulesItemType6Type3
        from ..models.escalation_policy_path_rules_item_type_6_type_4 import EscalationPolicyPathRulesItemType6Type4
        from ..models.escalation_policy_path_rules_item_type_6_type_5 import EscalationPolicyPathRulesItemType6Type5
        from ..models.escalation_policy_path_rules_item_type_7_type_0 import EscalationPolicyPathRulesItemType7Type0
        from ..models.escalation_policy_path_rules_item_type_7_type_1 import EscalationPolicyPathRulesItemType7Type1
        from ..models.escalation_policy_path_rules_item_type_7_type_2 import EscalationPolicyPathRulesItemType7Type2
        from ..models.escalation_policy_path_rules_item_type_7_type_3 import EscalationPolicyPathRulesItemType7Type3
        from ..models.escalation_policy_path_rules_item_type_7_type_4 import EscalationPolicyPathRulesItemType7Type4
        from ..models.escalation_policy_path_rules_item_type_7_type_5 import EscalationPolicyPathRulesItemType7Type5
        from ..models.escalation_policy_path_time_restrictions_item import EscalationPolicyPathTimeRestrictionsItem

        d = dict(src_dict)
        name = d.pop("name")

        default = d.pop("default")

        notification_type = d.pop("notification_type")

        escalation_policy_id = d.pop("escalation_policy_id")

        def _parse_repeat(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        repeat = _parse_repeat(d.pop("repeat"))

        def _parse_repeat_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        repeat_count = _parse_repeat_count(d.pop("repeat_count"))

        _path_type = d.pop("path_type", UNSET)
        path_type: EscalationPolicyPathPathType | Unset
        if isinstance(_path_type, Unset):
            path_type = UNSET
        else:
            path_type = check_escalation_policy_path_path_type(_path_type)

        _after_deferral_behavior = d.pop("after_deferral_behavior", UNSET)
        after_deferral_behavior: EscalationPolicyPathAfterDeferralBehavior | Unset
        if isinstance(_after_deferral_behavior, Unset):
            after_deferral_behavior = UNSET
        else:
            after_deferral_behavior = check_escalation_policy_path_after_deferral_behavior(_after_deferral_behavior)

        def _parse_after_deferral_path_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        after_deferral_path_id = _parse_after_deferral_path_id(d.pop("after_deferral_path_id", UNSET))

        _match_mode = d.pop("match_mode", UNSET)
        match_mode: EscalationPolicyPathMatchMode | Unset
        if isinstance(_match_mode, Unset):
            match_mode = UNSET
        else:
            match_mode = check_escalation_policy_path_match_mode(_match_mode)

        position = d.pop("position", UNSET)

        initial_delay = d.pop("initial_delay", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _rules = d.pop("rules", UNSET)
        rules: (
            list[
                EscalationPolicyPathRulesItemType0
                | EscalationPolicyPathRulesItemType1
                | EscalationPolicyPathRulesItemType2
                | EscalationPolicyPathRulesItemType3
                | EscalationPolicyPathRulesItemType4
                | EscalationPolicyPathRulesItemType5
                | EscalationPolicyPathRulesItemType6Type0
                | EscalationPolicyPathRulesItemType6Type1
                | EscalationPolicyPathRulesItemType6Type2
                | EscalationPolicyPathRulesItemType6Type3
                | EscalationPolicyPathRulesItemType6Type4
                | EscalationPolicyPathRulesItemType6Type5
                | EscalationPolicyPathRulesItemType7Type0
                | EscalationPolicyPathRulesItemType7Type1
                | EscalationPolicyPathRulesItemType7Type2
                | EscalationPolicyPathRulesItemType7Type3
                | EscalationPolicyPathRulesItemType7Type4
                | EscalationPolicyPathRulesItemType7Type5
            ]
            | Unset
        ) = UNSET
        if _rules is not UNSET:
            rules = []
            for rules_item_data in _rules:

                def _parse_rules_item(
                    data: object,
                ) -> (
                    EscalationPolicyPathRulesItemType0
                    | EscalationPolicyPathRulesItemType1
                    | EscalationPolicyPathRulesItemType2
                    | EscalationPolicyPathRulesItemType3
                    | EscalationPolicyPathRulesItemType4
                    | EscalationPolicyPathRulesItemType5
                    | EscalationPolicyPathRulesItemType6Type0
                    | EscalationPolicyPathRulesItemType6Type1
                    | EscalationPolicyPathRulesItemType6Type2
                    | EscalationPolicyPathRulesItemType6Type3
                    | EscalationPolicyPathRulesItemType6Type4
                    | EscalationPolicyPathRulesItemType6Type5
                    | EscalationPolicyPathRulesItemType7Type0
                    | EscalationPolicyPathRulesItemType7Type1
                    | EscalationPolicyPathRulesItemType7Type2
                    | EscalationPolicyPathRulesItemType7Type3
                    | EscalationPolicyPathRulesItemType7Type4
                    | EscalationPolicyPathRulesItemType7Type5
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_0 = EscalationPolicyPathRulesItemType0.from_dict(data)

                        return rules_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_1 = EscalationPolicyPathRulesItemType1.from_dict(data)

                        return rules_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_2 = EscalationPolicyPathRulesItemType2.from_dict(data)

                        return rules_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_3 = EscalationPolicyPathRulesItemType3.from_dict(data)

                        return rules_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_4 = EscalationPolicyPathRulesItemType4.from_dict(data)

                        return rules_item_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_5 = EscalationPolicyPathRulesItemType5.from_dict(data)

                        return rules_item_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_6_type_0 = EscalationPolicyPathRulesItemType6Type0.from_dict(data)

                        return rules_item_type_6_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_6_type_1 = EscalationPolicyPathRulesItemType6Type1.from_dict(data)

                        return rules_item_type_6_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_6_type_2 = EscalationPolicyPathRulesItemType6Type2.from_dict(data)

                        return rules_item_type_6_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_6_type_3 = EscalationPolicyPathRulesItemType6Type3.from_dict(data)

                        return rules_item_type_6_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_6_type_4 = EscalationPolicyPathRulesItemType6Type4.from_dict(data)

                        return rules_item_type_6_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_6_type_5 = EscalationPolicyPathRulesItemType6Type5.from_dict(data)

                        return rules_item_type_6_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_7_type_0 = EscalationPolicyPathRulesItemType7Type0.from_dict(data)

                        return rules_item_type_7_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_7_type_1 = EscalationPolicyPathRulesItemType7Type1.from_dict(data)

                        return rules_item_type_7_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_7_type_2 = EscalationPolicyPathRulesItemType7Type2.from_dict(data)

                        return rules_item_type_7_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_7_type_3 = EscalationPolicyPathRulesItemType7Type3.from_dict(data)

                        return rules_item_type_7_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        rules_item_type_7_type_4 = EscalationPolicyPathRulesItemType7Type4.from_dict(data)

                        return rules_item_type_7_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_7_type_5 = EscalationPolicyPathRulesItemType7Type5.from_dict(data)

                    return rules_item_type_7_type_5

                rules_item = _parse_rules_item(rules_item_data)

                rules.append(rules_item)

        _time_restriction_time_zone = d.pop("time_restriction_time_zone", UNSET)
        time_restriction_time_zone: EscalationPolicyPathTimeRestrictionTimeZone | Unset
        if isinstance(_time_restriction_time_zone, Unset):
            time_restriction_time_zone = UNSET
        else:
            time_restriction_time_zone = check_escalation_policy_path_time_restriction_time_zone(
                _time_restriction_time_zone
            )

        _time_restrictions = d.pop("time_restrictions", UNSET)
        time_restrictions: list[EscalationPolicyPathTimeRestrictionsItem] | Unset = UNSET
        if _time_restrictions is not UNSET:
            time_restrictions = []
            for time_restrictions_item_data in _time_restrictions:
                time_restrictions_item = EscalationPolicyPathTimeRestrictionsItem.from_dict(time_restrictions_item_data)

                time_restrictions.append(time_restrictions_item)

        escalation_policy_path = cls(
            name=name,
            default=default,
            notification_type=notification_type,
            escalation_policy_id=escalation_policy_id,
            repeat=repeat,
            repeat_count=repeat_count,
            path_type=path_type,
            after_deferral_behavior=after_deferral_behavior,
            after_deferral_path_id=after_deferral_path_id,
            match_mode=match_mode,
            position=position,
            initial_delay=initial_delay,
            created_at=created_at,
            updated_at=updated_at,
            rules=rules,
            time_restriction_time_zone=time_restriction_time_zone,
            time_restrictions=time_restrictions,
        )

        escalation_policy_path.additional_properties = d
        return escalation_policy_path

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
