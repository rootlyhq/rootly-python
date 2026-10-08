from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageAnnouncement")


@_attrs_define
class StatusPageAnnouncement:
    """
    Attributes:
        status_page_id (str): ID of the status page the announcement was posted to
        title (str): Title of the announcement
        body (str): Body of the announcement
        published_at (str): Date the announcement was published
        created_at (str): Date of creation
        updated_at (str): Date of last update
        user_id (int | None | Unset): ID of the user who posted the announcement
    """

    status_page_id: str
    title: str
    body: str
    published_at: str
    created_at: str
    updated_at: str
    user_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_page_id = self.status_page_id

        title = self.title

        body = self.body

        published_at = self.published_at

        created_at = self.created_at

        updated_at = self.updated_at

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status_page_id": status_page_id,
                "title": title,
                "body": body,
                "published_at": published_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status_page_id = d.pop("status_page_id")

        title = d.pop("title")

        body = d.pop("body")

        published_at = d.pop("published_at")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        status_page_announcement = cls(
            status_page_id=status_page_id,
            title=title,
            body=body,
            published_at=published_at,
            created_at=created_at,
            updated_at=updated_at,
            user_id=user_id,
        )

        status_page_announcement.additional_properties = d
        return status_page_announcement

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
