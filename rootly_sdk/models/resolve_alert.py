from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resolve_alert_data import ResolveAlertData


T = TypeVar("T", bound="ResolveAlert")


@_attrs_define
class ResolveAlert:
    """
    Attributes:
        data (ResolveAlertData | Unset):
    """

    data: ResolveAlertData | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resolve_alert_data import ResolveAlertData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: ResolveAlertData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ResolveAlertData.from_dict(_data)

        resolve_alert = cls(
            data=data,
        )

        return resolve_alert
