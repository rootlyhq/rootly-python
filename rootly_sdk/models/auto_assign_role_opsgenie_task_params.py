from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auto_assign_role_opsgenie_task_params_task_type import (
    AutoAssignRoleOpsgenieTaskParamsTaskType,
    check_auto_assign_role_opsgenie_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_assign_role_opsgenie_task_params_schedule import AutoAssignRoleOpsgenieTaskParamsSchedule


T = TypeVar("T", bound="AutoAssignRoleOpsgenieTaskParams")


@_attrs_define
class AutoAssignRoleOpsgenieTaskParams:
    """
    Attributes:
        incident_role_id (str): The role id
        schedule (AutoAssignRoleOpsgenieTaskParamsSchedule):
        task_type (Union[Unset, AutoAssignRoleOpsgenieTaskParamsTaskType]):
    """

    incident_role_id: str
    schedule: "AutoAssignRoleOpsgenieTaskParamsSchedule"
    task_type: Unset | AutoAssignRoleOpsgenieTaskParamsTaskType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_role_id = self.incident_role_id

        schedule = self.schedule.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_role_id": incident_role_id,
                "schedule": schedule,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_assign_role_opsgenie_task_params_schedule import AutoAssignRoleOpsgenieTaskParamsSchedule

        d = dict(src_dict)
        incident_role_id = d.pop("incident_role_id")

        schedule = AutoAssignRoleOpsgenieTaskParamsSchedule.from_dict(d.pop("schedule"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | AutoAssignRoleOpsgenieTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_auto_assign_role_opsgenie_task_params_task_type(_task_type)

        auto_assign_role_opsgenie_task_params = cls(
            incident_role_id=incident_role_id,
            schedule=schedule,
            task_type=task_type,
        )

        auto_assign_role_opsgenie_task_params.additional_properties = d
        return auto_assign_role_opsgenie_task_params

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
