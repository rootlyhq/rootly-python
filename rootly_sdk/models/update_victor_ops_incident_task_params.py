from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_victor_ops_incident_task_params_status import (
    UpdateVictorOpsIncidentTaskParamsStatus,
    check_update_victor_ops_incident_task_params_status,
)
from ..models.update_victor_ops_incident_task_params_task_type import (
    UpdateVictorOpsIncidentTaskParamsTaskType,
    check_update_victor_ops_incident_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateVictorOpsIncidentTaskParams")


@_attrs_define
class UpdateVictorOpsIncidentTaskParams:
    """
    Attributes:
        victor_ops_incident_id (str): The victor_ops incident ID, this can also be a Rootly incident variable ex. {{
            incident.victor_ops_incident_id }}
        status (UpdateVictorOpsIncidentTaskParamsStatus):
        task_type (Union[Unset, UpdateVictorOpsIncidentTaskParamsTaskType]):
        resolution_message (Union[Unset, str]): Resolution message
    """

    victor_ops_incident_id: str
    status: UpdateVictorOpsIncidentTaskParamsStatus
    task_type: Unset | UpdateVictorOpsIncidentTaskParamsTaskType = UNSET
    resolution_message: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        victor_ops_incident_id = self.victor_ops_incident_id

        status: str = self.status

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        resolution_message = self.resolution_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "victor_ops_incident_id": victor_ops_incident_id,
                "status": status,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if resolution_message is not UNSET:
            field_dict["resolution_message"] = resolution_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        victor_ops_incident_id = d.pop("victor_ops_incident_id")

        status = check_update_victor_ops_incident_task_params_status(d.pop("status"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateVictorOpsIncidentTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_victor_ops_incident_task_params_task_type(_task_type)

        resolution_message = d.pop("resolution_message", UNSET)

        update_victor_ops_incident_task_params = cls(
            victor_ops_incident_id=victor_ops_incident_id,
            status=status,
            task_type=task_type,
            resolution_message=resolution_message,
        )

        update_victor_ops_incident_task_params.additional_properties = d
        return update_victor_ops_incident_task_params

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
