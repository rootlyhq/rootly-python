from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_live_call_router_data import NewLiveCallRouterData


T = TypeVar("T", bound="NewLiveCallRouter")


@_attrs_define
class NewLiveCallRouter:
    """
    Attributes:
        data (NewLiveCallRouterData):
    """

    data: NewLiveCallRouterData

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
        from ..models.new_live_call_router_data import NewLiveCallRouterData

        d = dict(src_dict)
        data = NewLiveCallRouterData.from_dict(d.pop("data"))

        new_live_call_router = cls(
            data=data,
        )

        return new_live_call_router
