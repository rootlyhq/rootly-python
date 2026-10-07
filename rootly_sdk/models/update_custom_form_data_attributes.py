from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCustomFormDataAttributes")


@_attrs_define
class UpdateCustomFormDataAttributes:
    """
    Attributes:
        slug (None | str | Unset): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        name (str | Unset): The name of the custom form.
        description (None | str | Unset):
        enabled (bool | Unset):
        command (str | Unset): The Slack command used to trigger this form.
    """

    slug: None | str | Unset = UNSET
    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    enabled: bool | Unset = UNSET
    command: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled = self.enabled

        command = self.command

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if command is not UNSET:
            field_dict["command"] = command

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        enabled = d.pop("enabled", UNSET)

        command = d.pop("command", UNSET)

        update_custom_form_data_attributes = cls(
            slug=slug,
            name=name,
            description=description,
            enabled=enabled,
            command=command,
        )

        return update_custom_form_data_attributes
