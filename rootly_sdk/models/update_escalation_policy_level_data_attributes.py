from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.update_escalation_policy_level_data_attributes_paging_strategy_configuration_schedule_strategy import (
    UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy,
    check_update_escalation_policy_level_data_attributes_paging_strategy_configuration_schedule_strategy,
)
from ..models.update_escalation_policy_level_data_attributes_paging_strategy_configuration_strategy import (
    UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy,
    check_update_escalation_policy_level_data_attributes_paging_strategy_configuration_strategy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_escalation_policy_level_data_attributes_notification_target_params_item_type_0 import (
        UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0,
    )


T = TypeVar("T", bound="UpdateEscalationPolicyLevelDataAttributes")


@_attrs_define
class UpdateEscalationPolicyLevelDataAttributes:
    """
    Attributes:
        delay (Union[Unset, int]): Delay before notifying targets in the next Escalation Level.
        position (Union[Unset, int]): Position of the escalation policy level
        escalation_policy_path_id (Union[None, Unset, str]): The ID of the dynamic escalation policy path the level will
            belong to. If nothing is specified it will add the level to your default path.
        paging_strategy_configuration_strategy (Union[Unset,
            UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy]):  Default: 'default'.
        paging_strategy_configuration_schedule_strategy (Union[Unset,
            UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy]):  Default:
            'on_call_only'.
        notification_target_params (Union[Unset,
            list[Union['UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0', None]]]): Escalation
            level's notification targets
    """

    delay: Union[Unset, int] = UNSET
    position: Union[Unset, int] = UNSET
    escalation_policy_path_id: Union[None, Unset, str] = UNSET
    paging_strategy_configuration_strategy: Union[
        Unset, UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy
    ] = "default"
    paging_strategy_configuration_schedule_strategy: Union[
        Unset, UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy
    ] = "on_call_only"
    notification_target_params: Union[
        Unset, list[Union["UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0", None]]
    ] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_escalation_policy_level_data_attributes_notification_target_params_item_type_0 import (
            UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0,
        )

        delay = self.delay

        position = self.position

        escalation_policy_path_id: Union[None, Unset, str]
        if isinstance(self.escalation_policy_path_id, Unset):
            escalation_policy_path_id = UNSET
        else:
            escalation_policy_path_id = self.escalation_policy_path_id

        paging_strategy_configuration_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.paging_strategy_configuration_strategy, Unset):
            paging_strategy_configuration_strategy = self.paging_strategy_configuration_strategy

        paging_strategy_configuration_schedule_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.paging_strategy_configuration_schedule_strategy, Unset):
            paging_strategy_configuration_schedule_strategy = self.paging_strategy_configuration_schedule_strategy

        notification_target_params: Union[Unset, list[Union[None, dict[str, Any]]]] = UNSET
        if not isinstance(self.notification_target_params, Unset):
            notification_target_params = []
            for notification_target_params_item_data in self.notification_target_params:
                notification_target_params_item: Union[None, dict[str, Any]]
                if isinstance(
                    notification_target_params_item_data,
                    UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0,
                ):
                    notification_target_params_item = notification_target_params_item_data.to_dict()
                else:
                    notification_target_params_item = notification_target_params_item_data
                notification_target_params.append(notification_target_params_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if delay is not UNSET:
            field_dict["delay"] = delay
        if position is not UNSET:
            field_dict["position"] = position
        if escalation_policy_path_id is not UNSET:
            field_dict["escalation_policy_path_id"] = escalation_policy_path_id
        if paging_strategy_configuration_strategy is not UNSET:
            field_dict["paging_strategy_configuration_strategy"] = paging_strategy_configuration_strategy
        if paging_strategy_configuration_schedule_strategy is not UNSET:
            field_dict["paging_strategy_configuration_schedule_strategy"] = (
                paging_strategy_configuration_schedule_strategy
            )
        if notification_target_params is not UNSET:
            field_dict["notification_target_params"] = notification_target_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_escalation_policy_level_data_attributes_notification_target_params_item_type_0 import (
            UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0,
        )

        d = dict(src_dict)
        delay = d.pop("delay", UNSET)

        position = d.pop("position", UNSET)

        def _parse_escalation_policy_path_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        escalation_policy_path_id = _parse_escalation_policy_path_id(d.pop("escalation_policy_path_id", UNSET))

        _paging_strategy_configuration_strategy = d.pop("paging_strategy_configuration_strategy", UNSET)
        paging_strategy_configuration_strategy: Union[
            Unset, UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy
        ]
        if isinstance(_paging_strategy_configuration_strategy, Unset):
            paging_strategy_configuration_strategy = UNSET
        else:
            paging_strategy_configuration_strategy = (
                check_update_escalation_policy_level_data_attributes_paging_strategy_configuration_strategy(
                    _paging_strategy_configuration_strategy
                )
            )

        _paging_strategy_configuration_schedule_strategy = d.pop(
            "paging_strategy_configuration_schedule_strategy", UNSET
        )
        paging_strategy_configuration_schedule_strategy: Union[
            Unset, UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy
        ]
        if isinstance(_paging_strategy_configuration_schedule_strategy, Unset):
            paging_strategy_configuration_schedule_strategy = UNSET
        else:
            paging_strategy_configuration_schedule_strategy = (
                check_update_escalation_policy_level_data_attributes_paging_strategy_configuration_schedule_strategy(
                    _paging_strategy_configuration_schedule_strategy
                )
            )

        notification_target_params = []
        _notification_target_params = d.pop("notification_target_params", UNSET)
        for notification_target_params_item_data in _notification_target_params or []:

            def _parse_notification_target_params_item(
                data: object,
            ) -> Union["UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    notification_target_params_item_type_0 = (
                        UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0.from_dict(data)
                    )

                    return notification_target_params_item_type_0
                except:  # noqa: E722
                    pass
                return cast(
                    Union["UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0", None], data
                )

            notification_target_params_item = _parse_notification_target_params_item(
                notification_target_params_item_data
            )

            notification_target_params.append(notification_target_params_item)

        update_escalation_policy_level_data_attributes = cls(
            delay=delay,
            position=position,
            escalation_policy_path_id=escalation_policy_path_id,
            paging_strategy_configuration_strategy=paging_strategy_configuration_strategy,
            paging_strategy_configuration_schedule_strategy=paging_strategy_configuration_schedule_strategy,
            notification_target_params=notification_target_params,
        )

        return update_escalation_policy_level_data_attributes
