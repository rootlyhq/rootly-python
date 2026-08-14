from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_routing_rule_condition_property_field_condition_type import (
    AlertRoutingRuleConditionPropertyFieldConditionType,
    check_alert_routing_rule_condition_property_field_condition_type,
)
from ..models.alert_routing_rule_condition_property_field_type import (
    AlertRoutingRuleConditionPropertyFieldType,
    check_alert_routing_rule_condition_property_field_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertRoutingRuleCondition")


@_attrs_define
class AlertRoutingRuleCondition:
    """A condition for alert routing rule

    Attributes:
        property_field_type (AlertRoutingRuleConditionPropertyFieldType): The type of the property field
        property_field_name (str): The name of the property field
        property_field_condition_type (AlertRoutingRuleConditionPropertyFieldConditionType): The condition type of the
            property field
        id (Union[Unset, UUID]): Unique ID of the condition
        property_field_value (Union[None, Unset, str]): The value of the property field
        property_field_values (Union[None, Unset, list[str]]): The values of the property field
        conditionable_id (Union[None, UUID, Unset]): The ID of the conditionable object
        conditionable_type (Union[None, Unset, str]): The type of the conditionable object
        created_at (Union[Unset, str]): Date of creation
        updated_at (Union[Unset, str]): Date of last update
    """

    property_field_type: AlertRoutingRuleConditionPropertyFieldType
    property_field_name: str
    property_field_condition_type: AlertRoutingRuleConditionPropertyFieldConditionType
    id: Unset | UUID = UNSET
    property_field_value: None | Unset | str = UNSET
    property_field_values: None | Unset | list[str] = UNSET
    conditionable_id: None | UUID | Unset = UNSET
    conditionable_type: None | Unset | str = UNSET
    created_at: Unset | str = UNSET
    updated_at: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        property_field_type: str = self.property_field_type

        property_field_name = self.property_field_name

        property_field_condition_type: str = self.property_field_condition_type

        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        property_field_value: None | Unset | str
        if isinstance(self.property_field_value, Unset):
            property_field_value = UNSET
        else:
            property_field_value = self.property_field_value

        property_field_values: None | Unset | list[str]
        if isinstance(self.property_field_values, Unset):
            property_field_values = UNSET
        elif isinstance(self.property_field_values, list):
            property_field_values = self.property_field_values

        else:
            property_field_values = self.property_field_values

        conditionable_id: None | Unset | str
        if isinstance(self.conditionable_id, Unset):
            conditionable_id = UNSET
        elif isinstance(self.conditionable_id, UUID):
            conditionable_id = str(self.conditionable_id)
        else:
            conditionable_id = self.conditionable_id

        conditionable_type: None | Unset | str
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
        property_field_type = check_alert_routing_rule_condition_property_field_type(d.pop("property_field_type"))

        property_field_name = d.pop("property_field_name")

        property_field_condition_type = check_alert_routing_rule_condition_property_field_condition_type(
            d.pop("property_field_condition_type")
        )

        _id = d.pop("id", UNSET)
        id: Unset | UUID
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_property_field_value(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        property_field_value = _parse_property_field_value(d.pop("property_field_value", UNSET))

        def _parse_property_field_values(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                property_field_values_type_0 = cast(list[str], data)

                return property_field_values_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        property_field_values = _parse_property_field_values(d.pop("property_field_values", UNSET))

        def _parse_conditionable_id(data: object) -> None | UUID | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conditionable_id_type_0 = UUID(data)

                return conditionable_id_type_0
            except:  # noqa: E722
                pass
            return cast(None | UUID | Unset, data)

        conditionable_id = _parse_conditionable_id(d.pop("conditionable_id", UNSET))

        def _parse_conditionable_type(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        conditionable_type = _parse_conditionable_type(d.pop("conditionable_type", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        alert_routing_rule_condition = cls(
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

        alert_routing_rule_condition.additional_properties = d
        return alert_routing_rule_condition

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
