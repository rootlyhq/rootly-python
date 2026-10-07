from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertField")


@_attrs_define
class AlertField:
    """
    Attributes:
        name (str): The name of the alert field
        kind (str): The kind of alert field
        created_at (str): Date of creation
        updated_at (str): Date of last update
        slug (str | Unset): The slug of the alert field
        owner_group_ids (list[str] | Unset): IDs of the teams that own the alert field. Empty for org-wide fields.
    """

    name: str
    kind: str
    created_at: str
    updated_at: str
    slug: str | Unset = UNSET
    owner_group_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind = self.kind

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        owner_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.owner_group_ids, Unset):
            owner_group_ids = self.owner_group_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "kind": kind,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if owner_group_ids is not UNSET:
            field_dict["owner_group_ids"] = owner_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        kind = d.pop("kind")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        owner_group_ids = cast(list[str], d.pop("owner_group_ids", UNSET))

        alert_field = cls(
            name=name,
            kind=kind,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            owner_group_ids=owner_group_ids,
        )

        alert_field.additional_properties = d
        return alert_field

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
