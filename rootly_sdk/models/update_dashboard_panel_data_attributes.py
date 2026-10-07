from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_dashboard_panel_data_attributes_params import UpdateDashboardPanelDataAttributesParams
    from ..models.update_dashboard_panel_data_attributes_position_type_0 import (
        UpdateDashboardPanelDataAttributesPositionType0,
    )


T = TypeVar("T", bound="UpdateDashboardPanelDataAttributes")


@_attrs_define
class UpdateDashboardPanelDataAttributes:
    """
    Attributes:
        name (None | str | Unset): The name of the dashboard_panel
        params (UpdateDashboardPanelDataAttributesParams | Unset):
        position (None | Unset | UpdateDashboardPanelDataAttributesPositionType0):
    """

    name: None | str | Unset = UNSET
    params: UpdateDashboardPanelDataAttributesParams | Unset = UNSET
    position: None | Unset | UpdateDashboardPanelDataAttributesPositionType0 = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_dashboard_panel_data_attributes_position_type_0 import (
            UpdateDashboardPanelDataAttributesPositionType0,
        )

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        position: dict[str, Any] | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        elif isinstance(self.position, UpdateDashboardPanelDataAttributesPositionType0):
            position = self.position.to_dict()
        else:
            position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if params is not UNSET:
            field_dict["params"] = params
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_dashboard_panel_data_attributes_params import UpdateDashboardPanelDataAttributesParams
        from ..models.update_dashboard_panel_data_attributes_position_type_0 import (
            UpdateDashboardPanelDataAttributesPositionType0,
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _params = d.pop("params", UNSET)
        params: UpdateDashboardPanelDataAttributesParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = UpdateDashboardPanelDataAttributesParams.from_dict(_params)

        def _parse_position(data: object) -> None | Unset | UpdateDashboardPanelDataAttributesPositionType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                position_type_0 = UpdateDashboardPanelDataAttributesPositionType0.from_dict(data)

                return position_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateDashboardPanelDataAttributesPositionType0, data)

        position = _parse_position(d.pop("position", UNSET))

        update_dashboard_panel_data_attributes = cls(
            name=name,
            params=params,
            position=position,
        )

        return update_dashboard_panel_data_attributes
