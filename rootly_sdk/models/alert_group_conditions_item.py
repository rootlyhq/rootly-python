from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_group_conditions_item_conditionable_type import (
    AlertGroupConditionsItemConditionableType,
    check_alert_group_conditions_item_conditionable_type,
)
from ..models.alert_group_conditions_item_property_field_condition_type import (
    AlertGroupConditionsItemPropertyFieldConditionType,
    check_alert_group_conditions_item_property_field_condition_type,
)
from ..models.alert_group_conditions_item_property_field_type import (
    AlertGroupConditionsItemPropertyFieldType,
    check_alert_group_conditions_item_property_field_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_group_conditions_item_values_item_type_0 import AlertGroupConditionsItemValuesItemType0


T = TypeVar("T", bound="AlertGroupConditionsItem")


@_attrs_define
class AlertGroupConditionsItem:
    """
    Attributes:
        property_field_type (AlertGroupConditionsItemPropertyFieldType): The type of the property field
        property_field_condition_type (AlertGroupConditionsItemPropertyFieldConditionType): The condition type of the
            property field
        property_field_name (Union[None, Unset, str]): The name of the property field. If the property field type is
            selected as 'attribute', then the allowed property field names are 'summary' (for Title), 'description',
            'alert_urgency' and 'external_url' (for Alert Source URL). If the property field type is selected as 'payload',
            then the property field name should be supplied in JSON Path syntax.
        property_field_value (Union[None, Unset, str]): The value of the property field. Can be null if the property
            field condition type is 'is_one_of' or 'is_not_one_of'
        property_field_values (Union[Unset, list[str]]): The values of the property field. Used if the property field
            condition type is 'is_one_of' or 'is_not_one_of' except for when property field name is 'alert_urgency'
        values (Union[Unset, list[Union['AlertGroupConditionsItemValuesItemType0', None]]]):
        alert_urgency_ids (Union[None, Unset, list[str]]): The Alert Urgency IDs to check in the condition. Only need to
            be set when the property field type is 'attribute', the property field name is 'alert_urgency' and the property
            field condition type is 'is_one_of' or 'is_not_one_of'
        conditionable_type (Union[Unset, AlertGroupConditionsItemConditionableType]): The type of the conditionable
        conditionable_id (Union[None, Unset, str]): The ID of the conditionable. If conditionable_type is AlertField,
            this is the ID of the alert field.
    """

    property_field_type: AlertGroupConditionsItemPropertyFieldType
    property_field_condition_type: AlertGroupConditionsItemPropertyFieldConditionType
    property_field_name: None | Unset | str = UNSET
    property_field_value: None | Unset | str = UNSET
    property_field_values: Unset | list[str] = UNSET
    values: Unset | list[Union["AlertGroupConditionsItemValuesItemType0", None]] = UNSET
    alert_urgency_ids: None | Unset | list[str] = UNSET
    conditionable_type: Unset | AlertGroupConditionsItemConditionableType = UNSET
    conditionable_id: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alert_group_conditions_item_values_item_type_0 import AlertGroupConditionsItemValuesItemType0

        property_field_type: str = self.property_field_type

        property_field_condition_type: str = self.property_field_condition_type

        property_field_name: None | Unset | str
        if isinstance(self.property_field_name, Unset):
            property_field_name = UNSET
        else:
            property_field_name = self.property_field_name

        property_field_value: None | Unset | str
        if isinstance(self.property_field_value, Unset):
            property_field_value = UNSET
        else:
            property_field_value = self.property_field_value

        property_field_values: Unset | list[str] = UNSET
        if not isinstance(self.property_field_values, Unset):
            property_field_values = self.property_field_values

        values: Unset | list[None | dict[str, Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item: None | dict[str, Any]
                if isinstance(values_item_data, AlertGroupConditionsItemValuesItemType0):
                    values_item = values_item_data.to_dict()
                else:
                    values_item = values_item_data
                values.append(values_item)

        alert_urgency_ids: None | Unset | list[str]
        if isinstance(self.alert_urgency_ids, Unset):
            alert_urgency_ids = UNSET
        elif isinstance(self.alert_urgency_ids, list):
            alert_urgency_ids = self.alert_urgency_ids

        else:
            alert_urgency_ids = self.alert_urgency_ids

        conditionable_type: Unset | str = UNSET
        if not isinstance(self.conditionable_type, Unset):
            conditionable_type = self.conditionable_type

        conditionable_id: None | Unset | str
        if isinstance(self.conditionable_id, Unset):
            conditionable_id = UNSET
        else:
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
        if values is not UNSET:
            field_dict["values"] = values
        if alert_urgency_ids is not UNSET:
            field_dict["alert_urgency_ids"] = alert_urgency_ids
        if conditionable_type is not UNSET:
            field_dict["conditionable_type"] = conditionable_type
        if conditionable_id is not UNSET:
            field_dict["conditionable_id"] = conditionable_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_group_conditions_item_values_item_type_0 import AlertGroupConditionsItemValuesItemType0

        d = dict(src_dict)
        property_field_type = check_alert_group_conditions_item_property_field_type(d.pop("property_field_type"))

        property_field_condition_type = check_alert_group_conditions_item_property_field_condition_type(
            d.pop("property_field_condition_type")
        )

        def _parse_property_field_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        property_field_name = _parse_property_field_name(d.pop("property_field_name", UNSET))

        def _parse_property_field_value(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        property_field_value = _parse_property_field_value(d.pop("property_field_value", UNSET))

        property_field_values = cast(list[str], d.pop("property_field_values", UNSET))

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:

            def _parse_values_item(data: object) -> Union["AlertGroupConditionsItemValuesItemType0", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    values_item_type_0 = AlertGroupConditionsItemValuesItemType0.from_dict(data)

                    return values_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["AlertGroupConditionsItemValuesItemType0", None], data)

            values_item = _parse_values_item(values_item_data)

            values.append(values_item)

        def _parse_alert_urgency_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alert_urgency_ids_type_0 = cast(list[str], data)

                return alert_urgency_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        alert_urgency_ids = _parse_alert_urgency_ids(d.pop("alert_urgency_ids", UNSET))

        _conditionable_type = d.pop("conditionable_type", UNSET)
        conditionable_type: Unset | AlertGroupConditionsItemConditionableType
        if isinstance(_conditionable_type, Unset):
            conditionable_type = UNSET
        else:
            conditionable_type = check_alert_group_conditions_item_conditionable_type(_conditionable_type)

        def _parse_conditionable_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        conditionable_id = _parse_conditionable_id(d.pop("conditionable_id", UNSET))

        alert_group_conditions_item = cls(
            property_field_type=property_field_type,
            property_field_condition_type=property_field_condition_type,
            property_field_name=property_field_name,
            property_field_value=property_field_value,
            property_field_values=property_field_values,
            values=values,
            alert_urgency_ids=alert_urgency_ids,
            conditionable_type=conditionable_type,
            conditionable_id=conditionable_id,
        )

        alert_group_conditions_item.additional_properties = d
        return alert_group_conditions_item

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
