from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_field_placement_placement_operator import (
    FormFieldPlacementPlacementOperator,
    check_form_field_placement_placement_operator,
)
from ..models.form_field_placement_required_operator import (
    FormFieldPlacementRequiredOperator,
    check_form_field_placement_required_operator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FormFieldPlacement")


@_attrs_define
class FormFieldPlacement:
    """
    Attributes:
        form_field_id (str): The form field that is placed.
        form_set_id (str): The form set this field is placed in.
        form (str): The form this field is placed on.
        position (int): The position of the field placement.
        required (bool): Whether the field is unconditionally required on this form.
        required_operator (Union[Unset, FormFieldPlacementRequiredOperator]): Logical operator when evaluating multiple
            form_field_placement_conditions with conditioned=required
        placement_operator (Union[Unset, FormFieldPlacementPlacementOperator]): Logical operator when evaluating
            multiple form_field_placement_conditions with conditioned=placement
        non_editable (Union[Unset, bool]): Whether the field is read-only and cannot be edited by users.
    """

    form_field_id: str
    form_set_id: str
    form: str
    position: int
    required: bool
    required_operator: Unset | FormFieldPlacementRequiredOperator = UNSET
    placement_operator: Unset | FormFieldPlacementPlacementOperator = UNSET
    non_editable: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        form_field_id = self.form_field_id

        form_set_id = self.form_set_id

        form = self.form

        position = self.position

        required = self.required

        required_operator: Unset | str = UNSET
        if not isinstance(self.required_operator, Unset):
            required_operator = self.required_operator

        placement_operator: Unset | str = UNSET
        if not isinstance(self.placement_operator, Unset):
            placement_operator = self.placement_operator

        non_editable = self.non_editable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "form_field_id": form_field_id,
                "form_set_id": form_set_id,
                "form": form,
                "position": position,
                "required": required,
            }
        )
        if required_operator is not UNSET:
            field_dict["required_operator"] = required_operator
        if placement_operator is not UNSET:
            field_dict["placement_operator"] = placement_operator
        if non_editable is not UNSET:
            field_dict["non_editable"] = non_editable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        form_field_id = d.pop("form_field_id")

        form_set_id = d.pop("form_set_id")

        form = d.pop("form")

        position = d.pop("position")

        required = d.pop("required")

        _required_operator = d.pop("required_operator", UNSET)
        required_operator: Unset | FormFieldPlacementRequiredOperator
        if isinstance(_required_operator, Unset):
            required_operator = UNSET
        else:
            required_operator = check_form_field_placement_required_operator(_required_operator)

        _placement_operator = d.pop("placement_operator", UNSET)
        placement_operator: Unset | FormFieldPlacementPlacementOperator
        if isinstance(_placement_operator, Unset):
            placement_operator = UNSET
        else:
            placement_operator = check_form_field_placement_placement_operator(_placement_operator)

        non_editable = d.pop("non_editable", UNSET)

        form_field_placement = cls(
            form_field_id=form_field_id,
            form_set_id=form_set_id,
            form=form,
            position=position,
            required=required,
            required_operator=required_operator,
            placement_operator=placement_operator,
            non_editable=non_editable,
        )

        form_field_placement.additional_properties = d
        return form_field_placement

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
