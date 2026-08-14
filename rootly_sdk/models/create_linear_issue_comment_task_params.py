from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_linear_issue_comment_task_params_task_type import (
    CreateLinearIssueCommentTaskParamsTaskType,
    check_create_linear_issue_comment_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLinearIssueCommentTaskParams")


@_attrs_define
class CreateLinearIssueCommentTaskParams:
    """
    Attributes:
        issue_id (str): The issue id
        body (str): The issue description
        task_type (Union[Unset, CreateLinearIssueCommentTaskParamsTaskType]):
    """

    issue_id: str
    body: str
    task_type: Unset | CreateLinearIssueCommentTaskParamsTaskType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id = self.issue_id

        body = self.body

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_id": issue_id,
                "body": body,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_id = d.pop("issue_id")

        body = d.pop("body")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateLinearIssueCommentTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_linear_issue_comment_task_params_task_type(_task_type)

        create_linear_issue_comment_task_params = cls(
            issue_id=issue_id,
            body=body,
            task_type=task_type,
        )

        create_linear_issue_comment_task_params.additional_properties = d
        return create_linear_issue_comment_task_params

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
