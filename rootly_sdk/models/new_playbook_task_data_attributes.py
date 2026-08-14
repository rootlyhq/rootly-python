from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewPlaybookTaskDataAttributes")


@_attrs_define
class NewPlaybookTaskDataAttributes:
    """
    Attributes:
        task (str): The task of the task
        description (Union[None, Unset, str]): The description of the task
        position (Union[None, Unset, int]): The position of the task
    """

    task: str
    description: None | Unset | str = UNSET
    position: None | Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        task = self.task

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        position: None | Unset | int
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "task": task,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task = d.pop("task")

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        new_playbook_task_data_attributes = cls(
            task=task,
            description=description,
            position=position,
        )

        return new_playbook_task_data_attributes
