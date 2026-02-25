from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.http_client_task_params_method import HttpClientTaskParamsMethod, check_http_client_task_params_method
from ..models.http_client_task_params_task_type import (
    HttpClientTaskParamsTaskType,
    check_http_client_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_client_task_params_post_to_slack_channels_item import HttpClientTaskParamsPostToSlackChannelsItem


T = TypeVar("T", bound="HttpClientTaskParams")


@_attrs_define
class HttpClientTaskParams:
    """
    Attributes:
        url (str): URL endpoint Example: https://example.com/foo.json.
        succeed_on_status (str): HTTP status code expected. Can be a regular expression. Eg: 200, 200|203, 20[0-3]
            Example: 200.
        task_type (Union[Unset, HttpClientTaskParamsTaskType]):
        headers (Union[Unset, str]): JSON map of HTTP headers
        params (Union[Unset, str]): JSON map of HTTP query parameters
        body (Union[Unset, str]): HTTP body
        event_url (Union[Unset, str]):
        event_message (Union[Unset, str]):
        method (Union[Unset, HttpClientTaskParamsMethod]): HTTP method Default: 'GET'.
        post_to_incident_timeline (Union[Unset, bool]):
        post_to_slack_channels (Union[Unset, list['HttpClientTaskParamsPostToSlackChannelsItem']]):
    """

    url: str
    succeed_on_status: str
    task_type: Unset | HttpClientTaskParamsTaskType = UNSET
    headers: Unset | str = UNSET
    params: Unset | str = UNSET
    body: Unset | str = UNSET
    event_url: Unset | str = UNSET
    event_message: Unset | str = UNSET
    method: Unset | HttpClientTaskParamsMethod = "GET"
    post_to_incident_timeline: Unset | bool = UNSET
    post_to_slack_channels: Unset | list["HttpClientTaskParamsPostToSlackChannelsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        succeed_on_status = self.succeed_on_status

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        headers = self.headers

        params = self.params

        body = self.body

        event_url = self.event_url

        event_message = self.event_message

        method: Unset | str = UNSET
        if not isinstance(self.method, Unset):
            method = self.method

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
                "url": url,
                "succeed_on_status": succeed_on_status,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if headers is not UNSET:
            field_dict["headers"] = headers
        if params is not UNSET:
            field_dict["params"] = params
        if body is not UNSET:
            field_dict["body"] = body
        if event_url is not UNSET:
            field_dict["event_url"] = event_url
        if event_message is not UNSET:
            field_dict["event_message"] = event_message
        if method is not UNSET:
            field_dict["method"] = method
        if post_to_incident_timeline is not UNSET:
            field_dict["post_to_incident_timeline"] = post_to_incident_timeline
        if post_to_slack_channels is not UNSET:
            field_dict["post_to_slack_channels"] = post_to_slack_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_client_task_params_post_to_slack_channels_item import (
            HttpClientTaskParamsPostToSlackChannelsItem,
        )

        d = dict(src_dict)
        url = d.pop("url")

        succeed_on_status = d.pop("succeed_on_status")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | HttpClientTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_http_client_task_params_task_type(_task_type)

        headers = d.pop("headers", UNSET)

        params = d.pop("params", UNSET)

        body = d.pop("body", UNSET)

        event_url = d.pop("event_url", UNSET)

        event_message = d.pop("event_message", UNSET)

        _method = d.pop("method", UNSET)
        method: Unset | HttpClientTaskParamsMethod
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = check_http_client_task_params_method(_method)

        post_to_incident_timeline = d.pop("post_to_incident_timeline", UNSET)

        post_to_slack_channels = []
        _post_to_slack_channels = d.pop("post_to_slack_channels", UNSET)
        for post_to_slack_channels_item_data in _post_to_slack_channels or []:
            post_to_slack_channels_item = HttpClientTaskParamsPostToSlackChannelsItem.from_dict(
                post_to_slack_channels_item_data
            )

            post_to_slack_channels.append(post_to_slack_channels_item)

        http_client_task_params = cls(
            url=url,
            succeed_on_status=succeed_on_status,
            task_type=task_type,
            headers=headers,
            params=params,
            body=body,
            event_url=event_url,
            event_message=event_message,
            method=method,
            post_to_incident_timeline=post_to_incident_timeline,
            post_to_slack_channels=post_to_slack_channels,
        )

        http_client_task_params.additional_properties = d
        return http_client_task_params

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
