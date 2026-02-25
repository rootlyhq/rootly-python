from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_required_type_0_item import (
    CustomFieldRequiredType0Item,
    check_custom_field_required_type_0_item,
)
from ..models.custom_field_shown_item import CustomFieldShownItem, check_custom_field_shown_item
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomField")


@_attrs_define
class CustomField:
    """
    Attributes:
        label (str): The name of the custom_field
        shown (list[CustomFieldShownItem]):
        required (Union[None, list[CustomFieldRequiredType0Item]]):
        position (int): The position of the custom_field
        created_at (str): Date of creation
        updated_at (str): Date of last update
        kind (Union[Unset, str]): The kind of the custom_field
        enabled (Union[Unset, bool]): Whether the custom_field is enabled
        slug (Union[Unset, str]): The slug of the custom_field
        description (Union[None, Unset, str]): The description of the custom_field
        default (Union[None, Unset, str]): The default value for text field kinds
    """

    label: str
    shown: list[CustomFieldShownItem]
    required: Union[None, list[CustomFieldRequiredType0Item]]
    position: int
    created_at: str
    updated_at: str
    kind: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    slug: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    default: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        shown = []
        for shown_item_data in self.shown:
            shown_item: str = shown_item_data
            shown.append(shown_item)

        required: Union[None, list[str]]
        if isinstance(self.required, list):
            required = []
            for required_type_0_item_data in self.required:
                required_type_0_item: str = required_type_0_item_data
                required.append(required_type_0_item)

        else:
            required = self.required

        position = self.position

        created_at = self.created_at

        updated_at = self.updated_at

        kind = self.kind

        enabled = self.enabled

        slug = self.slug

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        default: Union[None, Unset, str]
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "shown": shown,
                "required": required,
                "position": position,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label = d.pop("label")

        shown = []
        _shown = d.pop("shown")
        for shown_item_data in _shown:
            shown_item = check_custom_field_shown_item(shown_item_data)

            shown.append(shown_item)

        def _parse_required(data: object) -> Union[None, list[CustomFieldRequiredType0Item]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                required_type_0 = []
                _required_type_0 = data
                for required_type_0_item_data in _required_type_0:
                    required_type_0_item = check_custom_field_required_type_0_item(required_type_0_item_data)

                    required_type_0.append(required_type_0_item)

                return required_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[CustomFieldRequiredType0Item]], data)

        required = _parse_required(d.pop("required"))

        position = d.pop("position")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        kind = d.pop("kind", UNSET)

        enabled = d.pop("enabled", UNSET)

        slug = d.pop("slug", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_default(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default = _parse_default(d.pop("default", UNSET))

        custom_field = cls(
            label=label,
            shown=shown,
            required=required,
            position=position,
            created_at=created_at,
            updated_at=updated_at,
            kind=kind,
            enabled=enabled,
            slug=slug,
            description=description,
            default=default,
        )

        custom_field.additional_properties = d
        return custom_field

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
