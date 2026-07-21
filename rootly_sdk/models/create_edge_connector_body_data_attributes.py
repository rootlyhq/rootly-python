from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_edge_connector_body_data_attributes_status import (
    CreateEdgeConnectorBodyDataAttributesStatus,
    check_create_edge_connector_body_data_attributes_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_edge_connector_body_data_attributes_filters import CreateEdgeConnectorBodyDataAttributesFilters


T = TypeVar("T", bound="CreateEdgeConnectorBodyDataAttributes")


@_attrs_define
class CreateEdgeConnectorBodyDataAttributes:
    """
    Attributes:
        name (str): Connector name
        description (str | Unset): Connector description
        status (CreateEdgeConnectorBodyDataAttributesStatus | Unset): Connector status
        subscriptions (list[str] | Unset): Array of event types to subscribe to
        filters (CreateEdgeConnectorBodyDataAttributesFilters | Unset): Event filters. OR within dimension, AND across
            dimensions.
    """

    name: str
    description: str | Unset = UNSET
    status: CreateEdgeConnectorBodyDataAttributesStatus | Unset = UNSET
    subscriptions: list[str] | Unset = UNSET
    filters: CreateEdgeConnectorBodyDataAttributesFilters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        name = self.name

        description = self.description

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        subscriptions: list[str] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = self.subscriptions

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

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
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_edge_connector_body_data_attributes_filters import (
            CreateEdgeConnectorBodyDataAttributesFilters,
        )

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _status = d.pop("status", UNSET)
        status: CreateEdgeConnectorBodyDataAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_create_edge_connector_body_data_attributes_status(_status)

        subscriptions = cast(list[str], d.pop("subscriptions", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: CreateEdgeConnectorBodyDataAttributesFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = CreateEdgeConnectorBodyDataAttributesFilters.from_dict(_filters)

        create_edge_connector_body_data_attributes = cls(
            name=name,
            description=description,
            status=status,
            subscriptions=subscriptions,
            filters=filters,
        )

        create_edge_connector_body_data_attributes.additional_properties = d
        return create_edge_connector_body_data_attributes

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
