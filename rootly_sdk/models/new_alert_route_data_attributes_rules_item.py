from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_alert_route_data_attributes_rules_item_condition_groups_item import (
        NewAlertRouteDataAttributesRulesItemConditionGroupsItem,
    )
    from ..models.new_alert_route_data_attributes_rules_item_destinations_item import (
        NewAlertRouteDataAttributesRulesItemDestinationsItem,
    )


T = TypeVar("T", bound="NewAlertRouteDataAttributesRulesItem")


@_attrs_define
class NewAlertRouteDataAttributesRulesItem:
    """
    Attributes:
        name (str): The name of the alert routing rule
        destinations (list[NewAlertRouteDataAttributesRulesItemDestinationsItem]):
        condition_groups (list[NewAlertRouteDataAttributesRulesItemConditionGroupsItem]):
        position (int | Unset): The position of the alert routing rule for ordering evaluation
        fallback_rule (bool | Unset): Whether this is a fallback rule Default: False.
    """

    name: str
    destinations: list[NewAlertRouteDataAttributesRulesItemDestinationsItem]
    condition_groups: list[NewAlertRouteDataAttributesRulesItemConditionGroupsItem]
    position: int | Unset = UNSET
    fallback_rule: bool | Unset = False

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        destinations = []
        for destinations_item_data in self.destinations:
            destinations_item = destinations_item_data.to_dict()
            destinations.append(destinations_item)

        condition_groups = []
        for condition_groups_item_data in self.condition_groups:
            condition_groups_item = condition_groups_item_data.to_dict()
            condition_groups.append(condition_groups_item)

        position = self.position

        fallback_rule = self.fallback_rule

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "destinations": destinations,
                "condition_groups": condition_groups,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position
        if fallback_rule is not UNSET:
            field_dict["fallback_rule"] = fallback_rule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_alert_route_data_attributes_rules_item_condition_groups_item import (
            NewAlertRouteDataAttributesRulesItemConditionGroupsItem,
        )
        from ..models.new_alert_route_data_attributes_rules_item_destinations_item import (
            NewAlertRouteDataAttributesRulesItemDestinationsItem,
        )

        d = dict(src_dict)
        name = d.pop("name")

        destinations = []
        _destinations = d.pop("destinations")
        for destinations_item_data in _destinations:
            destinations_item = NewAlertRouteDataAttributesRulesItemDestinationsItem.from_dict(destinations_item_data)

            destinations.append(destinations_item)

        condition_groups = []
        _condition_groups = d.pop("condition_groups")
        for condition_groups_item_data in _condition_groups:
            condition_groups_item = NewAlertRouteDataAttributesRulesItemConditionGroupsItem.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        position = d.pop("position", UNSET)

        fallback_rule = d.pop("fallback_rule", UNSET)

        new_alert_route_data_attributes_rules_item = cls(
            name=name,
            destinations=destinations,
            condition_groups=condition_groups,
            position=position,
            fallback_rule=fallback_rule,
        )

        return new_alert_route_data_attributes_rules_item
