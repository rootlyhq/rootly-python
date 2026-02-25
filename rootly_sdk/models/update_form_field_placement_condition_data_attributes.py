from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_form_field_placement_condition_data_attributes_comparison import (
    UpdateFormFieldPlacementConditionDataAttributesComparison,
    check_update_form_field_placement_condition_data_attributes_comparison,
)
from ..models.update_form_field_placement_condition_data_attributes_conditioned import (
    UpdateFormFieldPlacementConditionDataAttributesConditioned,
    check_update_form_field_placement_condition_data_attributes_conditioned,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFormFieldPlacementConditionDataAttributes")


@_attrs_define
class UpdateFormFieldPlacementConditionDataAttributes:
    """
    Attributes:
        conditioned (Union[Unset, UpdateFormFieldPlacementConditionDataAttributesConditioned]): The resource or
            attribute the condition applies.
        position (Union[Unset, int]): The condition position.
        form_field_id (Union[Unset, str]): The condition field.
        comparison (Union[Unset, UpdateFormFieldPlacementConditionDataAttributesComparison]): The condition comparison.
        values (Union[Unset, list[str]]): The values for comparison.
    """

    conditioned: Unset | UpdateFormFieldPlacementConditionDataAttributesConditioned = UNSET
    position: Unset | int = UNSET
    form_field_id: Unset | str = UNSET
    comparison: Unset | UpdateFormFieldPlacementConditionDataAttributesComparison = UNSET
    values: Unset | list[str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        conditioned: Unset | str = UNSET
        if not isinstance(self.conditioned, Unset):
            conditioned = self.conditioned

        position = self.position

        form_field_id = self.form_field_id

        comparison: Unset | str = UNSET
        if not isinstance(self.comparison, Unset):
            comparison = self.comparison

        values: Unset | list[str] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if conditioned is not UNSET:
            field_dict["conditioned"] = conditioned
        if position is not UNSET:
            field_dict["position"] = position
        if form_field_id is not UNSET:
            field_dict["form_field_id"] = form_field_id
        if comparison is not UNSET:
            field_dict["comparison"] = comparison
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _conditioned = d.pop("conditioned", UNSET)
        conditioned: Unset | UpdateFormFieldPlacementConditionDataAttributesConditioned
        if isinstance(_conditioned, Unset):
            conditioned = UNSET
        else:
            conditioned = check_update_form_field_placement_condition_data_attributes_conditioned(_conditioned)

        position = d.pop("position", UNSET)

        form_field_id = d.pop("form_field_id", UNSET)

        _comparison = d.pop("comparison", UNSET)
        comparison: Unset | UpdateFormFieldPlacementConditionDataAttributesComparison
        if isinstance(_comparison, Unset):
            comparison = UNSET
        else:
            comparison = check_update_form_field_placement_condition_data_attributes_comparison(_comparison)

        values = cast(list[str], d.pop("values", UNSET))

        update_form_field_placement_condition_data_attributes = cls(
            conditioned=conditioned,
            position=position,
            form_field_id=form_field_id,
            comparison=comparison,
            values=values,
        )

        return update_form_field_placement_condition_data_attributes
