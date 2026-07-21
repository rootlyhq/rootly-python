from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_alert_routing_rule_data_attributes_conditions_item_property_field_condition_type import (
    UpdateAlertRoutingRuleDataAttributesConditionsItemPropertyFieldConditionType,
    check_update_alert_routing_rule_data_attributes_conditions_item_property_field_condition_type,
)
from ..models.update_alert_routing_rule_data_attributes_conditions_item_property_field_type import (
    UpdateAlertRoutingRuleDataAttributesConditionsItemPropertyFieldType,
    check_update_alert_routing_rule_data_attributes_conditions_item_property_field_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlertRoutingRuleDataAttributesConditionsItem")


@_attrs_define
class UpdateAlertRoutingRuleDataAttributesConditionsItem:
    """
    Attributes:
        id (UUID | Unset): The ID of the alert routing rule condition
        property_field_type (UpdateAlertRoutingRuleDataAttributesConditionsItemPropertyFieldType | Unset): The type of
            the property field
        property_field_name (str | Unset): The name of the property field. If the property field type is selected as
            'attribute', then the allowed property field names are 'summary' (for Title), 'description', 'alert_urgency' and
            'external_url' (for Alert Source URL). If the property field type is selected as 'payload', then the property
            field name should be supplied in JSON Path syntax.
        property_field_condition_type (UpdateAlertRoutingRuleDataAttributesConditionsItemPropertyFieldConditionType |
            Unset): The condition type of the property field
        property_field_value (None | str | Unset): The value of the property field. Can be null if the property field
            condition type is 'is_one_of' or 'is_not_one_of'
        property_field_values (list[str] | Unset): The values of the property field. Used if the property field
            condition type is 'is_one_of' or 'is_not_one_of' except for when property field name is 'alert_urgency'
    """

    id: UUID | Unset = UNSET
    property_field_type: UpdateAlertRoutingRuleDataAttributesConditionsItemPropertyFieldType | Unset = UNSET
    property_field_name: str | Unset = UNSET
    property_field_condition_type: (
        UpdateAlertRoutingRuleDataAttributesConditionsItemPropertyFieldConditionType | Unset
    ) = UNSET
    property_field_value: None | str | Unset = UNSET
    property_field_values: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        property_field_type: str | Unset = UNSET
        if not isinstance(self.property_field_type, Unset):
            property_field_type = self.property_field_type

        property_field_name = self.property_field_name

        property_field_condition_type: str | Unset = UNSET
        if not isinstance(self.property_field_condition_type, Unset):
            property_field_condition_type = self.property_field_condition_type

        property_field_value: None | str | Unset
        if isinstance(self.property_field_value, Unset):
            property_field_value = UNSET
        else:
            property_field_value = self.property_field_value

        property_field_values: list[str] | Unset = UNSET
        if not isinstance(self.property_field_values, Unset):
            property_field_values = self.property_field_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if property_field_type is not UNSET:
            field_dict["property_field_type"] = property_field_type
        if property_field_name is not UNSET:
            field_dict["property_field_name"] = property_field_name
        if property_field_condition_type is not UNSET:
            field_dict["property_field_condition_type"] = property_field_condition_type
        if property_field_value is not UNSET:
            field_dict["property_field_value"] = property_field_value
        if property_field_values is not UNSET:
            field_dict["property_field_values"] = property_field_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _property_field_type = d.pop("property_field_type", UNSET)
        property_field_type: UpdateAlertRoutingRuleDataAttributesConditionsItemPropertyFieldType | Unset
        if isinstance(_property_field_type, Unset):
            property_field_type = UNSET
        else:
            property_field_type = check_update_alert_routing_rule_data_attributes_conditions_item_property_field_type(
                _property_field_type
            )

        property_field_name = d.pop("property_field_name", UNSET)

        _property_field_condition_type = d.pop("property_field_condition_type", UNSET)
        property_field_condition_type: (
            UpdateAlertRoutingRuleDataAttributesConditionsItemPropertyFieldConditionType | Unset
        )
        if isinstance(_property_field_condition_type, Unset):
            property_field_condition_type = UNSET
        else:
            property_field_condition_type = (
                check_update_alert_routing_rule_data_attributes_conditions_item_property_field_condition_type(
                    _property_field_condition_type
                )
            )

        def _parse_property_field_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_field_value = _parse_property_field_value(d.pop("property_field_value", UNSET))

        property_field_values = cast(list[str], d.pop("property_field_values", UNSET))

        update_alert_routing_rule_data_attributes_conditions_item = cls(
            id=id,
            property_field_type=property_field_type,
            property_field_name=property_field_name,
            property_field_condition_type=property_field_condition_type,
            property_field_value=property_field_value,
            property_field_values=property_field_values,
        )

        update_alert_routing_rule_data_attributes_conditions_item.additional_properties = d
        return update_alert_routing_rule_data_attributes_conditions_item

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
