from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_on_call_shadow_data import NewOnCallShadowData


T = TypeVar("T", bound="NewOnCallShadow")


@_attrs_define
class NewOnCallShadow:
    """
    Attributes:
        data (NewOnCallShadowData):
    """

    data: NewOnCallShadowData

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
        from ..models.new_on_call_shadow_data import NewOnCallShadowData

        d = dict(src_dict)
        data = NewOnCallShadowData.from_dict(d.pop("data"))

        new_on_call_shadow = cls(
            data=data,
        )

        return new_on_call_shadow
