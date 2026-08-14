from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_field_placement_condition_comparison import (
    FormFieldPlacementConditionComparison,
    check_form_field_placement_condition_comparison,
)
from ..models.form_field_placement_condition_conditioned import (
    FormFieldPlacementConditionConditioned,
    check_form_field_placement_condition_conditioned,
)

T = TypeVar("T", bound="FormFieldPlacementCondition")


@_attrs_define
class FormFieldPlacementCondition:
    """
    Attributes:
        form_field_placement_id (str): The form field placement this condition applies.
        conditioned (FormFieldPlacementConditionConditioned): The resource or attribute the condition applies.
        position (int): The condition position.
        form_field_id (str): The condition field.
        comparison (FormFieldPlacementConditionComparison): The condition comparison.
        values (list[str]): The values for comparison.
    """

    form_field_placement_id: str
    conditioned: FormFieldPlacementConditionConditioned
    position: int
    form_field_id: str
    comparison: FormFieldPlacementConditionComparison
    values: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        form_field_placement_id = self.form_field_placement_id

        conditioned: str = self.conditioned

        position = self.position

        form_field_id = self.form_field_id

        comparison: str = self.comparison

        values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "form_field_placement_id": form_field_placement_id,
                "conditioned": conditioned,
                "position": position,
                "form_field_id": form_field_id,
                "comparison": comparison,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        form_field_placement_id = d.pop("form_field_placement_id")

        conditioned = check_form_field_placement_condition_conditioned(d.pop("conditioned"))

        position = d.pop("position")

        form_field_id = d.pop("form_field_id")

        comparison = check_form_field_placement_condition_comparison(d.pop("comparison"))

        values = cast(list[str], d.pop("values"))

        form_field_placement_condition = cls(
            form_field_placement_id=form_field_placement_id,
            conditioned=conditioned,
            position=position,
            form_field_id=form_field_id,
            comparison=comparison,
            values=values,
        )

        form_field_placement_condition.additional_properties = d
        return form_field_placement_condition

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
