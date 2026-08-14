from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.form_field_position_form import FormFieldPositionForm, check_form_field_position_form

T = TypeVar("T", bound="FormFieldPosition")


@_attrs_define
class FormFieldPosition:
    """
    Attributes:
        form_field_id (str): The ID of the form field.
        form (FormFieldPositionForm): The form for the position
        position (int): The position of the form_field_position
    """

    form_field_id: str
    form: FormFieldPositionForm
    position: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        form_field_id = self.form_field_id

        form: str = self.form

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        form = check_form_field_position_form(d.pop("form"))

        position = d.pop("position")

        form_field_position = cls(
            form_field_id=form_field_id,
            form=form,
            position=position,
        )

        form_field_position.additional_properties = d
        return form_field_position

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
