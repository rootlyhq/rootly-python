from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.snapshot_new_relic_graph_task_params_metric_type import (
    SnapshotNewRelicGraphTaskParamsMetricType,
    check_snapshot_new_relic_graph_task_params_metric_type,
)
from ..models.snapshot_new_relic_graph_task_params_task_type import (
    SnapshotNewRelicGraphTaskParamsTaskType,
    check_snapshot_new_relic_graph_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snapshot_new_relic_graph_task_params_post_to_slack_channels_item import (
        SnapshotNewRelicGraphTaskParamsPostToSlackChannelsItem,
    )


T = TypeVar("T", bound="SnapshotNewRelicGraphTaskParams")


@_attrs_define
class SnapshotNewRelicGraphTaskParams:
    """
    Attributes:
        metric_query (str):
        metric_type (SnapshotNewRelicGraphTaskParamsMetricType):
        task_type (Union[Unset, SnapshotNewRelicGraphTaskParamsTaskType]):
        post_to_incident_timeline (Union[Unset, bool]):
        post_to_slack_channels (Union[Unset, list['SnapshotNewRelicGraphTaskParamsPostToSlackChannelsItem']]):
    """

    metric_query: str
    metric_type: SnapshotNewRelicGraphTaskParamsMetricType
    task_type: Unset | SnapshotNewRelicGraphTaskParamsTaskType = UNSET
    post_to_incident_timeline: Unset | bool = UNSET
    post_to_slack_channels: Unset | list["SnapshotNewRelicGraphTaskParamsPostToSlackChannelsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric_query = self.metric_query

        metric_type: str = self.metric_type

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        post_to_incident_timeline = self.post_to_incident_timeline

        post_to_slack_channels: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.post_to_slack_channels, Unset):
            post_to_slack_channels = []
            for post_to_slack_channels_item_data in self.post_to_slack_channels:
                post_to_slack_channels_item = post_to_slack_channels_item_data.to_dict()
                post_to_slack_channels.append(post_to_slack_channels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metric_query": metric_query,
                "metric_type": metric_type,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if post_to_incident_timeline is not UNSET:
            field_dict["post_to_incident_timeline"] = post_to_incident_timeline
        if post_to_slack_channels is not UNSET:
            field_dict["post_to_slack_channels"] = post_to_slack_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snapshot_new_relic_graph_task_params_post_to_slack_channels_item import (
            SnapshotNewRelicGraphTaskParamsPostToSlackChannelsItem,
        )

        d = dict(src_dict)
        metric_query = d.pop("metric_query")

        metric_type = check_snapshot_new_relic_graph_task_params_metric_type(d.pop("metric_type"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | SnapshotNewRelicGraphTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_snapshot_new_relic_graph_task_params_task_type(_task_type)

        post_to_incident_timeline = d.pop("post_to_incident_timeline", UNSET)

        post_to_slack_channels = []
        _post_to_slack_channels = d.pop("post_to_slack_channels", UNSET)
        for post_to_slack_channels_item_data in _post_to_slack_channels or []:
            post_to_slack_channels_item = SnapshotNewRelicGraphTaskParamsPostToSlackChannelsItem.from_dict(
                post_to_slack_channels_item_data
            )

            post_to_slack_channels.append(post_to_slack_channels_item)

        snapshot_new_relic_graph_task_params = cls(
            metric_query=metric_query,
            metric_type=metric_type,
            task_type=task_type,
            post_to_incident_timeline=post_to_incident_timeline,
            post_to_slack_channels=post_to_slack_channels,
        )

        snapshot_new_relic_graph_task_params.additional_properties = d
        return snapshot_new_relic_graph_task_params

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
