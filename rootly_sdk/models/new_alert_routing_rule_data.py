from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_alert_routing_rule_data_type import (
    NewAlertRoutingRuleDataType,
    check_new_alert_routing_rule_data_type,
)

if TYPE_CHECKING:
    from ..models.new_alert_routing_rule_data_attributes import NewAlertRoutingRuleDataAttributes


T = TypeVar("T", bound="NewAlertRoutingRuleData")


@_attrs_define
class NewAlertRoutingRuleData:
    """
    Attributes:
        type_ (NewAlertRoutingRuleDataType):
        attributes (NewAlertRoutingRuleDataAttributes):
    """

    type_: NewAlertRoutingRuleDataType
    attributes: NewAlertRoutingRuleDataAttributes

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_alert_routing_rule_data_attributes import NewAlertRoutingRuleDataAttributes

        d = dict(src_dict)
        type_ = check_new_alert_routing_rule_data_type(d.pop("type"))

        attributes = NewAlertRoutingRuleDataAttributes.from_dict(d.pop("attributes"))

        new_alert_routing_rule_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return new_alert_routing_rule_data
