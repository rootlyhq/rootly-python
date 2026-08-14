from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item import (
        PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem,
    )


T = TypeVar("T", bound="PatchAlertRouteDataAttributesRulesItemConditionGroupsItem")


@_attrs_define
class PatchAlertRouteDataAttributesRulesItemConditionGroupsItem:
    """
    Attributes:
        id (Union[Unset, UUID]): The ID of the condition group. Required for updating or deleting existing condition
            groups.
        field_destroy (Union[Unset, bool]): Set to true to delete this condition group
        position (Union[Unset, int]): The position of the condition group
        conditions (Union[Unset, list['PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem']]):
    """

    id: Unset | UUID = UNSET
    field_destroy: Unset | bool = UNSET
    position: Unset | int = UNSET
    conditions: Unset | list["PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_destroy = self.field_destroy

        position = self.position

        conditions: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if position is not UNSET:
            field_dict["position"] = position
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item import (
            PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem,
        )

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Unset | UUID
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        field_destroy = d.pop("_destroy", UNSET)

        position = d.pop("position", UNSET)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem.from_dict(
                conditions_item_data
            )

            conditions.append(conditions_item)

        patch_alert_route_data_attributes_rules_item_condition_groups_item = cls(
            id=id,
            field_destroy=field_destroy,
            position=position,
            conditions=conditions,
        )

        patch_alert_route_data_attributes_rules_item_condition_groups_item.additional_properties = d
        return patch_alert_route_data_attributes_rules_item_condition_groups_item

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
