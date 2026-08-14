from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewCustomFormDataAttributes")


@_attrs_define
class NewCustomFormDataAttributes:
    """
    Attributes:
        name (str): The name of the custom form.
        command (str): The Slack command used to trigger this form.
        slug (Union[None, Unset, str]): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        description (Union[None, Unset, str]):
        enabled (Union[Unset, bool]):
    """

    name: str
    command: str
    slug: None | Unset | str = UNSET
    description: None | Unset | str = UNSET
    enabled: Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        command = self.command

        slug: None | Unset | str
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "command": command,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        command = d.pop("command")

        def _parse_slug(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        enabled = d.pop("enabled", UNSET)

        new_custom_form_data_attributes = cls(
            name=name,
            command=command,
            slug=slug,
            description=description,
            enabled=enabled,
        )

        return new_custom_form_data_attributes
