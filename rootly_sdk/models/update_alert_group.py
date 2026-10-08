from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_alert_group_data import UpdateAlertGroupData


T = TypeVar("T", bound="UpdateAlertGroup")


@_attrs_define
class UpdateAlertGroup:
    """
    Attributes:
        data (UpdateAlertGroupData):
    """

    data: UpdateAlertGroupData

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
        from ..models.update_alert_group_data import UpdateAlertGroupData

        d = dict(src_dict)
        data = UpdateAlertGroupData.from_dict(d.pop("data"))

        update_alert_group = cls(
            data=data,
        )

        return update_alert_group
