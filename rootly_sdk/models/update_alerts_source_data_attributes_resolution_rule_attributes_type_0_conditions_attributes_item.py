from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_conditionable_type import (
    UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemConditionableType,
    check_update_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_conditionable_type,
)
from ..models.update_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_kind import (
    UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemKind,
    check_update_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_kind,
)
from ..models.update_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_operator import (
    UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemOperator,
    check_update_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_operator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItem")


@_attrs_define
class UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItem:
    """
    Attributes:
        field (Union[None, Unset, str]): JSON path expression to extract a specific value from the alert's payload for
            evaluation
        operator (Union[Unset,
            UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemOperator]): Comparison
            operator used to evaluate the extracted value against the specified condition
        value (Union[Unset, str]): Value that the extracted payload data is compared to using the specified operator to
            determine a match
        conditionable_type (Union[Unset,
            UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemConditionableType]): The
            type of the conditionable
        conditionable_id (Union[None, Unset, str]): The ID of the conditionable. If conditionable_type is AlertField,
            this is the ID of the alert field.
        kind (Union[Unset, UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemKind]):
            The kind of the conditionable
    """

    field: None | Unset | str = UNSET
    operator: Unset | UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemOperator = (
        UNSET
    )
    value: Unset | str = UNSET
    conditionable_type: (
        Unset | UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemConditionableType
    ) = UNSET
    conditionable_id: None | Unset | str = UNSET
    kind: Unset | UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemKind = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field: None | Unset | str
        if isinstance(self.field, Unset):
            field = UNSET
        else:
            field = self.field

        operator: Unset | str = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator

        value = self.value

        conditionable_type: Unset | str = UNSET
        if not isinstance(self.conditionable_type, Unset):
            conditionable_type = self.conditionable_type

        conditionable_id: None | Unset | str
        if isinstance(self.conditionable_id, Unset):
            conditionable_id = UNSET
        else:
            conditionable_id = self.conditionable_id

        kind: Unset | str = UNSET
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

        def _parse_field(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        field = _parse_field(d.pop("field", UNSET))

        _operator = d.pop("operator", UNSET)
        operator: Unset | UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemOperator
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = check_update_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_operator(
                _operator
            )

        value = d.pop("value", UNSET)

        _conditionable_type = d.pop("conditionable_type", UNSET)
        conditionable_type: (
            Unset
            | UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemConditionableType
        )
        if isinstance(_conditionable_type, Unset):
            conditionable_type = UNSET
        else:
            conditionable_type = check_update_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_conditionable_type(
                _conditionable_type
            )

        def _parse_conditionable_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        conditionable_id = _parse_conditionable_id(d.pop("conditionable_id", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: Unset | UpdateAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItemKind
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_update_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item_kind(
                _kind
            )

        update_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item = cls(
            field=field,
            operator=operator,
            value=value,
            conditionable_type=conditionable_type,
            conditionable_id=conditionable_id,
            kind=kind,
        )

        update_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item.additional_properties = d
        return update_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item

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
