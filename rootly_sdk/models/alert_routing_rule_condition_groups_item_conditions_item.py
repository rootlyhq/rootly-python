from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_routing_rule_condition_groups_item_conditions_item_property_field_condition_type import (
    AlertRoutingRuleConditionGroupsItemConditionsItemPropertyFieldConditionType,
    check_alert_routing_rule_condition_groups_item_conditions_item_property_field_condition_type,
)
from ..models.alert_routing_rule_condition_groups_item_conditions_item_property_field_type import (
    AlertRoutingRuleConditionGroupsItemConditionsItemPropertyFieldType,
    check_alert_routing_rule_condition_groups_item_conditions_item_property_field_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertRoutingRuleConditionGroupsItemConditionsItem")


@_attrs_define
class AlertRoutingRuleConditionGroupsItemConditionsItem:
    """
    Attributes:
        property_field_type (AlertRoutingRuleConditionGroupsItemConditionsItemPropertyFieldType): The type of the
            property field
        property_field_name (str): The name of the property field
        property_field_condition_type (AlertRoutingRuleConditionGroupsItemConditionsItemPropertyFieldConditionType): The
            condition type of the property field
        id (UUID | Unset): Unique ID of the condition
        property_field_value (None | str | Unset): The value of the property field
        property_field_values (list[str] | None | Unset): The values of the property field
        conditionable_id (None | Unset | UUID): The ID of the conditionable object
        conditionable_type (None | str | Unset): The type of the conditionable object
        created_at (str | Unset): Date of creation
        updated_at (str | Unset): Date of last update
    """

    property_field_type: AlertRoutingRuleConditionGroupsItemConditionsItemPropertyFieldType
    property_field_name: str
    property_field_condition_type: AlertRoutingRuleConditionGroupsItemConditionsItemPropertyFieldConditionType
    id: UUID | Unset = UNSET
    property_field_value: None | str | Unset = UNSET
    property_field_values: list[str] | None | Unset = UNSET
    conditionable_id: None | Unset | UUID = UNSET
    conditionable_type: None | str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_field_type: str = self.property_field_type

        property_field_name = self.property_field_name

        property_field_condition_type: str = self.property_field_condition_type

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        property_field_value: None | str | Unset
        if isinstance(self.property_field_value, Unset):
            property_field_value = UNSET
        else:
            property_field_value = self.property_field_value

        property_field_values: list[str] | None | Unset
        if isinstance(self.property_field_values, Unset):
            property_field_values = UNSET
        elif isinstance(self.property_field_values, list):
            property_field_values = self.property_field_values

        else:
            property_field_values = self.property_field_values

        conditionable_id: None | str | Unset
        if isinstance(self.conditionable_id, Unset):
            conditionable_id = UNSET
        elif isinstance(self.conditionable_id, UUID):
            conditionable_id = str(self.conditionable_id)
        else:
            conditionable_id = self.conditionable_id

        conditionable_type: None | str | Unset
        if isinstance(self.conditionable_type, Unset):
            conditionable_type = UNSET
        else:
            conditionable_type = self.conditionable_type

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "property_field_type": property_field_type,
                "property_field_name": property_field_name,
                "property_field_condition_type": property_field_condition_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if property_field_value is not UNSET:
            field_dict["property_field_value"] = property_field_value
        if property_field_values is not UNSET:
            field_dict["property_field_values"] = property_field_values
        if conditionable_id is not UNSET:
            field_dict["conditionable_id"] = conditionable_id
        if conditionable_type is not UNSET:
            field_dict["conditionable_type"] = conditionable_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        property_field_type = check_alert_routing_rule_condition_groups_item_conditions_item_property_field_type(
            d.pop("property_field_type")
        )

        property_field_name = d.pop("property_field_name")

        property_field_condition_type = (
            check_alert_routing_rule_condition_groups_item_conditions_item_property_field_condition_type(
                d.pop("property_field_condition_type")
            )
        )

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_property_field_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_field_value = _parse_property_field_value(d.pop("property_field_value", UNSET))

        def _parse_property_field_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                property_field_values_type_0 = cast(list[str], data)

                return property_field_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        property_field_values = _parse_property_field_values(d.pop("property_field_values", UNSET))

        def _parse_conditionable_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conditionable_id_type_0 = UUID(data)

                return conditionable_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        conditionable_id = _parse_conditionable_id(d.pop("conditionable_id", UNSET))

        def _parse_conditionable_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conditionable_type = _parse_conditionable_type(d.pop("conditionable_type", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        alert_routing_rule_condition_groups_item_conditions_item = cls(
            property_field_type=property_field_type,
            property_field_name=property_field_name,
            property_field_condition_type=property_field_condition_type,
            id=id,
            property_field_value=property_field_value,
            property_field_values=property_field_values,
            conditionable_id=conditionable_id,
            conditionable_type=conditionable_type,
            created_at=created_at,
            updated_at=updated_at,
        )

        alert_routing_rule_condition_groups_item_conditions_item.additional_properties = d
        return alert_routing_rule_condition_groups_item_conditions_item

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
