from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_live_call_router_data_attributes_escalation_policy_trigger_params_type import (
    NewLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType,
)

T = TypeVar("T", bound="NewLiveCallRouterDataAttributesEscalationPolicyTriggerParams")


@_attrs_define
class NewLiveCallRouterDataAttributesEscalationPolicyTriggerParams:
    """
    Attributes:
        id (str): The ID of notification target
        type_ (NewLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType): The type of the notification target
    """

    id: str
    type_: NewLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type_ = NewLiveCallRouterDataAttributesEscalationPolicyTriggerParamsType(d.pop("type"))

        new_live_call_router_data_attributes_escalation_policy_trigger_params = cls(
            id=id,
            type_=type_,
        )

        new_live_call_router_data_attributes_escalation_policy_trigger_params.additional_properties = d
        return new_live_call_router_data_attributes_escalation_policy_trigger_params

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
