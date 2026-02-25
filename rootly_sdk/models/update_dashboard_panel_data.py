from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_dashboard_panel_data_type import (
    UpdateDashboardPanelDataType,
    check_update_dashboard_panel_data_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_dashboard_panel_data_attributes import UpdateDashboardPanelDataAttributes


T = TypeVar("T", bound="UpdateDashboardPanelData")


@_attrs_define
class UpdateDashboardPanelData:
    """
    Attributes:
        type_ (Union[Unset, UpdateDashboardPanelDataType]):
        attributes (Union[Unset, UpdateDashboardPanelDataAttributes]):
    """

    type_: Unset | UpdateDashboardPanelDataType = UNSET
    attributes: Union[Unset, "UpdateDashboardPanelDataAttributes"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Unset | str = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        attributes: Unset | dict[str, Any] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_dashboard_panel_data_attributes import UpdateDashboardPanelDataAttributes

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Unset | UpdateDashboardPanelDataType
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_update_dashboard_panel_data_type(_type_)

        _attributes = d.pop("attributes", UNSET)
        attributes: Unset | UpdateDashboardPanelDataAttributes
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = UpdateDashboardPanelDataAttributes.from_dict(_attributes)

        update_dashboard_panel_data = cls(
            type_=type_,
            attributes=attributes,
        )

        update_dashboard_panel_data.additional_properties = d
        return update_dashboard_panel_data

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
