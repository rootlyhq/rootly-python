from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_sla_data_attributes_conditions_item_conditionable_type import (
    NewSlaDataAttributesConditionsItemConditionableType,
    check_new_sla_data_attributes_conditions_item_conditionable_type,
)
from ..models.new_sla_data_attributes_conditions_item_property import (
    NewSlaDataAttributesConditionsItemProperty,
    check_new_sla_data_attributes_conditions_item_property,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewSlaDataAttributesConditionsItem")


@_attrs_define
class NewSlaDataAttributesConditionsItem:
    """
    Attributes:
        conditionable_type (NewSlaDataAttributesConditionsItemConditionableType): The type of condition
        operator (str): The comparison operator
        property_ (NewSlaDataAttributesConditionsItemProperty | Unset): The property to evaluate (for built-in field
            conditions)
        values (list[str] | None | Unset): The values to compare against
        form_field_id (None | Unset | UUID): The ID of the form field (for custom field conditions)
        position (int | Unset): The position of the condition for ordering
    """

    conditionable_type: NewSlaDataAttributesConditionsItemConditionableType
    operator: str
    property_: NewSlaDataAttributesConditionsItemProperty | Unset = UNSET
    values: list[str] | None | Unset = UNSET
    form_field_id: None | Unset | UUID = UNSET
    position: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conditionable_type: str = self.conditionable_type

        operator = self.operator

        property_: str | Unset = UNSET
        if not isinstance(self.property_, Unset):
            property_ = self.property_

        values: list[str] | None | Unset
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, list):
            values = self.values

        else:
            values = self.values

        form_field_id: None | str | Unset
        if isinstance(self.form_field_id, Unset):
            form_field_id = UNSET
        elif isinstance(self.form_field_id, UUID):
            form_field_id = str(self.form_field_id)
        else:
            form_field_id = self.form_field_id

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conditionable_type": conditionable_type,
                "operator": operator,
            }
        )
        if property_ is not UNSET:
            field_dict["property"] = property_
        if values is not UNSET:
            field_dict["values"] = values
        if form_field_id is not UNSET:
            field_dict["form_field_id"] = form_field_id
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conditionable_type = check_new_sla_data_attributes_conditions_item_conditionable_type(
            d.pop("conditionable_type")
        )

        operator = d.pop("operator")

        _property_ = d.pop("property", UNSET)
        property_: NewSlaDataAttributesConditionsItemProperty | Unset
        if isinstance(_property_, Unset):
            property_ = UNSET
        else:
            property_ = check_new_sla_data_attributes_conditions_item_property(_property_)

        def _parse_values(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = cast(list[str], data)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        values = _parse_values(d.pop("values", UNSET))

        def _parse_form_field_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                form_field_id_type_0 = UUID(data)

                return form_field_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        form_field_id = _parse_form_field_id(d.pop("form_field_id", UNSET))

        position = d.pop("position", UNSET)

        new_sla_data_attributes_conditions_item = cls(
            conditionable_type=conditionable_type,
            operator=operator,
            property_=property_,
            values=values,
            form_field_id=form_field_id,
            position=position,
        )

        new_sla_data_attributes_conditions_item.additional_properties = d
        return new_sla_data_attributes_conditions_item

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
