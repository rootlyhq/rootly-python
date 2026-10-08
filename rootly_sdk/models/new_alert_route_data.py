from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_alert_route_data_type import NewAlertRouteDataType, check_new_alert_route_data_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_alert_route_data_attributes import NewAlertRouteDataAttributes


T = TypeVar("T", bound="NewAlertRouteData")


@_attrs_define
class NewAlertRouteData:
    """
    Attributes:
        type_ (NewAlertRouteDataType | Unset):
        attributes (NewAlertRouteDataAttributes | Unset):
    """

    type_: NewAlertRouteDataType | Unset = UNSET
    attributes: NewAlertRouteDataAttributes | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_alert_route_data_attributes import NewAlertRouteDataAttributes

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: NewAlertRouteDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_new_alert_route_data_type(_type_)

        _attributes = d.pop("attributes", UNSET)
        attributes: NewAlertRouteDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = NewAlertRouteDataAttributes.from_dict(_attributes)

        new_alert_route_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return new_alert_route_data
