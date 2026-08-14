from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_panel_data_item import DashboardPanelDataItem
    from ..models.dashboard_panel_params import DashboardPanelParams
    from ..models.dashboard_panel_position_type_0 import DashboardPanelPositionType0


T = TypeVar("T", bound="DashboardPanel")


@_attrs_define
class DashboardPanel:
    """
    Attributes:
        params (DashboardPanelParams):
        dashboard_id (Union[Unset, str]): The panel dashboard
        name (Union[None, Unset, str]): The name of the dashboard_panel
        position (Union['DashboardPanelPositionType0', None, Unset]):
        data (Union[Unset, list['DashboardPanelDataItem']]):
    """

    params: "DashboardPanelParams"
    dashboard_id: Unset | str = UNSET
    name: None | Unset | str = UNSET
    position: Union["DashboardPanelPositionType0", None, Unset] = UNSET
    data: Unset | list["DashboardPanelDataItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_panel_position_type_0 import DashboardPanelPositionType0

        params = self.params.to_dict()

        dashboard_id = self.dashboard_id

        name: None | Unset | str
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        position: None | Unset | dict[str, Any]
        if isinstance(self.position, Unset):
            position = UNSET
        elif isinstance(self.position, DashboardPanelPositionType0):
            position = self.position.to_dict()
        else:
            position = self.position

        data: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "params": params,
            }
        )
        if dashboard_id is not UNSET:
            field_dict["dashboard_id"] = dashboard_id
        if name is not UNSET:
            field_dict["name"] = name
        if position is not UNSET:
            field_dict["position"] = position
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_panel_data_item import DashboardPanelDataItem
        from ..models.dashboard_panel_params import DashboardPanelParams
        from ..models.dashboard_panel_position_type_0 import DashboardPanelPositionType0

        d = dict(src_dict)
        params = DashboardPanelParams.from_dict(d.pop("params"))

        dashboard_id = d.pop("dashboard_id", UNSET)

        def _parse_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_position(data: object) -> Union["DashboardPanelPositionType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                position_type_0 = DashboardPanelPositionType0.from_dict(data)

                return position_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DashboardPanelPositionType0", None, Unset], data)

        position = _parse_position(d.pop("position", UNSET))

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = DashboardPanelDataItem.from_dict(data_item_data)

            data.append(data_item)

        dashboard_panel = cls(
            params=params,
            dashboard_id=dashboard_id,
            name=name,
            position=position,
            data=data,
        )

        dashboard_panel.additional_properties = d
        return dashboard_panel

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
