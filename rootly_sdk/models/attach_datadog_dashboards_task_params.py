from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attach_datadog_dashboards_task_params_task_type import (
    AttachDatadogDashboardsTaskParamsTaskType,
    check_attach_datadog_dashboards_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attach_datadog_dashboards_task_params_dashboards_item import (
        AttachDatadogDashboardsTaskParamsDashboardsItem,
    )
    from ..models.attach_datadog_dashboards_task_params_post_to_slack_channels_item import (
        AttachDatadogDashboardsTaskParamsPostToSlackChannelsItem,
    )


T = TypeVar("T", bound="AttachDatadogDashboardsTaskParams")


@_attrs_define
class AttachDatadogDashboardsTaskParams:
    """
    Attributes:
        dashboards (list['AttachDatadogDashboardsTaskParamsDashboardsItem']):
        task_type (Union[Unset, AttachDatadogDashboardsTaskParamsTaskType]):
        post_to_incident_timeline (Union[Unset, bool]):
        post_to_slack_channels (Union[Unset, list['AttachDatadogDashboardsTaskParamsPostToSlackChannelsItem']]):
    """

    dashboards: list["AttachDatadogDashboardsTaskParamsDashboardsItem"]
    task_type: Unset | AttachDatadogDashboardsTaskParamsTaskType = UNSET
    post_to_incident_timeline: Unset | bool = UNSET
    post_to_slack_channels: Unset | list["AttachDatadogDashboardsTaskParamsPostToSlackChannelsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dashboards = []
        for dashboards_item_data in self.dashboards:
            dashboards_item = dashboards_item_data.to_dict()
            dashboards.append(dashboards_item)

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
                "dashboards": dashboards,
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
        from ..models.attach_datadog_dashboards_task_params_dashboards_item import (
            AttachDatadogDashboardsTaskParamsDashboardsItem,
        )
        from ..models.attach_datadog_dashboards_task_params_post_to_slack_channels_item import (
            AttachDatadogDashboardsTaskParamsPostToSlackChannelsItem,
        )

        d = dict(src_dict)
        dashboards = []
        _dashboards = d.pop("dashboards")
        for dashboards_item_data in _dashboards:
            dashboards_item = AttachDatadogDashboardsTaskParamsDashboardsItem.from_dict(dashboards_item_data)

            dashboards.append(dashboards_item)

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | AttachDatadogDashboardsTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_attach_datadog_dashboards_task_params_task_type(_task_type)

        post_to_incident_timeline = d.pop("post_to_incident_timeline", UNSET)

        post_to_slack_channels = []
        _post_to_slack_channels = d.pop("post_to_slack_channels", UNSET)
        for post_to_slack_channels_item_data in _post_to_slack_channels or []:
            post_to_slack_channels_item = AttachDatadogDashboardsTaskParamsPostToSlackChannelsItem.from_dict(
                post_to_slack_channels_item_data
            )

            post_to_slack_channels.append(post_to_slack_channels_item)

        attach_datadog_dashboards_task_params = cls(
            dashboards=dashboards,
            task_type=task_type,
            post_to_incident_timeline=post_to_incident_timeline,
            post_to_slack_channels=post_to_slack_channels,
        )

        attach_datadog_dashboards_task_params.additional_properties = d
        return attach_datadog_dashboards_task_params

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
