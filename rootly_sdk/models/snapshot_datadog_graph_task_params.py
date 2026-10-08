from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.snapshot_datadog_graph_task_params_task_type import (
    SnapshotDatadogGraphTaskParamsTaskType,
    check_snapshot_datadog_graph_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snapshot_datadog_graph_task_params_dashboards_item import SnapshotDatadogGraphTaskParamsDashboardsItem
    from ..models.snapshot_datadog_graph_task_params_post_to_slack_channels_item import (
        SnapshotDatadogGraphTaskParamsPostToSlackChannelsItem,
    )


T = TypeVar("T", bound="SnapshotDatadogGraphTaskParams")


@_attrs_define
class SnapshotDatadogGraphTaskParams:
    """
    Attributes:
        past_duration (str): in format '1 minute', '30 days', '3 months', etc Example: 1 hour.
        task_type (SnapshotDatadogGraphTaskParamsTaskType | Unset):
        dashboards (list[SnapshotDatadogGraphTaskParamsDashboardsItem] | Unset):
        metric_queries (list[str] | Unset):
        post_to_incident_timeline (bool | Unset):
        post_to_slack_channels (list[SnapshotDatadogGraphTaskParamsPostToSlackChannelsItem] | Unset):
    """

    past_duration: str
    task_type: SnapshotDatadogGraphTaskParamsTaskType | Unset = UNSET
    dashboards: list[SnapshotDatadogGraphTaskParamsDashboardsItem] | Unset = UNSET
    metric_queries: list[str] | Unset = UNSET
    post_to_incident_timeline: bool | Unset = UNSET
    post_to_slack_channels: list[SnapshotDatadogGraphTaskParamsPostToSlackChannelsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        past_duration = self.past_duration

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        dashboards: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dashboards, Unset):
            dashboards = []
            for dashboards_item_data in self.dashboards:
                dashboards_item = dashboards_item_data.to_dict()
                dashboards.append(dashboards_item)

        metric_queries: list[str] | Unset = UNSET
        if not isinstance(self.metric_queries, Unset):
            metric_queries = self.metric_queries

        post_to_incident_timeline = self.post_to_incident_timeline

        post_to_slack_channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.post_to_slack_channels, Unset):
            post_to_slack_channels = []
            for post_to_slack_channels_item_data in self.post_to_slack_channels:
                post_to_slack_channels_item = post_to_slack_channels_item_data.to_dict()
                post_to_slack_channels.append(post_to_slack_channels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "past_duration": past_duration,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if dashboards is not UNSET:
            field_dict["dashboards"] = dashboards
        if metric_queries is not UNSET:
            field_dict["metric_queries"] = metric_queries
        if post_to_incident_timeline is not UNSET:
            field_dict["post_to_incident_timeline"] = post_to_incident_timeline
        if post_to_slack_channels is not UNSET:
            field_dict["post_to_slack_channels"] = post_to_slack_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snapshot_datadog_graph_task_params_dashboards_item import (
            SnapshotDatadogGraphTaskParamsDashboardsItem,
        )
        from ..models.snapshot_datadog_graph_task_params_post_to_slack_channels_item import (
            SnapshotDatadogGraphTaskParamsPostToSlackChannelsItem,
        )

        d = dict(src_dict)
        past_duration = d.pop("past_duration")

        _task_type = d.pop("task_type", UNSET)
        task_type: SnapshotDatadogGraphTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_snapshot_datadog_graph_task_params_task_type(_task_type)

        _dashboards = d.pop("dashboards", UNSET)
        dashboards: list[SnapshotDatadogGraphTaskParamsDashboardsItem] | Unset = UNSET
        if _dashboards is not UNSET:
            dashboards = []
            for dashboards_item_data in _dashboards:
                dashboards_item = SnapshotDatadogGraphTaskParamsDashboardsItem.from_dict(dashboards_item_data)

                dashboards.append(dashboards_item)

        metric_queries = cast(list[str], d.pop("metric_queries", UNSET))

        post_to_incident_timeline = d.pop("post_to_incident_timeline", UNSET)

        _post_to_slack_channels = d.pop("post_to_slack_channels", UNSET)
        post_to_slack_channels: list[SnapshotDatadogGraphTaskParamsPostToSlackChannelsItem] | Unset = UNSET
        if _post_to_slack_channels is not UNSET:
            post_to_slack_channels = []
            for post_to_slack_channels_item_data in _post_to_slack_channels:
                post_to_slack_channels_item = SnapshotDatadogGraphTaskParamsPostToSlackChannelsItem.from_dict(
                    post_to_slack_channels_item_data
                )

                post_to_slack_channels.append(post_to_slack_channels_item)

        snapshot_datadog_graph_task_params = cls(
            past_duration=past_duration,
            task_type=task_type,
            dashboards=dashboards,
            metric_queries=metric_queries,
            post_to_incident_timeline=post_to_incident_timeline,
            post_to_slack_channels=post_to_slack_channels,
        )

        snapshot_datadog_graph_task_params.additional_properties = d
        return snapshot_datadog_graph_task_params

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
