from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
    from ..models.escalation_policy_path_rules_item_type_6 import EscalationPolicyPathRulesItemType6
    from ..models.escalation_policy_path_rules_item_type_7 import EscalationPolicyPathRulesItemType7
    from ..models.escalation_policy_path_rules_item_type_8_type_0 import EscalationPolicyPathRulesItemType8Type0
    from ..models.escalation_policy_path_rules_item_type_8_type_1 import EscalationPolicyPathRulesItemType8Type1
    from ..models.escalation_policy_path_rules_item_type_8_type_2 import EscalationPolicyPathRulesItemType8Type2
    from ..models.escalation_policy_path_rules_item_type_8_type_3 import EscalationPolicyPathRulesItemType8Type3
    from ..models.escalation_policy_path_rules_item_type_8_type_4 import EscalationPolicyPathRulesItemType8Type4
    from ..models.escalation_policy_path_rules_item_type_8_type_5 import EscalationPolicyPathRulesItemType8Type5
    from ..models.escalation_policy_path_rules_item_type_8_type_6 import EscalationPolicyPathRulesItemType8Type6
    from ..models.escalation_policy_path_rules_item_type_8_type_7 import EscalationPolicyPathRulesItemType8Type7
    from ..models.escalation_policy_path_rules_item_type_9_type_0 import EscalationPolicyPathRulesItemType9Type0
    from ..models.escalation_policy_path_rules_item_type_9_type_1 import EscalationPolicyPathRulesItemType9Type1
    from ..models.escalation_policy_path_rules_item_type_9_type_2 import EscalationPolicyPathRulesItemType9Type2
    from ..models.escalation_policy_path_rules_item_type_9_type_3 import EscalationPolicyPathRulesItemType9Type3
    from ..models.escalation_policy_path_rules_item_type_9_type_4 import EscalationPolicyPathRulesItemType9Type4
    from ..models.escalation_policy_path_rules_item_type_9_type_5 import EscalationPolicyPathRulesItemType9Type5
    from ..models.escalation_policy_path_rules_item_type_9_type_6 import EscalationPolicyPathRulesItemType9Type6
    from ..models.escalation_policy_path_rules_item_type_9_type_7 import EscalationPolicyPathRulesItemType9Type7
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
        repeat (Union[None, bool]): Whether this path should be repeated until someone acknowledges the alert
        repeat_count (Union[None, int]): The number of times this path will be executed until someone acknowledges the
            alert
        path_type (Union[Unset, EscalationPolicyPathPathType]): The type of escalation path
        after_deferral_behavior (Union[Unset, EscalationPolicyPathAfterDeferralBehavior]): What happens after a deferral
            path finishes
        after_deferral_path_id (Union[None, Unset, str]): The escalation path to execute after this deferral path when
            after_deferral_behavior is execute_path
        match_mode (Union[Unset, EscalationPolicyPathMatchMode]): How path rules are matched.
        position (Union[Unset, int]): The position of this path in the paths for this EP.
        initial_delay (Union[Unset, int]): Initial delay for escalation path in minutes. Maximum 1 week (10080).
        retrigger_timeout_minutes (Union[None, Unset, int]): Re-trigger acknowledged alerts on this path after N
            minutes; null inherits the urgency/workspace default, negative = never.
        created_at (Union[Unset, str]): Date of creation
        updated_at (Union[Unset, str]): Date of last update
        rules (Union[Unset, list[Union['EscalationPolicyPathRulesItemType0', 'EscalationPolicyPathRulesItemType1',
            'EscalationPolicyPathRulesItemType2', 'EscalationPolicyPathRulesItemType3',
            'EscalationPolicyPathRulesItemType4', 'EscalationPolicyPathRulesItemType5',
            'EscalationPolicyPathRulesItemType6', 'EscalationPolicyPathRulesItemType7',
            'EscalationPolicyPathRulesItemType8Type0', 'EscalationPolicyPathRulesItemType8Type1',
            'EscalationPolicyPathRulesItemType8Type2', 'EscalationPolicyPathRulesItemType8Type3',
            'EscalationPolicyPathRulesItemType8Type4', 'EscalationPolicyPathRulesItemType8Type5',
            'EscalationPolicyPathRulesItemType8Type6', 'EscalationPolicyPathRulesItemType8Type7',
            'EscalationPolicyPathRulesItemType9Type0', 'EscalationPolicyPathRulesItemType9Type1',
            'EscalationPolicyPathRulesItemType9Type2', 'EscalationPolicyPathRulesItemType9Type3',
            'EscalationPolicyPathRulesItemType9Type4', 'EscalationPolicyPathRulesItemType9Type5',
            'EscalationPolicyPathRulesItemType9Type6', 'EscalationPolicyPathRulesItemType9Type7']]]): Escalation path rules
        time_restriction_time_zone (Union[Unset, EscalationPolicyPathTimeRestrictionTimeZone]): Time zone used for time
            restrictions.
        time_restrictions (Union[Unset, list['EscalationPolicyPathTimeRestrictionsItem']]): If time restrictions are
            set, alerts will follow this path when they arrive within the specified time ranges and meet the rules.
    """

    name: str
    default: bool
    notification_type: str
    escalation_policy_id: str
    repeat: None | bool
    repeat_count: None | int
    path_type: Unset | EscalationPolicyPathPathType = UNSET
    after_deferral_behavior: Unset | EscalationPolicyPathAfterDeferralBehavior = UNSET
    after_deferral_path_id: None | Unset | str = UNSET
    match_mode: Unset | EscalationPolicyPathMatchMode = UNSET
    position: Unset | int = UNSET
    initial_delay: Unset | int = UNSET
    retrigger_timeout_minutes: None | Unset | int = UNSET
    created_at: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    rules: (
        Unset
        | list[
            Union[
                "EscalationPolicyPathRulesItemType0",
                "EscalationPolicyPathRulesItemType1",
                "EscalationPolicyPathRulesItemType2",
                "EscalationPolicyPathRulesItemType3",
                "EscalationPolicyPathRulesItemType4",
                "EscalationPolicyPathRulesItemType5",
                "EscalationPolicyPathRulesItemType6",
                "EscalationPolicyPathRulesItemType7",
                "EscalationPolicyPathRulesItemType8Type0",
                "EscalationPolicyPathRulesItemType8Type1",
                "EscalationPolicyPathRulesItemType8Type2",
                "EscalationPolicyPathRulesItemType8Type3",
                "EscalationPolicyPathRulesItemType8Type4",
                "EscalationPolicyPathRulesItemType8Type5",
                "EscalationPolicyPathRulesItemType8Type6",
                "EscalationPolicyPathRulesItemType8Type7",
                "EscalationPolicyPathRulesItemType9Type0",
                "EscalationPolicyPathRulesItemType9Type1",
                "EscalationPolicyPathRulesItemType9Type2",
                "EscalationPolicyPathRulesItemType9Type3",
                "EscalationPolicyPathRulesItemType9Type4",
                "EscalationPolicyPathRulesItemType9Type5",
                "EscalationPolicyPathRulesItemType9Type6",
                "EscalationPolicyPathRulesItemType9Type7",
            ]
        ]
    ) = UNSET
    time_restriction_time_zone: Unset | EscalationPolicyPathTimeRestrictionTimeZone = UNSET
    time_restrictions: Unset | list["EscalationPolicyPathTimeRestrictionsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.escalation_policy_path_rules_item_type_0 import EscalationPolicyPathRulesItemType0
        from ..models.escalation_policy_path_rules_item_type_1 import EscalationPolicyPathRulesItemType1
        from ..models.escalation_policy_path_rules_item_type_2 import EscalationPolicyPathRulesItemType2
        from ..models.escalation_policy_path_rules_item_type_3 import EscalationPolicyPathRulesItemType3
        from ..models.escalation_policy_path_rules_item_type_4 import EscalationPolicyPathRulesItemType4
        from ..models.escalation_policy_path_rules_item_type_5 import EscalationPolicyPathRulesItemType5
        from ..models.escalation_policy_path_rules_item_type_6 import EscalationPolicyPathRulesItemType6
        from ..models.escalation_policy_path_rules_item_type_7 import EscalationPolicyPathRulesItemType7
        from ..models.escalation_policy_path_rules_item_type_8_type_0 import EscalationPolicyPathRulesItemType8Type0
        from ..models.escalation_policy_path_rules_item_type_8_type_1 import EscalationPolicyPathRulesItemType8Type1
        from ..models.escalation_policy_path_rules_item_type_8_type_2 import EscalationPolicyPathRulesItemType8Type2
        from ..models.escalation_policy_path_rules_item_type_8_type_3 import EscalationPolicyPathRulesItemType8Type3
        from ..models.escalation_policy_path_rules_item_type_8_type_4 import EscalationPolicyPathRulesItemType8Type4
        from ..models.escalation_policy_path_rules_item_type_8_type_5 import EscalationPolicyPathRulesItemType8Type5
        from ..models.escalation_policy_path_rules_item_type_8_type_6 import EscalationPolicyPathRulesItemType8Type6
        from ..models.escalation_policy_path_rules_item_type_8_type_7 import EscalationPolicyPathRulesItemType8Type7
        from ..models.escalation_policy_path_rules_item_type_9_type_0 import EscalationPolicyPathRulesItemType9Type0
        from ..models.escalation_policy_path_rules_item_type_9_type_1 import EscalationPolicyPathRulesItemType9Type1
        from ..models.escalation_policy_path_rules_item_type_9_type_2 import EscalationPolicyPathRulesItemType9Type2
        from ..models.escalation_policy_path_rules_item_type_9_type_3 import EscalationPolicyPathRulesItemType9Type3
        from ..models.escalation_policy_path_rules_item_type_9_type_4 import EscalationPolicyPathRulesItemType9Type4
        from ..models.escalation_policy_path_rules_item_type_9_type_5 import EscalationPolicyPathRulesItemType9Type5
        from ..models.escalation_policy_path_rules_item_type_9_type_6 import EscalationPolicyPathRulesItemType9Type6

        name = self.name

        default = self.default

        notification_type = self.notification_type

        escalation_policy_id = self.escalation_policy_id

        repeat: None | bool
        repeat = self.repeat

        repeat_count: None | int
        repeat_count = self.repeat_count

        path_type: Unset | str = UNSET
        if not isinstance(self.path_type, Unset):
            path_type = self.path_type

        after_deferral_behavior: Unset | str = UNSET
        if not isinstance(self.after_deferral_behavior, Unset):
            after_deferral_behavior = self.after_deferral_behavior

        after_deferral_path_id: None | Unset | str
        if isinstance(self.after_deferral_path_id, Unset):
            after_deferral_path_id = UNSET
        else:
            after_deferral_path_id = self.after_deferral_path_id

        match_mode: Unset | str = UNSET
        if not isinstance(self.match_mode, Unset):
            match_mode = self.match_mode

        position = self.position

        initial_delay = self.initial_delay

        retrigger_timeout_minutes: None | Unset | int
        if isinstance(self.retrigger_timeout_minutes, Unset):
            retrigger_timeout_minutes = UNSET
        else:
            retrigger_timeout_minutes = self.retrigger_timeout_minutes

        created_at = self.created_at

        updated_at = self.updated_at

        rules: Unset | list[dict[str, Any]] = UNSET
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
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType6):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType7):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType8Type0):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType8Type1):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType8Type2):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType8Type3):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType8Type4):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType8Type5):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType8Type6):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType8Type7):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType9Type0):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType9Type1):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType9Type2):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType9Type3):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType9Type4):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType9Type5):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType9Type6):
                    rules_item = rules_item_data.to_dict()
                else:
                    rules_item = rules_item_data.to_dict()

                rules.append(rules_item)

        time_restriction_time_zone: Unset | str = UNSET
        if not isinstance(self.time_restriction_time_zone, Unset):
            time_restriction_time_zone = self.time_restriction_time_zone

        time_restrictions: Unset | list[dict[str, Any]] = UNSET
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
        if retrigger_timeout_minutes is not UNSET:
            field_dict["retrigger_timeout_minutes"] = retrigger_timeout_minutes
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
        from ..models.escalation_policy_path_rules_item_type_6 import EscalationPolicyPathRulesItemType6
        from ..models.escalation_policy_path_rules_item_type_7 import EscalationPolicyPathRulesItemType7
        from ..models.escalation_policy_path_rules_item_type_8_type_0 import EscalationPolicyPathRulesItemType8Type0
        from ..models.escalation_policy_path_rules_item_type_8_type_1 import EscalationPolicyPathRulesItemType8Type1
        from ..models.escalation_policy_path_rules_item_type_8_type_2 import EscalationPolicyPathRulesItemType8Type2
        from ..models.escalation_policy_path_rules_item_type_8_type_3 import EscalationPolicyPathRulesItemType8Type3
        from ..models.escalation_policy_path_rules_item_type_8_type_4 import EscalationPolicyPathRulesItemType8Type4
        from ..models.escalation_policy_path_rules_item_type_8_type_5 import EscalationPolicyPathRulesItemType8Type5
        from ..models.escalation_policy_path_rules_item_type_8_type_6 import EscalationPolicyPathRulesItemType8Type6
        from ..models.escalation_policy_path_rules_item_type_8_type_7 import EscalationPolicyPathRulesItemType8Type7
        from ..models.escalation_policy_path_rules_item_type_9_type_0 import EscalationPolicyPathRulesItemType9Type0
        from ..models.escalation_policy_path_rules_item_type_9_type_1 import EscalationPolicyPathRulesItemType9Type1
        from ..models.escalation_policy_path_rules_item_type_9_type_2 import EscalationPolicyPathRulesItemType9Type2
        from ..models.escalation_policy_path_rules_item_type_9_type_3 import EscalationPolicyPathRulesItemType9Type3
        from ..models.escalation_policy_path_rules_item_type_9_type_4 import EscalationPolicyPathRulesItemType9Type4
        from ..models.escalation_policy_path_rules_item_type_9_type_5 import EscalationPolicyPathRulesItemType9Type5
        from ..models.escalation_policy_path_rules_item_type_9_type_6 import EscalationPolicyPathRulesItemType9Type6
        from ..models.escalation_policy_path_rules_item_type_9_type_7 import EscalationPolicyPathRulesItemType9Type7
        from ..models.escalation_policy_path_time_restrictions_item import EscalationPolicyPathTimeRestrictionsItem

        d = dict(src_dict)
        name = d.pop("name")

        default = d.pop("default")

        notification_type = d.pop("notification_type")

        escalation_policy_id = d.pop("escalation_policy_id")

        def _parse_repeat(data: object) -> None | bool:
            if data is None:
                return data
            return cast(None | bool, data)

        repeat = _parse_repeat(d.pop("repeat"))

        def _parse_repeat_count(data: object) -> None | int:
            if data is None:
                return data
            return cast(None | int, data)

        repeat_count = _parse_repeat_count(d.pop("repeat_count"))

        _path_type = d.pop("path_type", UNSET)
        path_type: Unset | EscalationPolicyPathPathType
        if isinstance(_path_type, Unset):
            path_type = UNSET
        else:
            path_type = check_escalation_policy_path_path_type(_path_type)

        _after_deferral_behavior = d.pop("after_deferral_behavior", UNSET)
        after_deferral_behavior: Unset | EscalationPolicyPathAfterDeferralBehavior
        if isinstance(_after_deferral_behavior, Unset):
            after_deferral_behavior = UNSET
        else:
            after_deferral_behavior = check_escalation_policy_path_after_deferral_behavior(_after_deferral_behavior)

        def _parse_after_deferral_path_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        after_deferral_path_id = _parse_after_deferral_path_id(d.pop("after_deferral_path_id", UNSET))

        _match_mode = d.pop("match_mode", UNSET)
        match_mode: Unset | EscalationPolicyPathMatchMode
        if isinstance(_match_mode, Unset):
            match_mode = UNSET
        else:
            match_mode = check_escalation_policy_path_match_mode(_match_mode)

        position = d.pop("position", UNSET)

        initial_delay = d.pop("initial_delay", UNSET)

        def _parse_retrigger_timeout_minutes(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        retrigger_timeout_minutes = _parse_retrigger_timeout_minutes(d.pop("retrigger_timeout_minutes", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:

            def _parse_rules_item(
                data: object,
            ) -> Union[
                "EscalationPolicyPathRulesItemType0",
                "EscalationPolicyPathRulesItemType1",
                "EscalationPolicyPathRulesItemType2",
                "EscalationPolicyPathRulesItemType3",
                "EscalationPolicyPathRulesItemType4",
                "EscalationPolicyPathRulesItemType5",
                "EscalationPolicyPathRulesItemType6",
                "EscalationPolicyPathRulesItemType7",
                "EscalationPolicyPathRulesItemType8Type0",
                "EscalationPolicyPathRulesItemType8Type1",
                "EscalationPolicyPathRulesItemType8Type2",
                "EscalationPolicyPathRulesItemType8Type3",
                "EscalationPolicyPathRulesItemType8Type4",
                "EscalationPolicyPathRulesItemType8Type5",
                "EscalationPolicyPathRulesItemType8Type6",
                "EscalationPolicyPathRulesItemType8Type7",
                "EscalationPolicyPathRulesItemType9Type0",
                "EscalationPolicyPathRulesItemType9Type1",
                "EscalationPolicyPathRulesItemType9Type2",
                "EscalationPolicyPathRulesItemType9Type3",
                "EscalationPolicyPathRulesItemType9Type4",
                "EscalationPolicyPathRulesItemType9Type5",
                "EscalationPolicyPathRulesItemType9Type6",
                "EscalationPolicyPathRulesItemType9Type7",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_0 = EscalationPolicyPathRulesItemType0.from_dict(data)

                    return rules_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_1 = EscalationPolicyPathRulesItemType1.from_dict(data)

                    return rules_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_2 = EscalationPolicyPathRulesItemType2.from_dict(data)

                    return rules_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_3 = EscalationPolicyPathRulesItemType3.from_dict(data)

                    return rules_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_4 = EscalationPolicyPathRulesItemType4.from_dict(data)

                    return rules_item_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_5 = EscalationPolicyPathRulesItemType5.from_dict(data)

                    return rules_item_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_6 = EscalationPolicyPathRulesItemType6.from_dict(data)

                    return rules_item_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_7 = EscalationPolicyPathRulesItemType7.from_dict(data)

                    return rules_item_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_0 = EscalationPolicyPathRulesItemType8Type0.from_dict(data)

                    return rules_item_type_8_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_1 = EscalationPolicyPathRulesItemType8Type1.from_dict(data)

                    return rules_item_type_8_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_2 = EscalationPolicyPathRulesItemType8Type2.from_dict(data)

                    return rules_item_type_8_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_3 = EscalationPolicyPathRulesItemType8Type3.from_dict(data)

                    return rules_item_type_8_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_4 = EscalationPolicyPathRulesItemType8Type4.from_dict(data)

                    return rules_item_type_8_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_5 = EscalationPolicyPathRulesItemType8Type5.from_dict(data)

                    return rules_item_type_8_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_6 = EscalationPolicyPathRulesItemType8Type6.from_dict(data)

                    return rules_item_type_8_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_7 = EscalationPolicyPathRulesItemType8Type7.from_dict(data)

                    return rules_item_type_8_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_9_type_0 = EscalationPolicyPathRulesItemType9Type0.from_dict(data)

                    return rules_item_type_9_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_9_type_1 = EscalationPolicyPathRulesItemType9Type1.from_dict(data)

                    return rules_item_type_9_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_9_type_2 = EscalationPolicyPathRulesItemType9Type2.from_dict(data)

                    return rules_item_type_9_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_9_type_3 = EscalationPolicyPathRulesItemType9Type3.from_dict(data)

                    return rules_item_type_9_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_9_type_4 = EscalationPolicyPathRulesItemType9Type4.from_dict(data)

                    return rules_item_type_9_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_9_type_5 = EscalationPolicyPathRulesItemType9Type5.from_dict(data)

                    return rules_item_type_9_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_9_type_6 = EscalationPolicyPathRulesItemType9Type6.from_dict(data)

                    return rules_item_type_9_type_6
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                rules_item_type_9_type_7 = EscalationPolicyPathRulesItemType9Type7.from_dict(data)

                return rules_item_type_9_type_7

            rules_item = _parse_rules_item(rules_item_data)

            rules.append(rules_item)

        _time_restriction_time_zone = d.pop("time_restriction_time_zone", UNSET)
        time_restriction_time_zone: Unset | EscalationPolicyPathTimeRestrictionTimeZone
        if isinstance(_time_restriction_time_zone, Unset):
            time_restriction_time_zone = UNSET
        else:
            time_restriction_time_zone = check_escalation_policy_path_time_restriction_time_zone(
                _time_restriction_time_zone
            )

        time_restrictions = []
        _time_restrictions = d.pop("time_restrictions", UNSET)
        for time_restrictions_item_data in _time_restrictions or []:
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
            retrigger_timeout_minutes=retrigger_timeout_minutes,
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
