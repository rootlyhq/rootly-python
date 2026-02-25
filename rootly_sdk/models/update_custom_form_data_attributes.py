from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCustomFormDataAttributes")


@_attrs_define
class UpdateCustomFormDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the custom form.
        description (Union[None, Unset, str]):
        enabled (Union[Unset, bool]):
        command (Union[Unset, str]): The Slack command used to trigger this form.
    """

    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    command: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: Union[None, Unset, str]
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

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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
