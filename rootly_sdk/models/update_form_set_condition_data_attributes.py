from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_form_set_condition_data_attributes_comparison import (
    UpdateFormSetConditionDataAttributesComparison,
    check_update_form_set_condition_data_attributes_comparison,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFormSetConditionDataAttributes")


@_attrs_define
class UpdateFormSetConditionDataAttributes:
    """
    Attributes:
        form_field_id (str | Unset): The form field this condition applies.
        comparison (UpdateFormSetConditionDataAttributesComparison | Unset): The condition comparison.
        values (list[str] | Unset): The values for comparison.
    """

    form_field_id: str | Unset = UNSET
    comparison: UpdateFormSetConditionDataAttributesComparison | Unset = UNSET
    values: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        form_field_id = self.form_field_id

        comparison: str | Unset = UNSET
        if not isinstance(self.comparison, Unset):
            comparison = self.comparison

        values: list[str] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}

        field_dict.update({})
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
        form_field_id = d.pop("form_field_id", UNSET)

        _comparison = d.pop("comparison", UNSET)
        comparison: UpdateFormSetConditionDataAttributesComparison | Unset
        if isinstance(_comparison, Unset):
            comparison = UNSET
        else:
            comparison = check_update_form_set_condition_data_attributes_comparison(_comparison)

        values = cast(list[str], d.pop("values", UNSET))

        update_form_set_condition_data_attributes = cls(
            form_field_id=form_field_id,
            comparison=comparison,
            values=values,
        )

        return update_form_set_condition_data_attributes
