from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_action_item_task_params_attribute_to_query_by import (
    UpdateActionItemTaskParamsAttributeToQueryBy,
    check_update_action_item_task_params_attribute_to_query_by,
)
from ..models.update_action_item_task_params_priority import (
    UpdateActionItemTaskParamsPriority,
    check_update_action_item_task_params_priority,
)
from ..models.update_action_item_task_params_status import (
    UpdateActionItemTaskParamsStatus,
    check_update_action_item_task_params_status,
)
from ..models.update_action_item_task_params_task_type import (
    UpdateActionItemTaskParamsTaskType,
    check_update_action_item_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_action_item_task_params_assigned_to_user import UpdateActionItemTaskParamsAssignedToUser


T = TypeVar("T", bound="UpdateActionItemTaskParams")


@_attrs_define
class UpdateActionItemTaskParams:
    """
    Attributes:
        query_value (str): Value that attribute_to_query_by to uses to match against
        attribute_to_query_by (UpdateActionItemTaskParamsAttributeToQueryBy): Attribute of the action item to match
            against Default: 'id'.
        task_type (Union[Unset, UpdateActionItemTaskParamsTaskType]):
        summary (Union[Unset, str]): Brief description of the action item
        assigned_to_user_id (Union[Unset, str]): [DEPRECATED] Use assigned_to_user attribute instead. The user id this
            action item is assigned to
        assigned_to_user (Union[Unset, UpdateActionItemTaskParamsAssignedToUser]):  The user this action item is
            assigned to
        group_ids (Union[None, Unset, list[str]]):
        description (Union[Unset, str]): The action item description
        priority (Union[Unset, UpdateActionItemTaskParamsPriority]): The action item priority
        status (Union[Unset, UpdateActionItemTaskParamsStatus]): The action item status
        custom_fields_mapping (Union[None, Unset, str]): Custom field mappings. Can contain liquid markup and need to be
            valid JSON
        post_to_incident_timeline (Union[Unset, bool]):
    """

    query_value: str
    attribute_to_query_by: UpdateActionItemTaskParamsAttributeToQueryBy = "id"
    task_type: Unset | UpdateActionItemTaskParamsTaskType = UNSET
    summary: Unset | str = UNSET
    assigned_to_user_id: Unset | str = UNSET
    assigned_to_user: Union[Unset, "UpdateActionItemTaskParamsAssignedToUser"] = UNSET
    group_ids: None | Unset | list[str] = UNSET
    description: Unset | str = UNSET
    priority: Unset | UpdateActionItemTaskParamsPriority = UNSET
    status: Unset | UpdateActionItemTaskParamsStatus = UNSET
    custom_fields_mapping: None | Unset | str = UNSET
    post_to_incident_timeline: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query_value = self.query_value

        attribute_to_query_by: str = self.attribute_to_query_by

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        summary = self.summary

        assigned_to_user_id = self.assigned_to_user_id

        assigned_to_user: Unset | dict[str, Any] = UNSET
        if not isinstance(self.assigned_to_user, Unset):
            assigned_to_user = self.assigned_to_user.to_dict()

        group_ids: None | Unset | list[str]
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        description = self.description

        priority: Unset | str = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        custom_fields_mapping: None | Unset | str
        if isinstance(self.custom_fields_mapping, Unset):
            custom_fields_mapping = UNSET
        else:
            custom_fields_mapping = self.custom_fields_mapping

        post_to_incident_timeline = self.post_to_incident_timeline

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query_value": query_value,
                "attribute_to_query_by": attribute_to_query_by,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if summary is not UNSET:
            field_dict["summary"] = summary
        if assigned_to_user_id is not UNSET:
            field_dict["assigned_to_user_id"] = assigned_to_user_id
        if assigned_to_user is not UNSET:
            field_dict["assigned_to_user"] = assigned_to_user
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if description is not UNSET:
            field_dict["description"] = description
        if priority is not UNSET:
            field_dict["priority"] = priority
        if status is not UNSET:
            field_dict["status"] = status
        if custom_fields_mapping is not UNSET:
            field_dict["custom_fields_mapping"] = custom_fields_mapping
        if post_to_incident_timeline is not UNSET:
            field_dict["post_to_incident_timeline"] = post_to_incident_timeline

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_action_item_task_params_assigned_to_user import UpdateActionItemTaskParamsAssignedToUser

        d = dict(src_dict)
        query_value = d.pop("query_value")

        attribute_to_query_by = check_update_action_item_task_params_attribute_to_query_by(
            d.pop("attribute_to_query_by")
        )

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateActionItemTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_action_item_task_params_task_type(_task_type)

        summary = d.pop("summary", UNSET)

        assigned_to_user_id = d.pop("assigned_to_user_id", UNSET)

        _assigned_to_user = d.pop("assigned_to_user", UNSET)
        assigned_to_user: Unset | UpdateActionItemTaskParamsAssignedToUser
        if isinstance(_assigned_to_user, Unset):
            assigned_to_user = UNSET
        else:
            assigned_to_user = UpdateActionItemTaskParamsAssignedToUser.from_dict(_assigned_to_user)

        def _parse_group_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = cast(list[str], data)

                return group_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        description = d.pop("description", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Unset | UpdateActionItemTaskParamsPriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = check_update_action_item_task_params_priority(_priority)

        _status = d.pop("status", UNSET)
        status: Unset | UpdateActionItemTaskParamsStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_action_item_task_params_status(_status)

        def _parse_custom_fields_mapping(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        post_to_incident_timeline = d.pop("post_to_incident_timeline", UNSET)

        update_action_item_task_params = cls(
            query_value=query_value,
            attribute_to_query_by=attribute_to_query_by,
            task_type=task_type,
            summary=summary,
            assigned_to_user_id=assigned_to_user_id,
            assigned_to_user=assigned_to_user,
            group_ids=group_ids,
            description=description,
            priority=priority,
            status=status,
            custom_fields_mapping=custom_fields_mapping,
            post_to_incident_timeline=post_to_incident_timeline,
        )

        update_action_item_task_params.additional_properties = d
        return update_action_item_task_params

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
