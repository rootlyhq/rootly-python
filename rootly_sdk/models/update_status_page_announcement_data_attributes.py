from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateStatusPageAnnouncementDataAttributes")


@_attrs_define
class UpdateStatusPageAnnouncementDataAttributes:
    """
    Attributes:
        title (str | Unset): Title of the announcement
        body (str | Unset): Body of the announcement
    """

    title: str | Unset = UNSET
    body: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        body = self.body

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        body = d.pop("body", UNSET)

        update_status_page_announcement_data_attributes = cls(
            title=title,
            body=body,
        )

        return update_status_page_announcement_data_attributes
