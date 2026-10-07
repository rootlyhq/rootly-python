from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_dashboard_panel_data_type import NewDashboardPanelDataType, check_new_dashboard_panel_data_type

if TYPE_CHECKING:
    from ..models.new_dashboard_panel_data_attributes import NewDashboardPanelDataAttributes


T = TypeVar("T", bound="NewDashboardPanelData")


@_attrs_define
class NewDashboardPanelData:
    """
    Attributes:
        type_ (NewDashboardPanelDataType):
        attributes (NewDashboardPanelDataAttributes):
    """

    type_: NewDashboardPanelDataType
    attributes: NewDashboardPanelDataAttributes

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_dashboard_panel_data_attributes import NewDashboardPanelDataAttributes

        d = dict(src_dict)
        type_ = check_new_dashboard_panel_data_type(d.pop("type"))

        attributes = NewDashboardPanelDataAttributes.from_dict(d.pop("attributes"))

        new_dashboard_panel_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return new_dashboard_panel_data
