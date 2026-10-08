from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_route_rules_item_condition_groups_item_conditions_item_conditionable_type import (
    AlertRouteRulesItemConditionGroupsItemConditionsItemConditionableType,
    check_alert_route_rules_item_condition_groups_item_conditions_item_conditionable_type,
)
from ..models.alert_route_rules_item_condition_groups_item_conditions_item_property_field_condition_type import (
    AlertRouteRulesItemConditionGroupsItemConditionsItemPropertyFieldConditionType,
    check_alert_route_rules_item_condition_groups_item_conditions_item_property_field_condition_type,
)
from ..models.alert_route_rules_item_condition_groups_item_conditions_item_property_field_type import (
    AlertRouteRulesItemConditionGroupsItemConditionsItemPropertyFieldType,
    check_alert_route_rules_item_condition_groups_item_conditions_item_property_field_type,
)

T = TypeVar("T", bound="AlertRouteRulesItemConditionGroupsItemConditionsItem")


@_attrs_define
class AlertRouteRulesItemConditionGroupsItemConditionsItem:
    """
    Attributes:
        property_field_condition_type (AlertRouteRulesItemConditionGroupsItemConditionsItemPropertyFieldConditionType):
        property_field_name (str): The name of the property field
        property_field_type (AlertRouteRulesItemConditionGroupsItemConditionsItemPropertyFieldType):
        property_field_value (None | str): The value of the property field
        property_field_values (list[str] | None):
        alert_urgency_ids (list[str] | None): The Alert Urgency IDs to check in the condition
        conditionable_type (AlertRouteRulesItemConditionGroupsItemConditionsItemConditionableType): The type of the
            conditionable
        conditionable_id (None | UUID): The ID of the conditionable
    """

    property_field_condition_type: AlertRouteRulesItemConditionGroupsItemConditionsItemPropertyFieldConditionType
    property_field_name: str
    property_field_type: AlertRouteRulesItemConditionGroupsItemConditionsItemPropertyFieldType
    property_field_value: None | str
    property_field_values: list[str] | None
    alert_urgency_ids: list[str] | None
    conditionable_type: AlertRouteRulesItemConditionGroupsItemConditionsItemConditionableType
    conditionable_id: None | UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_field_condition_type: str = self.property_field_condition_type

        property_field_name = self.property_field_name

        property_field_type: str = self.property_field_type

        property_field_value: None | str
        property_field_value = self.property_field_value

        property_field_values: list[str] | None
        if isinstance(self.property_field_values, list):
            property_field_values = self.property_field_values

        else:
            property_field_values = self.property_field_values

        alert_urgency_ids: list[str] | None
        if isinstance(self.alert_urgency_ids, list):
            alert_urgency_ids = self.alert_urgency_ids

        else:
            alert_urgency_ids = self.alert_urgency_ids

        conditionable_type: str = self.conditionable_type

        conditionable_id: None | str
        if isinstance(self.conditionable_id, UUID):
            conditionable_id = str(self.conditionable_id)
        else:
            conditionable_id = self.conditionable_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "property_field_condition_type": property_field_condition_type,
                "property_field_name": property_field_name,
                "property_field_type": property_field_type,
                "property_field_value": property_field_value,
                "property_field_values": property_field_values,
                "alert_urgency_ids": alert_urgency_ids,
                "conditionable_type": conditionable_type,
                "conditionable_id": conditionable_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        property_field_condition_type = (
            check_alert_route_rules_item_condition_groups_item_conditions_item_property_field_condition_type(
                d.pop("property_field_condition_type")
            )
        )

        property_field_name = d.pop("property_field_name")

        property_field_type = check_alert_route_rules_item_condition_groups_item_conditions_item_property_field_type(
            d.pop("property_field_type")
        )

        def _parse_property_field_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        property_field_value = _parse_property_field_value(d.pop("property_field_value"))

        def _parse_property_field_values(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                property_field_values_type_0 = cast(list[str], data)

                return property_field_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        property_field_values = _parse_property_field_values(d.pop("property_field_values"))

        def _parse_alert_urgency_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alert_urgency_ids_type_0 = cast(list[str], data)

                return alert_urgency_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        alert_urgency_ids = _parse_alert_urgency_ids(d.pop("alert_urgency_ids"))

        conditionable_type = check_alert_route_rules_item_condition_groups_item_conditions_item_conditionable_type(
            d.pop("conditionable_type")
        )

        def _parse_conditionable_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conditionable_id_type_0 = UUID(data)

                return conditionable_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        conditionable_id = _parse_conditionable_id(d.pop("conditionable_id"))

        alert_route_rules_item_condition_groups_item_conditions_item = cls(
            property_field_condition_type=property_field_condition_type,
            property_field_name=property_field_name,
            property_field_type=property_field_type,
            property_field_value=property_field_value,
            property_field_values=property_field_values,
            alert_urgency_ids=alert_urgency_ids,
            conditionable_type=conditionable_type,
            conditionable_id=conditionable_id,
        )

        alert_route_rules_item_condition_groups_item_conditions_item.additional_properties = d
        return alert_route_rules_item_condition_groups_item_conditions_item

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
