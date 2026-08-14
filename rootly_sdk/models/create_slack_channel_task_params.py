from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_slack_channel_task_params_private import (
    CreateSlackChannelTaskParamsPrivate,
    check_create_slack_channel_task_params_private,
)
from ..models.create_slack_channel_task_params_task_type import (
    CreateSlackChannelTaskParamsTaskType,
    check_create_slack_channel_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_slack_channel_task_params_workspace import CreateSlackChannelTaskParamsWorkspace


T = TypeVar("T", bound="CreateSlackChannelTaskParams")


@_attrs_define
class CreateSlackChannelTaskParams:
    """
    Attributes:
        workspace (CreateSlackChannelTaskParamsWorkspace):
        title (str): Slack channel title
        task_type (Union[Unset, CreateSlackChannelTaskParamsTaskType]):
        private (Union[Unset, CreateSlackChannelTaskParamsPrivate]):  Default: 'auto'.
    """

    workspace: "CreateSlackChannelTaskParamsWorkspace"
    title: str
    task_type: Unset | CreateSlackChannelTaskParamsTaskType = UNSET
    private: Unset | CreateSlackChannelTaskParamsPrivate = "auto"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace = self.workspace.to_dict()

        title = self.title

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        private: Unset | str = UNSET
        if not isinstance(self.private, Unset):
            private = self.private

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workspace": workspace,
                "title": title,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if private is not UNSET:
            field_dict["private"] = private

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_slack_channel_task_params_workspace import CreateSlackChannelTaskParamsWorkspace

        d = dict(src_dict)
        workspace = CreateSlackChannelTaskParamsWorkspace.from_dict(d.pop("workspace"))

        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateSlackChannelTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_slack_channel_task_params_task_type(_task_type)

        _private = d.pop("private", UNSET)
        private: Unset | CreateSlackChannelTaskParamsPrivate
        if isinstance(_private, Unset):
            private = UNSET
        else:
            private = check_create_slack_channel_task_params_private(_private)

        create_slack_channel_task_params = cls(
            workspace=workspace,
            title=title,
            task_type=task_type,
            private=private,
        )

        create_slack_channel_task_params.additional_properties = d
        return create_slack_channel_task_params

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
