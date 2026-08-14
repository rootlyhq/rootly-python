from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_incident_status_timestamp_task_params_task_type import (
    UpdateIncidentStatusTimestampTaskParamsTaskType,
    check_update_incident_status_timestamp_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateIncidentStatusTimestampTaskParams")


@_attrs_define
class UpdateIncidentStatusTimestampTaskParams:
    """
    Attributes:
        sub_status_id (str): Sub-status to update timestamp for
        assigned_at (str): Timestamp of when the sub-status was assigned
        task_type (Union[Unset, UpdateIncidentStatusTimestampTaskParamsTaskType]):
    """

    sub_status_id: str
    assigned_at: str
    task_type: Unset | UpdateIncidentStatusTimestampTaskParamsTaskType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sub_status_id = self.sub_status_id

        assigned_at = self.assigned_at

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sub_status_id": sub_status_id,
                "assigned_at": assigned_at,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sub_status_id = d.pop("sub_status_id")

        assigned_at = d.pop("assigned_at")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateIncidentStatusTimestampTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_incident_status_timestamp_task_params_task_type(_task_type)

        update_incident_status_timestamp_task_params = cls(
            sub_status_id=sub_status_id,
            assigned_at=assigned_at,
            task_type=task_type,
        )

        update_incident_status_timestamp_task_params.additional_properties = d
        return update_incident_status_timestamp_task_params

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
