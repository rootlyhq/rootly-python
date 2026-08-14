from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentRole")


@_attrs_define
class IncidentRole:
    """
    Attributes:
        name (str): The name of the incident role
        created_at (str): Date of creation
        updated_at (str): Date of last update
        slug (Union[Unset, str]): The slug of the incident role
        summary (Union[None, Unset, str]): The summary of the incident role
        description (Union[None, Unset, str]): The description of the incident role
        position (Union[None, Unset, int]): Position of the incident role
        optional (Union[Unset, bool]):
        enabled (Union[Unset, bool]):
        allow_multi_user_assignment (Union[Unset, bool]):
    """

    name: str
    created_at: str
    updated_at: str
    slug: Unset | str = UNSET
    summary: None | Unset | str = UNSET
    description: None | Unset | str = UNSET
    position: None | Unset | int = UNSET
    optional: Unset | bool = UNSET
    enabled: Unset | bool = UNSET
    allow_multi_user_assignment: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        summary: None | Unset | str
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        position: None | Unset | int
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        optional = self.optional

        enabled = self.enabled

        allow_multi_user_assignment = self.allow_multi_user_assignment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position
        if optional is not UNSET:
            field_dict["optional"] = optional
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if allow_multi_user_assignment is not UNSET:
            field_dict["allow_multi_user_assignment"] = allow_multi_user_assignment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        def _parse_summary(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        optional = d.pop("optional", UNSET)

        enabled = d.pop("enabled", UNSET)

        allow_multi_user_assignment = d.pop("allow_multi_user_assignment", UNSET)

        incident_role = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            summary=summary,
            description=description,
            position=position,
            optional=optional,
            enabled=enabled,
            allow_multi_user_assignment=allow_multi_user_assignment,
        )

        incident_role.additional_properties = d
        return incident_role

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
