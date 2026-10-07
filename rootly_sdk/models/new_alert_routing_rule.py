from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_alert_routing_rule_data import NewAlertRoutingRuleData


T = TypeVar("T", bound="NewAlertRoutingRule")


@_attrs_define
class NewAlertRoutingRule:
    """
    Attributes:
        data (NewAlertRoutingRuleData):
    """

    data: NewAlertRoutingRuleData

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_alert_routing_rule_data import NewAlertRoutingRuleData

        d = dict(src_dict)
        data = NewAlertRoutingRuleData.from_dict(d.pop("data"))

        new_alert_routing_rule = cls(
            data=data,
        )

        return new_alert_routing_rule
