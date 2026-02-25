from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_form_field_placement_data_attributes_placement_operator import (
    UpdateFormFieldPlacementDataAttributesPlacementOperator,
    check_update_form_field_placement_data_attributes_placement_operator,
)
from ..models.update_form_field_placement_data_attributes_required_operator import (
    UpdateFormFieldPlacementDataAttributesRequiredOperator,
    check_update_form_field_placement_data_attributes_required_operator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFormFieldPlacementDataAttributes")


@_attrs_define
class UpdateFormFieldPlacementDataAttributes:
    """
    Attributes:
        form_set_id (Union[Unset, str]): The form set this field is placed in.
        form (Union[Unset, str]): The form this field is placed on.
        position (Union[Unset, int]): The position of the field placement.
        required (Union[Unset, bool]): Whether the field is unconditionally required on this form.
        required_operator (Union[Unset, UpdateFormFieldPlacementDataAttributesRequiredOperator]): Logical operator when
            evaluating multiple form_field_placement_conditions with conditioned=required
        placement_operator (Union[Unset, UpdateFormFieldPlacementDataAttributesPlacementOperator]): Logical operator
            when evaluating multiple form_field_placement_conditions with conditioned=placement
        non_editable (Union[Unset, bool]): Whether the field is read-only and cannot be edited by users.
    """

    form_set_id: Unset | str = UNSET
    form: Unset | str = UNSET
    position: Unset | int = UNSET
    required: Unset | bool = UNSET
    required_operator: Unset | UpdateFormFieldPlacementDataAttributesRequiredOperator = UNSET
    placement_operator: Unset | UpdateFormFieldPlacementDataAttributesPlacementOperator = UNSET
    non_editable: Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        field_dict.update({})
        if form_set_id is not UNSET:
            field_dict["form_set_id"] = form_set_id
        if form is not UNSET:
            field_dict["form"] = form
        if position is not UNSET:
            field_dict["position"] = position
        if required is not UNSET:
            field_dict["required"] = required
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
        form_set_id = d.pop("form_set_id", UNSET)

        form = d.pop("form", UNSET)

        position = d.pop("position", UNSET)

        required = d.pop("required", UNSET)

        _required_operator = d.pop("required_operator", UNSET)
        required_operator: Unset | UpdateFormFieldPlacementDataAttributesRequiredOperator
        if isinstance(_required_operator, Unset):
            required_operator = UNSET
        else:
            required_operator = check_update_form_field_placement_data_attributes_required_operator(_required_operator)

        _placement_operator = d.pop("placement_operator", UNSET)
        placement_operator: Unset | UpdateFormFieldPlacementDataAttributesPlacementOperator
        if isinstance(_placement_operator, Unset):
            placement_operator = UNSET
        else:
            placement_operator = check_update_form_field_placement_data_attributes_placement_operator(
                _placement_operator
            )

        non_editable = d.pop("non_editable", UNSET)

        update_form_field_placement_data_attributes = cls(
            form_set_id=form_set_id,
            form=form,
            position=position,
            required=required,
            required_operator=required_operator,
            placement_operator=placement_operator,
            non_editable=non_editable,
        )

        return update_form_field_placement_data_attributes
