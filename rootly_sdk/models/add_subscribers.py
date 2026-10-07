from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.add_subscribers_data import AddSubscribersData


T = TypeVar("T", bound="AddSubscribers")


@_attrs_define
class AddSubscribers:
    """
    Attributes:
        data (AddSubscribersData):
    """

    data: AddSubscribersData

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_subscribers_data import AddSubscribersData

        d = dict(src_dict)
        data = AddSubscribersData.from_dict(d.pop("data"))

        add_subscribers = cls(
            data=data,
        )

        return add_subscribers
