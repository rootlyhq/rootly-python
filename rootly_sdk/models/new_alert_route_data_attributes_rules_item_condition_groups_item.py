from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item import (
        NewAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem,
    )


T = TypeVar("T", bound="NewAlertRouteDataAttributesRulesItemConditionGroupsItem")


@_attrs_define
class NewAlertRouteDataAttributesRulesItemConditionGroupsItem:
    """
    Attributes:
        conditions (list[NewAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem]):
        position (int | Unset): The position of the condition group
    """

    conditions: list[NewAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem]
    position: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        conditions = []
        for conditions_item_data in self.conditions:
            conditions_item = conditions_item_data.to_dict()
            conditions.append(conditions_item)

        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "conditions": conditions,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item import (
            NewAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem,
        )

        d = dict(src_dict)
        conditions = []
        _conditions = d.pop("conditions")
        for conditions_item_data in _conditions:
            conditions_item = NewAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem.from_dict(
                conditions_item_data
            )

            conditions.append(conditions_item)

        position = d.pop("position", UNSET)

        new_alert_route_data_attributes_rules_item_condition_groups_item = cls(
            conditions=conditions,
            position=position,
        )

        return new_alert_route_data_attributes_rules_item_condition_groups_item
