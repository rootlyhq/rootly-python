from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.new_escalation_policy_level_data_attributes_paging_strategy_configuration_repeats_mode import (
    NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRepeatsMode,
    check_new_escalation_policy_level_data_attributes_paging_strategy_configuration_repeats_mode,
)
from ..models.new_escalation_policy_level_data_attributes_paging_strategy_configuration_rotation_scope import (
    NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRotationScope,
    check_new_escalation_policy_level_data_attributes_paging_strategy_configuration_rotation_scope,
)
from ..models.new_escalation_policy_level_data_attributes_paging_strategy_configuration_schedule_strategy import (
    NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy,
    check_new_escalation_policy_level_data_attributes_paging_strategy_configuration_schedule_strategy,
)
from ..models.new_escalation_policy_level_data_attributes_paging_strategy_configuration_strategy import (
    NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy,
    check_new_escalation_policy_level_data_attributes_paging_strategy_configuration_strategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_escalation_policy_level_data_attributes_notification_target_params_item_type_0 import (
        NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0,
    )


T = TypeVar("T", bound="NewEscalationPolicyLevelDataAttributes")


@_attrs_define
class NewEscalationPolicyLevelDataAttributes:
    """
    Attributes:
        position (int): Position of the escalation policy level
        notification_target_params
            (list[Union['NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0', None]]): Escalation
            level's notification targets
        delay (Union[Unset, int]): Delay before notifying targets in the next Escalation Level.
        paging_strategy_configuration_strategy (Union[Unset,
            NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy]):  Default: 'default'.
        paging_strategy_configuration_schedule_strategy (Union[Unset,
            NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy]):  Default: 'on_call_only'.
        paging_strategy_configuration_repeats (Union[None, Unset, int]): Number of times to rotate through the roster
            (cycle-based round robin).
        paging_strategy_configuration_repeats_mode (Union[Unset,
            NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRepeatsMode]): Controls how repeats are
            interpreted: 'users' pages exactly N users, 'all' pages everyone once.
        paging_strategy_configuration_rotation_scope (Union[Unset,
            NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRotationScope]): Scope of rotation ordering:
            active rotation members only, or entire schedule.
        paging_strategy_configuration_page_users_count (Union[None, Unset, int]): Number of users to page at a time
            (cycle-based round robin).
        escalation_policy_path_id (Union[None, Unset, str]): The ID of the dynamic escalation policy path the level will
            belong to. If nothing is specified it will add the level to your default path.
    """

    position: int
    notification_target_params: list[
        Union["NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0", None]
    ]
    delay: Unset | int = UNSET
    paging_strategy_configuration_strategy: (
        Unset | NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy
    ) = "default"
    paging_strategy_configuration_schedule_strategy: (
        Unset | NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy
    ) = "on_call_only"
    paging_strategy_configuration_repeats: None | Unset | int = UNSET
    paging_strategy_configuration_repeats_mode: (
        Unset | NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRepeatsMode
    ) = UNSET
    paging_strategy_configuration_rotation_scope: (
        Unset | NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRotationScope
    ) = UNSET
    paging_strategy_configuration_page_users_count: None | Unset | int = UNSET
    escalation_policy_path_id: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_escalation_policy_level_data_attributes_notification_target_params_item_type_0 import (
            NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0,
        )

        position = self.position

        notification_target_params = []
        for notification_target_params_item_data in self.notification_target_params:
            notification_target_params_item: None | dict[str, Any]
            if isinstance(
                notification_target_params_item_data,
                NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0,
            ):
                notification_target_params_item = notification_target_params_item_data.to_dict()
            else:
                notification_target_params_item = notification_target_params_item_data
            notification_target_params.append(notification_target_params_item)

        delay = self.delay

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

        escalation_policy_path_id: None | Unset | str
        if isinstance(self.escalation_policy_path_id, Unset):
            escalation_policy_path_id = UNSET
        else:
            escalation_policy_path_id = self.escalation_policy_path_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "position": position,
                "notification_target_params": notification_target_params,
            }
        )
        if delay is not UNSET:
            field_dict["delay"] = delay
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
        if escalation_policy_path_id is not UNSET:
            field_dict["escalation_policy_path_id"] = escalation_policy_path_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_escalation_policy_level_data_attributes_notification_target_params_item_type_0 import (
            NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0,
        )

        d = dict(src_dict)
        position = d.pop("position")

        notification_target_params = []
        _notification_target_params = d.pop("notification_target_params")
        for notification_target_params_item_data in _notification_target_params:

            def _parse_notification_target_params_item(
                data: object,
            ) -> Union["NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    notification_target_params_item_type_0 = (
                        NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0.from_dict(data)
                    )

                    return notification_target_params_item_type_0
                except:  # noqa: E722
                    pass
                return cast(
                    Union["NewEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0", None], data
                )

            notification_target_params_item = _parse_notification_target_params_item(
                notification_target_params_item_data
            )

            notification_target_params.append(notification_target_params_item)

        delay = d.pop("delay", UNSET)

        _paging_strategy_configuration_strategy = d.pop("paging_strategy_configuration_strategy", UNSET)
        paging_strategy_configuration_strategy: (
            Unset | NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy
        )
        if isinstance(_paging_strategy_configuration_strategy, Unset):
            paging_strategy_configuration_strategy = UNSET
        else:
            paging_strategy_configuration_strategy = (
                check_new_escalation_policy_level_data_attributes_paging_strategy_configuration_strategy(
                    _paging_strategy_configuration_strategy
                )
            )

        _paging_strategy_configuration_schedule_strategy = d.pop(
            "paging_strategy_configuration_schedule_strategy", UNSET
        )
        paging_strategy_configuration_schedule_strategy: (
            Unset | NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy
        )
        if isinstance(_paging_strategy_configuration_schedule_strategy, Unset):
            paging_strategy_configuration_schedule_strategy = UNSET
        else:
            paging_strategy_configuration_schedule_strategy = (
                check_new_escalation_policy_level_data_attributes_paging_strategy_configuration_schedule_strategy(
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
        paging_strategy_configuration_repeats_mode: (
            Unset | NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRepeatsMode
        )
        if isinstance(_paging_strategy_configuration_repeats_mode, Unset):
            paging_strategy_configuration_repeats_mode = UNSET
        else:
            paging_strategy_configuration_repeats_mode = (
                check_new_escalation_policy_level_data_attributes_paging_strategy_configuration_repeats_mode(
                    _paging_strategy_configuration_repeats_mode
                )
            )

        _paging_strategy_configuration_rotation_scope = d.pop("paging_strategy_configuration_rotation_scope", UNSET)
        paging_strategy_configuration_rotation_scope: (
            Unset | NewEscalationPolicyLevelDataAttributesPagingStrategyConfigurationRotationScope
        )
        if isinstance(_paging_strategy_configuration_rotation_scope, Unset):
            paging_strategy_configuration_rotation_scope = UNSET
        else:
            paging_strategy_configuration_rotation_scope = (
                check_new_escalation_policy_level_data_attributes_paging_strategy_configuration_rotation_scope(
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

        def _parse_escalation_policy_path_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        escalation_policy_path_id = _parse_escalation_policy_path_id(d.pop("escalation_policy_path_id", UNSET))

        new_escalation_policy_level_data_attributes = cls(
            position=position,
            notification_target_params=notification_target_params,
            delay=delay,
            paging_strategy_configuration_strategy=paging_strategy_configuration_strategy,
            paging_strategy_configuration_schedule_strategy=paging_strategy_configuration_schedule_strategy,
            paging_strategy_configuration_repeats=paging_strategy_configuration_repeats,
            paging_strategy_configuration_repeats_mode=paging_strategy_configuration_repeats_mode,
            paging_strategy_configuration_rotation_scope=paging_strategy_configuration_rotation_scope,
            paging_strategy_configuration_page_users_count=paging_strategy_configuration_page_users_count,
            escalation_policy_path_id=escalation_policy_path_id,
        )

        return new_escalation_policy_level_data_attributes
