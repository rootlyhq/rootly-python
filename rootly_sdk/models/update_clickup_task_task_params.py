from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_clickup_task_task_params_task_type import (
    UpdateClickupTaskTaskParamsTaskType,
    check_update_clickup_task_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_clickup_task_task_params_priority import UpdateClickupTaskTaskParamsPriority


T = TypeVar("T", bound="UpdateClickupTaskTaskParams")


@_attrs_define
class UpdateClickupTaskTaskParams:
    """
    Attributes:
        task_id (str): The task id
        task_type (Union[Unset, UpdateClickupTaskTaskParamsTaskType]):
        title (Union[Unset, str]): The task title
        description (Union[Unset, str]): The task description
        tags (Union[Unset, str]): The task tags
        priority (Union[Unset, UpdateClickupTaskTaskParamsPriority]): The priority id and display name
        due_date (Union[Unset, str]): The due date
        custom_fields_mapping (Union[None, Unset, str]): Custom field mappings. Can contain liquid markup and need to be
            valid JSON
        task_payload (Union[None, Unset, str]): Additional ClickUp task attributes. Will be merged into whatever was
            specified in this tasks current parameters. Can contain liquid markup and need to be valid JSON
    """

    task_id: str
    task_type: Unset | UpdateClickupTaskTaskParamsTaskType = UNSET
    title: Unset | str = UNSET
    description: Unset | str = UNSET
    tags: Unset | str = UNSET
    priority: Union[Unset, "UpdateClickupTaskTaskParamsPriority"] = UNSET
    due_date: Unset | str = UNSET
    custom_fields_mapping: None | Unset | str = UNSET
    task_payload: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title = self.title

        description = self.description

        tags = self.tags

        priority: Unset | dict[str, Any] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        due_date = self.due_date

        custom_fields_mapping: None | Unset | str
        if isinstance(self.custom_fields_mapping, Unset):
            custom_fields_mapping = UNSET
        else:
            custom_fields_mapping = self.custom_fields_mapping

        task_payload: None | Unset | str
        if isinstance(self.task_payload, Unset):
            task_payload = UNSET
        else:
            task_payload = self.task_payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_id": task_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if priority is not UNSET:
            field_dict["priority"] = priority
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if custom_fields_mapping is not UNSET:
            field_dict["custom_fields_mapping"] = custom_fields_mapping
        if task_payload is not UNSET:
            field_dict["task_payload"] = task_payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_clickup_task_task_params_priority import UpdateClickupTaskTaskParamsPriority

        d = dict(src_dict)
        task_id = d.pop("task_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateClickupTaskTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_clickup_task_task_params_task_type(_task_type)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        tags = d.pop("tags", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Unset | UpdateClickupTaskTaskParamsPriority
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = UpdateClickupTaskTaskParamsPriority.from_dict(_priority)

        due_date = d.pop("due_date", UNSET)

        def _parse_custom_fields_mapping(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        def _parse_task_payload(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        task_payload = _parse_task_payload(d.pop("task_payload", UNSET))

        update_clickup_task_task_params = cls(
            task_id=task_id,
            task_type=task_type,
            title=title,
            description=description,
            tags=tags,
            priority=priority,
            due_date=due_date,
            custom_fields_mapping=custom_fields_mapping,
            task_payload=task_payload,
        )

        update_clickup_task_task_params.additional_properties = d
        return update_clickup_task_task_params

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
