from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomForm")


@_attrs_define
class CustomForm:
    """
    Attributes:
        name (str): The name of the custom form.
        slug (str): The custom form slug. Add this to form_field.shown or form_field.required to associate form fields
            with custom forms.
        enabled (bool):
        command (str): The Slack command used to trigger this form.
        created_at (str): Date of creation.
        updated_at (str): Date of last update.
        description (Union[None, Unset, str]):
    """

    name: str
    slug: str
    enabled: bool
    command: str
    created_at: str
    updated_at: str
    description: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug = self.slug

        enabled = self.enabled

        command = self.command

        created_at = self.created_at

        updated_at = self.updated_at

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "slug": slug,
                "enabled": enabled,
                "command": command,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        slug = d.pop("slug")

        enabled = d.pop("enabled")

        command = d.pop("command")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        custom_form = cls(
            name=name,
            slug=slug,
            enabled=enabled,
            command=command,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
        )

        custom_form.additional_properties = d
        return custom_form

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
