from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_edge_connector_body_data import UpdateEdgeConnectorBodyData


T = TypeVar("T", bound="UpdateEdgeConnectorBody")


@_attrs_define
class UpdateEdgeConnectorBody:
    """
    Attributes:
        data (Union[Unset, UpdateEdgeConnectorBodyData]):
    """

    data: Union[Unset, "UpdateEdgeConnectorBodyData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, dict[str, Any]] = UNSET
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
        from ..models.update_edge_connector_body_data import UpdateEdgeConnectorBodyData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Union[Unset, UpdateEdgeConnectorBodyData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = UpdateEdgeConnectorBodyData.from_dict(_data)

        update_edge_connector_body = cls(
            data=data,
        )

        update_edge_connector_body.additional_properties = d
        return update_edge_connector_body

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
