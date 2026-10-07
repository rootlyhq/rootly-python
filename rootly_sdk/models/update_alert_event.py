from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_alert_event_data import UpdateAlertEventData


T = TypeVar("T", bound="UpdateAlertEvent")


@_attrs_define
class UpdateAlertEvent:
    """Update an alert event. Note: Only alert events with kind='note' can be updated. You cannot change the kind field.

    Attributes:
        data (UpdateAlertEventData):
    """

    data: UpdateAlertEventData

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
        from ..models.update_alert_event_data import UpdateAlertEventData

        d = dict(src_dict)
        data = UpdateAlertEventData.from_dict(d.pop("data"))

        update_alert_event = cls(
            data=data,
        )

        return update_alert_event
