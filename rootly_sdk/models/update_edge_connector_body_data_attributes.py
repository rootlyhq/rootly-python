from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_edge_connector_body_data_attributes_status import (
    UpdateEdgeConnectorBodyDataAttributesStatus,
    check_update_edge_connector_body_data_attributes_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateEdgeConnectorBodyDataAttributes")


@_attrs_define
class UpdateEdgeConnectorBodyDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        status (Union[Unset, UpdateEdgeConnectorBodyDataAttributesStatus]):
        subscriptions (Union[Unset, list[str]]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    status: Union[Unset, UpdateEdgeConnectorBodyDataAttributesStatus] = UNSET
    subscriptions: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        subscriptions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = self.subscriptions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, UpdateEdgeConnectorBodyDataAttributesStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_edge_connector_body_data_attributes_status(_status)

        subscriptions = cast(list[str], d.pop("subscriptions", UNSET))

        update_edge_connector_body_data_attributes = cls(
            name=name,
            description=description,
            status=status,
            subscriptions=subscriptions,
        )

        update_edge_connector_body_data_attributes.additional_properties = d
        return update_edge_connector_body_data_attributes

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
