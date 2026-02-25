from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_incident_action_item_data_attributes_kind import (
    UpdateIncidentActionItemDataAttributesKind,
    check_update_incident_action_item_data_attributes_kind,
)
from ..models.update_incident_action_item_data_attributes_priority import (
    UpdateIncidentActionItemDataAttributesPriority,
    check_update_incident_action_item_data_attributes_priority,
)
from ..models.update_incident_action_item_data_attributes_status import (
    UpdateIncidentActionItemDataAttributesStatus,
    check_update_incident_action_item_data_attributes_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateIncidentActionItemDataAttributes")


@_attrs_define
class UpdateIncidentActionItemDataAttributes:
    """
    Attributes:
        summary (Union[Unset, str]): The summary of the action item
        description (Union[None, Unset, str]): The description of the action item
        kind (Union[Unset, UpdateIncidentActionItemDataAttributesKind]): The kind of the action item
        assigned_to_user_id (Union[None, Unset, int]): ID of user you wish to assign this action item
        assigned_to_group_ids (Union[None, Unset, list[str]]): IDs of groups you wish to assign this action item
        priority (Union[Unset, UpdateIncidentActionItemDataAttributesPriority]): The priority of the action item
        status (Union[Unset, UpdateIncidentActionItemDataAttributesStatus]): The status of the action item
        due_date (Union[None, Unset, str]): The due date of the action item
        jira_issue_id (Union[None, Unset, str]): The Jira issue ID.
        jira_issue_key (Union[None, Unset, str]): The Jira issue key.
        jira_issue_url (Union[None, Unset, str]): The Jira issue URL.
    """

    summary: Unset | str = UNSET
    description: None | Unset | str = UNSET
    kind: Unset | UpdateIncidentActionItemDataAttributesKind = UNSET
    assigned_to_user_id: None | Unset | int = UNSET
    assigned_to_group_ids: None | Unset | list[str] = UNSET
    priority: Unset | UpdateIncidentActionItemDataAttributesPriority = UNSET
    status: Unset | UpdateIncidentActionItemDataAttributesStatus = UNSET
    due_date: None | Unset | str = UNSET
    jira_issue_id: None | Unset | str = UNSET
    jira_issue_key: None | Unset | str = UNSET
    jira_issue_url: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        kind: Unset | str = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        assigned_to_user_id: None | Unset | int
        if isinstance(self.assigned_to_user_id, Unset):
            assigned_to_user_id = UNSET
        else:
            assigned_to_user_id = self.assigned_to_user_id

        assigned_to_group_ids: None | Unset | list[str]
        if isinstance(self.assigned_to_group_ids, Unset):
            assigned_to_group_ids = UNSET
        elif isinstance(self.assigned_to_group_ids, list):
            assigned_to_group_ids = self.assigned_to_group_ids

        else:
            assigned_to_group_ids = self.assigned_to_group_ids

        priority: Unset | str = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        due_date: None | Unset | str
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        else:
            due_date = self.due_date

        jira_issue_id: None | Unset | str
        if isinstance(self.jira_issue_id, Unset):
            jira_issue_id = UNSET
        else:
            jira_issue_id = self.jira_issue_id

        jira_issue_key: None | Unset | str
        if isinstance(self.jira_issue_key, Unset):
            jira_issue_key = UNSET
        else:
            jira_issue_key = self.jira_issue_key

        jira_issue_url: None | Unset | str
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
        if kind is not UNSET:
            field_dict["kind"] = kind
        if assigned_to_user_id is not UNSET:
            field_dict["assigned_to_user_id"] = assigned_to_user_id
        if assigned_to_group_ids is not UNSET:
            field_dict["assigned_to_group_ids"] = assigned_to_group_ids
        if priority is not UNSET:
            field_dict["priority"] = priority
        if status is not UNSET:
            field_dict["status"] = status
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if jira_issue_id is not UNSET:
            field_dict["jira_issue_id"] = jira_issue_id
        if jira_issue_key is not UNSET:
            field_dict["jira_issue_key"] = jira_issue_key
        if jira_issue_url is not UNSET:
            field_dict["jira_issue_url"] = jira_issue_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        summary = d.pop("summary", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: Unset | UpdateIncidentActionItemDataAttributesKind
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_update_incident_action_item_data_attributes_kind(_kind)

        def _parse_assigned_to_user_id(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        assigned_to_user_id = _parse_assigned_to_user_id(d.pop("assigned_to_user_id", UNSET))

        def _parse_assigned_to_group_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_to_group_ids_type_0 = cast(list[str], data)

                return assigned_to_group_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        assigned_to_group_ids = _parse_assigned_to_group_ids(d.pop("assigned_to_group_ids", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: Unset | UpdateIncidentActionItemDataAttributesPriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = check_update_incident_action_item_data_attributes_priority(_priority)

        _status = d.pop("status", UNSET)
        status: Unset | UpdateIncidentActionItemDataAttributesStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_incident_action_item_data_attributes_status(_status)

        def _parse_due_date(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        def _parse_jira_issue_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        jira_issue_id = _parse_jira_issue_id(d.pop("jira_issue_id", UNSET))

        def _parse_jira_issue_key(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        jira_issue_key = _parse_jira_issue_key(d.pop("jira_issue_key", UNSET))

        def _parse_jira_issue_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        jira_issue_url = _parse_jira_issue_url(d.pop("jira_issue_url", UNSET))

        update_incident_action_item_data_attributes = cls(
            summary=summary,
            description=description,
            kind=kind,
            assigned_to_user_id=assigned_to_user_id,
            assigned_to_group_ids=assigned_to_group_ids,
            priority=priority,
            status=status,
            due_date=due_date,
            jira_issue_id=jira_issue_id,
            jira_issue_key=jira_issue_key,
            jira_issue_url=jira_issue_url,
        )

        return update_incident_action_item_data_attributes
