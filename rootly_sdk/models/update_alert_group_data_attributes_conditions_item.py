from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_alert_group_data_attributes_conditions_item_conditionable_type import (
    UpdateAlertGroupDataAttributesConditionsItemConditionableType,
    check_update_alert_group_data_attributes_conditions_item_conditionable_type,
)
from ..models.update_alert_group_data_attributes_conditions_item_property_field_condition_type import (
    UpdateAlertGroupDataAttributesConditionsItemPropertyFieldConditionType,
    check_update_alert_group_data_attributes_conditions_item_property_field_condition_type,
)
from ..models.update_alert_group_data_attributes_conditions_item_property_field_type import (
    UpdateAlertGroupDataAttributesConditionsItemPropertyFieldType,
    check_update_alert_group_data_attributes_conditions_item_property_field_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlertGroupDataAttributesConditionsItem")


@_attrs_define
class UpdateAlertGroupDataAttributesConditionsItem:
    """
    Attributes:
        property_field_type (UpdateAlertGroupDataAttributesConditionsItemPropertyFieldType): The type of the property
            field
        property_field_condition_type (UpdateAlertGroupDataAttributesConditionsItemPropertyFieldConditionType): The
            condition type of the property field
        property_field_name (str | Unset): The name of the property field. If the property field type is selected as
            'attribute', then the allowed property field names are 'summary' (for Title), 'description', 'alert_urgency' and
            'external_url' (for Alert Source URL). If the property field type is selected as 'payload', then the property
            field name should be supplied in JSON Path syntax.
        property_field_value (str | Unset): The value of the property field. Can be null if the property field condition
            type is 'is_one_of' or 'is_not_one_of'
        property_field_values (list[str] | Unset): The values of the property field. Need to be passed if the property
            field condition type is 'is_one_of' or 'is_not_one_of' except for when property field name is 'alert_urgency'
        alert_urgency_ids (list[str] | None | Unset): The Alert Urgency IDs to check in the condition. Only need to be
            set when the property field type is 'attribute', the property field name is 'alert_urgency' and the property
            field condition type is 'is_one_of' or 'is_not_one_of'
        conditionable_type (UpdateAlertGroupDataAttributesConditionsItemConditionableType | Unset): The type of the
            conditionable
        conditionable_id (str | Unset): The ID of the conditionable. If conditionable_type is AlertField, this is the ID
            of the alert field.
    """

    property_field_type: UpdateAlertGroupDataAttributesConditionsItemPropertyFieldType
    property_field_condition_type: UpdateAlertGroupDataAttributesConditionsItemPropertyFieldConditionType
    property_field_name: str | Unset = UNSET
    property_field_value: str | Unset = UNSET
    property_field_values: list[str] | Unset = UNSET
    alert_urgency_ids: list[str] | None | Unset = UNSET
    conditionable_type: UpdateAlertGroupDataAttributesConditionsItemConditionableType | Unset = UNSET
    conditionable_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_field_type: str = self.property_field_type

        property_field_condition_type: str = self.property_field_condition_type

        property_field_name = self.property_field_name

        property_field_value = self.property_field_value

        property_field_values: list[str] | Unset = UNSET
        if not isinstance(self.property_field_values, Unset):
            property_field_values = self.property_field_values

        alert_urgency_ids: list[str] | None | Unset
        if isinstance(self.alert_urgency_ids, Unset):
            alert_urgency_ids = UNSET
        elif isinstance(self.alert_urgency_ids, list):
            alert_urgency_ids = self.alert_urgency_ids

        else:
            alert_urgency_ids = self.alert_urgency_ids

        conditionable_type: str | Unset = UNSET
        if not isinstance(self.conditionable_type, Unset):
            conditionable_type = self.conditionable_type

        conditionable_id = self.conditionable_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "property_field_type": property_field_type,
                "property_field_condition_type": property_field_condition_type,
            }
        )
        if property_field_name is not UNSET:
            field_dict["property_field_name"] = property_field_name
        if property_field_value is not UNSET:
            field_dict["property_field_value"] = property_field_value
        if property_field_values is not UNSET:
            field_dict["property_field_values"] = property_field_values
        if alert_urgency_ids is not UNSET:
            field_dict["alert_urgency_ids"] = alert_urgency_ids
        if conditionable_type is not UNSET:
            field_dict["conditionable_type"] = conditionable_type
        if conditionable_id is not UNSET:
            field_dict["conditionable_id"] = conditionable_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        property_field_type = check_update_alert_group_data_attributes_conditions_item_property_field_type(
            d.pop("property_field_type")
        )

        property_field_condition_type = (
            check_update_alert_group_data_attributes_conditions_item_property_field_condition_type(
                d.pop("property_field_condition_type")
            )
        )

        property_field_name = d.pop("property_field_name", UNSET)

        property_field_value = d.pop("property_field_value", UNSET)

        property_field_values = cast(list[str], d.pop("property_field_values", UNSET))

        def _parse_alert_urgency_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alert_urgency_ids_type_0 = cast(list[str], data)

                return alert_urgency_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        alert_urgency_ids = _parse_alert_urgency_ids(d.pop("alert_urgency_ids", UNSET))

        _conditionable_type = d.pop("conditionable_type", UNSET)
        conditionable_type: UpdateAlertGroupDataAttributesConditionsItemConditionableType | Unset
        if isinstance(_conditionable_type, Unset):
            conditionable_type = UNSET
        else:
            conditionable_type = check_update_alert_group_data_attributes_conditions_item_conditionable_type(
                _conditionable_type
            )

        conditionable_id = d.pop("conditionable_id", UNSET)

        update_alert_group_data_attributes_conditions_item = cls(
            property_field_type=property_field_type,
            property_field_condition_type=property_field_condition_type,
            property_field_name=property_field_name,
            property_field_value=property_field_value,
            property_field_values=property_field_values,
            alert_urgency_ids=alert_urgency_ids,
            conditionable_type=conditionable_type,
            conditionable_id=conditionable_id,
        )

        update_alert_group_data_attributes_conditions_item.additional_properties = d
        return update_alert_group_data_attributes_conditions_item

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
