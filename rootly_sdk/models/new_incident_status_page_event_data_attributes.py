from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_incident_status_page_event_data_attributes_status import (
    NewIncidentStatusPageEventDataAttributesStatus,
    check_new_incident_status_page_event_data_attributes_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_incident_status_page_event_data_attributes_status_page_components_type_0_item import (
        NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0Item,
    )


T = TypeVar("T", bound="NewIncidentStatusPageEventDataAttributes")


@_attrs_define
class NewIncidentStatusPageEventDataAttributes:
    """
    Attributes:
        event (str): The summary of the incident event
        status_page_id (str | Unset): Unique ID of the status page you wish to post the event to
        status (NewIncidentStatusPageEventDataAttributesStatus | Unset): The status of the incident event
        notify_subscribers (bool | None | Unset): Notify all status pages subscribers Default: False.
        should_tweet (bool | None | Unset): For Statuspage.io integrated pages auto publishes a tweet for your update
            Default: False.
        started_at (datetime.datetime | None | Unset): When the event started. Defaults to the time of creation.
        status_page_components (list[NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0Item] | None |
            Unset): Affected status page components and their statuses. This field is in Early Access and is not generally
            available; contact Rootly Support to request access. Ignored for terminal event statuses (resolved, completed),
            which clear component impact. A status is required per component except for scheduled maintenance incidents.
    """

    event: str
    status_page_id: str | Unset = UNSET
    status: NewIncidentStatusPageEventDataAttributesStatus | Unset = UNSET
    notify_subscribers: bool | None | Unset = False
    should_tweet: bool | None | Unset = False
    started_at: datetime.datetime | None | Unset = UNSET
    status_page_components: (
        list[NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0Item] | None | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        status_page_id = self.status_page_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        notify_subscribers: bool | None | Unset
        if isinstance(self.notify_subscribers, Unset):
            notify_subscribers = UNSET
        else:
            notify_subscribers = self.notify_subscribers

        should_tweet: bool | None | Unset
        if isinstance(self.should_tweet, Unset):
            should_tweet = UNSET
        else:
            should_tweet = self.should_tweet

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        status_page_components: list[dict[str, Any]] | None | Unset
        if isinstance(self.status_page_components, Unset):
            status_page_components = UNSET
        elif isinstance(self.status_page_components, list):
            status_page_components = []
            for status_page_components_type_0_item_data in self.status_page_components:
                status_page_components_type_0_item = status_page_components_type_0_item_data.to_dict()
                status_page_components.append(status_page_components_type_0_item)

        else:
            status_page_components = self.status_page_components

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "event": event,
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
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if status_page_components is not UNSET:
            field_dict["status_page_components"] = status_page_components

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_incident_status_page_event_data_attributes_status_page_components_type_0_item import (
            NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0Item,
        )

        d = dict(src_dict)
        event = d.pop("event")

        status_page_id = d.pop("status_page_id", UNSET)

        _status = d.pop("status", UNSET)
        status: NewIncidentStatusPageEventDataAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_new_incident_status_page_event_data_attributes_status(_status)

        def _parse_notify_subscribers(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        notify_subscribers = _parse_notify_subscribers(d.pop("notify_subscribers", UNSET))

        def _parse_should_tweet(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        should_tweet = _parse_should_tweet(d.pop("should_tweet", UNSET))

        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_status_page_components(
            data: object,
        ) -> list[NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                status_page_components_type_0 = []
                _status_page_components_type_0 = data
                for status_page_components_type_0_item_data in _status_page_components_type_0:
                    status_page_components_type_0_item = (
                        NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0Item.from_dict(
                            status_page_components_type_0_item_data
                        )
                    )

                    status_page_components_type_0.append(status_page_components_type_0_item)

                return status_page_components_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0Item] | None | Unset, data
            )

        status_page_components = _parse_status_page_components(d.pop("status_page_components", UNSET))

        new_incident_status_page_event_data_attributes = cls(
            event=event,
            status_page_id=status_page_id,
            status=status,
            notify_subscribers=notify_subscribers,
            should_tweet=should_tweet,
            started_at=started_at,
            status_page_components=status_page_components,
        )

        return new_incident_status_page_event_data_attributes
