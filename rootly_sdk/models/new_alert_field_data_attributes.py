from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewAlertFieldDataAttributes")


@_attrs_define
class NewAlertFieldDataAttributes:
    """
    Attributes:
        name (str): The name of the alert field
        slug (None | str | Unset): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        owner_group_ids (list[str] | None | Unset): IDs of the teams that own the alert field. Callers with org-wide
            alert field permissions may omit it or pass an empty list to create an org-wide field. Callers without them
            (team admins, team-scoped API keys) get their administered teams by default when it is omitted, and must
            otherwise pass at least one team they administer; an explicit empty list or null is rejected.
    """

    name: str
    slug: None | str | Unset = UNSET
    owner_group_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        owner_group_ids: list[str] | None | Unset
        if isinstance(self.owner_group_ids, Unset):
            owner_group_ids = UNSET
        elif isinstance(self.owner_group_ids, list):
            owner_group_ids = self.owner_group_ids

        else:
            owner_group_ids = self.owner_group_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
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

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_owner_group_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_group_ids_type_0 = cast(list[str], data)

                return owner_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        owner_group_ids = _parse_owner_group_ids(d.pop("owner_group_ids", UNSET))

        new_alert_field_data_attributes = cls(
            name=name,
            slug=slug,
            owner_group_ids=owner_group_ids,
        )

        return new_alert_field_data_attributes
