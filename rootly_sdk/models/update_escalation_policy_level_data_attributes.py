from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        delay (int | Unset): Delay before notifying targets in the next Escalation Level.
        position (int | Unset): Position of the escalation policy level
        escalation_policy_path_id (None | str | Unset): The ID of the dynamic escalation policy path the level will
            belong to. If nothing is specified it will add the level to your default path.
        paging_strategy_configuration_strategy
            (UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy | Unset):  Default: 'default'.
        paging_strategy_configuration_schedule_strategy
            (UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy | Unset):  Default:
            'on_call_only'.
        notification_target_params (list[None |
            UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0] | Unset): Escalation level's
            notification targets
    """

    delay: int | Unset = UNSET
    position: int | Unset = UNSET
    escalation_policy_path_id: None | str | Unset = UNSET
    paging_strategy_configuration_strategy: (
        UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy | Unset
    ) = "default"
    paging_strategy_configuration_schedule_strategy: (
        UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy | Unset
    ) = "on_call_only"
    notification_target_params: (
        list[None | UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0] | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_escalation_policy_level_data_attributes_notification_target_params_item_type_0 import (
            UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0,
        )

        delay = self.delay

        position = self.position

        escalation_policy_path_id: None | str | Unset
        if isinstance(self.escalation_policy_path_id, Unset):
            escalation_policy_path_id = UNSET
        else:
            escalation_policy_path_id = self.escalation_policy_path_id

        paging_strategy_configuration_strategy: str | Unset = UNSET
        if not isinstance(self.paging_strategy_configuration_strategy, Unset):
            paging_strategy_configuration_strategy = self.paging_strategy_configuration_strategy

        paging_strategy_configuration_schedule_strategy: str | Unset = UNSET
        if not isinstance(self.paging_strategy_configuration_schedule_strategy, Unset):
            paging_strategy_configuration_schedule_strategy = self.paging_strategy_configuration_schedule_strategy

        notification_target_params: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.notification_target_params, Unset):
            notification_target_params = []
            for notification_target_params_item_data in self.notification_target_params:
                notification_target_params_item: dict[str, Any] | None
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

        def _parse_escalation_policy_path_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        escalation_policy_path_id = _parse_escalation_policy_path_id(d.pop("escalation_policy_path_id", UNSET))

        _paging_strategy_configuration_strategy = d.pop("paging_strategy_configuration_strategy", UNSET)
        paging_strategy_configuration_strategy: (
            UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationStrategy | Unset
        )
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
        paging_strategy_configuration_schedule_strategy: (
            UpdateEscalationPolicyLevelDataAttributesPagingStrategyConfigurationScheduleStrategy | Unset
        )
        if isinstance(_paging_strategy_configuration_schedule_strategy, Unset):
            paging_strategy_configuration_schedule_strategy = UNSET
        else:
            paging_strategy_configuration_schedule_strategy = (
                check_update_escalation_policy_level_data_attributes_paging_strategy_configuration_schedule_strategy(
                    _paging_strategy_configuration_schedule_strategy
                )
            )

        _notification_target_params = d.pop("notification_target_params", UNSET)
        notification_target_params: (
            list[None | UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0] | Unset
        ) = UNSET
        if _notification_target_params is not UNSET:
            notification_target_params = []
            for notification_target_params_item_data in _notification_target_params:

                def _parse_notification_target_params_item(
                    data: object,
                ) -> None | UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        notification_target_params_item_type_0 = (
                            UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0.from_dict(data)
                        )

                        return notification_target_params_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(None | UpdateEscalationPolicyLevelDataAttributesNotificationTargetParamsItemType0, data)

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
