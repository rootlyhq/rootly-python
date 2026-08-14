import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

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
        status_page_id (Union[Unset, str]): Unique ID of the status page you wish to post the event to
        status (Union[Unset, NewIncidentStatusPageEventDataAttributesStatus]): The status of the incident event
        notify_subscribers (Union[None, Unset, bool]): Notify all status pages subscribers Default: False.
        should_tweet (Union[None, Unset, bool]): For Statuspage.io integrated pages auto publishes a tweet for your
            update Default: False.
        started_at (Union[None, Unset, datetime.datetime]): When the event started. Defaults to the time of creation.
        status_page_components (Union[None, Unset,
            list['NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0Item']]): Affected status page components
            and their statuses. Requires the status-page-v3-phase-1 feature. Ignored for terminal event statuses (resolved,
            completed), which clear component impact. A status is required per component except for scheduled maintenance
            incidents.
    """

    event: str
    status_page_id: Unset | str = UNSET
    status: Unset | NewIncidentStatusPageEventDataAttributesStatus = UNSET
    notify_subscribers: None | Unset | bool = False
    should_tweet: None | Unset | bool = False
    started_at: None | Unset | datetime.datetime = UNSET
    status_page_components: (
        None | Unset | list["NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0Item"]
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        status_page_id = self.status_page_id

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        notify_subscribers: None | Unset | bool
        if isinstance(self.notify_subscribers, Unset):
            notify_subscribers = UNSET
        else:
            notify_subscribers = self.notify_subscribers

        should_tweet: None | Unset | bool
        if isinstance(self.should_tweet, Unset):
            should_tweet = UNSET
        else:
            should_tweet = self.should_tweet

        started_at: None | Unset | str
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        status_page_components: None | Unset | list[dict[str, Any]]
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
        status: Unset | NewIncidentStatusPageEventDataAttributesStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_new_incident_status_page_event_data_attributes_status(_status)

        def _parse_notify_subscribers(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        notify_subscribers = _parse_notify_subscribers(d.pop("notify_subscribers", UNSET))

        def _parse_should_tweet(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        should_tweet = _parse_should_tweet(d.pop("should_tweet", UNSET))

        def _parse_started_at(data: object) -> None | Unset | datetime.datetime:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.datetime, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_status_page_components(
            data: object,
        ) -> None | Unset | list["NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0Item"]:
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
            except:  # noqa: E722
                pass
            return cast(
                None | Unset | list["NewIncidentStatusPageEventDataAttributesStatusPageComponentsType0Item"], data
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
