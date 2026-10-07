from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

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
        target_type (UpdateAlertRoutingRuleDataAttributesDestinationTargetType | Unset): The type of the target. Please
            contact support if you encounter issues using `Functionality` as a target type.
        target_id (UUID | Unset): The ID of the target
    """

    target_type: UpdateAlertRoutingRuleDataAttributesDestinationTargetType | Unset = UNSET
    target_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target_type: str | Unset = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type

        target_id: str | Unset = UNSET
        if not isinstance(self.target_id, Unset):
            target_id = str(self.target_id)

        field_dict: dict[str, Any] = {}

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
        target_type: UpdateAlertRoutingRuleDataAttributesDestinationTargetType | Unset
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = check_update_alert_routing_rule_data_attributes_destination_target_type(_target_type)

        _target_id = d.pop("target_id", UNSET)
        target_id: UUID | Unset
        if isinstance(_target_id, Unset):
            target_id = UNSET
        else:
            target_id = UUID(_target_id)

        update_alert_routing_rule_data_attributes_destination = cls(
            target_type=target_type,
            target_id=target_id,
        )

        return update_alert_routing_rule_data_attributes_destination
