from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_edge_connector_edge_connector_status import (
    NewEdgeConnectorEdgeConnectorStatus,
    check_new_edge_connector_edge_connector_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewEdgeConnectorEdgeConnector")


@_attrs_define
class NewEdgeConnectorEdgeConnector:
    """
    Attributes:
        name (str): Connector name
        description (Union[None, Unset, str]): Connector description
        status (Union[Unset, NewEdgeConnectorEdgeConnectorStatus]): Connector status
        subscriptions (Union[Unset, list[str]]): Array of event types to subscribe to
    """

    name: str
    description: Union[None, Unset, str] = UNSET
    status: Union[Unset, NewEdgeConnectorEdgeConnectorStatus] = UNSET
    subscriptions: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        subscriptions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = self.subscriptions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
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
        name = d.pop("name")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, NewEdgeConnectorEdgeConnectorStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_new_edge_connector_edge_connector_status(_status)

        subscriptions = cast(list[str], d.pop("subscriptions", UNSET))

        new_edge_connector_edge_connector = cls(
            name=name,
            description=description,
            status=status,
            subscriptions=subscriptions,
        )

        new_edge_connector_edge_connector.additional_properties = d
        return new_edge_connector_edge_connector

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
