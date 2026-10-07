from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

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
        description (None | str | Unset): Connector description
        status (NewEdgeConnectorEdgeConnectorStatus | Unset): Connector status
        subscriptions (list[str] | Unset): Array of event types to subscribe to
        owner_group_ids (list[UUID] | Unset): IDs of the teams (groups) that own this connector. Required when the
            caller is a team admin without tenant-wide edge connector permissions
    """

    name: str
    description: None | str | Unset = UNSET
    status: NewEdgeConnectorEdgeConnectorStatus | Unset = UNSET
    subscriptions: list[str] | Unset = UNSET
    owner_group_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        subscriptions: list[str] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = self.subscriptions

        owner_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.owner_group_ids, Unset):
            owner_group_ids = []
            for owner_group_ids_item_data in self.owner_group_ids:
                owner_group_ids_item = str(owner_group_ids_item_data)
                owner_group_ids.append(owner_group_ids_item)

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
        if owner_group_ids is not UNSET:
            field_dict["owner_group_ids"] = owner_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _status = d.pop("status", UNSET)
        status: NewEdgeConnectorEdgeConnectorStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_new_edge_connector_edge_connector_status(_status)

        subscriptions = cast(list[str], d.pop("subscriptions", UNSET))

        _owner_group_ids = d.pop("owner_group_ids", UNSET)
        owner_group_ids: list[UUID] | Unset = UNSET
        if _owner_group_ids is not UNSET:
            owner_group_ids = []
            for owner_group_ids_item_data in _owner_group_ids:
                owner_group_ids_item = UUID(owner_group_ids_item_data)

                owner_group_ids.append(owner_group_ids_item)

        new_edge_connector_edge_connector = cls(
            name=name,
            description=description,
            status=status,
            subscriptions=subscriptions,
            owner_group_ids=owner_group_ids,
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
