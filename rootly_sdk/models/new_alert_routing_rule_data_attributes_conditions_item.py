from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_alert_routing_rule_data_attributes_conditions_item_property_field_condition_type import (
    NewAlertRoutingRuleDataAttributesConditionsItemPropertyFieldConditionType,
    check_new_alert_routing_rule_data_attributes_conditions_item_property_field_condition_type,
)
from ..models.new_alert_routing_rule_data_attributes_conditions_item_property_field_type import (
    NewAlertRoutingRuleDataAttributesConditionsItemPropertyFieldType,
    check_new_alert_routing_rule_data_attributes_conditions_item_property_field_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewAlertRoutingRuleDataAttributesConditionsItem")


@_attrs_define
class NewAlertRoutingRuleDataAttributesConditionsItem:
    """
    Attributes:
        property_field_type (NewAlertRoutingRuleDataAttributesConditionsItemPropertyFieldType): The type of the property
            field
        property_field_name (str): The name of the property field. If the property field type is selected as
            'attribute', then the allowed property field names are 'summary' (for Title), 'description', 'alert_urgency' and
            'external_url' (for Alert Source URL). If the property field type is selected as 'payload', then the property
            field name should be supplied in JSON Path syntax.
        property_field_condition_type (NewAlertRoutingRuleDataAttributesConditionsItemPropertyFieldConditionType): The
            condition type of the property field
        property_field_value (Union[Unset, str]): The value of the property field. Can be null if the property field
            condition type is 'is_one_of' or 'is_not_one_of'
        property_field_values (Union[Unset, list[str]]): The values of the property field. Need to be passed if the
            property field condition type is 'is_one_of' or 'is_not_one_of' except for when property field name is
            'alert_urgency'
    """

    property_field_type: NewAlertRoutingRuleDataAttributesConditionsItemPropertyFieldType
    property_field_name: str
    property_field_condition_type: NewAlertRoutingRuleDataAttributesConditionsItemPropertyFieldConditionType
    property_field_value: Unset | str = UNSET
    property_field_values: Unset | list[str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_field_type: str = self.property_field_type

        property_field_name = self.property_field_name

        property_field_condition_type: str = self.property_field_condition_type

        property_field_value = self.property_field_value

        property_field_values: Unset | list[str] = UNSET
        if not isinstance(self.property_field_values, Unset):
            property_field_values = self.property_field_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "property_field_type": property_field_type,
                "property_field_name": property_field_name,
                "property_field_condition_type": property_field_condition_type,
            }
        )
        if property_field_value is not UNSET:
            field_dict["property_field_value"] = property_field_value
        if property_field_values is not UNSET:
            field_dict["property_field_values"] = property_field_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        property_field_type = check_new_alert_routing_rule_data_attributes_conditions_item_property_field_type(
            d.pop("property_field_type")
        )

        property_field_name = d.pop("property_field_name")

        property_field_condition_type = (
            check_new_alert_routing_rule_data_attributes_conditions_item_property_field_condition_type(
                d.pop("property_field_condition_type")
            )
        )

        property_field_value = d.pop("property_field_value", UNSET)

        property_field_values = cast(list[str], d.pop("property_field_values", UNSET))

        new_alert_routing_rule_data_attributes_conditions_item = cls(
            property_field_type=property_field_type,
            property_field_name=property_field_name,
            property_field_condition_type=property_field_condition_type,
            property_field_value=property_field_value,
            property_field_values=property_field_values,
        )

        new_alert_routing_rule_data_attributes_conditions_item.additional_properties = d
        return new_alert_routing_rule_data_attributes_conditions_item

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
