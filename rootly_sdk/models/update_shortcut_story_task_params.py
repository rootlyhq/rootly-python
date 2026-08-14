from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_shortcut_story_task_params_task_type import (
    UpdateShortcutStoryTaskParamsTaskType,
    check_update_shortcut_story_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_shortcut_story_task_params_archivation import UpdateShortcutStoryTaskParamsArchivation


T = TypeVar("T", bound="UpdateShortcutStoryTaskParams")


@_attrs_define
class UpdateShortcutStoryTaskParams:
    """
    Attributes:
        story_id (str): The story id
        archivation (UpdateShortcutStoryTaskParamsArchivation): The archivation id and display name
        task_type (Union[Unset, UpdateShortcutStoryTaskParamsTaskType]):
        title (Union[Unset, str]): The incident title
        description (Union[Unset, str]): The incident description
        labels (Union[Unset, str]): The story labels
        due_date (Union[Unset, str]): The due date
    """

    story_id: str
    archivation: "UpdateShortcutStoryTaskParamsArchivation"
    task_type: Unset | UpdateShortcutStoryTaskParamsTaskType = UNSET
    title: Unset | str = UNSET
    description: Unset | str = UNSET
    labels: Unset | str = UNSET
    due_date: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        story_id = self.story_id

        archivation = self.archivation.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title = self.title

        description = self.description

        labels = self.labels

        due_date = self.due_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "story_id": story_id,
                "archivation": archivation,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels
        if due_date is not UNSET:
            field_dict["due_date"] = due_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_shortcut_story_task_params_archivation import UpdateShortcutStoryTaskParamsArchivation

        d = dict(src_dict)
        story_id = d.pop("story_id")

        archivation = UpdateShortcutStoryTaskParamsArchivation.from_dict(d.pop("archivation"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateShortcutStoryTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_shortcut_story_task_params_task_type(_task_type)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        labels = d.pop("labels", UNSET)

        due_date = d.pop("due_date", UNSET)

        update_shortcut_story_task_params = cls(
            story_id=story_id,
            archivation=archivation,
            task_type=task_type,
            title=title,
            description=description,
            labels=labels,
            due_date=due_date,
        )

        update_shortcut_story_task_params.additional_properties = d
        return update_shortcut_story_task_params

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
