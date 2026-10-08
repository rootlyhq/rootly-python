from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_live_call_router_data_attributes_escalation_policy_trigger_params_type import (
    NewLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType,
    check_new_live_call_router_data_attributes_escalation_policy_trigger_params_type,
)

T = TypeVar("T", bound="NewLiveCallRouterDataAttributesEscalationPolicyTriggerParams")


@_attrs_define
class NewLiveCallRouterDataAttributesEscalationPolicyTriggerParams:
    """
    Attributes:
        id (str): The ID of notification target
        type_ (NewLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType): The type of the notification target.
            Please contact support if you encounter issues using `functionality` as a target type.
    """

    id: str
    type_: NewLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_new_live_call_router_data_attributes_escalation_policy_trigger_params_type(d.pop("type"))

        new_live_call_router_data_attributes_escalation_policy_trigger_params = cls(
            id=id,
            type_=type_,
        )

        return new_live_call_router_data_attributes_escalation_policy_trigger_params
