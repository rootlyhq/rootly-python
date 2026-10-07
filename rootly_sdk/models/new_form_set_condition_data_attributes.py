from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_form_set_condition_data_attributes_comparison import (
    NewFormSetConditionDataAttributesComparison,
    check_new_form_set_condition_data_attributes_comparison,
)

T = TypeVar("T", bound="NewFormSetConditionDataAttributes")


@_attrs_define
class NewFormSetConditionDataAttributes:
    """
    Attributes:
        form_field_id (str): The form field this condition applies.
        comparison (NewFormSetConditionDataAttributesComparison): The condition comparison.
        values (list[str]): The values for comparison.
    """

    form_field_id: str
    comparison: NewFormSetConditionDataAttributesComparison
    values: list[str]

    def to_dict(self) -> dict[str, Any]:
        form_field_id = self.form_field_id

        comparison: str = self.comparison

        values = self.values

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "form_field_id": form_field_id,
                "comparison": comparison,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        form_field_id = d.pop("form_field_id")

        comparison = check_new_form_set_condition_data_attributes_comparison(d.pop("comparison"))

        values = cast(list[str], d.pop("values"))

        new_form_set_condition_data_attributes = cls(
            form_field_id=form_field_id,
            comparison=comparison,
            values=values,
        )

        return new_form_set_condition_data_attributes
