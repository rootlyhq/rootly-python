from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_team_task_params_task_type import AddTeamTaskParamsTaskType, check_add_team_task_params_task_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddTeamTaskParams")


@_attrs_define
class AddTeamTaskParams:
    """
    Attributes:
        group_id (str): The team id
        task_type (Union[Unset, AddTeamTaskParamsTaskType]):
    """

    group_id: str
    task_type: Unset | AddTeamTaskParamsTaskType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_id": group_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_id = d.pop("group_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | AddTeamTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_add_team_task_params_task_type(_task_type)

        add_team_task_params = cls(
            group_id=group_id,
            task_type=task_type,
        )

        add_team_task_params.additional_properties = d
        return add_team_task_params

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
