from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Links")


@_attrs_define
class Links:
    """
    Attributes:
        self_ (str):
        first (str):
        prev (Union[None, str]):
        next_ (Union[None, str]):
        last (str):
    """

    self_: str
    first: str
    prev: None | str
    next_: None | str
    last: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_

        first = self.first

        prev: None | str
        prev = self.prev

        next_: None | str
        next_ = self.next_

        last = self.last

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "first": first,
                "prev": prev,
                "next": next_,
                "last": last,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        self_ = d.pop("self")

        first = d.pop("first")

        def _parse_prev(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        prev = _parse_prev(d.pop("prev"))

        def _parse_next_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_ = _parse_next_(d.pop("next"))

        last = d.pop("last")

        links = cls(
            self_=self_,
            first=first,
            prev=prev,
            next_=next_,
            last=last,
        )

        links.additional_properties = d
        return links

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
