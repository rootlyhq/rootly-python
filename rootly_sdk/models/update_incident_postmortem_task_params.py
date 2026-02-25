from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_incident_postmortem_task_params_task_type import (
    UpdateIncidentPostmortemTaskParamsTaskType,
    check_update_incident_postmortem_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateIncidentPostmortemTaskParams")


@_attrs_define
class UpdateIncidentPostmortemTaskParams:
    """
    Attributes:
        postmortem_id (str): UUID of the retrospective that needs to be updated
        task_type (Union[Unset, UpdateIncidentPostmortemTaskParamsTaskType]):
        title (Union[None, Unset, str]): The incident title
        status (Union[None, Unset, str]):
    """

    postmortem_id: str
    task_type: Unset | UpdateIncidentPostmortemTaskParamsTaskType = UNSET
    title: None | Unset | str = UNSET
    status: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        postmortem_id = self.postmortem_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title: None | Unset | str
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        status: None | Unset | str
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "postmortem_id": postmortem_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        postmortem_id = d.pop("postmortem_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateIncidentPostmortemTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_incident_postmortem_task_params_task_type(_task_type)

        def _parse_title(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_status(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        status = _parse_status(d.pop("status", UNSET))

        update_incident_postmortem_task_params = cls(
            postmortem_id=postmortem_id,
            task_type=task_type,
            title=title,
            status=status,
        )

        update_incident_postmortem_task_params.additional_properties = d
        return update_incident_postmortem_task_params

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
