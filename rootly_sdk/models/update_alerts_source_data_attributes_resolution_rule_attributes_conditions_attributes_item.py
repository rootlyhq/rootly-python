from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_alerts_source_data_attributes_resolution_rule_attributes_conditions_attributes_item_operator import (
    UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionsAttributesItemOperator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionsAttributesItem")


@_attrs_define
class UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionsAttributesItem:
    """
    Attributes:
        field (Union[Unset, str]): JSON path expression to extract a specific value from the alert's payload for
            evaluation
        operator (Union[Unset,
            UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionsAttributesItemOperator]): Comparison operator
            used to evaluate the extracted value against the specified condition
        value (Union[Unset, str]): Value that the extracted payload data is compared to using the specified operator to
            determine a match
    """

    field: Union[Unset, str] = UNSET
    operator: Union[Unset, UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionsAttributesItemOperator] = (
        UNSET
    )
    value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        operator: Union[Unset, str] = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if operator is not UNSET:
            field_dict["operator"] = operator
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        field = d.pop("field", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: Union[Unset, UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionsAttributesItemOperator]
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionsAttributesItemOperator(
                _operator
            )

        value = d.pop("value", UNSET)

        update_alerts_source_data_attributes_resolution_rule_attributes_conditions_attributes_item = cls(
            field=field,
            operator=operator,
            value=value,
        )

        update_alerts_source_data_attributes_resolution_rule_attributes_conditions_attributes_item.additional_properties = d
        return update_alerts_source_data_attributes_resolution_rule_attributes_conditions_attributes_item

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
