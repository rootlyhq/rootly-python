from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SnoozeAlertDataAttributes")


@_attrs_define
class SnoozeAlertDataAttributes:
    """
    Attributes:
        delay_minutes (int): Number of minutes to snooze the alert for
    """

    delay_minutes: int

    def to_dict(self) -> dict[str, Any]:
        delay_minutes = self.delay_minutes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "delay_minutes": delay_minutes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delay_minutes = d.pop("delay_minutes")

        snooze_alert_data_attributes = cls(
            delay_minutes=delay_minutes,
        )

        return snooze_alert_data_attributes
