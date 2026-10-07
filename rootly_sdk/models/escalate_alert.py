from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalate_alert_data import EscalateAlertData


T = TypeVar("T", bound="EscalateAlert")


@_attrs_define
class EscalateAlert:
    """
    Attributes:
        data (EscalateAlertData | Unset):
    """

    data: EscalateAlertData | Unset = UNSET

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
        from ..models.escalate_alert_data import EscalateAlertData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: EscalateAlertData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = EscalateAlertData.from_dict(_data)

        escalate_alert = cls(
            data=data,
        )

        return escalate_alert
