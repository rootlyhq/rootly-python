from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaybookTask")


@_attrs_define
class PlaybookTask:
    """
    Attributes:
        task (str): The task of the task
        created_at (str): Date of creation
        updated_at (str): Date of last update
        playbook_id (Union[Unset, str]):
        description (Union[None, Unset, str]): The description of task
        position (Union[None, Unset, int]): The position of the task
    """

    task: str
    created_at: str
    updated_at: str
    playbook_id: Unset | str = UNSET
    description: None | Unset | str = UNSET
    position: None | Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task = self.task

        created_at = self.created_at

        updated_at = self.updated_at

        playbook_id = self.playbook_id

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
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task": task,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if playbook_id is not UNSET:
            field_dict["playbook_id"] = playbook_id
        if description is not UNSET:
            field_dict["description"] = description
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task = d.pop("task")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        playbook_id = d.pop("playbook_id", UNSET)

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

        playbook_task = cls(
            task=task,
            created_at=created_at,
            updated_at=updated_at,
            playbook_id=playbook_id,
            description=description,
            position=position,
        )

        playbook_task.additional_properties = d
        return playbook_task

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
