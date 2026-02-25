from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Meta")


@_attrs_define
class Meta:
    """
    Attributes:
        current_page (int):
        next_page (Union[None, int]):
        prev_page (Union[None, int]):
        total_count (int):
        total_pages (int):
    """

    current_page: int
    next_page: None | int
    prev_page: None | int
    total_count: int
    total_pages: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        next_page: None | int
        next_page = self.next_page

        prev_page: None | int
        prev_page = self.prev_page

        total_count = self.total_count

        total_pages = self.total_pages

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_page = d.pop("current_page")

        def _parse_next_page(data: object) -> None | int:
            if data is None:
                return data
            return cast(None | int, data)

        next_page = _parse_next_page(d.pop("next_page"))

        def _parse_prev_page(data: object) -> None | int:
            if data is None:
                return data
            return cast(None | int, data)

        prev_page = _parse_prev_page(d.pop("prev_page"))

        total_count = d.pop("total_count")

        total_pages = d.pop("total_pages")

        meta = cls(
            current_page=current_page,
            next_page=next_page,
            prev_page=prev_page,
            total_count=total_count,
            total_pages=total_pages,
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
