from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_form_field_placement_condition_data_attributes_comparison import (
    NewFormFieldPlacementConditionDataAttributesComparison,
    check_new_form_field_placement_condition_data_attributes_comparison,
)
from ..models.new_form_field_placement_condition_data_attributes_conditioned import (
    NewFormFieldPlacementConditionDataAttributesConditioned,
    check_new_form_field_placement_condition_data_attributes_conditioned,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewFormFieldPlacementConditionDataAttributes")


@_attrs_define
class NewFormFieldPlacementConditionDataAttributes:
    """
    Attributes:
        conditioned (NewFormFieldPlacementConditionDataAttributesConditioned): The resource or attribute the condition
            applies.
        form_field_id (str): The condition field.
        comparison (NewFormFieldPlacementConditionDataAttributesComparison): The condition comparison.
        values (list[str]): The values for comparison.
        position (Union[Unset, int]): The condition position.
    """

    conditioned: NewFormFieldPlacementConditionDataAttributesConditioned
    form_field_id: str
    comparison: NewFormFieldPlacementConditionDataAttributesComparison
    values: list[str]
    position: Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conditioned: str = self.conditioned

        form_field_id = self.form_field_id

        comparison: str = self.comparison

        values = self.values

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conditioned": conditioned,
                "form_field_id": form_field_id,
                "comparison": comparison,
                "values": values,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conditioned = check_new_form_field_placement_condition_data_attributes_conditioned(d.pop("conditioned"))

        form_field_id = d.pop("form_field_id")

        comparison = check_new_form_field_placement_condition_data_attributes_comparison(d.pop("comparison"))

        values = cast(list[str], d.pop("values"))

        position = d.pop("position", UNSET)

        new_form_field_placement_condition_data_attributes = cls(
            conditioned=conditioned,
            form_field_id=form_field_id,
            comparison=comparison,
            values=values,
            position=position,
        )

        new_form_field_placement_condition_data_attributes.additional_properties = d
        return new_form_field_placement_condition_data_attributes

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
