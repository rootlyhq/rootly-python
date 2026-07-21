from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_form_field_position_data_attributes_form import (
    UpdateFormFieldPositionDataAttributesForm,
    check_update_form_field_position_data_attributes_form,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFormFieldPositionDataAttributes")


@_attrs_define
class UpdateFormFieldPositionDataAttributes:
    """
    Attributes:
        form_field_id (str | Unset): The ID of the form field.
        form (UpdateFormFieldPositionDataAttributesForm | Unset): The form for the position
        position (int | Unset): The position of the form_field_position
    """

    form_field_id: str | Unset = UNSET
    form: UpdateFormFieldPositionDataAttributesForm | Unset = UNSET
    position: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        form_field_id = self.form_field_id

        form: str | Unset = UNSET
        if not isinstance(self.form, Unset):
            form = self.form

        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if form_field_id is not UNSET:
            field_dict["form_field_id"] = form_field_id
        if form is not UNSET:
            field_dict["form"] = form
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        form_field_id = d.pop("form_field_id", UNSET)

        _form = d.pop("form", UNSET)
        form: UpdateFormFieldPositionDataAttributesForm | Unset
        if isinstance(_form, Unset):
            form = UNSET
        else:
            form = check_update_form_field_position_data_attributes_form(_form)

        position = d.pop("position", UNSET)

        update_form_field_position_data_attributes = cls(
            form_field_id=form_field_id,
            form=form,
            position=position,
        )

        return update_form_field_position_data_attributes
