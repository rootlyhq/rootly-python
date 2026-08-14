from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
        task_type (Union[Unset, CreateGithubIssueTaskParamsTaskType]):
        body (Union[Unset, str]): The issue body
        labels (Union[Unset, list['CreateGithubIssueTaskParamsLabelsItem']]): The issue labels
        issue_type (Union[Unset, CreateGithubIssueTaskParamsIssueType]): The issue type
        parent_issue_number (Union[None, Unset, str]): The parent issue number for sub-issue linking
        custom_fields_mapping (Union[None, Unset, str]): Custom field mappings. Can contain liquid markup and need to be
            valid JSON
    """

    title: str
    repository: "CreateGithubIssueTaskParamsRepository"
    task_type: Unset | CreateGithubIssueTaskParamsTaskType = UNSET
    body: Unset | str = UNSET
    labels: Unset | list["CreateGithubIssueTaskParamsLabelsItem"] = UNSET
    issue_type: Union[Unset, "CreateGithubIssueTaskParamsIssueType"] = UNSET
    parent_issue_number: None | Unset | str = UNSET
    custom_fields_mapping: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        repository = self.repository.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        body = self.body

        labels: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        issue_type: Unset | dict[str, Any] = UNSET
        if not isinstance(self.issue_type, Unset):
            issue_type = self.issue_type.to_dict()

        parent_issue_number: None | Unset | str
        if isinstance(self.parent_issue_number, Unset):
            parent_issue_number = UNSET
        else:
            parent_issue_number = self.parent_issue_number

        custom_fields_mapping: None | Unset | str
        if isinstance(self.custom_fields_mapping, Unset):
            custom_fields_mapping = UNSET
        else:
            custom_fields_mapping = self.custom_fields_mapping

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
        if custom_fields_mapping is not UNSET:
            field_dict["custom_fields_mapping"] = custom_fields_mapping

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
        task_type: Unset | CreateGithubIssueTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_github_issue_task_params_task_type(_task_type)

        body = d.pop("body", UNSET)

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in _labels or []:
            labels_item = CreateGithubIssueTaskParamsLabelsItem.from_dict(labels_item_data)

            labels.append(labels_item)

        _issue_type = d.pop("issue_type", UNSET)
        issue_type: Unset | CreateGithubIssueTaskParamsIssueType
        if isinstance(_issue_type, Unset):
            issue_type = UNSET
        else:
            issue_type = CreateGithubIssueTaskParamsIssueType.from_dict(_issue_type)

        def _parse_parent_issue_number(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        parent_issue_number = _parse_parent_issue_number(d.pop("parent_issue_number", UNSET))

        def _parse_custom_fields_mapping(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        create_github_issue_task_params = cls(
            title=title,
            repository=repository,
            task_type=task_type,
            body=body,
            labels=labels,
            issue_type=issue_type,
            parent_issue_number=parent_issue_number,
            custom_fields_mapping=custom_fields_mapping,
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
