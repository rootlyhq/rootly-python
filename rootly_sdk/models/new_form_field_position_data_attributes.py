from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_form_field_position_data_attributes_form import (
    NewFormFieldPositionDataAttributesForm,
    check_new_form_field_position_data_attributes_form,
)

T = TypeVar("T", bound="NewFormFieldPositionDataAttributes")


@_attrs_define
class NewFormFieldPositionDataAttributes:
    """
    Attributes:
        form_field_id (str): The ID of the form field.
        form (NewFormFieldPositionDataAttributesForm): The form for the position
        position (int): The position of the form_field_position
    """

    form_field_id: str
    form: NewFormFieldPositionDataAttributesForm
    position: int

    def to_dict(self) -> dict[str, Any]:
        form_field_id = self.form_field_id

        form: str = self.form

        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "form_field_id": form_field_id,
                "form": form,
                "position": position,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        form_field_id = d.pop("form_field_id")

        form = check_new_form_field_position_data_attributes_form(d.pop("form"))

        position = d.pop("position")

        new_form_field_position_data_attributes = cls(
            form_field_id=form_field_id,
            form=form,
            position=position,
        )

        return new_form_field_position_data_attributes
