from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_alert_route_data_attributes_rules_item_condition_groups_item import (
        PatchAlertRouteDataAttributesRulesItemConditionGroupsItem,
    )
    from ..models.patch_alert_route_data_attributes_rules_item_destinations_item import (
        PatchAlertRouteDataAttributesRulesItemDestinationsItem,
    )


T = TypeVar("T", bound="PatchAlertRouteDataAttributesRulesItem")


@_attrs_define
class PatchAlertRouteDataAttributesRulesItem:
    """
    Attributes:
        id (Union[Unset, UUID]): The ID of the alert routing rule. Required for updating or deleting existing rules.
        field_destroy (Union[Unset, bool]): Set to true to delete this rule. When true, only the id field is required.
        name (Union[Unset, str]): The name of the alert routing rule
        position (Union[Unset, int]): The position of the alert routing rule for ordering evaluation
        fallback_rule (Union[Unset, bool]): Whether this is a fallback rule
        destinations (Union[Unset, list['PatchAlertRouteDataAttributesRulesItemDestinationsItem']]):
        condition_groups (Union[Unset, list['PatchAlertRouteDataAttributesRulesItemConditionGroupsItem']]):
    """

    id: Union[Unset, UUID] = UNSET
    field_destroy: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET
    fallback_rule: Union[Unset, bool] = UNSET
    destinations: Union[Unset, list["PatchAlertRouteDataAttributesRulesItemDestinationsItem"]] = UNSET
    condition_groups: Union[Unset, list["PatchAlertRouteDataAttributesRulesItemConditionGroupsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_destroy = self.field_destroy

        name = self.name

        position = self.position

        fallback_rule = self.fallback_rule

        destinations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.destinations, Unset):
            destinations = []
            for destinations_item_data in self.destinations:
                destinations_item = destinations_item_data.to_dict()
                destinations.append(destinations_item)

        condition_groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.condition_groups, Unset):
            condition_groups = []
            for condition_groups_item_data in self.condition_groups:
                condition_groups_item = condition_groups_item_data.to_dict()
                condition_groups.append(condition_groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if name is not UNSET:
            field_dict["name"] = name
        if position is not UNSET:
            field_dict["position"] = position
        if fallback_rule is not UNSET:
            field_dict["fallback_rule"] = fallback_rule
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if condition_groups is not UNSET:
            field_dict["condition_groups"] = condition_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_alert_route_data_attributes_rules_item_condition_groups_item import (
            PatchAlertRouteDataAttributesRulesItemConditionGroupsItem,
        )
        from ..models.patch_alert_route_data_attributes_rules_item_destinations_item import (
            PatchAlertRouteDataAttributesRulesItemDestinationsItem,
        )

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        field_destroy = d.pop("_destroy", UNSET)

        name = d.pop("name", UNSET)

        position = d.pop("position", UNSET)

        fallback_rule = d.pop("fallback_rule", UNSET)

        destinations = []
        _destinations = d.pop("destinations", UNSET)
        for destinations_item_data in _destinations or []:
            destinations_item = PatchAlertRouteDataAttributesRulesItemDestinationsItem.from_dict(destinations_item_data)

            destinations.append(destinations_item)

        condition_groups = []
        _condition_groups = d.pop("condition_groups", UNSET)
        for condition_groups_item_data in _condition_groups or []:
            condition_groups_item = PatchAlertRouteDataAttributesRulesItemConditionGroupsItem.from_dict(
                condition_groups_item_data
            )

            condition_groups.append(condition_groups_item)

        patch_alert_route_data_attributes_rules_item = cls(
            id=id,
            field_destroy=field_destroy,
            name=name,
            position=position,
            fallback_rule=fallback_rule,
            destinations=destinations,
            condition_groups=condition_groups,
        )

        patch_alert_route_data_attributes_rules_item.additional_properties = d
        return patch_alert_route_data_attributes_rules_item

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
