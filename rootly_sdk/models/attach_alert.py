from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.attach_alert_data import AttachAlertData


T = TypeVar("T", bound="AttachAlert")


@_attrs_define
class AttachAlert:
    """
    Attributes:
        data (AttachAlertData):
    """

    data: AttachAlertData

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
        from ..models.attach_alert_data import AttachAlertData

        d = dict(src_dict)
        data = AttachAlertData.from_dict(d.pop("data"))

        attach_alert = cls(
            data=data,
        )

        return attach_alert
