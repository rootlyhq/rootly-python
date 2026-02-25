from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_sub_incident_task_params_task_type import (
    CreateSubIncidentTaskParamsTaskType,
    check_create_sub_incident_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSubIncidentTaskParams")


@_attrs_define
class CreateSubIncidentTaskParams:
    """
    Attributes:
        title (str): The sub incident title
        task_type (Union[Unset, CreateSubIncidentTaskParamsTaskType]):
        summary (Union[Unset, str]): The sub incident summary
    """

    title: str
    task_type: Unset | CreateSubIncidentTaskParamsTaskType = UNSET
    summary: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateSubIncidentTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_sub_incident_task_params_task_type(_task_type)

        summary = d.pop("summary", UNSET)

        create_sub_incident_task_params = cls(
            title=title,
            task_type=task_type,
            summary=summary,
        )

        create_sub_incident_task_params.additional_properties = d
        return create_sub_incident_task_params

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
