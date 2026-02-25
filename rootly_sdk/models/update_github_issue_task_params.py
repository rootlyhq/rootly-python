from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_github_issue_task_params_task_type import (
    UpdateGithubIssueTaskParamsTaskType,
    check_update_github_issue_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_github_issue_task_params_completion import UpdateGithubIssueTaskParamsCompletion


T = TypeVar("T", bound="UpdateGithubIssueTaskParams")


@_attrs_define
class UpdateGithubIssueTaskParams:
    """
    Attributes:
        issue_id (str): The issue id
        completion (UpdateGithubIssueTaskParamsCompletion):
        task_type (Union[Unset, UpdateGithubIssueTaskParamsTaskType]):
        title (Union[Unset, str]): The issue title
        body (Union[Unset, str]): The issue body
    """

    issue_id: str
    completion: "UpdateGithubIssueTaskParamsCompletion"
    task_type: Unset | UpdateGithubIssueTaskParamsTaskType = UNSET
    title: Unset | str = UNSET
    body: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id = self.issue_id

        completion = self.completion.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title = self.title

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_id": issue_id,
                "completion": completion,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_github_issue_task_params_completion import UpdateGithubIssueTaskParamsCompletion

        d = dict(src_dict)
        issue_id = d.pop("issue_id")

        completion = UpdateGithubIssueTaskParamsCompletion.from_dict(d.pop("completion"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateGithubIssueTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_github_issue_task_params_task_type(_task_type)

        title = d.pop("title", UNSET)

        body = d.pop("body", UNSET)

        update_github_issue_task_params = cls(
            issue_id=issue_id,
            completion=completion,
            task_type=task_type,
            title=title,
            body=body,
        )

        update_github_issue_task_params.additional_properties = d
        return update_github_issue_task_params

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
