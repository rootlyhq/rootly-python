from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_dashboard_panel_data_attributes_params import NewDashboardPanelDataAttributesParams
    from ..models.new_dashboard_panel_data_attributes_position_type_0 import (
        NewDashboardPanelDataAttributesPositionType0,
    )


T = TypeVar("T", bound="NewDashboardPanelDataAttributes")


@_attrs_define
class NewDashboardPanelDataAttributes:
    """
    Attributes:
        params (NewDashboardPanelDataAttributesParams):
        name (Union[None, Unset, str]): The name of the dashboard_panel
        position (Union['NewDashboardPanelDataAttributesPositionType0', None, Unset]):
    """

    params: "NewDashboardPanelDataAttributesParams"
    name: None | Unset | str = UNSET
    position: Union["NewDashboardPanelDataAttributesPositionType0", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_dashboard_panel_data_attributes_position_type_0 import (
            NewDashboardPanelDataAttributesPositionType0,
        )

        params = self.params.to_dict()

        name: None | Unset | str
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        position: None | Unset | dict[str, Any]
        if isinstance(self.position, Unset):
            position = UNSET
        elif isinstance(self.position, NewDashboardPanelDataAttributesPositionType0):
            position = self.position.to_dict()
        else:
            position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "params": params,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_dashboard_panel_data_attributes_params import NewDashboardPanelDataAttributesParams
        from ..models.new_dashboard_panel_data_attributes_position_type_0 import (
            NewDashboardPanelDataAttributesPositionType0,
        )

        d = dict(src_dict)
        params = NewDashboardPanelDataAttributesParams.from_dict(d.pop("params"))

        def _parse_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_position(data: object) -> Union["NewDashboardPanelDataAttributesPositionType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                position_type_0 = NewDashboardPanelDataAttributesPositionType0.from_dict(data)

                return position_type_0
            except:  # noqa: E722
                pass
            return cast(Union["NewDashboardPanelDataAttributesPositionType0", None, Unset], data)

        position = _parse_position(d.pop("position", UNSET))

        new_dashboard_panel_data_attributes = cls(
            params=params,
            name=name,
            position=position,
        )

        return new_dashboard_panel_data_attributes
