from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_alerts_task_params_task_type import (
    GetAlertsTaskParamsTaskType,
    check_get_alerts_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_alerts_task_params_parent_message_thread_task import GetAlertsTaskParamsParentMessageThreadTask
    from ..models.get_alerts_task_params_post_to_slack_channels_item import GetAlertsTaskParamsPostToSlackChannelsItem


T = TypeVar("T", bound="GetAlertsTaskParams")


@_attrs_define
class GetAlertsTaskParams:
    """
    Attributes:
        past_duration (str): How far back to fetch commits (in format '1 minute', '30 days', '3 months', etc.) Example:
            1 hour.
        task_type (Union[Unset, GetAlertsTaskParamsTaskType]):
        service_ids (Union[Unset, list[str]]):
        environment_ids (Union[Unset, list[str]]):
        labels (Union[Unset, list[str]]):
        sources (Union[Unset, list[str]]):
        services_impacted_by_incident (Union[Unset, bool]):
        environments_impacted_by_incident (Union[Unset, bool]):
        post_to_incident_timeline (Union[Unset, bool]):
        post_to_slack_channels (Union[Unset, list['GetAlertsTaskParamsPostToSlackChannelsItem']]):
        parent_message_thread_task (Union[Unset, GetAlertsTaskParamsParentMessageThreadTask]): A hash where [id] is the
            task id of the parent task that sent a message, and [name] is the name of the parent task
    """

    past_duration: str
    task_type: Unset | GetAlertsTaskParamsTaskType = UNSET
    service_ids: Unset | list[str] = UNSET
    environment_ids: Unset | list[str] = UNSET
    labels: Unset | list[str] = UNSET
    sources: Unset | list[str] = UNSET
    services_impacted_by_incident: Unset | bool = UNSET
    environments_impacted_by_incident: Unset | bool = UNSET
    post_to_incident_timeline: Unset | bool = UNSET
    post_to_slack_channels: Unset | list["GetAlertsTaskParamsPostToSlackChannelsItem"] = UNSET
    parent_message_thread_task: Union[Unset, "GetAlertsTaskParamsParentMessageThreadTask"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        past_duration = self.past_duration

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        service_ids: Unset | list[str] = UNSET
        if not isinstance(self.service_ids, Unset):
            service_ids = self.service_ids

        environment_ids: Unset | list[str] = UNSET
        if not isinstance(self.environment_ids, Unset):
            environment_ids = self.environment_ids

        labels: Unset | list[str] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        sources: Unset | list[str] = UNSET
        if not isinstance(self.sources, Unset):
            sources = self.sources

        services_impacted_by_incident = self.services_impacted_by_incident

        environments_impacted_by_incident = self.environments_impacted_by_incident

        post_to_incident_timeline = self.post_to_incident_timeline

        post_to_slack_channels: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.post_to_slack_channels, Unset):
            post_to_slack_channels = []
            for post_to_slack_channels_item_data in self.post_to_slack_channels:
                post_to_slack_channels_item = post_to_slack_channels_item_data.to_dict()
                post_to_slack_channels.append(post_to_slack_channels_item)

        parent_message_thread_task: Unset | dict[str, Any] = UNSET
        if not isinstance(self.parent_message_thread_task, Unset):
            parent_message_thread_task = self.parent_message_thread_task.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "past_duration": past_duration,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if environment_ids is not UNSET:
            field_dict["environment_ids"] = environment_ids
        if labels is not UNSET:
            field_dict["labels"] = labels
        if sources is not UNSET:
            field_dict["sources"] = sources
        if services_impacted_by_incident is not UNSET:
            field_dict["services_impacted_by_incident"] = services_impacted_by_incident
        if environments_impacted_by_incident is not UNSET:
            field_dict["environments_impacted_by_incident"] = environments_impacted_by_incident
        if post_to_incident_timeline is not UNSET:
            field_dict["post_to_incident_timeline"] = post_to_incident_timeline
        if post_to_slack_channels is not UNSET:
            field_dict["post_to_slack_channels"] = post_to_slack_channels
        if parent_message_thread_task is not UNSET:
            field_dict["parent_message_thread_task"] = parent_message_thread_task

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_alerts_task_params_parent_message_thread_task import (
            GetAlertsTaskParamsParentMessageThreadTask,
        )
        from ..models.get_alerts_task_params_post_to_slack_channels_item import (
            GetAlertsTaskParamsPostToSlackChannelsItem,
        )

        d = dict(src_dict)
        past_duration = d.pop("past_duration")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | GetAlertsTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_get_alerts_task_params_task_type(_task_type)

        service_ids = cast(list[str], d.pop("service_ids", UNSET))

        environment_ids = cast(list[str], d.pop("environment_ids", UNSET))

        labels = cast(list[str], d.pop("labels", UNSET))

        sources = cast(list[str], d.pop("sources", UNSET))

        services_impacted_by_incident = d.pop("services_impacted_by_incident", UNSET)

        environments_impacted_by_incident = d.pop("environments_impacted_by_incident", UNSET)

        post_to_incident_timeline = d.pop("post_to_incident_timeline", UNSET)

        post_to_slack_channels = []
        _post_to_slack_channels = d.pop("post_to_slack_channels", UNSET)
        for post_to_slack_channels_item_data in _post_to_slack_channels or []:
            post_to_slack_channels_item = GetAlertsTaskParamsPostToSlackChannelsItem.from_dict(
                post_to_slack_channels_item_data
            )

            post_to_slack_channels.append(post_to_slack_channels_item)

        _parent_message_thread_task = d.pop("parent_message_thread_task", UNSET)
        parent_message_thread_task: Unset | GetAlertsTaskParamsParentMessageThreadTask
        if isinstance(_parent_message_thread_task, Unset):
            parent_message_thread_task = UNSET
        else:
            parent_message_thread_task = GetAlertsTaskParamsParentMessageThreadTask.from_dict(
                _parent_message_thread_task
            )

        get_alerts_task_params = cls(
            past_duration=past_duration,
            task_type=task_type,
            service_ids=service_ids,
            environment_ids=environment_ids,
            labels=labels,
            sources=sources,
            services_impacted_by_incident=services_impacted_by_incident,
            environments_impacted_by_incident=environments_impacted_by_incident,
            post_to_incident_timeline=post_to_incident_timeline,
            post_to_slack_channels=post_to_slack_channels,
            parent_message_thread_task=parent_message_thread_task,
        )

        get_alerts_task_params.additional_properties = d
        return get_alerts_task_params

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
