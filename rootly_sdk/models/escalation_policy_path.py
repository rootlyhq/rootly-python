from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_policy_path_match_mode import (
    EscalationPolicyPathMatchMode,
    check_escalation_policy_path_match_mode,
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
    from ..models.escalation_policy_path_rules_item_type_4_type_0 import EscalationPolicyPathRulesItemType4Type0
    from ..models.escalation_policy_path_rules_item_type_4_type_1 import EscalationPolicyPathRulesItemType4Type1
    from ..models.escalation_policy_path_rules_item_type_4_type_2 import EscalationPolicyPathRulesItemType4Type2
    from ..models.escalation_policy_path_rules_item_type_4_type_3 import EscalationPolicyPathRulesItemType4Type3
    from ..models.escalation_policy_path_rules_item_type_5_type_0 import EscalationPolicyPathRulesItemType5Type0
    from ..models.escalation_policy_path_rules_item_type_5_type_1 import EscalationPolicyPathRulesItemType5Type1
    from ..models.escalation_policy_path_rules_item_type_5_type_2 import EscalationPolicyPathRulesItemType5Type2
    from ..models.escalation_policy_path_rules_item_type_5_type_3 import EscalationPolicyPathRulesItemType5Type3
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
        match_mode (Union[Unset, EscalationPolicyPathMatchMode]): How path rules are matched.
        position (Union[Unset, int]): The position of this path in the paths for this EP.
        initial_delay (Union[Unset, int]): Initial delay for escalation path in minutes. Maximum 1 week (10080).
        created_at (Union[Unset, str]): Date of creation
        updated_at (Union[Unset, str]): Date of last update
        rules (Union[Unset, list[Union['EscalationPolicyPathRulesItemType0', 'EscalationPolicyPathRulesItemType1',
            'EscalationPolicyPathRulesItemType2', 'EscalationPolicyPathRulesItemType3',
            'EscalationPolicyPathRulesItemType4Type0', 'EscalationPolicyPathRulesItemType4Type1',
            'EscalationPolicyPathRulesItemType4Type2', 'EscalationPolicyPathRulesItemType4Type3',
            'EscalationPolicyPathRulesItemType5Type0', 'EscalationPolicyPathRulesItemType5Type1',
            'EscalationPolicyPathRulesItemType5Type2', 'EscalationPolicyPathRulesItemType5Type3']]]): Escalation path rules
        time_restriction_time_zone (Union[Unset, EscalationPolicyPathTimeRestrictionTimeZone]): Time zone used for time
            restrictions.
        time_restrictions (Union[Unset, list['EscalationPolicyPathTimeRestrictionsItem']]): If time restrictions are
            set, alerts will follow this path when they arrive within the specified time ranges and meet the rules.
    """

    name: str
    default: bool
    notification_type: str
    escalation_policy_id: str
    repeat: Union[None, bool]
    repeat_count: Union[None, int]
    match_mode: Union[Unset, EscalationPolicyPathMatchMode] = UNSET
    position: Union[Unset, int] = UNSET
    initial_delay: Union[Unset, int] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    rules: Union[
        Unset,
        list[
            Union[
                "EscalationPolicyPathRulesItemType0",
                "EscalationPolicyPathRulesItemType1",
                "EscalationPolicyPathRulesItemType2",
                "EscalationPolicyPathRulesItemType3",
                "EscalationPolicyPathRulesItemType4Type0",
                "EscalationPolicyPathRulesItemType4Type1",
                "EscalationPolicyPathRulesItemType4Type2",
                "EscalationPolicyPathRulesItemType4Type3",
                "EscalationPolicyPathRulesItemType5Type0",
                "EscalationPolicyPathRulesItemType5Type1",
                "EscalationPolicyPathRulesItemType5Type2",
                "EscalationPolicyPathRulesItemType5Type3",
            ]
        ],
    ] = UNSET
    time_restriction_time_zone: Union[Unset, EscalationPolicyPathTimeRestrictionTimeZone] = UNSET
    time_restrictions: Union[Unset, list["EscalationPolicyPathTimeRestrictionsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.escalation_policy_path_rules_item_type_0 import EscalationPolicyPathRulesItemType0
        from ..models.escalation_policy_path_rules_item_type_1 import EscalationPolicyPathRulesItemType1
        from ..models.escalation_policy_path_rules_item_type_2 import EscalationPolicyPathRulesItemType2
        from ..models.escalation_policy_path_rules_item_type_3 import EscalationPolicyPathRulesItemType3
        from ..models.escalation_policy_path_rules_item_type_4_type_0 import EscalationPolicyPathRulesItemType4Type0
        from ..models.escalation_policy_path_rules_item_type_4_type_1 import EscalationPolicyPathRulesItemType4Type1
        from ..models.escalation_policy_path_rules_item_type_4_type_2 import EscalationPolicyPathRulesItemType4Type2
        from ..models.escalation_policy_path_rules_item_type_4_type_3 import EscalationPolicyPathRulesItemType4Type3
        from ..models.escalation_policy_path_rules_item_type_5_type_0 import EscalationPolicyPathRulesItemType5Type0
        from ..models.escalation_policy_path_rules_item_type_5_type_1 import EscalationPolicyPathRulesItemType5Type1
        from ..models.escalation_policy_path_rules_item_type_5_type_2 import EscalationPolicyPathRulesItemType5Type2

        name = self.name

        default = self.default

        notification_type = self.notification_type

        escalation_policy_id = self.escalation_policy_id

        repeat: Union[None, bool]
        repeat = self.repeat

        repeat_count: Union[None, int]
        repeat_count = self.repeat_count

        match_mode: Union[Unset, str] = UNSET
        if not isinstance(self.match_mode, Unset):
            match_mode = self.match_mode

        position = self.position

        initial_delay = self.initial_delay

        created_at = self.created_at

        updated_at = self.updated_at

        rules: Union[Unset, list[dict[str, Any]]] = UNSET
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
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType4Type0):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType4Type1):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType4Type2):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType4Type3):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType5Type0):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType5Type1):
                    rules_item = rules_item_data.to_dict()
                elif isinstance(rules_item_data, EscalationPolicyPathRulesItemType5Type2):
                    rules_item = rules_item_data.to_dict()
                else:
                    rules_item = rules_item_data.to_dict()

                rules.append(rules_item)

        time_restriction_time_zone: Union[Unset, str] = UNSET
        if not isinstance(self.time_restriction_time_zone, Unset):
            time_restriction_time_zone = self.time_restriction_time_zone

        time_restrictions: Union[Unset, list[dict[str, Any]]] = UNSET
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
        from ..models.escalation_policy_path_rules_item_type_4_type_0 import EscalationPolicyPathRulesItemType4Type0
        from ..models.escalation_policy_path_rules_item_type_4_type_1 import EscalationPolicyPathRulesItemType4Type1
        from ..models.escalation_policy_path_rules_item_type_4_type_2 import EscalationPolicyPathRulesItemType4Type2
        from ..models.escalation_policy_path_rules_item_type_4_type_3 import EscalationPolicyPathRulesItemType4Type3
        from ..models.escalation_policy_path_rules_item_type_5_type_0 import EscalationPolicyPathRulesItemType5Type0
        from ..models.escalation_policy_path_rules_item_type_5_type_1 import EscalationPolicyPathRulesItemType5Type1
        from ..models.escalation_policy_path_rules_item_type_5_type_2 import EscalationPolicyPathRulesItemType5Type2
        from ..models.escalation_policy_path_rules_item_type_5_type_3 import EscalationPolicyPathRulesItemType5Type3
        from ..models.escalation_policy_path_time_restrictions_item import EscalationPolicyPathTimeRestrictionsItem

        d = dict(src_dict)
        name = d.pop("name")

        default = d.pop("default")

        notification_type = d.pop("notification_type")

        escalation_policy_id = d.pop("escalation_policy_id")

        def _parse_repeat(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        repeat = _parse_repeat(d.pop("repeat"))

        def _parse_repeat_count(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        repeat_count = _parse_repeat_count(d.pop("repeat_count"))

        _match_mode = d.pop("match_mode", UNSET)
        match_mode: Union[Unset, EscalationPolicyPathMatchMode]
        if isinstance(_match_mode, Unset):
            match_mode = UNSET
        else:
            match_mode = check_escalation_policy_path_match_mode(_match_mode)

        position = d.pop("position", UNSET)

        initial_delay = d.pop("initial_delay", UNSET)

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
                "EscalationPolicyPathRulesItemType4Type0",
                "EscalationPolicyPathRulesItemType4Type1",
                "EscalationPolicyPathRulesItemType4Type2",
                "EscalationPolicyPathRulesItemType4Type3",
                "EscalationPolicyPathRulesItemType5Type0",
                "EscalationPolicyPathRulesItemType5Type1",
                "EscalationPolicyPathRulesItemType5Type2",
                "EscalationPolicyPathRulesItemType5Type3",
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
                    rules_item_type_4_type_0 = EscalationPolicyPathRulesItemType4Type0.from_dict(data)

                    return rules_item_type_4_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_4_type_1 = EscalationPolicyPathRulesItemType4Type1.from_dict(data)

                    return rules_item_type_4_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_4_type_2 = EscalationPolicyPathRulesItemType4Type2.from_dict(data)

                    return rules_item_type_4_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_4_type_3 = EscalationPolicyPathRulesItemType4Type3.from_dict(data)

                    return rules_item_type_4_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_5_type_0 = EscalationPolicyPathRulesItemType5Type0.from_dict(data)

                    return rules_item_type_5_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_5_type_1 = EscalationPolicyPathRulesItemType5Type1.from_dict(data)

                    return rules_item_type_5_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    rules_item_type_5_type_2 = EscalationPolicyPathRulesItemType5Type2.from_dict(data)

                    return rules_item_type_5_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                rules_item_type_5_type_3 = EscalationPolicyPathRulesItemType5Type3.from_dict(data)

                return rules_item_type_5_type_3

            rules_item = _parse_rules_item(rules_item_data)

            rules.append(rules_item)

        _time_restriction_time_zone = d.pop("time_restriction_time_zone", UNSET)
        time_restriction_time_zone: Union[Unset, EscalationPolicyPathTimeRestrictionTimeZone]
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
