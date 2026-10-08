from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.update_dashboard_data_type import UpdateDashboardDataType, check_update_dashboard_data_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_dashboard_data_attributes import UpdateDashboardDataAttributes


T = TypeVar("T", bound="UpdateDashboardData")


@_attrs_define
class UpdateDashboardData:
    """
    Attributes:
        id (str | Unset): Accepted for JSON:API client compatibility, but ignored. The resource to update is identified
            by the id in the path.
        type_ (UpdateDashboardDataType | Unset):
        attributes (UpdateDashboardDataAttributes | Unset):
    """

    id: str | Unset = UNSET
    type_: UpdateDashboardDataType | Unset = UNSET
    attributes: UpdateDashboardDataAttributes | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_dashboard_data_attributes import UpdateDashboardDataAttributes

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: UpdateDashboardDataType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_update_dashboard_data_type(_type_)

        _attributes = d.pop("attributes", UNSET)
        attributes: UpdateDashboardDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = UpdateDashboardDataAttributes.from_dict(_attributes)

        update_dashboard_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        return update_dashboard_data
