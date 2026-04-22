from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_routing_rule_target_type_0_target_type import (
    AlertRoutingRuleTargetType0TargetType,
    check_alert_routing_rule_target_type_0_target_type,
)

T = TypeVar("T", bound="AlertRoutingRuleTargetType0")


@_attrs_define
class AlertRoutingRuleTargetType0:
    """The destination target for the alert routing rule

    Attributes:
        target_type (AlertRoutingRuleTargetType0TargetType): The type of the target. Please contact support if you
            encounter issues using `Functionality` as a target type.
        target_id (UUID): The ID of the target
    """

    target_type: AlertRoutingRuleTargetType0TargetType
    target_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_type: str = self.target_type

        target_id = str(self.target_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_type": target_type,
                "target_id": target_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_type = check_alert_routing_rule_target_type_0_target_type(d.pop("target_type"))

        target_id = UUID(d.pop("target_id"))

        alert_routing_rule_target_type_0 = cls(
            target_type=target_type,
            target_id=target_id,
        )

        alert_routing_rule_target_type_0.additional_properties = d
        return alert_routing_rule_target_type_0

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
