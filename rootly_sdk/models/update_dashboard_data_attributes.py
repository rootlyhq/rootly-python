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
        name (Union[Unset, str]): The name of the dashboard
        description (Union[None, Unset, str]): The description of the dashboard
        owner (Union[Unset, UpdateDashboardDataAttributesOwner]): The owner type of the dashboard
        public (Union[Unset, bool]): Whether the dashboard is public
        range_ (Union[None, Unset, str]): The date range for dashboard panel data
        auto_refresh (Union[Unset, bool]): Whether the dashboard auto-updates the UI with new data.
        color (Union[Unset, UpdateDashboardDataAttributesColor]): The hex color of the dashboard
        icon (Union[Unset, str]): The emoji icon of the dashboard
        period (Union[Unset, UpdateDashboardDataAttributesPeriod]): The grouping period for dashboard panel data
    """

    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    owner: Unset | UpdateDashboardDataAttributesOwner = UNSET
    public: Unset | bool = UNSET
    range_: None | Unset | str = UNSET
    auto_refresh: Unset | bool = UNSET
    color: Unset | UpdateDashboardDataAttributesColor = UNSET
    icon: Unset | str = UNSET
    period: Unset | UpdateDashboardDataAttributesPeriod = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        owner: Unset | str = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner

        public = self.public

        range_: None | Unset | str
        if isinstance(self.range_, Unset):
            range_ = UNSET
        else:
            range_ = self.range_

        auto_refresh = self.auto_refresh

        color: Unset | str = UNSET
        if not isinstance(self.color, Unset):
            color = self.color

        icon = self.icon

        period: Unset | str = UNSET
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

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        _owner = d.pop("owner", UNSET)
        owner: Unset | UpdateDashboardDataAttributesOwner
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = check_update_dashboard_data_attributes_owner(_owner)

        public = d.pop("public", UNSET)

        def _parse_range_(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        range_ = _parse_range_(d.pop("range", UNSET))

        auto_refresh = d.pop("auto_refresh", UNSET)

        _color = d.pop("color", UNSET)
        color: Unset | UpdateDashboardDataAttributesColor
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = check_update_dashboard_data_attributes_color(_color)

        icon = d.pop("icon", UNSET)

        _period = d.pop("period", UNSET)
        period: Unset | UpdateDashboardDataAttributesPeriod
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
