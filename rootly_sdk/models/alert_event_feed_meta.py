from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertEventFeedMeta")


@_attrs_define
class AlertEventFeedMeta:
    """Cursor-pagination meta. `total_count` and `total_pages` are nullable because the feed does not run a COUNT query.

    Attributes:
        next_cursor (Union[None, str]): Pass as `page[after]` on the next request to fetch the following page.
        current_page (Union[None, Unset, int]):
        next_page (Union[None, Unset, int]):
        prev_page (Union[None, Unset, int]):
        total_count (Union[None, Unset, int]):
        total_pages (Union[None, Unset, int]):
    """

    next_cursor: Union[None, str]
    current_page: Union[None, Unset, int] = UNSET
    next_page: Union[None, Unset, int] = UNSET
    prev_page: Union[None, Unset, int] = UNSET
    total_count: Union[None, Unset, int] = UNSET
    total_pages: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_cursor: Union[None, str]
        next_cursor = self.next_cursor

        current_page: Union[None, Unset, int]
        if isinstance(self.current_page, Unset):
            current_page = UNSET
        else:
            current_page = self.current_page

        next_page: Union[None, Unset, int]
        if isinstance(self.next_page, Unset):
            next_page = UNSET
        else:
            next_page = self.next_page

        prev_page: Union[None, Unset, int]
        if isinstance(self.prev_page, Unset):
            prev_page = UNSET
        else:
            prev_page = self.prev_page

        total_count: Union[None, Unset, int]
        if isinstance(self.total_count, Unset):
            total_count = UNSET
        else:
            total_count = self.total_count

        total_pages: Union[None, Unset, int]
        if isinstance(self.total_pages, Unset):
            total_pages = UNSET
        else:
            total_pages = self.total_pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "next_cursor": next_cursor,
            }
        )
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if next_page is not UNSET:
            field_dict["next_page"] = next_page
        if prev_page is not UNSET:
            field_dict["prev_page"] = prev_page
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_next_cursor(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        def _parse_current_page(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        current_page = _parse_current_page(d.pop("current_page", UNSET))

        def _parse_next_page(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        next_page = _parse_next_page(d.pop("next_page", UNSET))

        def _parse_prev_page(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        prev_page = _parse_prev_page(d.pop("prev_page", UNSET))

        def _parse_total_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_count = _parse_total_count(d.pop("total_count", UNSET))

        def _parse_total_pages(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_pages = _parse_total_pages(d.pop("total_pages", UNSET))

        alert_event_feed_meta = cls(
            next_cursor=next_cursor,
            current_page=current_page,
            next_page=next_page,
            prev_page=prev_page,
            total_count=total_count,
            total_pages=total_pages,
        )

        alert_event_feed_meta.additional_properties = d
        return alert_event_feed_meta

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
