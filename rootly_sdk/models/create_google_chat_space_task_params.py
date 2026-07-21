from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_google_chat_space_task_params_task_type import (
    CreateGoogleChatSpaceTaskParamsTaskType,
    check_create_google_chat_space_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateGoogleChatSpaceTaskParams")


@_attrs_define
class CreateGoogleChatSpaceTaskParams:
    """
    Attributes:
        title (str):
        task_type (CreateGoogleChatSpaceTaskParamsTaskType | Unset):
        description (str | Unset):
        audience (str | Unset): Target audience resource name (e.g. audiences/default). Leave blank for private space.
    """

    title: str
    task_type: CreateGoogleChatSpaceTaskParamsTaskType | Unset = UNSET
    description: str | Unset = UNSET
    audience: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        task_type: str | Unset = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        description = self.description

        audience = self.audience

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
        if audience is not UNSET:
            field_dict["audience"] = audience

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: CreateGoogleChatSpaceTaskParamsTaskType | Unset
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_google_chat_space_task_params_task_type(_task_type)

        description = d.pop("description", UNSET)

        audience = d.pop("audience", UNSET)

        create_google_chat_space_task_params = cls(
            title=title,
            task_type=task_type,
            description=description,
            audience=audience,
        )

        create_google_chat_space_task_params.additional_properties = d
        return create_google_chat_space_task_params

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
