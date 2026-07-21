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
        name (str | Unset): The name of the custom form.
        description (None | str | Unset):
        enabled (bool | Unset):
        command (str | Unset): The Slack command used to trigger this form.
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    enabled: bool | Unset = UNSET
    command: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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
            name=name,
            description=description,
            enabled=enabled,
            command=command,
        )

        return update_custom_form_data_attributes
