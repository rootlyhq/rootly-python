from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        form_field_id = self.form_field_id

        comparison: str = self.comparison

        values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        new_form_set_condition_data_attributes.additional_properties = d
        return new_form_set_condition_data_attributes

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
