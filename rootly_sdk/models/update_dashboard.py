from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_dashboard_data import UpdateDashboardData


T = TypeVar("T", bound="UpdateDashboard")


@_attrs_define
class UpdateDashboard:
    """
    Attributes:
        data (UpdateDashboardData):
    """

    data: UpdateDashboardData

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
        from ..models.update_dashboard_data import UpdateDashboardData

        d = dict(src_dict)
        data = UpdateDashboardData.from_dict(d.pop("data"))

        update_dashboard = cls(
            data=data,
        )

        return update_dashboard
