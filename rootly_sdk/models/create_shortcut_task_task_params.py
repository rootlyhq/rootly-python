from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_shortcut_task_task_params_task_type import (
    CreateShortcutTaskTaskParamsTaskType,
    check_create_shortcut_task_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_shortcut_task_task_params_completion import CreateShortcutTaskTaskParamsCompletion


T = TypeVar("T", bound="CreateShortcutTaskTaskParams")


@_attrs_define
class CreateShortcutTaskTaskParams:
    """
    Attributes:
        parent_story_id (str): The parent story
        description (str): The task description
        completion (CreateShortcutTaskTaskParamsCompletion): The completion id and display name
        task_type (Union[Unset, CreateShortcutTaskTaskParamsTaskType]):
    """

    parent_story_id: str
    description: str
    completion: "CreateShortcutTaskTaskParamsCompletion"
    task_type: Unset | CreateShortcutTaskTaskParamsTaskType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_story_id = self.parent_story_id

        description = self.description

        completion = self.completion.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_story_id": parent_story_id,
                "description": description,
                "completion": completion,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_shortcut_task_task_params_completion import CreateShortcutTaskTaskParamsCompletion

        d = dict(src_dict)
        parent_story_id = d.pop("parent_story_id")

        description = d.pop("description")

        completion = CreateShortcutTaskTaskParamsCompletion.from_dict(d.pop("completion"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateShortcutTaskTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_shortcut_task_task_params_task_type(_task_type)

        create_shortcut_task_task_params = cls(
            parent_story_id=parent_story_id,
            description=description,
            completion=completion,
            task_type=task_type,
        )

        create_shortcut_task_task_params.additional_properties = d
        return create_shortcut_task_task_params

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
