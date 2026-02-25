from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_github_issue_task_params_task_type import (
    CreateGithubIssueTaskParamsTaskType,
    check_create_github_issue_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
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
    """

    title: str
    repository: "CreateGithubIssueTaskParamsRepository"
    task_type: Unset | CreateGithubIssueTaskParamsTaskType = UNSET
    body: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        repository = self.repository.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        body = self.body

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        create_github_issue_task_params = cls(
            title=title,
            repository=repository,
            task_type=task_type,
            body=body,
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
