from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_problem_action_item_data_attributes_priority import (
    UpdateProblemActionItemDataAttributesPriority,
    check_update_problem_action_item_data_attributes_priority,
)
from ..models.update_problem_action_item_data_attributes_status import (
    UpdateProblemActionItemDataAttributesStatus,
    check_update_problem_action_item_data_attributes_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateProblemActionItemDataAttributes")


@_attrs_define
class UpdateProblemActionItemDataAttributes:
    """
    Attributes:
        summary (str | Unset): The summary of the action item
        description (None | str | Unset): The description of the action item
        assigned_to_user_id (int | None | Unset): ID of user you wish to assign this action item
        priority (UpdateProblemActionItemDataAttributesPriority | Unset): The priority of the action item
        status (UpdateProblemActionItemDataAttributesStatus | Unset): The status of the action item
        due_date (None | str | Unset): The due date of the action item
        jira_issue_url (None | str | Unset): The Jira issue URL.
    """

    summary: str | Unset = UNSET
    description: None | str | Unset = UNSET
    assigned_to_user_id: int | None | Unset = UNSET
    priority: UpdateProblemActionItemDataAttributesPriority | Unset = UNSET
    status: UpdateProblemActionItemDataAttributesStatus | Unset = UNSET
    due_date: None | str | Unset = UNSET
    jira_issue_url: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        assigned_to_user_id: int | None | Unset
        if isinstance(self.assigned_to_user_id, Unset):
            assigned_to_user_id = UNSET
        else:
            assigned_to_user_id = self.assigned_to_user_id

        priority: str | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        due_date: None | str | Unset
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        else:
            due_date = self.due_date

        jira_issue_url: None | str | Unset
        if isinstance(self.jira_issue_url, Unset):
            jira_issue_url = UNSET
        else:
            jira_issue_url = self.jira_issue_url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if summary is not UNSET:
            field_dict["summary"] = summary
        if description is not UNSET:
            field_dict["description"] = description
        if assigned_to_user_id is not UNSET:
            field_dict["assigned_to_user_id"] = assigned_to_user_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if status is not UNSET:
            field_dict["status"] = status
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if jira_issue_url is not UNSET:
            field_dict["jira_issue_url"] = jira_issue_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        summary = d.pop("summary", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_assigned_to_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        assigned_to_user_id = _parse_assigned_to_user_id(d.pop("assigned_to_user_id", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: UpdateProblemActionItemDataAttributesPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = check_update_problem_action_item_data_attributes_priority(_priority)

        _status = d.pop("status", UNSET)
        status: UpdateProblemActionItemDataAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_problem_action_item_data_attributes_status(_status)

        def _parse_due_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        def _parse_jira_issue_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jira_issue_url = _parse_jira_issue_url(d.pop("jira_issue_url", UNSET))

        update_problem_action_item_data_attributes = cls(
            summary=summary,
            description=description,
            assigned_to_user_id=assigned_to_user_id,
            priority=priority,
            status=status,
            due_date=due_date,
            jira_issue_url=jira_issue_url,
        )

        return update_problem_action_item_data_attributes
