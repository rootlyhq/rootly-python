from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_shortcut_task_task_params_task_type import (
    UpdateShortcutTaskTaskParamsTaskType,
    check_update_shortcut_task_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_shortcut_task_task_params_completion import UpdateShortcutTaskTaskParamsCompletion


T = TypeVar("T", bound="UpdateShortcutTaskTaskParams")


@_attrs_define
class UpdateShortcutTaskTaskParams:
    """
    Attributes:
        task_id (str): The task id
        parent_story_id (str): The parent story
        completion (UpdateShortcutTaskTaskParamsCompletion): The completion id and display name
        task_type (Union[Unset, UpdateShortcutTaskTaskParamsTaskType]):
        description (Union[Unset, str]): The task description
    """

    task_id: str
    parent_story_id: str
    completion: "UpdateShortcutTaskTaskParamsCompletion"
    task_type: Unset | UpdateShortcutTaskTaskParamsTaskType = UNSET
    description: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        parent_story_id = self.parent_story_id

        completion = self.completion.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_id": task_id,
                "parent_story_id": parent_story_id,
                "completion": completion,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_shortcut_task_task_params_completion import UpdateShortcutTaskTaskParamsCompletion

        d = dict(src_dict)
        task_id = d.pop("task_id")

        parent_story_id = d.pop("parent_story_id")

        completion = UpdateShortcutTaskTaskParamsCompletion.from_dict(d.pop("completion"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateShortcutTaskTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_shortcut_task_task_params_task_type(_task_type)

        description = d.pop("description", UNSET)

        update_shortcut_task_task_params = cls(
            task_id=task_id,
            parent_story_id=parent_story_id,
            completion=completion,
            task_type=task_type,
            description=description,
        )

        update_shortcut_task_task_params.additional_properties = d
        return update_shortcut_task_task_params

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
