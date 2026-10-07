from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_dashboard_data_attributes_color import (
    UpdateDashboardDataAttributesColor,
    check_update_dashboard_data_attributes_color,
)
from ..models.update_dashboard_data_attributes_owner import (
    UpdateDashboardDataAttributesOwner,
    check_update_dashboard_data_attributes_owner,
)
from ..models.update_dashboard_data_attributes_period import (
    UpdateDashboardDataAttributesPeriod,
    check_update_dashboard_data_attributes_period,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateDashboardDataAttributes")


@_attrs_define
class UpdateDashboardDataAttributes:
    """
    Attributes:
        name (str | Unset): The name of the dashboard
        description (None | str | Unset): The description of the dashboard
        owner (UpdateDashboardDataAttributesOwner | Unset): The owner type of the dashboard
        public (bool | Unset): Whether the dashboard is public
        range_ (None | str | Unset): The date range for dashboard panel data
        auto_refresh (bool | Unset): Whether the dashboard auto-updates the UI with new data.
        color (UpdateDashboardDataAttributesColor | Unset): The hex color of the dashboard
        icon (str | Unset): The emoji icon of the dashboard
        period (UpdateDashboardDataAttributesPeriod | Unset): The grouping period for dashboard panel data
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    owner: UpdateDashboardDataAttributesOwner | Unset = UNSET
    public: bool | Unset = UNSET
    range_: None | str | Unset = UNSET
    auto_refresh: bool | Unset = UNSET
    color: UpdateDashboardDataAttributesColor | Unset = UNSET
    icon: str | Unset = UNSET
    period: UpdateDashboardDataAttributesPeriod | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        owner: str | Unset = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner

        public = self.public

        range_: None | str | Unset
        if isinstance(self.range_, Unset):
            range_ = UNSET
        else:
            range_ = self.range_

        auto_refresh = self.auto_refresh

        color: str | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color

        icon = self.icon

        period: str | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if owner is not UNSET:
            field_dict["owner"] = owner
        if public is not UNSET:
            field_dict["public"] = public
        if range_ is not UNSET:
            field_dict["range"] = range_
        if auto_refresh is not UNSET:
            field_dict["auto_refresh"] = auto_refresh
        if color is not UNSET:
            field_dict["color"] = color
        if icon is not UNSET:
            field_dict["icon"] = icon
        if period is not UNSET:
            field_dict["period"] = period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _owner = d.pop("owner", UNSET)
        owner: UpdateDashboardDataAttributesOwner | Unset
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = check_update_dashboard_data_attributes_owner(_owner)

        public = d.pop("public", UNSET)

        def _parse_range_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        range_ = _parse_range_(d.pop("range", UNSET))

        auto_refresh = d.pop("auto_refresh", UNSET)

        _color = d.pop("color", UNSET)
        color: UpdateDashboardDataAttributesColor | Unset
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = check_update_dashboard_data_attributes_color(_color)

        icon = d.pop("icon", UNSET)

        _period = d.pop("period", UNSET)
        period: UpdateDashboardDataAttributesPeriod | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = check_update_dashboard_data_attributes_period(_period)

        update_dashboard_data_attributes = cls(
            name=name,
            description=description,
            owner=owner,
            public=public,
            range_=range_,
            auto_refresh=auto_refresh,
            color=color,
            icon=icon,
            period=period,
        )

        return update_dashboard_data_attributes
