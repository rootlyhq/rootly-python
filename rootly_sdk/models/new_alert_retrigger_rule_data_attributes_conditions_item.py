from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_alert_retrigger_rule_data_attributes_conditions_item_kind import (
    NewAlertRetriggerRuleDataAttributesConditionsItemKind,
    check_new_alert_retrigger_rule_data_attributes_conditions_item_kind,
)
from ..models.new_alert_retrigger_rule_data_attributes_conditions_item_operator import (
    NewAlertRetriggerRuleDataAttributesConditionsItemOperator,
    check_new_alert_retrigger_rule_data_attributes_conditions_item_operator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewAlertRetriggerRuleDataAttributesConditionsItem")


@_attrs_define
class NewAlertRetriggerRuleDataAttributesConditionsItem:
    """
    Attributes:
        kind (NewAlertRetriggerRuleDataAttributesConditionsItemKind): The operand the condition matches on. Native
            operands (urgency, source, service, group) match by record; alert_field/payload match a field value.
        operator (NewAlertRetriggerRuleDataAttributesConditionsItemOperator): How the operand is compared. Native
            operands support is_one_of/is_not_one_of/is_set/is_not_set; alert_field/payload additionally support the
            string/regex operators.
        record_ids (Union[Unset, list[UUID]]): For urgency/service/group/source conditions: the IDs of the matched
            records (AlertUrgency, Service, Group, or Alerts::Source).
        values (Union[Unset, list[str]]): For source conditions: non-integration source aliases (e.g. manual, api). For
            alert_field/payload conditions: the values to compare against.
        property_field_name (Union[Unset, str]): For alert_field conditions: the alert field id. For payload conditions:
            a JSON Path (e.g. $.priority).
    """

    kind: NewAlertRetriggerRuleDataAttributesConditionsItemKind
    operator: NewAlertRetriggerRuleDataAttributesConditionsItemOperator
    record_ids: Union[Unset, list[UUID]] = UNSET
    values: Union[Unset, list[str]] = UNSET
    property_field_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        operator: str = self.operator

        record_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.record_ids, Unset):
            record_ids = []
            for record_ids_item_data in self.record_ids:
                record_ids_item = str(record_ids_item_data)
                record_ids.append(record_ids_item)

        values: Union[Unset, list[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        property_field_name = self.property_field_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "operator": operator,
            }
        )
        if record_ids is not UNSET:
            field_dict["record_ids"] = record_ids
        if values is not UNSET:
            field_dict["values"] = values
        if property_field_name is not UNSET:
            field_dict["property_field_name"] = property_field_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = check_new_alert_retrigger_rule_data_attributes_conditions_item_kind(d.pop("kind"))

        operator = check_new_alert_retrigger_rule_data_attributes_conditions_item_operator(d.pop("operator"))

        record_ids = []
        _record_ids = d.pop("record_ids", UNSET)
        for record_ids_item_data in _record_ids or []:
            record_ids_item = UUID(record_ids_item_data)

            record_ids.append(record_ids_item)

        values = cast(list[str], d.pop("values", UNSET))

        property_field_name = d.pop("property_field_name", UNSET)

        new_alert_retrigger_rule_data_attributes_conditions_item = cls(
            kind=kind,
            operator=operator,
            record_ids=record_ids,
            values=values,
            property_field_name=property_field_name,
        )

        new_alert_retrigger_rule_data_attributes_conditions_item.additional_properties = d
        return new_alert_retrigger_rule_data_attributes_conditions_item

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
