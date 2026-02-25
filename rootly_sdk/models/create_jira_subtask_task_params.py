from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_jira_subtask_task_params_task_type import (
    CreateJiraSubtaskTaskParamsTaskType,
    check_create_jira_subtask_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_jira_subtask_task_params_integration import CreateJiraSubtaskTaskParamsIntegration
    from ..models.create_jira_subtask_task_params_priority import CreateJiraSubtaskTaskParamsPriority
    from ..models.create_jira_subtask_task_params_status import CreateJiraSubtaskTaskParamsStatus
    from ..models.create_jira_subtask_task_params_subtask_issue_type import CreateJiraSubtaskTaskParamsSubtaskIssueType


T = TypeVar("T", bound="CreateJiraSubtaskTaskParams")


@_attrs_define
class CreateJiraSubtaskTaskParams:
    """
    Attributes:
        project_key (str): The project key
        parent_issue_id (str): The parent issue
        title (str): The issue title
        subtask_issue_type (CreateJiraSubtaskTaskParamsSubtaskIssueType): The issue type id and display name
        task_type (Union[Unset, CreateJiraSubtaskTaskParamsTaskType]):
        integration (Union[Unset, CreateJiraSubtaskTaskParamsIntegration]): Specify integration id if you have more than
            one Jira instance
        description (Union[Unset, str]): The issue description
        labels (Union[Unset, str]): The issue labels
        due_date (Union[Unset, str]): The due date
        assign_user_email (Union[Unset, str]): The assigned user's email
        reporter_user_email (Union[Unset, str]): The reporter user's email
        priority (Union[Unset, CreateJiraSubtaskTaskParamsPriority]): The priority id and display name
        status (Union[Unset, CreateJiraSubtaskTaskParamsStatus]): The status id and display name
        custom_fields_mapping (Union[None, Unset, str]): Custom field mappings. Can contain liquid markup and need to be
            valid JSON
        update_payload (Union[None, Unset, str]): Update payload. Can contain liquid markup and need to be valid JSON
    """

    project_key: str
    parent_issue_id: str
    title: str
    subtask_issue_type: "CreateJiraSubtaskTaskParamsSubtaskIssueType"
    task_type: Unset | CreateJiraSubtaskTaskParamsTaskType = UNSET
    integration: Union[Unset, "CreateJiraSubtaskTaskParamsIntegration"] = UNSET
    description: Unset | str = UNSET
    labels: Unset | str = UNSET
    due_date: Unset | str = UNSET
    assign_user_email: Unset | str = UNSET
    reporter_user_email: Unset | str = UNSET
    priority: Union[Unset, "CreateJiraSubtaskTaskParamsPriority"] = UNSET
    status: Union[Unset, "CreateJiraSubtaskTaskParamsStatus"] = UNSET
    custom_fields_mapping: None | Unset | str = UNSET
    update_payload: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_key = self.project_key

        parent_issue_id = self.parent_issue_id

        title = self.title

        subtask_issue_type = self.subtask_issue_type.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        integration: Unset | dict[str, Any] = UNSET
        if not isinstance(self.integration, Unset):
            integration = self.integration.to_dict()

        description = self.description

        labels = self.labels

        due_date = self.due_date

        assign_user_email = self.assign_user_email

        reporter_user_email = self.reporter_user_email

        priority: Unset | dict[str, Any] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        status: Unset | dict[str, Any] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        custom_fields_mapping: None | Unset | str
        if isinstance(self.custom_fields_mapping, Unset):
            custom_fields_mapping = UNSET
        else:
            custom_fields_mapping = self.custom_fields_mapping

        update_payload: None | Unset | str
        if isinstance(self.update_payload, Unset):
            update_payload = UNSET
        else:
            update_payload = self.update_payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_key": project_key,
                "parent_issue_id": parent_issue_id,
                "title": title,
                "subtask_issue_type": subtask_issue_type,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if integration is not UNSET:
            field_dict["integration"] = integration
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if assign_user_email is not UNSET:
            field_dict["assign_user_email"] = assign_user_email
        if reporter_user_email is not UNSET:
            field_dict["reporter_user_email"] = reporter_user_email
        if priority is not UNSET:
            field_dict["priority"] = priority
        if status is not UNSET:
            field_dict["status"] = status
        if custom_fields_mapping is not UNSET:
            field_dict["custom_fields_mapping"] = custom_fields_mapping
        if update_payload is not UNSET:
            field_dict["update_payload"] = update_payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_jira_subtask_task_params_integration import CreateJiraSubtaskTaskParamsIntegration
        from ..models.create_jira_subtask_task_params_priority import CreateJiraSubtaskTaskParamsPriority
        from ..models.create_jira_subtask_task_params_status import CreateJiraSubtaskTaskParamsStatus
        from ..models.create_jira_subtask_task_params_subtask_issue_type import (
            CreateJiraSubtaskTaskParamsSubtaskIssueType,
        )

        d = dict(src_dict)
        project_key = d.pop("project_key")

        parent_issue_id = d.pop("parent_issue_id")

        title = d.pop("title")

        subtask_issue_type = CreateJiraSubtaskTaskParamsSubtaskIssueType.from_dict(d.pop("subtask_issue_type"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateJiraSubtaskTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_jira_subtask_task_params_task_type(_task_type)

        _integration = d.pop("integration", UNSET)
        integration: Unset | CreateJiraSubtaskTaskParamsIntegration
        if isinstance(_integration, Unset):
            integration = UNSET
        else:
            integration = CreateJiraSubtaskTaskParamsIntegration.from_dict(_integration)

        description = d.pop("description", UNSET)

        labels = d.pop("labels", UNSET)

        due_date = d.pop("due_date", UNSET)

        assign_user_email = d.pop("assign_user_email", UNSET)

        reporter_user_email = d.pop("reporter_user_email", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Unset | CreateJiraSubtaskTaskParamsPriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CreateJiraSubtaskTaskParamsPriority.from_dict(_priority)

        _status = d.pop("status", UNSET)
        status: Unset | CreateJiraSubtaskTaskParamsStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateJiraSubtaskTaskParamsStatus.from_dict(_status)

        def _parse_custom_fields_mapping(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        def _parse_update_payload(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        update_payload = _parse_update_payload(d.pop("update_payload", UNSET))

        create_jira_subtask_task_params = cls(
            project_key=project_key,
            parent_issue_id=parent_issue_id,
            title=title,
            subtask_issue_type=subtask_issue_type,
            task_type=task_type,
            integration=integration,
            description=description,
            labels=labels,
            due_date=due_date,
            assign_user_email=assign_user_email,
            reporter_user_email=reporter_user_email,
            priority=priority,
            status=status,
            custom_fields_mapping=custom_fields_mapping,
            update_payload=update_payload,
        )

        create_jira_subtask_task_params.additional_properties = d
        return create_jira_subtask_task_params

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
