from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_on_call_shadow_data import UpdateOnCallShadowData


T = TypeVar("T", bound="UpdateOnCallShadow")


@_attrs_define
class UpdateOnCallShadow:
    """
    Attributes:
        data (UpdateOnCallShadowData):
    """

    data: UpdateOnCallShadowData

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
        from ..models.update_on_call_shadow_data import UpdateOnCallShadowData

        d = dict(src_dict)
        data = UpdateOnCallShadowData.from_dict(d.pop("data"))

        update_on_call_shadow = cls(
            data=data,
        )

        return update_on_call_shadow
