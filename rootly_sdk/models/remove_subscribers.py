from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.remove_subscribers_data import RemoveSubscribersData


T = TypeVar("T", bound="RemoveSubscribers")


@_attrs_define
class RemoveSubscribers:
    """
    Attributes:
        data (RemoveSubscribersData):
    """

    data: RemoveSubscribersData

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
        from ..models.remove_subscribers_data import RemoveSubscribersData

        d = dict(src_dict)
        data = RemoveSubscribersData.from_dict(d.pop("data"))

        remove_subscribers = cls(
            data=data,
        )

        return remove_subscribers
