from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_github_issue_task_params_task_type import (
    CreateGithubIssueTaskParamsTaskType,
    check_create_github_issue_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_github_issue_task_params_issue_type import CreateGithubIssueTaskParamsIssueType
    from ..models.create_github_issue_task_params_labels_item import CreateGithubIssueTaskParamsLabelsItem
    from ..models.create_github_issue_task_params_repository import CreateGithubIssueTaskParamsRepository


T = TypeVar("T", bound="CreateGithubIssueTaskParams")


@_attrs_define
class CreateGithubIssueTaskParams:
    """
    Attributes:
        title (str): The issue title
        repository (CreateGithubIssueTaskParamsRepository):
        task_type (CreateGithubIssueTaskParamsTaskType | Unset):
        body (str | Unset): The issue body
        labels (list[CreateGithubIssueTaskParamsLabelsItem] | Unset): The issue labels
        issue_type (CreateGithubIssueTaskParamsIssueType | Unset): The issue type
        parent_issue_number (None | str | Unset): The parent issue number for sub-issue linking
    """

    title: str
    repository: CreateGithubIssueTaskParamsRepository
    task_type: CreateGithubIssueTaskParamsTaskType | Unset = UNSET
    body: str | Unset = UNSET
    labels: list[CreateGithubIssueTaskParamsLabelsItem] | Unset = UNSET
    issue_type: CreateGithubIssueTaskParamsIssueType | Unset = UNSET
    parent_issue_number: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        repository = self.repository.to_dict()

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        body = self.body

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        issue_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue_type, Unset):
            issue_type = self.issue_type.to_dict()

        parent_issue_number: None | str | Unset
        if isinstance(self.parent_issue_number, Unset):
            parent_issue_number = UNSET
        else:
            parent_issue_number = self.parent_issue_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "repository": repository,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if body is not UNSET:
            field_dict["body"] = body
        if labels is not UNSET:
            field_dict["labels"] = labels
        if issue_type is not UNSET:
            field_dict["issue_type"] = issue_type
        if parent_issue_number is not UNSET:
            field_dict["parent_issue_number"] = parent_issue_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_github_issue_task_params_issue_type import CreateGithubIssueTaskParamsIssueType
        from ..models.create_github_issue_task_params_labels_item import CreateGithubIssueTaskParamsLabelsItem
        from ..models.create_github_issue_task_params_repository import CreateGithubIssueTaskParamsRepository

        d = dict(src_dict)
        title = d.pop("title")

        repository = CreateGithubIssueTaskParamsRepository.from_dict(d.pop("repository"))

        _task_type = d.pop("task_type", UNSET)
        task_type: CreateGithubIssueTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_github_issue_task_params_task_type(_task_type)

        body = d.pop("body", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[CreateGithubIssueTaskParamsLabelsItem] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = CreateGithubIssueTaskParamsLabelsItem.from_dict(labels_item_data)

                labels.append(labels_item)

        _issue_type = d.pop("issue_type", UNSET)
        issue_type: CreateGithubIssueTaskParamsIssueType | Unset
        if isinstance(_issue_type, Unset):
            issue_type = UNSET
        else:
            issue_type = CreateGithubIssueTaskParamsIssueType.from_dict(_issue_type)

        def _parse_parent_issue_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_issue_number = _parse_parent_issue_number(d.pop("parent_issue_number", UNSET))

        create_github_issue_task_params = cls(
            title=title,
            repository=repository,
            task_type=task_type,
            body=body,
            labels=labels,
            issue_type=issue_type,
            parent_issue_number=parent_issue_number,
        )

        create_github_issue_task_params.additional_properties = d
        return create_github_issue_task_params

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
