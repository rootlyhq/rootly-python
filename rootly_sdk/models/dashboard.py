from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dashboard_color import DashboardColor, check_dashboard_color
from ..models.dashboard_owner import DashboardOwner, check_dashboard_owner
from ..types import UNSET, Unset

T = TypeVar("T", bound="Dashboard")


@_attrs_define
class Dashboard:
    """
    Attributes:
        name (str): The name of the dashboard
        owner (DashboardOwner): The owner type of the dashboard
        public (bool): Whether the dashboard is public
        team_id (int | Unset): The dashboard team
        user_id (int | None | Unset): The dashboard user owner if owner is of type user
        description (None | str | Unset): The description of the dashboard
        range_ (None | str | Unset): The date range for dashboard panel data
        period (None | str | Unset): The grouping period for dashboard panel data
        auto_refresh (bool | Unset): Whether the dashboard auto-updates the UI with new data.
        color (DashboardColor | Unset): The hex color of the dashboard
        icon (str | Unset): The emoji icon of the dashboard
        created_at (str | Unset): Date of creation
        updated_at (str | Unset): Date of last update
    """

    name: str
    owner: DashboardOwner
    public: bool
    team_id: int | Unset = UNSET
    user_id: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    range_: None | str | Unset = UNSET
    period: None | str | Unset = UNSET
    auto_refresh: bool | Unset = UNSET
    color: DashboardColor | Unset = UNSET
    icon: str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        owner: str = self.owner

        public = self.public

        team_id = self.team_id

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        range_: None | str | Unset
        if isinstance(self.range_, Unset):
            range_ = UNSET
        else:
            range_ = self.range_

        period: None | str | Unset
        if isinstance(self.period, Unset):
            period = UNSET
        else:
            period = self.period

        auto_refresh = self.auto_refresh

        color: str | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color

        icon = self.icon

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "owner": owner,
                "public": public,
            }
        )
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if description is not UNSET:
            field_dict["description"] = description
        if range_ is not UNSET:
            field_dict["range"] = range_
        if period is not UNSET:
            field_dict["period"] = period
        if auto_refresh is not UNSET:
            field_dict["auto_refresh"] = auto_refresh
        if color is not UNSET:
            field_dict["color"] = color
        if icon is not UNSET:
            field_dict["icon"] = icon
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        owner = check_dashboard_owner(d.pop("owner"))

        public = d.pop("public")

        team_id = d.pop("team_id", UNSET)

        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_range_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        range_ = _parse_range_(d.pop("range", UNSET))

        def _parse_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        period = _parse_period(d.pop("period", UNSET))

        auto_refresh = d.pop("auto_refresh", UNSET)

        _color = d.pop("color", UNSET)
        color: DashboardColor | Unset
        if isinstance(_color, Unset):
            color = UNSET
        else:
            color = check_dashboard_color(_color)

        icon = d.pop("icon", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        dashboard = cls(
            name=name,
            owner=owner,
            public=public,
            team_id=team_id,
            user_id=user_id,
            description=description,
            range_=range_,
            period=period,
            auto_refresh=auto_refresh,
            color=color,
            icon=icon,
            created_at=created_at,
            updated_at=updated_at,
        )

        dashboard.additional_properties = d
        return dashboard

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
