from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_status_page_event_status import (
    IncidentStatusPageEventStatus,
    check_incident_status_page_event_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentStatusPageEvent")


@_attrs_define
class IncidentStatusPageEvent:
    """
    Attributes:
        event (str): The summary of the incident event
        started_at (str): Date of start
        created_at (str): Date of creation
        updated_at (str): Date of last update
        status_page_id (Union[Unset, str]): Unique ID of the status page you wish to post the event to
        status (Union[Unset, IncidentStatusPageEventStatus]): The status of the incident event
        notify_subscribers (Union[Unset, bool]): Notify all status pages subscribers
        should_tweet (Union[Unset, bool]): For Statuspage.io integrated pages auto publishes a tweet for your update
    """

    event: str
    started_at: str
    created_at: str
    updated_at: str
    status_page_id: Unset | str = UNSET
    status: Unset | IncidentStatusPageEventStatus = UNSET
    notify_subscribers: Unset | bool = UNSET
    should_tweet: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        started_at = self.started_at

        created_at = self.created_at

        updated_at = self.updated_at

        status_page_id = self.status_page_id

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        notify_subscribers = self.notify_subscribers

        should_tweet = self.should_tweet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
                "started_at": started_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if status_page_id is not UNSET:
            field_dict["status_page_id"] = status_page_id
        if status is not UNSET:
            field_dict["status"] = status
        if notify_subscribers is not UNSET:
            field_dict["notify_subscribers"] = notify_subscribers
        if should_tweet is not UNSET:
            field_dict["should_tweet"] = should_tweet

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event = d.pop("event")

        started_at = d.pop("started_at")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        status_page_id = d.pop("status_page_id", UNSET)

        _status = d.pop("status", UNSET)
        status: Unset | IncidentStatusPageEventStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_incident_status_page_event_status(_status)

        notify_subscribers = d.pop("notify_subscribers", UNSET)

        should_tweet = d.pop("should_tweet", UNSET)

        incident_status_page_event = cls(
            event=event,
            started_at=started_at,
            created_at=created_at,
            updated_at=updated_at,
            status_page_id=status_page_id,
            status=status,
            notify_subscribers=notify_subscribers,
            should_tweet=should_tweet,
        )

        incident_status_page_event.additional_properties = d
        return incident_status_page_event

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
