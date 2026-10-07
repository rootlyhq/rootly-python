from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_dashboard_panel_data import NewDashboardPanelData


T = TypeVar("T", bound="NewDashboardPanel")


@_attrs_define
class NewDashboardPanel:
    """
    Attributes:
        data (NewDashboardPanelData):
    """

    data: NewDashboardPanelData

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
        from ..models.new_dashboard_panel_data import NewDashboardPanelData

        d = dict(src_dict)
        data = NewDashboardPanelData.from_dict(d.pop("data"))

        new_dashboard_panel = cls(
            data=data,
        )

        return new_dashboard_panel
