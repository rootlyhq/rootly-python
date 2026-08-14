import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.edge_connector_data_attributes_status import (
    EdgeConnectorDataAttributesStatus,
    check_edge_connector_data_attributes_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EdgeConnectorDataAttributes")


@_attrs_define
class EdgeConnectorDataAttributes:
    """
    Attributes:
        name (str): Connector name
        status (EdgeConnectorDataAttributesStatus): Connector status
        description (Union[None, Unset, str]): Connector description
        subscriptions (Union[Unset, list[str]]): Array of event types to subscribe to
        last_poll_at (Union[None, Unset, datetime.datetime]): Last time connector polled
        online (Union[Unset, bool]): Whether connector is currently online
        deliveries_count (Union[Unset, int]): Total number of deliveries
        deliveries_queued_count (Union[Unset, int]): Number of queued deliveries
        deliveries_running_count (Union[Unset, int]): Number of running deliveries
        deliveries_completed_count (Union[Unset, int]): Number of completed deliveries
        deliveries_failed_count (Union[Unset, int]): Number of failed deliveries
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    name: str
    status: EdgeConnectorDataAttributesStatus
    description: None | Unset | str = UNSET
    subscriptions: Unset | list[str] = UNSET
    last_poll_at: None | Unset | datetime.datetime = UNSET
    online: Unset | bool = UNSET
    deliveries_count: Unset | int = UNSET
    deliveries_queued_count: Unset | int = UNSET
    deliveries_running_count: Unset | int = UNSET
    deliveries_completed_count: Unset | int = UNSET
    deliveries_failed_count: Unset | int = UNSET
    created_at: Unset | datetime.datetime = UNSET
    updated_at: Unset | datetime.datetime = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status: str = self.status

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        subscriptions: Unset | list[str] = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = self.subscriptions

        last_poll_at: None | Unset | str
        if isinstance(self.last_poll_at, Unset):
            last_poll_at = UNSET
        elif isinstance(self.last_poll_at, datetime.datetime):
            last_poll_at = self.last_poll_at.isoformat()
        else:
            last_poll_at = self.last_poll_at

        online = self.online

        deliveries_count = self.deliveries_count

        deliveries_queued_count = self.deliveries_queued_count

        deliveries_running_count = self.deliveries_running_count

        deliveries_completed_count = self.deliveries_completed_count

        deliveries_failed_count = self.deliveries_failed_count

        created_at: Unset | str = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Unset | str = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if last_poll_at is not UNSET:
            field_dict["last_poll_at"] = last_poll_at
        if online is not UNSET:
            field_dict["online"] = online
        if deliveries_count is not UNSET:
            field_dict["deliveries_count"] = deliveries_count
        if deliveries_queued_count is not UNSET:
            field_dict["deliveries_queued_count"] = deliveries_queued_count
        if deliveries_running_count is not UNSET:
            field_dict["deliveries_running_count"] = deliveries_running_count
        if deliveries_completed_count is not UNSET:
            field_dict["deliveries_completed_count"] = deliveries_completed_count
        if deliveries_failed_count is not UNSET:
            field_dict["deliveries_failed_count"] = deliveries_failed_count
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        status = check_edge_connector_data_attributes_status(d.pop("status"))

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        subscriptions = cast(list[str], d.pop("subscriptions", UNSET))

        def _parse_last_poll_at(data: object) -> None | Unset | datetime.datetime:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_poll_at_type_0 = isoparse(data)

                return last_poll_at_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.datetime, data)

        last_poll_at = _parse_last_poll_at(d.pop("last_poll_at", UNSET))

        online = d.pop("online", UNSET)

        deliveries_count = d.pop("deliveries_count", UNSET)

        deliveries_queued_count = d.pop("deliveries_queued_count", UNSET)

        deliveries_running_count = d.pop("deliveries_running_count", UNSET)

        deliveries_completed_count = d.pop("deliveries_completed_count", UNSET)

        deliveries_failed_count = d.pop("deliveries_failed_count", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Unset | datetime.datetime
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Unset | datetime.datetime
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        edge_connector_data_attributes = cls(
            name=name,
            status=status,
            description=description,
            subscriptions=subscriptions,
            last_poll_at=last_poll_at,
            online=online,
            deliveries_count=deliveries_count,
            deliveries_queued_count=deliveries_queued_count,
            deliveries_running_count=deliveries_running_count,
            deliveries_completed_count=deliveries_completed_count,
            deliveries_failed_count=deliveries_failed_count,
            created_at=created_at,
            updated_at=updated_at,
        )

        edge_connector_data_attributes.additional_properties = d
        return edge_connector_data_attributes

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
