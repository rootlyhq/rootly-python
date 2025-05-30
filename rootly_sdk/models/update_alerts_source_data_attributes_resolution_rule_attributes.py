from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_alerts_source_data_attributes_resolution_rule_attributes_condition_type import (
    UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_alerts_source_data_attributes_resolution_rule_attributes_conditions_attributes_item import (
        UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionsAttributesItem,
    )


T = TypeVar("T", bound="UpdateAlertsSourceDataAttributesResolutionRuleAttributes")


@_attrs_define
class UpdateAlertsSourceDataAttributesResolutionRuleAttributes:
    """Provide additional attributes for email alerts source

    Attributes:
        enabled (Union[Unset, bool]): Set this to true to enable the auto resolution rule
        condition_type (Union[Unset, UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionType]): The type
            of condition to evaluate to apply auto resolution rule
        identifier_json_path (Union[Unset, str]): JSON path expression to extract unique alert identifier used to match
            triggered alerts with resolving alerts
        identifier_value_regex (Union[Unset, str]): Regex group to further specify the part of the string used as a
            unique identifier
        conditions_attributes (Union[Unset,
            list['UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionsAttributesItem']]): List of conditions
            to evaluate for auto resolution
    """

    enabled: Union[Unset, bool] = UNSET
    condition_type: Union[Unset, UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionType] = UNSET
    identifier_json_path: Union[Unset, str] = UNSET
    identifier_value_regex: Union[Unset, str] = UNSET
    conditions_attributes: Union[
        Unset, list["UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionsAttributesItem"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        condition_type: Union[Unset, str] = UNSET
        if not isinstance(self.condition_type, Unset):
            condition_type = self.condition_type.value

        identifier_json_path = self.identifier_json_path

        identifier_value_regex = self.identifier_value_regex

        conditions_attributes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.conditions_attributes, Unset):
            conditions_attributes = []
            for conditions_attributes_item_data in self.conditions_attributes:
                conditions_attributes_item = conditions_attributes_item_data.to_dict()
                conditions_attributes.append(conditions_attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if condition_type is not UNSET:
            field_dict["condition_type"] = condition_type
        if identifier_json_path is not UNSET:
            field_dict["identifier_json_path"] = identifier_json_path
        if identifier_value_regex is not UNSET:
            field_dict["identifier_value_regex"] = identifier_value_regex
        if conditions_attributes is not UNSET:
            field_dict["conditions_attributes"] = conditions_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.update_alerts_source_data_attributes_resolution_rule_attributes_conditions_attributes_item import (
            UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionsAttributesItem,
        )

        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        _condition_type = d.pop("condition_type", UNSET)
        condition_type: Union[Unset, UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionType]
        if isinstance(_condition_type, Unset):
            condition_type = UNSET
        else:
            condition_type = UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionType(_condition_type)

        identifier_json_path = d.pop("identifier_json_path", UNSET)

        identifier_value_regex = d.pop("identifier_value_regex", UNSET)

        conditions_attributes = []
        _conditions_attributes = d.pop("conditions_attributes", UNSET)
        for conditions_attributes_item_data in _conditions_attributes or []:
            conditions_attributes_item = (
                UpdateAlertsSourceDataAttributesResolutionRuleAttributesConditionsAttributesItem.from_dict(
                    conditions_attributes_item_data
                )
            )

            conditions_attributes.append(conditions_attributes_item)

        update_alerts_source_data_attributes_resolution_rule_attributes = cls(
            enabled=enabled,
            condition_type=condition_type,
            identifier_json_path=identifier_json_path,
            identifier_value_regex=identifier_value_regex,
            conditions_attributes=conditions_attributes,
        )

        update_alerts_source_data_attributes_resolution_rule_attributes.additional_properties = d
        return update_alerts_source_data_attributes_resolution_rule_attributes

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
