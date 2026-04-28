from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.publish_incident_task_params_status import (
    PublishIncidentTaskParamsStatus,
    check_publish_incident_task_params_status,
)
from ..models.publish_incident_task_params_task_type import (
    PublishIncidentTaskParamsTaskType,
    check_publish_incident_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.publish_incident_task_params_incident import PublishIncidentTaskParamsIncident
    from ..models.publish_incident_task_params_status_page_template import PublishIncidentTaskParamsStatusPageTemplate


T = TypeVar("T", bound="PublishIncidentTaskParams")


@_attrs_define
class PublishIncidentTaskParams:
    """
    Attributes:
        incident (PublishIncidentTaskParamsIncident):
        public_title (str):
        status (PublishIncidentTaskParamsStatus):  Default: 'resolved'.
        status_page_id (str):
        task_type (PublishIncidentTaskParamsTaskType | Unset):
        event (str | Unset): Incident event description
        notify_subscribers (bool | Unset): When true notifies subscribers of the status page by email/text Default:
            False.
        should_tweet (bool | Unset): For Statuspage.io integrated pages auto publishes a tweet for your update Default:
            False.
        status_page_template (PublishIncidentTaskParamsStatusPageTemplate | Unset):
        integration_payload (None | str | Unset): Additional API Payload you can pass to statuspage.io for example. Can
            contain liquid markup and need to be valid JSON
    """

    incident: PublishIncidentTaskParamsIncident
    public_title: str
    status_page_id: str
    status: PublishIncidentTaskParamsStatus = "resolved"
    task_type: PublishIncidentTaskParamsTaskType | Unset = UNSET
    event: str | Unset = UNSET
    notify_subscribers: bool | Unset = False
    should_tweet: bool | Unset = False
    status_page_template: PublishIncidentTaskParamsStatusPageTemplate | Unset = UNSET
    integration_payload: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident = self.incident.to_dict()

        public_title = self.public_title

        status: str = self.status

        status_page_id = self.status_page_id

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        event = self.event

        notify_subscribers = self.notify_subscribers

        should_tweet = self.should_tweet

        status_page_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_page_template, Unset):
            status_page_template = self.status_page_template.to_dict()

        integration_payload: None | str | Unset
        if isinstance(self.integration_payload, Unset):
            integration_payload = UNSET
        else:
            integration_payload = self.integration_payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident": incident,
                "public_title": public_title,
                "status": status,
                "status_page_id": status_page_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if event is not UNSET:
            field_dict["event"] = event
        if notify_subscribers is not UNSET:
            field_dict["notify_subscribers"] = notify_subscribers
        if should_tweet is not UNSET:
            field_dict["should_tweet"] = should_tweet
        if status_page_template is not UNSET:
            field_dict["status_page_template"] = status_page_template
        if integration_payload is not UNSET:
            field_dict["integration_payload"] = integration_payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.publish_incident_task_params_incident import PublishIncidentTaskParamsIncident
        from ..models.publish_incident_task_params_status_page_template import (
            PublishIncidentTaskParamsStatusPageTemplate,
        )

        d = dict(src_dict)
        incident = PublishIncidentTaskParamsIncident.from_dict(d.pop("incident"))

        public_title = d.pop("public_title")

        status = check_publish_incident_task_params_status(d.pop("status"))

        status_page_id = d.pop("status_page_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: PublishIncidentTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_publish_incident_task_params_task_type(_task_type)

        event = d.pop("event", UNSET)

        notify_subscribers = d.pop("notify_subscribers", UNSET)

        should_tweet = d.pop("should_tweet", UNSET)

        _status_page_template = d.pop("status_page_template", UNSET)
        status_page_template: PublishIncidentTaskParamsStatusPageTemplate | Unset
        if isinstance(_status_page_template, Unset):
            status_page_template = UNSET
        else:
            status_page_template = PublishIncidentTaskParamsStatusPageTemplate.from_dict(_status_page_template)

        def _parse_integration_payload(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        integration_payload = _parse_integration_payload(d.pop("integration_payload", UNSET))

        publish_incident_task_params = cls(
            incident=incident,
            public_title=public_title,
            status=status,
            status_page_id=status_page_id,
            task_type=task_type,
            event=event,
            notify_subscribers=notify_subscribers,
            should_tweet=should_tweet,
            status_page_template=status_page_template,
            integration_payload=integration_payload,
        )

        publish_incident_task_params.additional_properties = d
        return publish_incident_task_params

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
