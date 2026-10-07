from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.patch_alert_route_data import PatchAlertRouteData


T = TypeVar("T", bound="PatchAlertRoute")


@_attrs_define
class PatchAlertRoute:
    """
    Attributes:
        data (PatchAlertRouteData):
    """

    data: PatchAlertRouteData

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
        from ..models.patch_alert_route_data import PatchAlertRouteData

        d = dict(src_dict)
        data = PatchAlertRouteData.from_dict(d.pop("data"))

        patch_alert_route = cls(
            data=data,
        )

        return patch_alert_route
