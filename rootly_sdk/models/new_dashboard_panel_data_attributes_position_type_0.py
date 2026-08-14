from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NewDashboardPanelDataAttributesPositionType0")


@_attrs_define
class NewDashboardPanelDataAttributesPositionType0:
    """
    Attributes:
        x (float):
        y (float):
        w (float):
        h (float):
    """

    x: float
    y: float
    w: float
    h: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        x = self.x

        y = self.y

        w = self.w

        h = self.h

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "x": x,
                "y": y,
                "w": w,
                "h": h,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        x = d.pop("x")

        y = d.pop("y")

        w = d.pop("w")

        h = d.pop("h")

        new_dashboard_panel_data_attributes_position_type_0 = cls(
            x=x,
            y=y,
            w=w,
            h=h,
        )

        new_dashboard_panel_data_attributes_position_type_0.additional_properties = d
        return new_dashboard_panel_data_attributes_position_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
