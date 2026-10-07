from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_alert_field_data import UpdateAlertFieldData


T = TypeVar("T", bound="UpdateAlertField")


@_attrs_define
class UpdateAlertField:
    """
    Attributes:
        data (UpdateAlertFieldData):
    """

    data: UpdateAlertFieldData

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
        from ..models.update_alert_field_data import UpdateAlertFieldData

        d = dict(src_dict)
        data = UpdateAlertFieldData.from_dict(d.pop("data"))

        update_alert_field = cls(
            data=data,
        )

        return update_alert_field
