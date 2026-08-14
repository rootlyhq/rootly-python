from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_action_item_task_params_attribute_to_query_by import (
    AddActionItemTaskParamsAttributeToQueryBy,
    check_add_action_item_task_params_attribute_to_query_by,
)
from ..models.add_action_item_task_params_priority import (
    AddActionItemTaskParamsPriority,
    check_add_action_item_task_params_priority,
)
from ..models.add_action_item_task_params_status import (
    AddActionItemTaskParamsStatus,
    check_add_action_item_task_params_status,
)
from ..models.add_action_item_task_params_task_type import (
    AddActionItemTaskParamsTaskType,
    check_add_action_item_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_action_item_task_params_assigned_to_user import AddActionItemTaskParamsAssignedToUser
    from ..models.add_action_item_task_params_post_to_slack_channels_item import (
        AddActionItemTaskParamsPostToSlackChannelsItem,
    )


T = TypeVar("T", bound="AddActionItemTaskParams")


@_attrs_define
class AddActionItemTaskParams:
    """
    Attributes:
        priority (AddActionItemTaskParamsPriority): The action item priority
        summary (str): The action item summary
        status (AddActionItemTaskParamsStatus): The action item status
        task_type (Union[Unset, AddActionItemTaskParamsTaskType]):
        attribute_to_query_by (Union[Unset, AddActionItemTaskParamsAttributeToQueryBy]): Attribute of the Incident to
            match against
        query_value (Union[None, Unset, str]): Value that attribute_to_query_by to uses to match against
        incident_role_id (Union[Unset, str]): The role id this action item is associated with
        assigned_to_user_id (Union[Unset, str]): [DEPRECATED] Use assigned_to_user attribute instead. The user id this
            action item is assigned to
        assigned_to_user (Union[Unset, AddActionItemTaskParamsAssignedToUser]):  The user this action item is assigned
            to
        kind (Union[Unset, str]): The action item kind
        description (Union[Unset, str]): The action item description
        post_to_incident_timeline (Union[Unset, bool]):
        custom_fields_mapping (Union[None, Unset, str]): Custom field mappings. Can contain liquid markup and need to be
            valid JSON
        post_to_slack_channels (Union[Unset, list['AddActionItemTaskParamsPostToSlackChannelsItem']]):
    """

    priority: AddActionItemTaskParamsPriority
    summary: str
    status: AddActionItemTaskParamsStatus
    task_type: Unset | AddActionItemTaskParamsTaskType = UNSET
    attribute_to_query_by: Unset | AddActionItemTaskParamsAttributeToQueryBy = UNSET
    query_value: None | Unset | str = UNSET
    incident_role_id: Unset | str = UNSET
    assigned_to_user_id: Unset | str = UNSET
    assigned_to_user: Union[Unset, "AddActionItemTaskParamsAssignedToUser"] = UNSET
    kind: Unset | str = UNSET
    description: Unset | str = UNSET
    post_to_incident_timeline: Unset | bool = UNSET
    custom_fields_mapping: None | Unset | str = UNSET
    post_to_slack_channels: Unset | list["AddActionItemTaskParamsPostToSlackChannelsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        priority: str = self.priority

        summary = self.summary

        status: str = self.status

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        attribute_to_query_by: Unset | str = UNSET
        if not isinstance(self.attribute_to_query_by, Unset):
            attribute_to_query_by = self.attribute_to_query_by

        query_value: None | Unset | str
        if isinstance(self.query_value, Unset):
            query_value = UNSET
        else:
            query_value = self.query_value

        incident_role_id = self.incident_role_id

        assigned_to_user_id = self.assigned_to_user_id

        assigned_to_user: Unset | dict[str, Any] = UNSET
        if not isinstance(self.assigned_to_user, Unset):
            assigned_to_user = self.assigned_to_user.to_dict()

        kind = self.kind

        description = self.description

        post_to_incident_timeline = self.post_to_incident_timeline

        custom_fields_mapping: None | Unset | str
        if isinstance(self.custom_fields_mapping, Unset):
            custom_fields_mapping = UNSET
        else:
            custom_fields_mapping = self.custom_fields_mapping

        post_to_slack_channels: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.post_to_slack_channels, Unset):
            post_to_slack_channels = []
            for post_to_slack_channels_item_data in self.post_to_slack_channels:
                post_to_slack_channels_item = post_to_slack_channels_item_data.to_dict()
                post_to_slack_channels.append(post_to_slack_channels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "priority": priority,
                "summary": summary,
                "status": status,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if attribute_to_query_by is not UNSET:
            field_dict["attribute_to_query_by"] = attribute_to_query_by
        if query_value is not UNSET:
            field_dict["query_value"] = query_value
        if incident_role_id is not UNSET:
            field_dict["incident_role_id"] = incident_role_id
        if assigned_to_user_id is not UNSET:
            field_dict["assigned_to_user_id"] = assigned_to_user_id
        if assigned_to_user is not UNSET:
            field_dict["assigned_to_user"] = assigned_to_user
        if kind is not UNSET:
            field_dict["kind"] = kind
        if description is not UNSET:
            field_dict["description"] = description
        if post_to_incident_timeline is not UNSET:
            field_dict["post_to_incident_timeline"] = post_to_incident_timeline
        if custom_fields_mapping is not UNSET:
            field_dict["custom_fields_mapping"] = custom_fields_mapping
        if post_to_slack_channels is not UNSET:
            field_dict["post_to_slack_channels"] = post_to_slack_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_action_item_task_params_assigned_to_user import AddActionItemTaskParamsAssignedToUser
        from ..models.add_action_item_task_params_post_to_slack_channels_item import (
            AddActionItemTaskParamsPostToSlackChannelsItem,
        )

        d = dict(src_dict)
        priority = check_add_action_item_task_params_priority(d.pop("priority"))

        summary = d.pop("summary")

        status = check_add_action_item_task_params_status(d.pop("status"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | AddActionItemTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_add_action_item_task_params_task_type(_task_type)

        _attribute_to_query_by = d.pop("attribute_to_query_by", UNSET)
        attribute_to_query_by: Unset | AddActionItemTaskParamsAttributeToQueryBy
        if isinstance(_attribute_to_query_by, Unset):
            attribute_to_query_by = UNSET
        else:
            attribute_to_query_by = check_add_action_item_task_params_attribute_to_query_by(_attribute_to_query_by)

        def _parse_query_value(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        query_value = _parse_query_value(d.pop("query_value", UNSET))

        incident_role_id = d.pop("incident_role_id", UNSET)

        assigned_to_user_id = d.pop("assigned_to_user_id", UNSET)

        _assigned_to_user = d.pop("assigned_to_user", UNSET)
        assigned_to_user: Unset | AddActionItemTaskParamsAssignedToUser
        if isinstance(_assigned_to_user, Unset):
            assigned_to_user = UNSET
        else:
            assigned_to_user = AddActionItemTaskParamsAssignedToUser.from_dict(_assigned_to_user)

        kind = d.pop("kind", UNSET)

        description = d.pop("description", UNSET)

        post_to_incident_timeline = d.pop("post_to_incident_timeline", UNSET)

        def _parse_custom_fields_mapping(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        post_to_slack_channels = []
        _post_to_slack_channels = d.pop("post_to_slack_channels", UNSET)
        for post_to_slack_channels_item_data in _post_to_slack_channels or []:
            post_to_slack_channels_item = AddActionItemTaskParamsPostToSlackChannelsItem.from_dict(
                post_to_slack_channels_item_data
            )

            post_to_slack_channels.append(post_to_slack_channels_item)

        add_action_item_task_params = cls(
            priority=priority,
            summary=summary,
            status=status,
            task_type=task_type,
            attribute_to_query_by=attribute_to_query_by,
            query_value=query_value,
            incident_role_id=incident_role_id,
            assigned_to_user_id=assigned_to_user_id,
            assigned_to_user=assigned_to_user,
            kind=kind,
            description=description,
            post_to_incident_timeline=post_to_incident_timeline,
            custom_fields_mapping=custom_fields_mapping,
            post_to_slack_channels=post_to_slack_channels,
        )

        add_action_item_task_params.additional_properties = d
        return add_action_item_task_params

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
