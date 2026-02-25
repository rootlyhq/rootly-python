from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_alert_routing_rule_data_attributes_destination_target_type import (
    UpdateAlertRoutingRuleDataAttributesDestinationTargetType,
    check_update_alert_routing_rule_data_attributes_destination_target_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlertRoutingRuleDataAttributesDestination")


@_attrs_define
class UpdateAlertRoutingRuleDataAttributesDestination:
    """
    Attributes:
        target_type (Union[Unset, UpdateAlertRoutingRuleDataAttributesDestinationTargetType]): The type of the target
        target_id (Union[Unset, UUID]): The ID of the target
    """

    target_type: Unset | UpdateAlertRoutingRuleDataAttributesDestinationTargetType = UNSET
    target_id: Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_type: Unset | str = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type

        target_id: Unset | str = UNSET
        if not isinstance(self.target_id, Unset):
            target_id = str(self.target_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_type is not UNSET:
            field_dict["target_type"] = target_type
        if target_id is not UNSET:
            field_dict["target_id"] = target_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _target_type = d.pop("target_type", UNSET)
        target_type: Unset | UpdateAlertRoutingRuleDataAttributesDestinationTargetType
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = check_update_alert_routing_rule_data_attributes_destination_target_type(_target_type)

        _target_id = d.pop("target_id", UNSET)
        target_id: Unset | UUID
        if isinstance(_target_id, Unset):
            target_id = UNSET
        else:
            target_id = UUID(_target_id)

        update_alert_routing_rule_data_attributes_destination = cls(
            target_type=target_type,
            target_id=target_id,
        )

        update_alert_routing_rule_data_attributes_destination.additional_properties = d
        return update_alert_routing_rule_data_attributes_destination

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
