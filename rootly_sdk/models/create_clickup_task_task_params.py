from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_clickup_task_task_params_task_type import (
    CreateClickupTaskTaskParamsTaskType,
    check_create_clickup_task_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_clickup_task_task_params_priority import CreateClickupTaskTaskParamsPriority


T = TypeVar("T", bound="CreateClickupTaskTaskParams")


@_attrs_define
class CreateClickupTaskTaskParams:
    """
    Attributes:
        title (str): The task title
        task_type (CreateClickupTaskTaskParamsTaskType | Unset):
        description (str | Unset): The task description
        tags (str | Unset): The task tags
        priority (CreateClickupTaskTaskParamsPriority | Unset): The priority id and display name
        due_date (str | Unset): The due date
        custom_fields_mapping (None | str | Unset): Custom field mappings. Can contain liquid markup and need to be
            valid JSON
        task_payload (None | str | Unset): Additional ClickUp task attributes. Will be merged into whatever was
            specified in this tasks current parameters. Can contain liquid markup and need to be valid JSON
    """

    title: str
    task_type: CreateClickupTaskTaskParamsTaskType | Unset = UNSET
    description: str | Unset = UNSET
    tags: str | Unset = UNSET
    priority: CreateClickupTaskTaskParamsPriority | Unset = UNSET
    due_date: str | Unset = UNSET
    custom_fields_mapping: None | str | Unset = UNSET
    task_payload: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        description = self.description

        tags = self.tags

        priority: dict[str, Any] | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.to_dict()

        due_date = self.due_date

        custom_fields_mapping: None | str | Unset
        if isinstance(self.custom_fields_mapping, Unset):
            custom_fields_mapping = UNSET
        else:
            custom_fields_mapping = self.custom_fields_mapping

        task_payload: None | str | Unset
        if isinstance(self.task_payload, Unset):
            task_payload = UNSET
        else:
            task_payload = self.task_payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
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
        from ..models.create_clickup_task_task_params_priority import CreateClickupTaskTaskParamsPriority

        d = dict(src_dict)
        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: CreateClickupTaskTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_clickup_task_task_params_task_type(_task_type)

        description = d.pop("description", UNSET)

        tags = d.pop("tags", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: CreateClickupTaskTaskParamsPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = CreateClickupTaskTaskParamsPriority.from_dict(_priority)

        due_date = d.pop("due_date", UNSET)

        def _parse_custom_fields_mapping(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_fields_mapping = _parse_custom_fields_mapping(d.pop("custom_fields_mapping", UNSET))

        def _parse_task_payload(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_payload = _parse_task_payload(d.pop("task_payload", UNSET))

        create_clickup_task_task_params = cls(
            title=title,
            task_type=task_type,
            description=description,
            tags=tags,
            priority=priority,
            due_date=due_date,
            custom_fields_mapping=custom_fields_mapping,
            task_payload=task_payload,
        )

        create_clickup_task_task_params.additional_properties = d
        return create_clickup_task_task_params

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
