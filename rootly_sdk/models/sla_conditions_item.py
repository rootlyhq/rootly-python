from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sla_conditions_item_conditionable_type import (
    SlaConditionsItemConditionableType,
    check_sla_conditions_item_conditionable_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SlaConditionsItem")


@_attrs_define
class SlaConditionsItem:
    """
    Attributes:
        id (UUID | Unset): Unique ID of the condition
        position (int | Unset): The position of the condition
        conditionable_type (SlaConditionsItemConditionableType | Unset): The type of condition
        property_ (None | str | Unset): The property to evaluate (for built-in field conditions)
        operator (str | Unset): The comparison operator
        values (list[str] | None | Unset): The values to compare against
        form_field_id (None | Unset | UUID): The ID of the form field (for custom field conditions)
    """

    id: UUID | Unset = UNSET
    position: int | Unset = UNSET
    conditionable_type: SlaConditionsItemConditionableType | Unset = UNSET
    property_: None | str | Unset = UNSET
    operator: str | Unset = UNSET
    values: list[str] | None | Unset = UNSET
    form_field_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        position = self.position

        conditionable_type: str | Unset = UNSET
        if not isinstance(self.conditionable_type, Unset):
            conditionable_type = self.conditionable_type

        property_: None | str | Unset
        if isinstance(self.property_, Unset):
            property_ = UNSET
        else:
            property_ = self.property_

        operator = self.operator

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if position is not UNSET:
            field_dict["position"] = position
        if conditionable_type is not UNSET:
            field_dict["conditionable_type"] = conditionable_type
        if property_ is not UNSET:
            field_dict["property"] = property_
        if operator is not UNSET:
            field_dict["operator"] = operator
        if values is not UNSET:
            field_dict["values"] = values
        if form_field_id is not UNSET:
            field_dict["form_field_id"] = form_field_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        position = d.pop("position", UNSET)

        _conditionable_type = d.pop("conditionable_type", UNSET)
        conditionable_type: SlaConditionsItemConditionableType | Unset
        if isinstance(_conditionable_type, Unset):
            conditionable_type = UNSET
        else:
            conditionable_type = check_sla_conditions_item_conditionable_type(_conditionable_type)

        def _parse_property_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_ = _parse_property_(d.pop("property", UNSET))

        operator = d.pop("operator", UNSET)

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

        sla_conditions_item = cls(
            id=id,
            position=position,
            conditionable_type=conditionable_type,
            property_=property_,
            operator=operator,
            values=values,
            form_field_id=form_field_id,
        )

        sla_conditions_item.additional_properties = d
        return sla_conditions_item

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
