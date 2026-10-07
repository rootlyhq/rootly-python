from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.snooze_alert_data import SnoozeAlertData


T = TypeVar("T", bound="SnoozeAlert")


@_attrs_define
class SnoozeAlert:
    """
    Attributes:
        data (SnoozeAlertData):
    """

    data: SnoozeAlertData

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
        from ..models.snooze_alert_data import SnoozeAlertData

        d = dict(src_dict)
        data = SnoozeAlertData.from_dict(d.pop("data"))

        snooze_alert = cls(
            data=data,
        )

        return snooze_alert
