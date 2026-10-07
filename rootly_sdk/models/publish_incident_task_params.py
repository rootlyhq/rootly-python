from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.publish_incident_task_params_status import (
    PublishIncidentTaskParamsStatus,
    check_publish_incident_task_params_status,
)
from ..models.publish_incident_task_params_synced_component_status import (
    PublishIncidentTaskParamsSyncedComponentStatus,
    check_publish_incident_task_params_synced_component_status,
)
from ..models.publish_incident_task_params_task_type import (
    PublishIncidentTaskParamsTaskType,
    check_publish_incident_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.publish_incident_task_params_incident import PublishIncidentTaskParamsIncident
    from ..models.publish_incident_task_params_selected_component_statuses import (
        PublishIncidentTaskParamsSelectedComponentStatuses,
    )
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
        status_page_ids (list[str] | Unset): Publishes the update to every listed status page. This field is in limited
            Early Access; contact Rootly Support to request access. When set, it takes precedence over status_page_id and
            the first entry becomes status_page_id.
        selected_component_keys (list[str] | Unset): Composite "SourceType:<id>" keys of the status page components
            affected by the publish. This field is in Early Access and is not generally available; contact Rootly Support to
            request access.
        selected_component_statuses (PublishIncidentTaskParamsSelectedComponentStatuses | Unset): Impact status to
            publish for each selected component key. Keys must match selected_component_keys entries.
        sync_incident_components (bool | None | Unset): When true, every run also publishes the incident's tagged
            services and functionalities that are components on the target page. Defaults to true when
            selected_component_keys is empty. This field is in Early Access and is not generally available; contact Rootly
            Support to request access.
        synced_component_status (PublishIncidentTaskParamsSyncedComponentStatus | Unset): Impact status published for
            components synced from the incident. Defaults to degraded_performance. A component also listed in
            selected_component_keys keeps its selected_component_statuses entry.
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
    status_page_ids: list[str] | Unset = UNSET
    selected_component_keys: list[str] | Unset = UNSET
    selected_component_statuses: PublishIncidentTaskParamsSelectedComponentStatuses | Unset = UNSET
    sync_incident_components: bool | None | Unset = UNSET
    synced_component_status: PublishIncidentTaskParamsSyncedComponentStatus | Unset = UNSET
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

        status_page_ids: list[str] | Unset = UNSET
        if not isinstance(self.status_page_ids, Unset):
            status_page_ids = self.status_page_ids

        selected_component_keys: list[str] | Unset = UNSET
        if not isinstance(self.selected_component_keys, Unset):
            selected_component_keys = self.selected_component_keys

        selected_component_statuses: dict[str, Any] | Unset = UNSET
        if not isinstance(self.selected_component_statuses, Unset):
            selected_component_statuses = self.selected_component_statuses.to_dict()

        sync_incident_components: bool | None | Unset
        if isinstance(self.sync_incident_components, Unset):
            sync_incident_components = UNSET
        else:
            sync_incident_components = self.sync_incident_components

        synced_component_status: str | Unset = UNSET
        if not isinstance(self.synced_component_status, Unset):
            synced_component_status = self.synced_component_status

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
        if status_page_ids is not UNSET:
            field_dict["status_page_ids"] = status_page_ids
        if selected_component_keys is not UNSET:
            field_dict["selected_component_keys"] = selected_component_keys
        if selected_component_statuses is not UNSET:
            field_dict["selected_component_statuses"] = selected_component_statuses
        if sync_incident_components is not UNSET:
            field_dict["sync_incident_components"] = sync_incident_components
        if synced_component_status is not UNSET:
            field_dict["synced_component_status"] = synced_component_status
        if integration_payload is not UNSET:
            field_dict["integration_payload"] = integration_payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.publish_incident_task_params_incident import PublishIncidentTaskParamsIncident
        from ..models.publish_incident_task_params_selected_component_statuses import (
            PublishIncidentTaskParamsSelectedComponentStatuses,
        )
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

        status_page_ids = cast(list[str], d.pop("status_page_ids", UNSET))

        selected_component_keys = cast(list[str], d.pop("selected_component_keys", UNSET))

        _selected_component_statuses = d.pop("selected_component_statuses", UNSET)
        selected_component_statuses: PublishIncidentTaskParamsSelectedComponentStatuses | Unset
        if isinstance(_selected_component_statuses, Unset):
            selected_component_statuses = UNSET
        else:
            selected_component_statuses = PublishIncidentTaskParamsSelectedComponentStatuses.from_dict(
                _selected_component_statuses
            )

        def _parse_sync_incident_components(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sync_incident_components = _parse_sync_incident_components(d.pop("sync_incident_components", UNSET))

        _synced_component_status = d.pop("synced_component_status", UNSET)
        synced_component_status: PublishIncidentTaskParamsSyncedComponentStatus | Unset
        if isinstance(_synced_component_status, Unset):
            synced_component_status = UNSET
        else:
            synced_component_status = check_publish_incident_task_params_synced_component_status(
                _synced_component_status
            )

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
            status_page_ids=status_page_ids,
            selected_component_keys=selected_component_keys,
            selected_component_statuses=selected_component_statuses,
            sync_incident_components=sync_incident_components,
            synced_component_status=synced_component_status,
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
