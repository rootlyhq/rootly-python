from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.new_form_field_data_attributes_input_kind import (
    NewFormFieldDataAttributesInputKind,
    check_new_form_field_data_attributes_input_kind,
)
from ..models.new_form_field_data_attributes_kind import (
    NewFormFieldDataAttributesKind,
    check_new_form_field_data_attributes_kind,
)
from ..models.new_form_field_data_attributes_value_kind import (
    NewFormFieldDataAttributesValueKind,
    check_new_form_field_data_attributes_value_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewFormFieldDataAttributes")


@_attrs_define
class NewFormFieldDataAttributes:
    """
    Attributes:
        kind (NewFormFieldDataAttributesKind): The kind of the form field
        name (str): The name of the form field
        input_kind (Union[Unset, NewFormFieldDataAttributesInputKind]): The input kind of the form field
        value_kind (Union[Unset, NewFormFieldDataAttributesValueKind]): The value kind of the form field
        value_kind_catalog_id (Union[None, Unset, str]): The ID of the catalog used when value_kind is `catalog_entity`
        description (Union[None, Unset, str]): The description of the form field
        shown (Union[Unset, list[str]]):
        required (Union[Unset, list[str]]):
        show_on_incident_details (Union[Unset, bool]): Whether the form field is shown on the incident details panel
        enabled (Union[Unset, bool]): Whether the form field is enabled
        default_values (Union[Unset, list[str]]):
        auto_set_by_catalog_field_id (Union[None, Unset, str]): Catalog field ID to auto-set this form field. Only
            reference-kind catalog fields are supported.
    """

    kind: NewFormFieldDataAttributesKind
    name: str
    input_kind: Union[Unset, NewFormFieldDataAttributesInputKind] = UNSET
    value_kind: Union[Unset, NewFormFieldDataAttributesValueKind] = UNSET
    value_kind_catalog_id: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    shown: Union[Unset, list[str]] = UNSET
    required: Union[Unset, list[str]] = UNSET
    show_on_incident_details: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET
    default_values: Union[Unset, list[str]] = UNSET
    auto_set_by_catalog_field_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        name = self.name

        input_kind: Union[Unset, str] = UNSET
        if not isinstance(self.input_kind, Unset):
            input_kind = self.input_kind

        value_kind: Union[Unset, str] = UNSET
        if not isinstance(self.value_kind, Unset):
            value_kind = self.value_kind

        value_kind_catalog_id: Union[None, Unset, str]
        if isinstance(self.value_kind_catalog_id, Unset):
            value_kind_catalog_id = UNSET
        else:
            value_kind_catalog_id = self.value_kind_catalog_id

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        shown: Union[Unset, list[str]] = UNSET
        if not isinstance(self.shown, Unset):
            shown = self.shown

        required: Union[Unset, list[str]] = UNSET
        if not isinstance(self.required, Unset):
            required = self.required

        show_on_incident_details = self.show_on_incident_details

        enabled = self.enabled

        default_values: Union[Unset, list[str]] = UNSET
        if not isinstance(self.default_values, Unset):
            default_values = self.default_values

        auto_set_by_catalog_field_id: Union[None, Unset, str]
        if isinstance(self.auto_set_by_catalog_field_id, Unset):
            auto_set_by_catalog_field_id = UNSET
        else:
            auto_set_by_catalog_field_id = self.auto_set_by_catalog_field_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "name": name,
            }
        )
        if input_kind is not UNSET:
            field_dict["input_kind"] = input_kind
        if value_kind is not UNSET:
            field_dict["value_kind"] = value_kind
        if value_kind_catalog_id is not UNSET:
            field_dict["value_kind_catalog_id"] = value_kind_catalog_id
        if description is not UNSET:
            field_dict["description"] = description
        if shown is not UNSET:
            field_dict["shown"] = shown
        if required is not UNSET:
            field_dict["required"] = required
        if show_on_incident_details is not UNSET:
            field_dict["show_on_incident_details"] = show_on_incident_details
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if default_values is not UNSET:
            field_dict["default_values"] = default_values
        if auto_set_by_catalog_field_id is not UNSET:
            field_dict["auto_set_by_catalog_field_id"] = auto_set_by_catalog_field_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = check_new_form_field_data_attributes_kind(d.pop("kind"))

        name = d.pop("name")

        _input_kind = d.pop("input_kind", UNSET)
        input_kind: Union[Unset, NewFormFieldDataAttributesInputKind]
        if isinstance(_input_kind, Unset):
            input_kind = UNSET
        else:
            input_kind = check_new_form_field_data_attributes_input_kind(_input_kind)

        _value_kind = d.pop("value_kind", UNSET)
        value_kind: Union[Unset, NewFormFieldDataAttributesValueKind]
        if isinstance(_value_kind, Unset):
            value_kind = UNSET
        else:
            value_kind = check_new_form_field_data_attributes_value_kind(_value_kind)

        def _parse_value_kind_catalog_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        value_kind_catalog_id = _parse_value_kind_catalog_id(d.pop("value_kind_catalog_id", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        shown = cast(list[str], d.pop("shown", UNSET))

        required = cast(list[str], d.pop("required", UNSET))

        show_on_incident_details = d.pop("show_on_incident_details", UNSET)

        enabled = d.pop("enabled", UNSET)

        default_values = cast(list[str], d.pop("default_values", UNSET))

        def _parse_auto_set_by_catalog_field_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        auto_set_by_catalog_field_id = _parse_auto_set_by_catalog_field_id(d.pop("auto_set_by_catalog_field_id", UNSET))

        new_form_field_data_attributes = cls(
            kind=kind,
            name=name,
            input_kind=input_kind,
            value_kind=value_kind,
            value_kind_catalog_id=value_kind_catalog_id,
            description=description,
            shown=shown,
            required=required,
            show_on_incident_details=show_on_incident_details,
            enabled=enabled,
            default_values=default_values,
            auto_set_by_catalog_field_id=auto_set_by_catalog_field_id,
        )

        return new_form_field_data_attributes
