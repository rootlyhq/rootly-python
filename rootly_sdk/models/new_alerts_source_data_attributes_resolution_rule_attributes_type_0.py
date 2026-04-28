from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_alerts_source_data_attributes_resolution_rule_attributes_type_0_condition_type import (
    NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionType,
    check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_condition_type,
)
from ..models.new_alerts_source_data_attributes_resolution_rule_attributes_type_0_identifier_matchable_type import (
    NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierMatchableType,
    check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_identifier_matchable_type,
)
from ..models.new_alerts_source_data_attributes_resolution_rule_attributes_type_0_identifier_reference_kind import (
    NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierReferenceKind,
    check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_identifier_reference_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item import (
        NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItem,
    )


T = TypeVar("T", bound="NewAlertsSourceDataAttributesResolutionRuleAttributesType0")


@_attrs_define
class NewAlertsSourceDataAttributesResolutionRuleAttributesType0:
    """Provide additional attributes for email alerts source

    Attributes:
        enabled (bool | Unset): Set this to true to enable the auto resolution rule
        condition_type (NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionType | Unset): The type of
            condition to evaluate to apply auto resolution rule
        identifier_matchable_type (NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierMatchableType |
            Unset): The type of the identifier matchable
        identifier_matchable_id (None | str | Unset): The ID of the identifier matchable. If identifier_matchable_type
            is AlertField, this is the ID of the alert field.
        identifier_reference_kind (NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierReferenceKind |
            Unset): The kind of the identifier reference
        identifier_json_path (None | str | Unset): JSON path expression to extract unique alert identifier used to match
            triggered alerts with resolving alerts
        identifier_value_regex (None | str | Unset): Regex group to further specify the part of the string used as a
            unique identifier
        conditions_attributes (list[NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItem]
            | Unset): List of conditions to evaluate for auto resolution
    """

    enabled: bool | Unset = UNSET
    condition_type: NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionType | Unset = UNSET
    identifier_matchable_type: (
        NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierMatchableType | Unset
    ) = UNSET
    identifier_matchable_id: None | str | Unset = UNSET
    identifier_reference_kind: (
        NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierReferenceKind | Unset
    ) = UNSET
    identifier_json_path: None | str | Unset = UNSET
    identifier_value_regex: None | str | Unset = UNSET
    conditions_attributes: (
        list[NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItem] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        condition_type: str | Unset = UNSET
        if not isinstance(self.condition_type, Unset):
            condition_type = self.condition_type

        identifier_matchable_type: str | Unset = UNSET
        if not isinstance(self.identifier_matchable_type, Unset):
            identifier_matchable_type = self.identifier_matchable_type

        identifier_matchable_id: None | str | Unset
        if isinstance(self.identifier_matchable_id, Unset):
            identifier_matchable_id = UNSET
        else:
            identifier_matchable_id = self.identifier_matchable_id

        identifier_reference_kind: str | Unset = UNSET
        if not isinstance(self.identifier_reference_kind, Unset):
            identifier_reference_kind = self.identifier_reference_kind

        identifier_json_path: None | str | Unset
        if isinstance(self.identifier_json_path, Unset):
            identifier_json_path = UNSET
        else:
            identifier_json_path = self.identifier_json_path

        identifier_value_regex: None | str | Unset
        if isinstance(self.identifier_value_regex, Unset):
            identifier_value_regex = UNSET
        else:
            identifier_value_regex = self.identifier_value_regex

        conditions_attributes: list[dict[str, Any]] | Unset = UNSET
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
        if identifier_matchable_type is not UNSET:
            field_dict["identifier_matchable_type"] = identifier_matchable_type
        if identifier_matchable_id is not UNSET:
            field_dict["identifier_matchable_id"] = identifier_matchable_id
        if identifier_reference_kind is not UNSET:
            field_dict["identifier_reference_kind"] = identifier_reference_kind
        if identifier_json_path is not UNSET:
            field_dict["identifier_json_path"] = identifier_json_path
        if identifier_value_regex is not UNSET:
            field_dict["identifier_value_regex"] = identifier_value_regex
        if conditions_attributes is not UNSET:
            field_dict["conditions_attributes"] = conditions_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_alerts_source_data_attributes_resolution_rule_attributes_type_0_conditions_attributes_item import (
            NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItem,
        )

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _condition_type = d.pop("condition_type", UNSET)
        condition_type: NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionType | Unset
        if isinstance(_condition_type, Unset):
            condition_type = UNSET
        else:
            condition_type = check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_condition_type(
                _condition_type
            )

        _identifier_matchable_type = d.pop("identifier_matchable_type", UNSET)
        identifier_matchable_type: (
            NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierMatchableType | Unset
        )
        if isinstance(_identifier_matchable_type, Unset):
            identifier_matchable_type = UNSET
        else:
            identifier_matchable_type = (
                check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_identifier_matchable_type(
                    _identifier_matchable_type
                )
            )

        def _parse_identifier_matchable_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identifier_matchable_id = _parse_identifier_matchable_id(d.pop("identifier_matchable_id", UNSET))

        _identifier_reference_kind = d.pop("identifier_reference_kind", UNSET)
        identifier_reference_kind: (
            NewAlertsSourceDataAttributesResolutionRuleAttributesType0IdentifierReferenceKind | Unset
        )
        if isinstance(_identifier_reference_kind, Unset):
            identifier_reference_kind = UNSET
        else:
            identifier_reference_kind = (
                check_new_alerts_source_data_attributes_resolution_rule_attributes_type_0_identifier_reference_kind(
                    _identifier_reference_kind
                )
            )

        def _parse_identifier_json_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identifier_json_path = _parse_identifier_json_path(d.pop("identifier_json_path", UNSET))

        def _parse_identifier_value_regex(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identifier_value_regex = _parse_identifier_value_regex(d.pop("identifier_value_regex", UNSET))

        _conditions_attributes = d.pop("conditions_attributes", UNSET)
        conditions_attributes: (
            list[NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItem] | Unset
        ) = UNSET
        if _conditions_attributes is not UNSET:
            conditions_attributes = []
            for conditions_attributes_item_data in _conditions_attributes:
                conditions_attributes_item = (
                    NewAlertsSourceDataAttributesResolutionRuleAttributesType0ConditionsAttributesItem.from_dict(
                        conditions_attributes_item_data
                    )
                )

                conditions_attributes.append(conditions_attributes_item)

        new_alerts_source_data_attributes_resolution_rule_attributes_type_0 = cls(
            enabled=enabled,
            condition_type=condition_type,
            identifier_matchable_type=identifier_matchable_type,
            identifier_matchable_id=identifier_matchable_id,
            identifier_reference_kind=identifier_reference_kind,
            identifier_json_path=identifier_json_path,
            identifier_value_regex=identifier_value_regex,
            conditions_attributes=conditions_attributes,
        )

        new_alerts_source_data_attributes_resolution_rule_attributes_type_0.additional_properties = d
        return new_alerts_source_data_attributes_resolution_rule_attributes_type_0

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
