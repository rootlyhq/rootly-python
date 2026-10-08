from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attach_retrospective_pdf_to_jira_issue_task_params_task_type import (
    AttachRetrospectivePdfToJiraIssueTaskParamsTaskType,
    check_attach_retrospective_pdf_to_jira_issue_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attach_retrospective_pdf_to_jira_issue_task_params_integration import (
        AttachRetrospectivePdfToJiraIssueTaskParamsIntegration,
    )


T = TypeVar("T", bound="AttachRetrospectivePdfToJiraIssueTaskParams")


@_attrs_define
class AttachRetrospectivePdfToJiraIssueTaskParams:
    """
    Attributes:
        issue_id (str): The issue id
        task_type (AttachRetrospectivePdfToJiraIssueTaskParamsTaskType | Unset):
        integration (AttachRetrospectivePdfToJiraIssueTaskParamsIntegration | Unset): Specify integration id if you have
            more than one Jira instance
        filename (str | Unset): The attachment filename
    """

    issue_id: str
    task_type: AttachRetrospectivePdfToJiraIssueTaskParamsTaskType | Unset = UNSET
    integration: AttachRetrospectivePdfToJiraIssueTaskParamsIntegration | Unset = UNSET
    filename: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_id = self.issue_id

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        integration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.integration, Unset):
            integration = self.integration.to_dict()

        filename = self.filename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_id": issue_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if integration is not UNSET:
            field_dict["integration"] = integration
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attach_retrospective_pdf_to_jira_issue_task_params_integration import (
            AttachRetrospectivePdfToJiraIssueTaskParamsIntegration,
        )

        d = dict(src_dict)
        issue_id = d.pop("issue_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: AttachRetrospectivePdfToJiraIssueTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_attach_retrospective_pdf_to_jira_issue_task_params_task_type(_task_type)

        _integration = d.pop("integration", UNSET)
        integration: AttachRetrospectivePdfToJiraIssueTaskParamsIntegration | Unset
        if isinstance(_integration, Unset):
            integration = UNSET
        else:
            integration = AttachRetrospectivePdfToJiraIssueTaskParamsIntegration.from_dict(_integration)

        filename = d.pop("filename", UNSET)

        attach_retrospective_pdf_to_jira_issue_task_params = cls(
            issue_id=issue_id,
            task_type=task_type,
            integration=integration,
            filename=filename,
        )

        attach_retrospective_pdf_to_jira_issue_task_params.additional_properties = d
        return attach_retrospective_pdf_to_jira_issue_task_params

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
