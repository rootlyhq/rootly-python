from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_conditionable_type import (
    NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemConditionableType,
    check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_conditionable_type,
)
from ..models.new_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_kind import (
    NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemKind,
    check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_kind,
)
from ..models.new_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_operator import (
    NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemOperator,
    check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_operator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItem")


@_attrs_define
class NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItem:
    """
    Attributes:
        field (None | str | Unset): JSON path expression to extract a specific value from the alert's payload for
            evaluation
        operator (NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemOperator | Unset):
            Comparison operator used to evaluate the extracted value against the specified condition
        value (str | Unset): Value that the extracted payload data is compared to using the specified operator to
            determine a match
        conditionable_type
            (NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemConditionableType | Unset):
            The type of the conditionable
        conditionable_id (None | str | Unset): The ID of the conditionable. If conditionable_type is AlertField, this is
            the ID of the alert field.
        kind (NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemKind | Unset): The kind
            of the conditionable
    """

    field: None | str | Unset = UNSET
    operator: NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemOperator | Unset = UNSET
    value: str | Unset = UNSET
    conditionable_type: (
        NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemConditionableType | Unset
    ) = UNSET
    conditionable_id: None | str | Unset = UNSET
    kind: NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemKind | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field: None | str | Unset
        if isinstance(self.field, Unset):
            field = UNSET
        else:
            field = self.field

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator

        value = self.value

        conditionable_type: str | Unset = UNSET
        if not isinstance(self.conditionable_type, Unset):
            conditionable_type = self.conditionable_type

        conditionable_id: None | str | Unset
        if isinstance(self.conditionable_id, Unset):
            conditionable_id = UNSET
        else:
            conditionable_id = self.conditionable_id

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if operator is not UNSET:
            field_dict["operator"] = operator
        if value is not UNSET:
            field_dict["value"] = value
        if conditionable_type is not UNSET:
            field_dict["conditionable_type"] = conditionable_type
        if conditionable_id is not UNSET:
            field_dict["conditionable_id"] = conditionable_id
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field = _parse_field(d.pop("field", UNSET))

        _operator = d.pop("operator", UNSET)
        operator: NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_operator(
                _operator
            )

        value = d.pop("value", UNSET)

        _conditionable_type = d.pop("conditionable_type", UNSET)
        conditionable_type: (
            NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemConditionableType | Unset
        )
        if isinstance(_conditionable_type, Unset):
            conditionable_type = UNSET
        else:
            conditionable_type = check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_conditionable_type(
                _conditionable_type
            )

        def _parse_conditionable_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conditionable_id = _parse_conditionable_id(d.pop("conditionable_id", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_kind(
                _kind
            )

        new_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item = cls(
            field=field,
            operator=operator,
            value=value,
            conditionable_type=conditionable_type,
            conditionable_id=conditionable_id,
            kind=kind,
        )

        new_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item.additional_properties = d
        return new_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item

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
