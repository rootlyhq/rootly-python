from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item import (
        UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem,
    )


T = TypeVar("T", bound="UpdateAlertRouteDataAttributesRulesItemConditionGroupsItem")


@_attrs_define
class UpdateAlertRouteDataAttributesRulesItemConditionGroupsItem:
    """
    Attributes:
        conditions (list[UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem]):
        position (int | Unset): The position of the condition group
    """

    conditions: list[UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem]
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
        from ..models.update_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item import (
            UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem,
        )

        d = dict(src_dict)
        conditions = []
        _conditions = d.pop("conditions")
        for conditions_item_data in _conditions:
            conditions_item = UpdateAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem.from_dict(
                conditions_item_data
            )

            conditions.append(conditions_item)

        position = d.pop("position", UNSET)

        update_alert_route_data_attributes_rules_item_condition_groups_item = cls(
            conditions=conditions,
            position=position,
        )

        return update_alert_route_data_attributes_rules_item_condition_groups_item
