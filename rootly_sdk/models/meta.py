from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Meta")


@_attrs_define
class Meta:
    """
    Attributes:
        current_page (int | None):
        next_page (int | None):
        prev_page (int | None):
        total_count (int):
        total_pages (int):
        next_cursor (None | str | Unset):
    """

    current_page: int | None
    next_page: int | None
    prev_page: int | None
    total_count: int
    total_pages: int
    next_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page: int | None
        current_page = self.current_page

        next_page: int | None
        next_page = self.next_page

        prev_page: int | None
        prev_page = self.prev_page

        total_count = self.total_count

        total_pages = self.total_pages

        next_cursor: None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_page": current_page,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_count": total_count,
                "total_pages": total_pages,
            }
        )
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_current_page(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        current_page = _parse_current_page(d.pop("current_page"))

        def _parse_next_page(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        next_page = _parse_next_page(d.pop("next_page"))

        def _parse_prev_page(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        prev_page = _parse_prev_page(d.pop("prev_page"))

        total_count = d.pop("total_count")

        total_pages = d.pop("total_pages")

        def _parse_next_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))

        meta = cls(
            current_page=current_page,
            next_page=next_page,
            prev_page=prev_page,
            total_count=total_count,
            total_pages=total_pages,
            next_cursor=next_cursor,
        )

        meta.additional_properties = d
        return meta

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
