from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acknowledge_alert_data import AcknowledgeAlertData


T = TypeVar("T", bound="AcknowledgeAlert")


@_attrs_define
class AcknowledgeAlert:
    """
    Attributes:
        data (AcknowledgeAlertData | Unset):
    """

    data: AcknowledgeAlertData | Unset = UNSET

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
        from ..models.acknowledge_alert_data import AcknowledgeAlertData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: AcknowledgeAlertData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = AcknowledgeAlertData.from_dict(_data)

        acknowledge_alert = cls(
            data=data,
        )

        return acknowledge_alert
