from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.escalation_policy_level_paging_strategy_configuration_repeats_mode import (
    EscalationPolicyLevelPagingStrategyConfigurationRepeatsMode,
    check_escalation_policy_level_paging_strategy_configuration_repeats_mode,
)
from ..models.escalation_policy_level_paging_strategy_configuration_rotation_scope import (
    EscalationPolicyLevelPagingStrategyConfigurationRotationScope,
    check_escalation_policy_level_paging_strategy_configuration_rotation_scope,
)
from ..models.escalation_policy_level_paging_strategy_configuration_schedule_strategy import (
    EscalationPolicyLevelPagingStrategyConfigurationScheduleStrategy,
    check_escalation_policy_level_paging_strategy_configuration_schedule_strategy,
)
from ..models.escalation_policy_level_paging_strategy_configuration_strategy import (
    EscalationPolicyLevelPagingStrategyConfigurationStrategy,
    check_escalation_policy_level_paging_strategy_configuration_strategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalation_policy_level_notification_target_params_item_type_0 import (
        EscalationPolicyLevelNotificationTargetParamsItemType0,
    )


T = TypeVar("T", bound="EscalationPolicyLevel")


@_attrs_define
class EscalationPolicyLevel:
    """
    Attributes:
        escalation_policy_id (str): The ID of the escalation policy
        delay (int): Delay before notifying targets in the next Escalation Level.
        position (int): Position of the escalation policy level
        notification_target_params (list[Union['EscalationPolicyLevelNotificationTargetParamsItemType0', None]]):
            Escalation level's notification targets
        escalation_policy_path_id (Union[None, Unset, str]): The ID of the dynamic escalation policy path the level will
            belong to. If nothing is specified it will add the level to your default path.
        paging_strategy_configuration_strategy (Union[Unset, EscalationPolicyLevelPagingStrategyConfigurationStrategy]):
            Default: 'default'.
        paging_strategy_configuration_schedule_strategy (Union[Unset,
            EscalationPolicyLevelPagingStrategyConfigurationScheduleStrategy]):  Default: 'on_call_only'.
        paging_strategy_configuration_repeats (Union[None, Unset, int]): Number of times to rotate through the roster
            (cycle-based round robin).
        paging_strategy_configuration_repeats_mode (Union[Unset,
            EscalationPolicyLevelPagingStrategyConfigurationRepeatsMode]): Controls how repeats are interpreted: 'users'
            pages exactly N users, 'all' pages everyone once.
        paging_strategy_configuration_rotation_scope (Union[Unset,
            EscalationPolicyLevelPagingStrategyConfigurationRotationScope]): Scope of rotation ordering: active rotation
            members only, or entire schedule.
        paging_strategy_configuration_page_users_count (Union[None, Unset, int]): Number of users to page at a time
            (cycle-based round robin).
        created_at (Union[Unset, str]): Date of creation
        updated_at (Union[Unset, str]): Date of last update
    """

    escalation_policy_id: str
    delay: int
    position: int
    notification_target_params: list[Union["EscalationPolicyLevelNotificationTargetParamsItemType0", None]]
    escalation_policy_path_id: None | Unset | str = UNSET
    paging_strategy_configuration_strategy: Unset | EscalationPolicyLevelPagingStrategyConfigurationStrategy = "default"
    paging_strategy_configuration_schedule_strategy: (
        Unset | EscalationPolicyLevelPagingStrategyConfigurationScheduleStrategy
    ) = "on_call_only"
    paging_strategy_configuration_repeats: None | Unset | int = UNSET
    paging_strategy_configuration_repeats_mode: Unset | EscalationPolicyLevelPagingStrategyConfigurationRepeatsMode = (
        UNSET
    )
    paging_strategy_configuration_rotation_scope: (
        Unset | EscalationPolicyLevelPagingStrategyConfigurationRotationScope
    ) = UNSET
    paging_strategy_configuration_page_users_count: None | Unset | int = UNSET
    created_at: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.escalation_policy_level_notification_target_params_item_type_0 import (
            EscalationPolicyLevelNotificationTargetParamsItemType0,
        )

        escalation_policy_id = self.escalation_policy_id

        delay = self.delay

        position = self.position

        notification_target_params = []
        for notification_target_params_item_data in self.notification_target_params:
            notification_target_params_item: None | dict[str, Any]
            if isinstance(notification_target_params_item_data, EscalationPolicyLevelNotificationTargetParamsItemType0):
                notification_target_params_item = notification_target_params_item_data.to_dict()
            else:
                notification_target_params_item = notification_target_params_item_data
            notification_target_params.append(notification_target_params_item)

        escalation_policy_path_id: None | Unset | str
        if isinstance(self.escalation_policy_path_id, Unset):
            escalation_policy_path_id = UNSET
        else:
            escalation_policy_path_id = self.escalation_policy_path_id

        paging_strategy_configuration_strategy: Unset | str = UNSET
        if not isinstance(self.paging_strategy_configuration_strategy, Unset):
            paging_strategy_configuration_strategy = self.paging_strategy_configuration_strategy

        paging_strategy_configuration_schedule_strategy: Unset | str = UNSET
        if not isinstance(self.paging_strategy_configuration_schedule_strategy, Unset):
            paging_strategy_configuration_schedule_strategy = self.paging_strategy_configuration_schedule_strategy

        paging_strategy_configuration_repeats: None | Unset | int
        if isinstance(self.paging_strategy_configuration_repeats, Unset):
            paging_strategy_configuration_repeats = UNSET
        else:
            paging_strategy_configuration_repeats = self.paging_strategy_configuration_repeats

        paging_strategy_configuration_repeats_mode: Unset | str = UNSET
        if not isinstance(self.paging_strategy_configuration_repeats_mode, Unset):
            paging_strategy_configuration_repeats_mode = self.paging_strategy_configuration_repeats_mode

        paging_strategy_configuration_rotation_scope: Unset | str = UNSET
        if not isinstance(self.paging_strategy_configuration_rotation_scope, Unset):
            paging_strategy_configuration_rotation_scope = self.paging_strategy_configuration_rotation_scope

        paging_strategy_configuration_page_users_count: None | Unset | int
        if isinstance(self.paging_strategy_configuration_page_users_count, Unset):
            paging_strategy_configuration_page_users_count = UNSET
        else:
            paging_strategy_configuration_page_users_count = self.paging_strategy_configuration_page_users_count

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "escalation_policy_id": escalation_policy_id,
                "delay": delay,
                "position": position,
                "notification_target_params": notification_target_params,
            }
        )
        if escalation_policy_path_id is not UNSET:
            field_dict["escalation_policy_path_id"] = escalation_policy_path_id
        if paging_strategy_configuration_strategy is not UNSET:
            field_dict["paging_strategy_configuration_strategy"] = paging_strategy_configuration_strategy
        if paging_strategy_configuration_schedule_strategy is not UNSET:
            field_dict["paging_strategy_configuration_schedule_strategy"] = (
                paging_strategy_configuration_schedule_strategy
            )
        if paging_strategy_configuration_repeats is not UNSET:
            field_dict["paging_strategy_configuration_repeats"] = paging_strategy_configuration_repeats
        if paging_strategy_configuration_repeats_mode is not UNSET:
            field_dict["paging_strategy_configuration_repeats_mode"] = paging_strategy_configuration_repeats_mode
        if paging_strategy_configuration_rotation_scope is not UNSET:
            field_dict["paging_strategy_configuration_rotation_scope"] = paging_strategy_configuration_rotation_scope
        if paging_strategy_configuration_page_users_count is not UNSET:
            field_dict["paging_strategy_configuration_page_users_count"] = (
                paging_strategy_configuration_page_users_count
            )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.escalation_policy_level_notification_target_params_item_type_0 import (
            EscalationPolicyLevelNotificationTargetParamsItemType0,
        )

        d = dict(src_dict)
        escalation_policy_id = d.pop("escalation_policy_id")

        delay = d.pop("delay")

        position = d.pop("position")

        notification_target_params = []
        _notification_target_params = d.pop("notification_target_params")
        for notification_target_params_item_data in _notification_target_params:

            def _parse_notification_target_params_item(
                data: object,
            ) -> Union["EscalationPolicyLevelNotificationTargetParamsItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    notification_target_params_item_type_0 = (
                        EscalationPolicyLevelNotificationTargetParamsItemType0.from_dict(data)
                    )

                    return notification_target_params_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["EscalationPolicyLevelNotificationTargetParamsItemType0", None], data)

            notification_target_params_item = _parse_notification_target_params_item(
                notification_target_params_item_data
            )

            notification_target_params.append(notification_target_params_item)

        def _parse_escalation_policy_path_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        escalation_policy_path_id = _parse_escalation_policy_path_id(d.pop("escalation_policy_path_id", UNSET))

        _paging_strategy_configuration_strategy = d.pop("paging_strategy_configuration_strategy", UNSET)
        paging_strategy_configuration_strategy: Unset | EscalationPolicyLevelPagingStrategyConfigurationStrategy
        if isinstance(_paging_strategy_configuration_strategy, Unset):
            paging_strategy_configuration_strategy = UNSET
        else:
            paging_strategy_configuration_strategy = (
                check_escalation_policy_level_paging_strategy_configuration_strategy(
                    _paging_strategy_configuration_strategy
                )
            )

        _paging_strategy_configuration_schedule_strategy = d.pop(
            "paging_strategy_configuration_schedule_strategy", UNSET
        )
        paging_strategy_configuration_schedule_strategy: (
            Unset | EscalationPolicyLevelPagingStrategyConfigurationScheduleStrategy
        )
        if isinstance(_paging_strategy_configuration_schedule_strategy, Unset):
            paging_strategy_configuration_schedule_strategy = UNSET
        else:
            paging_strategy_configuration_schedule_strategy = (
                check_escalation_policy_level_paging_strategy_configuration_schedule_strategy(
                    _paging_strategy_configuration_schedule_strategy
                )
            )

        def _parse_paging_strategy_configuration_repeats(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        paging_strategy_configuration_repeats = _parse_paging_strategy_configuration_repeats(
            d.pop("paging_strategy_configuration_repeats", UNSET)
        )

        _paging_strategy_configuration_repeats_mode = d.pop("paging_strategy_configuration_repeats_mode", UNSET)
        paging_strategy_configuration_repeats_mode: Unset | EscalationPolicyLevelPagingStrategyConfigurationRepeatsMode
        if isinstance(_paging_strategy_configuration_repeats_mode, Unset):
            paging_strategy_configuration_repeats_mode = UNSET
        else:
            paging_strategy_configuration_repeats_mode = (
                check_escalation_policy_level_paging_strategy_configuration_repeats_mode(
                    _paging_strategy_configuration_repeats_mode
                )
            )

        _paging_strategy_configuration_rotation_scope = d.pop("paging_strategy_configuration_rotation_scope", UNSET)
        paging_strategy_configuration_rotation_scope: (
            Unset | EscalationPolicyLevelPagingStrategyConfigurationRotationScope
        )
        if isinstance(_paging_strategy_configuration_rotation_scope, Unset):
            paging_strategy_configuration_rotation_scope = UNSET
        else:
            paging_strategy_configuration_rotation_scope = (
                check_escalation_policy_level_paging_strategy_configuration_rotation_scope(
                    _paging_strategy_configuration_rotation_scope
                )
            )

        def _parse_paging_strategy_configuration_page_users_count(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        paging_strategy_configuration_page_users_count = _parse_paging_strategy_configuration_page_users_count(
            d.pop("paging_strategy_configuration_page_users_count", UNSET)
        )

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        escalation_policy_level = cls(
            escalation_policy_id=escalation_policy_id,
            delay=delay,
            position=position,
            notification_target_params=notification_target_params,
            escalation_policy_path_id=escalation_policy_path_id,
            paging_strategy_configuration_strategy=paging_strategy_configuration_strategy,
            paging_strategy_configuration_schedule_strategy=paging_strategy_configuration_schedule_strategy,
            paging_strategy_configuration_repeats=paging_strategy_configuration_repeats,
            paging_strategy_configuration_repeats_mode=paging_strategy_configuration_repeats_mode,
            paging_strategy_configuration_rotation_scope=paging_strategy_configuration_rotation_scope,
            paging_strategy_configuration_page_users_count=paging_strategy_configuration_page_users_count,
            created_at=created_at,
            updated_at=updated_at,
        )

        escalation_policy_level.additional_properties = d
        return escalation_policy_level

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
