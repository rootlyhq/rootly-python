from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormFieldOption")


@_attrs_define
class FormFieldOption:
    """
    Attributes:
        value (str): The value of the form field option
        color (str): The hex color of the form field option
        position (int): The position of the form field option
        created_at (str): Date of creation
        updated_at (str): Date of last update
        id (Union[Unset, str]): Unique ID of the form field option
        form_field_id (Union[Unset, str]): The ID of the parent custom field
        default (Union[Unset, bool]):
    """

    value: str
    color: str
    position: int
    created_at: str
    updated_at: str
    id: Unset | str = UNSET
    form_field_id: Unset | str = UNSET
    default: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        color = self.color

        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        id = self.id

        form_field_id = self.form_field_id

        default = self.default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "color": color,
                "position": position,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if form_field_id is not UNSET:
            field_dict["form_field_id"] = form_field_id
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        color = d.pop("color")

        position = d.pop("position")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        id = d.pop("id", UNSET)

        form_field_id = d.pop("form_field_id", UNSET)

        default = d.pop("default", UNSET)

        form_field_option = cls(
            value=value,
            color=color,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            form_field_id=form_field_id,
            default=default,
        )

        form_field_option.additional_properties = d
        return form_field_option

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
