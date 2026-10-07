from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_alert_urgency_data import NewAlertUrgencyData


T = TypeVar("T", bound="NewAlertUrgency")


@_attrs_define
class NewAlertUrgency:
    """
    Attributes:
        data (NewAlertUrgencyData):
    """

    data: NewAlertUrgencyData

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
        from ..models.new_alert_urgency_data import NewAlertUrgencyData

        d = dict(src_dict)
        data = NewAlertUrgencyData.from_dict(d.pop("data"))

        new_alert_urgency = cls(
            data=data,
        )

        return new_alert_urgency
