from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.update_escalation_policy_path_data_attributes_after_deferral_behavior import (
    UpdateEscalationPolicyPathDataAttributesAfterDeferralBehavior,
    check_update_escalation_policy_path_data_attributes_after_deferral_behavior,
)
from ..models.update_escalation_policy_path_data_attributes_match_mode import (
    UpdateEscalationPolicyPathDataAttributesMatchMode,
    check_update_escalation_policy_path_data_attributes_match_mode,
)
from ..models.update_escalation_policy_path_data_attributes_notification_type import (
    UpdateEscalationPolicyPathDataAttributesNotificationType,
    check_update_escalation_policy_path_data_attributes_notification_type,
)
from ..models.update_escalation_policy_path_data_attributes_path_type import (
    UpdateEscalationPolicyPathDataAttributesPathType,
    check_update_escalation_policy_path_data_attributes_path_type,
)
from ..models.update_escalation_policy_path_data_attributes_time_restriction_time_zone import (
    UpdateEscalationPolicyPathDataAttributesTimeRestrictionTimeZone,
    check_update_escalation_policy_path_data_attributes_time_restriction_time_zone,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_0 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType0,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_1 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType1,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_2 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType2,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_3 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType3,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_4 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType4,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_5 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType5,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_6 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType6,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_7 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType7,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_0 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType8Type0,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_1 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType8Type1,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_2 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType8Type2,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_3 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType8Type3,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_4 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType8Type4,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_5 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType8Type5,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_6 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType8Type6,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_7 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType8Type7,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_0 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType9Type0,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_1 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType9Type1,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_2 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType9Type2,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_3 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType9Type3,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_4 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType9Type4,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_5 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType9Type5,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_6 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType9Type6,
    )
    from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_7 import (
        UpdateEscalationPolicyPathDataAttributesRulesItemType9Type7,
    )
    from ..models.update_escalation_policy_path_data_attributes_time_restrictions_item import (
        UpdateEscalationPolicyPathDataAttributesTimeRestrictionsItem,
    )


T = TypeVar("T", bound="UpdateEscalationPolicyPathDataAttributes")


@_attrs_define
class UpdateEscalationPolicyPathDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the escalation path
        notification_type (Union[Unset, UpdateEscalationPolicyPathDataAttributesNotificationType]): Position of the
            escalation policy level Default: 'audible'.
        path_type (Union[Unset, UpdateEscalationPolicyPathDataAttributesPathType]): The type of escalation path. Cannot
            be changed after creation.
        after_deferral_behavior (Union[Unset, UpdateEscalationPolicyPathDataAttributesAfterDeferralBehavior]): What
            happens after a deferral path finishes.
        after_deferral_path_id (Union[None, Unset, str]): The escalation path to execute after this deferral path when
            after_deferral_behavior is execute_path.
        default (Union[None, Unset, bool]): Whether this escalation path is the default path
        match_mode (Union[Unset, UpdateEscalationPolicyPathDataAttributesMatchMode]): How path rules are matched.
            Default: 'match-all-rules'.
        position (Union[Unset, int]): The position of this path in the paths for this EP.
        repeat (Union[None, Unset, bool]): Whether this path should be repeated until someone acknowledges the alert
        repeat_count (Union[None, Unset, int]): The number of times this path will be executed until someone
            acknowledges the alert
        initial_delay (Union[Unset, int]): Initial delay for escalation path in minutes. Maximum 1 week (10080).
        retrigger_timeout_minutes (Union[None, Unset, int]): Re-trigger acknowledged alerts on this path after N
            minutes; null inherits the urgency/workspace default, negative = never.
        rules (Union[Unset, list[Union['UpdateEscalationPolicyPathDataAttributesRulesItemType0',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType1',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType2',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType3',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType4',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType5',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType6',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType7',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType8Type0',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType8Type1',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType8Type2',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType8Type3',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType8Type4',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType8Type5',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType8Type6',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType8Type7',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType9Type0',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType9Type1',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType9Type2',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType9Type3',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType9Type4',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType9Type5',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType9Type6',
            'UpdateEscalationPolicyPathDataAttributesRulesItemType9Type7']]]): Escalation path conditions
        time_restriction_time_zone (Union[Unset, UpdateEscalationPolicyPathDataAttributesTimeRestrictionTimeZone]): Time
            zone used for time restrictions.
        time_restrictions (Union[Unset, list['UpdateEscalationPolicyPathDataAttributesTimeRestrictionsItem']]): If time
            restrictions are set, alerts will follow this path when they arrive within the specified time ranges and meet
            the rules.
    """

    name: Unset | str = UNSET
    notification_type: Unset | UpdateEscalationPolicyPathDataAttributesNotificationType = "audible"
    path_type: Unset | UpdateEscalationPolicyPathDataAttributesPathType = UNSET
    after_deferral_behavior: Unset | UpdateEscalationPolicyPathDataAttributesAfterDeferralBehavior = UNSET
    after_deferral_path_id: None | Unset | str = UNSET
    default: None | Unset | bool = UNSET
    match_mode: Unset | UpdateEscalationPolicyPathDataAttributesMatchMode = "match-all-rules"
    position: Unset | int = UNSET
    repeat: None | Unset | bool = UNSET
    repeat_count: None | Unset | int = UNSET
    initial_delay: Unset | int = UNSET
    retrigger_timeout_minutes: None | Unset | int = UNSET
    rules: (
        Unset
        | list[
            Union[
                "UpdateEscalationPolicyPathDataAttributesRulesItemType0",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType1",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType2",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType3",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType4",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType5",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType6",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType7",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type0",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type1",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type2",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type3",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type4",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type5",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type6",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type7",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type0",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type1",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type2",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type3",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type4",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type5",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type6",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type7",
            ]
        ]
    ) = UNSET
    time_restriction_time_zone: Unset | UpdateEscalationPolicyPathDataAttributesTimeRestrictionTimeZone = UNSET
    time_restrictions: Unset | list["UpdateEscalationPolicyPathDataAttributesTimeRestrictionsItem"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_0 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType0,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_1 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType1,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_2 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType2,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_3 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType3,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_4 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType4,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_5 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType5,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_6 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType6,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_7 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType7,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_0 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type0,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_1 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type1,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_2 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type2,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_3 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type3,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_4 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type4,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_5 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type5,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_6 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type6,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_7 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type7,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_0 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType9Type0,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_1 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType9Type1,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_2 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType9Type2,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_3 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType9Type3,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_4 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType9Type4,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_5 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType9Type5,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_6 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType9Type6,
        )

        name = self.name

        notification_type: Unset | str = UNSET
        if not isinstance(self.notification_type, Unset):
            notification_type = self.notification_type

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

        default: None | Unset | bool
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        match_mode: Unset | str = UNSET
        if not isinstance(self.match_mode, Unset):
            match_mode = self.match_mode

        position = self.position

        repeat: None | Unset | bool
        if isinstance(self.repeat, Unset):
            repeat = UNSET
        else:
            repeat = self.repeat

        repeat_count: None | Unset | int
        if isinstance(self.repeat_count, Unset):
            repeat_count = UNSET
        else:
            repeat_count = self.repeat_count

        initial_delay = self.initial_delay

        retrigger_timeout_minutes: None | Unset | int
        if isinstance(self.retrigger_timeout_minutes, Unset):
            retrigger_timeout_minutes = UNSET
        else:
            retrigger_timeout_minutes = self.retrigger_timeout_minutes

        rules: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item: dict[str, Any]
                if isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType0):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType1):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType2):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType3):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType4):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType5):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType6):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType7):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType8Type0):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType8Type1):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType8Type2):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType8Type3):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType8Type4):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType8Type5):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType8Type6):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType8Type7):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType9Type0):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType9Type1):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType9Type2):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType9Type3):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType9Type4):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType9Type5):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, UpdateEscalationPolicyPathDataAttributesRulesItemType9Type6):
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

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        if retrigger_timeout_minutes is not UNSET:
            field_dict["retrigger_timeout_minutes"] = retrigger_timeout_minutes
        if rules is not UNSET:
            field_dict["rules"] = rules
        if time_restriction_time_zone is not UNSET:
            field_dict["time_restriction_time_zone"] = time_restriction_time_zone
        if time_restrictions is not UNSET:
            field_dict["time_restrictions"] = time_restrictions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_0 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType0,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_1 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType1,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_2 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType2,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_3 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType3,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_4 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType4,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_5 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType5,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_6 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType6,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_7 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType7,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_0 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type0,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_1 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type1,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_2 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type2,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_3 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type3,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_4 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type4,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_5 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type5,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_6 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type6,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_8_type_7 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType8Type7,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_0 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType9Type0,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_1 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType9Type1,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_2 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType9Type2,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_3 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType9Type3,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_4 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType9Type4,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_5 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType9Type5,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_6 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType9Type6,
        )
        from ..models.update_escalation_policy_path_data_attributes_rules_item_type_9_type_7 import (
            UpdateEscalationPolicyPathDataAttributesRulesItemType9Type7,
        )
        from ..models.update_escalation_policy_path_data_attributes_time_restrictions_item import (
            UpdateEscalationPolicyPathDataAttributesTimeRestrictionsItem,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _notification_type = d.pop("notification_type", UNSET)
        notification_type: Unset | UpdateEscalationPolicyPathDataAttributesNotificationType
        if isinstance(_notification_type, Unset):
            notification_type = UNSET
        else:
            notification_type = check_update_escalation_policy_path_data_attributes_notification_type(
                _notification_type
            )

        _path_type = d.pop("path_type", UNSET)
        path_type: Unset | UpdateEscalationPolicyPathDataAttributesPathType
        if isinstance(_path_type, Unset):
            path_type = UNSET
        else:
            path_type = check_update_escalation_policy_path_data_attributes_path_type(_path_type)

        _after_deferral_behavior = d.pop("after_deferral_behavior", UNSET)
        after_deferral_behavior: Unset | UpdateEscalationPolicyPathDataAttributesAfterDeferralBehavior
        if isinstance(_after_deferral_behavior, Unset):
            after_deferral_behavior = UNSET
        else:
            after_deferral_behavior = check_update_escalation_policy_path_data_attributes_after_deferral_behavior(
                _after_deferral_behavior
            )

        def _parse_after_deferral_path_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        after_deferral_path_id = _parse_after_deferral_path_id(d.pop("after_deferral_path_id", UNSET))

        def _parse_default(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        default = _parse_default(d.pop("default", UNSET))

        _match_mode = d.pop("match_mode", UNSET)
        match_mode: Unset | UpdateEscalationPolicyPathDataAttributesMatchMode
        if isinstance(_match_mode, Unset):
            match_mode = UNSET
        else:
            match_mode = check_update_escalation_policy_path_data_attributes_match_mode(_match_mode)

        position = d.pop("position", UNSET)

        def _parse_repeat(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        repeat = _parse_repeat(d.pop("repeat", UNSET))

        def _parse_repeat_count(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        repeat_count = _parse_repeat_count(d.pop("repeat_count", UNSET))

        initial_delay = d.pop("initial_delay", UNSET)

        def _parse_retrigger_timeout_minutes(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        retrigger_timeout_minutes = _parse_retrigger_timeout_minutes(d.pop("retrigger_timeout_minutes", UNSET))

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:

            def _parse_rules_item(
                data: object,
            ) -> Union[
                "UpdateEscalationPolicyPathDataAttributesRulesItemType0",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType1",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType2",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType3",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType4",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType5",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType6",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType7",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type0",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type1",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type2",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type3",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type4",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type5",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type6",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType8Type7",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type0",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type1",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type2",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type3",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type4",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type5",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type6",
                "UpdateEscalationPolicyPathDataAttributesRulesItemType9Type7",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_0 = UpdateEscalationPolicyPathDataAttributesRulesItemType0.from_dict(data)

                    return rules_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_1 = UpdateEscalationPolicyPathDataAttributesRulesItemType1.from_dict(data)

                    return rules_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_2 = UpdateEscalationPolicyPathDataAttributesRulesItemType2.from_dict(data)

                    return rules_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_3 = UpdateEscalationPolicyPathDataAttributesRulesItemType3.from_dict(data)

                    return rules_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_4 = UpdateEscalationPolicyPathDataAttributesRulesItemType4.from_dict(data)

                    return rules_item_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_5 = UpdateEscalationPolicyPathDataAttributesRulesItemType5.from_dict(data)

                    return rules_item_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_6 = UpdateEscalationPolicyPathDataAttributesRulesItemType6.from_dict(data)

                    return rules_item_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_7 = UpdateEscalationPolicyPathDataAttributesRulesItemType7.from_dict(data)

                    return rules_item_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_0 = UpdateEscalationPolicyPathDataAttributesRulesItemType8Type0.from_dict(
                        data
                    )

                    return rules_item_type_8_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_1 = UpdateEscalationPolicyPathDataAttributesRulesItemType8Type1.from_dict(
                        data
                    )

                    return rules_item_type_8_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_2 = UpdateEscalationPolicyPathDataAttributesRulesItemType8Type2.from_dict(
                        data
                    )

                    return rules_item_type_8_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_3 = UpdateEscalationPolicyPathDataAttributesRulesItemType8Type3.from_dict(
                        data
                    )

                    return rules_item_type_8_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_4 = UpdateEscalationPolicyPathDataAttributesRulesItemType8Type4.from_dict(
                        data
                    )

                    return rules_item_type_8_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_5 = UpdateEscalationPolicyPathDataAttributesRulesItemType8Type5.from_dict(
                        data
                    )

                    return rules_item_type_8_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_6 = UpdateEscalationPolicyPathDataAttributesRulesItemType8Type6.from_dict(
                        data
                    )

                    return rules_item_type_8_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_8_type_7 = UpdateEscalationPolicyPathDataAttributesRulesItemType8Type7.from_dict(
                        data
                    )

                    return rules_item_type_8_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_9_type_0 = UpdateEscalationPolicyPathDataAttributesRulesItemType9Type0.from_dict(
                        data
                    )

                    return rules_item_type_9_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_9_type_1 = UpdateEscalationPolicyPathDataAttributesRulesItemType9Type1.from_dict(
                        data
                    )

                    return rules_item_type_9_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_9_type_2 = UpdateEscalationPolicyPathDataAttributesRulesItemType9Type2.from_dict(
                        data
                    )

                    return rules_item_type_9_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_9_type_3 = UpdateEscalationPolicyPathDataAttributesRulesItemType9Type3.from_dict(
                        data
                    )

                    return rules_item_type_9_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_9_type_4 = UpdateEscalationPolicyPathDataAttributesRulesItemType9Type4.from_dict(
                        data
                    )

                    return rules_item_type_9_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_9_type_5 = UpdateEscalationPolicyPathDataAttributesRulesItemType9Type5.from_dict(
                        data
                    )

                    return rules_item_type_9_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_9_type_6 = UpdateEscalationPolicyPathDataAttributesRulesItemType9Type6.from_dict(
                        data
                    )

                    return rules_item_type_9_type_6
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                rules_item_type_9_type_7 = UpdateEscalationPolicyPathDataAttributesRulesItemType9Type7.from_dict(data)

                return rules_item_type_9_type_7

            rules_item = _parse_rules_item(rules_item_data)

            rules.append(rules_item)

        _time_restriction_time_zone = d.pop("time_restriction_time_zone", UNSET)
        time_restriction_time_zone: Unset | UpdateEscalationPolicyPathDataAttributesTimeRestrictionTimeZone
        if isinstance(_time_restriction_time_zone, Unset):
            time_restriction_time_zone = UNSET
        else:
            time_restriction_time_zone = check_update_escalation_policy_path_data_attributes_time_restriction_time_zone(
                _time_restriction_time_zone
            )

        time_restrictions = []
        _time_restrictions = d.pop("time_restrictions", UNSET)
        for time_restrictions_item_data in _time_restrictions or []:
            time_restrictions_item = UpdateEscalationPolicyPathDataAttributesTimeRestrictionsItem.from_dict(
                time_restrictions_item_data
            )

            time_restrictions.append(time_restrictions_item)

        update_escalation_policy_path_data_attributes = cls(
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
            retrigger_timeout_minutes=retrigger_timeout_minutes,
            rules=rules,
            time_restriction_time_zone=time_restriction_time_zone,
            time_restrictions=time_restrictions,
        )

        return update_escalation_policy_path_data_attributes
