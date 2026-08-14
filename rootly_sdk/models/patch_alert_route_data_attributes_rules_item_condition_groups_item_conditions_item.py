from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_conditionable_type import (
    PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType,
    check_patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_conditionable_type,
)
from ..models.patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_property_field_condition_type import (
    PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldConditionType,
    check_patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_property_field_condition_type,
)
from ..models.patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_property_field_type import (
    PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType,
    check_patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_property_field_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem")


@_attrs_define
class PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItem:
    """
    Attributes:
        id (Union[Unset, UUID]): The ID of the condition. Required for updating or deleting existing conditions.
        field_destroy (Union[Unset, bool]): Set to true to delete this condition
        property_field_condition_type (Union[Unset,
            PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldConditionType]):
        property_field_name (Union[Unset, str]): The name of the property field
        property_field_type (Union[Unset,
            PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType]):
        property_field_value (Union[None, Unset, str]): The value of the property field
        property_field_values (Union[None, Unset, list[str]]):
        alert_urgency_ids (Union[None, Unset, list[str]]): The Alert Urgency IDs to check in the condition
        conditionable_type (Union[Unset,
            PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType]): The type of the
            conditionable
        conditionable_id (Union[None, UUID, Unset]): The ID of the conditionable
    """

    id: Unset | UUID = UNSET
    field_destroy: Unset | bool = UNSET
    property_field_condition_type: (
        Unset | PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldConditionType
    ) = UNSET
    property_field_name: Unset | str = UNSET
    property_field_type: (
        Unset | PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType
    ) = UNSET
    property_field_value: None | Unset | str = UNSET
    property_field_values: None | Unset | list[str] = UNSET
    alert_urgency_ids: None | Unset | list[str] = UNSET
    conditionable_type: (
        Unset | PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType
    ) = UNSET
    conditionable_id: None | UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Unset | str = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        field_destroy = self.field_destroy

        property_field_condition_type: Unset | str = UNSET
        if not isinstance(self.property_field_condition_type, Unset):
            property_field_condition_type = self.property_field_condition_type

        property_field_name = self.property_field_name

        property_field_type: Unset | str = UNSET
        if not isinstance(self.property_field_type, Unset):
            property_field_type = self.property_field_type

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
        elif isinstance(self.conditionable_id, UUID):
            conditionable_id = str(self.conditionable_id)
        else:
            conditionable_id = self.conditionable_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy
        if property_field_condition_type is not UNSET:
            field_dict["property_field_condition_type"] = property_field_condition_type
        if property_field_name is not UNSET:
            field_dict["property_field_name"] = property_field_name
        if property_field_type is not UNSET:
            field_dict["property_field_type"] = property_field_type
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
        _id = d.pop("id", UNSET)
        id: Unset | UUID
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        field_destroy = d.pop("_destroy", UNSET)

        _property_field_condition_type = d.pop("property_field_condition_type", UNSET)
        property_field_condition_type: (
            Unset | PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldConditionType
        )
        if isinstance(_property_field_condition_type, Unset):
            property_field_condition_type = UNSET
        else:
            property_field_condition_type = check_patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_property_field_condition_type(
                _property_field_condition_type
            )

        property_field_name = d.pop("property_field_name", UNSET)

        _property_field_type = d.pop("property_field_type", UNSET)
        property_field_type: (
            Unset | PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemPropertyFieldType
        )
        if isinstance(_property_field_type, Unset):
            property_field_type = UNSET
        else:
            property_field_type = check_patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_property_field_type(
                _property_field_type
            )

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
        conditionable_type: (
            Unset | PatchAlertRouteDataAttributesRulesItemConditionGroupsItemConditionsItemConditionableType
        )
        if isinstance(_conditionable_type, Unset):
            conditionable_type = UNSET
        else:
            conditionable_type = check_patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item_conditionable_type(
                _conditionable_type
            )

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

        patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item = cls(
            id=id,
            field_destroy=field_destroy,
            property_field_condition_type=property_field_condition_type,
            property_field_name=property_field_name,
            property_field_type=property_field_type,
            property_field_value=property_field_value,
            property_field_values=property_field_values,
            alert_urgency_ids=alert_urgency_ids,
            conditionable_type=conditionable_type,
            conditionable_id=conditionable_id,
        )

        patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item.additional_properties = d
        return patch_alert_route_data_attributes_rules_item_condition_groups_item_conditions_item

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
