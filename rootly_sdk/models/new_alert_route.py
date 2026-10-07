from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_alert_route_data import NewAlertRouteData


T = TypeVar("T", bound="NewAlertRoute")


@_attrs_define
class NewAlertRoute:
    """
    Attributes:
        data (NewAlertRouteData | Unset):
    """

    data: NewAlertRouteData | Unset = UNSET

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
        from ..models.new_alert_route_data import NewAlertRouteData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: NewAlertRouteData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = NewAlertRouteData.from_dict(_data)

        new_alert_route = cls(
            data=data,
        )

        return new_alert_route
