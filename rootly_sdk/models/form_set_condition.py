from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_set_condition_comparison import FormSetConditionComparison, check_form_set_condition_comparison

T = TypeVar("T", bound="FormSetCondition")


@_attrs_define
class FormSetCondition:
    """
    Attributes:
        form_set_id (str): The form set this condition applies.
        form_field_id (str): The form field this condition applies.
        comparison (FormSetConditionComparison): The condition comparison.
        values (list[str]): The values for comparison.
    """

    form_set_id: str
    form_field_id: str
    comparison: FormSetConditionComparison
    values: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        form_set_id = self.form_set_id

        form_field_id = self.form_field_id

        comparison: str = self.comparison

        values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "form_set_id": form_set_id,
                "form_field_id": form_field_id,
                "comparison": comparison,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        form_set_id = d.pop("form_set_id")

        form_field_id = d.pop("form_field_id")

        comparison = check_form_set_condition_comparison(d.pop("comparison"))

        values = cast(list[str], d.pop("values"))

        form_set_condition = cls(
            form_set_id=form_set_id,
            form_field_id=form_field_id,
            comparison=comparison,
            values=values,
        )

        form_set_condition.additional_properties = d
        return form_set_condition

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
