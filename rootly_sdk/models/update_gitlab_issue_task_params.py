from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_gitlab_issue_task_params_issue_type import (
    UpdateGitlabIssueTaskParamsIssueType,
    check_update_gitlab_issue_task_params_issue_type,
)
from ..models.update_gitlab_issue_task_params_task_type import (
    UpdateGitlabIssueTaskParamsTaskType,
    check_update_gitlab_issue_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_gitlab_issue_task_params_completion import UpdateGitlabIssueTaskParamsCompletion


T = TypeVar("T", bound="UpdateGitlabIssueTaskParams")


@_attrs_define
class UpdateGitlabIssueTaskParams:
    """
    Attributes:
        issue_id (str): The issue id
        completion (UpdateGitlabIssueTaskParamsCompletion):
        task_type (Union[Unset, UpdateGitlabIssueTaskParamsTaskType]):
        issue_type (Union[Unset, UpdateGitlabIssueTaskParamsIssueType]): The issue type
        title (Union[Unset, str]): The issue title
        description (Union[Unset, str]): The issue description
        labels (Union[Unset, str]): The issue labels
        due_date (Union[Unset, str]): The due date
    """

    issue_id: str
    completion: "UpdateGitlabIssueTaskParamsCompletion"
    task_type: Unset | UpdateGitlabIssueTaskParamsTaskType = UNSET
    issue_type: Unset | UpdateGitlabIssueTaskParamsIssueType = UNSET
    title: Unset | str = UNSET
    description: Unset | str = UNSET
    labels: Unset | str = UNSET
    due_date: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id = self.issue_id

        completion = self.completion.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        issue_type: Unset | str = UNSET
        if not isinstance(self.issue_type, Unset):
            issue_type = self.issue_type

        title = self.title

        description = self.description

        labels = self.labels

        due_date = self.due_date

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
        if issue_type is not UNSET:
            field_dict["issue_type"] = issue_type
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if due_date is not UNSET:
            field_dict["due_date"] = due_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_gitlab_issue_task_params_completion import UpdateGitlabIssueTaskParamsCompletion

        d = dict(src_dict)
        issue_id = d.pop("issue_id")

        completion = UpdateGitlabIssueTaskParamsCompletion.from_dict(d.pop("completion"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateGitlabIssueTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_gitlab_issue_task_params_task_type(_task_type)

        _issue_type = d.pop("issue_type", UNSET)
        issue_type: Unset | UpdateGitlabIssueTaskParamsIssueType
        if isinstance(_issue_type, Unset):
            issue_type = UNSET
        else:
            issue_type = check_update_gitlab_issue_task_params_issue_type(_issue_type)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        labels = d.pop("labels", UNSET)

        due_date = d.pop("due_date", UNSET)

        update_gitlab_issue_task_params = cls(
            issue_id=issue_id,
            completion=completion,
            task_type=task_type,
            issue_type=issue_type,
            title=title,
            description=description,
            labels=labels,
            due_date=due_date,
        )

        update_gitlab_issue_task_params.additional_properties = d
        return update_gitlab_issue_task_params

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
