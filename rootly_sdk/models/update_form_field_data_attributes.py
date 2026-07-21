from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_form_field_data_attributes_input_kind import (
    UpdateFormFieldDataAttributesInputKind,
    check_update_form_field_data_attributes_input_kind,
)
from ..models.update_form_field_data_attributes_kind import (
    UpdateFormFieldDataAttributesKind,
    check_update_form_field_data_attributes_kind,
)
from ..models.update_form_field_data_attributes_value_kind import (
    UpdateFormFieldDataAttributesValueKind,
    check_update_form_field_data_attributes_value_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateFormFieldDataAttributes")


@_attrs_define
class UpdateFormFieldDataAttributes:
    """
    Attributes:
        kind (UpdateFormFieldDataAttributesKind | Unset): The kind of the form field
        input_kind (UpdateFormFieldDataAttributesInputKind | Unset): The input kind of the form field
        value_kind (UpdateFormFieldDataAttributesValueKind | Unset): The value kind of the form field
        value_kind_catalog_id (None | str | Unset): The ID of the catalog used when value_kind is `catalog_entity`
        name (str | Unset): The name of the form field
        description (None | str | Unset): The description of the form field
        shown (list[str] | Unset):
        required (list[str] | Unset):
        show_on_incident_details (bool | Unset): Whether the form field is shown on the incident details panel
        enabled (bool | Unset): Whether the form field is enabled
        default_values (list[str] | Unset):
        auto_set_by_catalog_property_id (None | str | Unset): Catalog property ID to auto-set this form field. Only
            reference-kind catalog properties are supported.
    """

    kind: UpdateFormFieldDataAttributesKind | Unset = UNSET
    input_kind: UpdateFormFieldDataAttributesInputKind | Unset = UNSET
    value_kind: UpdateFormFieldDataAttributesValueKind | Unset = UNSET
    value_kind_catalog_id: None | str | Unset = UNSET
    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    shown: list[str] | Unset = UNSET
    required: list[str] | Unset = UNSET
    show_on_incident_details: bool | Unset = UNSET
    enabled: bool | Unset = UNSET
    default_values: list[str] | Unset = UNSET
    auto_set_by_catalog_property_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        input_kind: str | Unset = UNSET
        if not isinstance(self.input_kind, Unset):
            input_kind = self.input_kind

        value_kind: str | Unset = UNSET
        if not isinstance(self.value_kind, Unset):
            value_kind = self.value_kind

        value_kind_catalog_id: None | str | Unset
        if isinstance(self.value_kind_catalog_id, Unset):
            value_kind_catalog_id = UNSET
        else:
            value_kind_catalog_id = self.value_kind_catalog_id

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        shown: list[str] | Unset = UNSET
        if not isinstance(self.shown, Unset):
            shown = self.shown

        required: list[str] | Unset = UNSET
        if not isinstance(self.required, Unset):
            required = self.required

        show_on_incident_details = self.show_on_incident_details

        enabled = self.enabled

        default_values: list[str] | Unset = UNSET
        if not isinstance(self.default_values, Unset):
            default_values = self.default_values

        auto_set_by_catalog_property_id: None | str | Unset
        if isinstance(self.auto_set_by_catalog_property_id, Unset):
            auto_set_by_catalog_property_id = UNSET
        else:
            auto_set_by_catalog_property_id = self.auto_set_by_catalog_property_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if input_kind is not UNSET:
            field_dict["input_kind"] = input_kind
        if value_kind is not UNSET:
            field_dict["value_kind"] = value_kind
        if value_kind_catalog_id is not UNSET:
            field_dict["value_kind_catalog_id"] = value_kind_catalog_id
        if name is not UNSET:
            field_dict["name"] = name
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
        if auto_set_by_catalog_property_id is not UNSET:
            field_dict["auto_set_by_catalog_property_id"] = auto_set_by_catalog_property_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: UpdateFormFieldDataAttributesKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_update_form_field_data_attributes_kind(_kind)

        _input_kind = d.pop("input_kind", UNSET)
        input_kind: UpdateFormFieldDataAttributesInputKind | Unset
        if isinstance(_input_kind, Unset):
            input_kind = UNSET
        else:
            input_kind = check_update_form_field_data_attributes_input_kind(_input_kind)

        _value_kind = d.pop("value_kind", UNSET)
        value_kind: UpdateFormFieldDataAttributesValueKind | Unset
        if isinstance(_value_kind, Unset):
            value_kind = UNSET
        else:
            value_kind = check_update_form_field_data_attributes_value_kind(_value_kind)

        def _parse_value_kind_catalog_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_kind_catalog_id = _parse_value_kind_catalog_id(d.pop("value_kind_catalog_id", UNSET))

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        shown = cast(list[str], d.pop("shown", UNSET))

        required = cast(list[str], d.pop("required", UNSET))

        show_on_incident_details = d.pop("show_on_incident_details", UNSET)

        enabled = d.pop("enabled", UNSET)

        default_values = cast(list[str], d.pop("default_values", UNSET))

        def _parse_auto_set_by_catalog_property_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auto_set_by_catalog_property_id = _parse_auto_set_by_catalog_property_id(
            d.pop("auto_set_by_catalog_property_id", UNSET)
        )

        update_form_field_data_attributes = cls(
            kind=kind,
            input_kind=input_kind,
            value_kind=value_kind,
            value_kind_catalog_id=value_kind_catalog_id,
            name=name,
            description=description,
            shown=shown,
            required=required,
            show_on_incident_details=show_on_incident_details,
            enabled=enabled,
            default_values=default_values,
            auto_set_by_catalog_property_id=auto_set_by_catalog_property_id,
        )

        return update_form_field_data_attributes
