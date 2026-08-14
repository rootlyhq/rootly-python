from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_alert_route_response_200_data import DeleteAlertRouteResponse200Data


T = TypeVar("T", bound="DeleteAlertRouteResponse200")


@_attrs_define
class DeleteAlertRouteResponse200:
    """
    Attributes:
        data (Union[Unset, DeleteAlertRouteResponse200Data]):
    """

    data: Union[Unset, "DeleteAlertRouteResponse200Data"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Unset | dict[str, Any] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_alert_route_response_200_data import DeleteAlertRouteResponse200Data

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Unset | DeleteAlertRouteResponse200Data
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = DeleteAlertRouteResponse200Data.from_dict(_data)

        delete_alert_route_response_200 = cls(
            data=data,
        )

        delete_alert_route_response_200.additional_properties = d
        return delete_alert_route_response_200

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
