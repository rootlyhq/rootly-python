from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auto_assign_role_rootly_task_params_task_type import (
    AutoAssignRoleRootlyTaskParamsTaskType,
    check_auto_assign_role_rootly_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_assign_role_rootly_task_params_escalation_policy_target import (
        AutoAssignRoleRootlyTaskParamsEscalationPolicyTarget,
    )
    from ..models.auto_assign_role_rootly_task_params_group_target import AutoAssignRoleRootlyTaskParamsGroupTarget
    from ..models.auto_assign_role_rootly_task_params_schedule_target import (
        AutoAssignRoleRootlyTaskParamsScheduleTarget,
    )
    from ..models.auto_assign_role_rootly_task_params_service_target import AutoAssignRoleRootlyTaskParamsServiceTarget
    from ..models.auto_assign_role_rootly_task_params_user_target import AutoAssignRoleRootlyTaskParamsUserTarget


T = TypeVar("T", bound="AutoAssignRoleRootlyTaskParams")


@_attrs_define
class AutoAssignRoleRootlyTaskParams:
    """
    Attributes:
        incident_role_id (str): The role id
        task_type (Union[Unset, AutoAssignRoleRootlyTaskParamsTaskType]):
        escalation_policy_target (Union[Unset, AutoAssignRoleRootlyTaskParamsEscalationPolicyTarget]):
        service_target (Union[Unset, AutoAssignRoleRootlyTaskParamsServiceTarget]):
        user_target (Union[Unset, AutoAssignRoleRootlyTaskParamsUserTarget]):
        group_target (Union[Unset, AutoAssignRoleRootlyTaskParamsGroupTarget]):
        schedule_target (Union[Unset, AutoAssignRoleRootlyTaskParamsScheduleTarget]):
    """

    incident_role_id: str
    task_type: Unset | AutoAssignRoleRootlyTaskParamsTaskType = UNSET
    escalation_policy_target: Union[Unset, "AutoAssignRoleRootlyTaskParamsEscalationPolicyTarget"] = UNSET
    service_target: Union[Unset, "AutoAssignRoleRootlyTaskParamsServiceTarget"] = UNSET
    user_target: Union[Unset, "AutoAssignRoleRootlyTaskParamsUserTarget"] = UNSET
    group_target: Union[Unset, "AutoAssignRoleRootlyTaskParamsGroupTarget"] = UNSET
    schedule_target: Union[Unset, "AutoAssignRoleRootlyTaskParamsScheduleTarget"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_role_id = self.incident_role_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        escalation_policy_target: Unset | dict[str, Any] = UNSET
        if not isinstance(self.escalation_policy_target, Unset):
            escalation_policy_target = self.escalation_policy_target.to_dict()

        service_target: Unset | dict[str, Any] = UNSET
        if not isinstance(self.service_target, Unset):
            service_target = self.service_target.to_dict()

        user_target: Unset | dict[str, Any] = UNSET
        if not isinstance(self.user_target, Unset):
            user_target = self.user_target.to_dict()

        group_target: Unset | dict[str, Any] = UNSET
        if not isinstance(self.group_target, Unset):
            group_target = self.group_target.to_dict()

        schedule_target: Unset | dict[str, Any] = UNSET
        if not isinstance(self.schedule_target, Unset):
            schedule_target = self.schedule_target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_role_id": incident_role_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if escalation_policy_target is not UNSET:
            field_dict["escalation_policy_target"] = escalation_policy_target
        if service_target is not UNSET:
            field_dict["service_target"] = service_target
        if user_target is not UNSET:
            field_dict["user_target"] = user_target
        if group_target is not UNSET:
            field_dict["group_target"] = group_target
        if schedule_target is not UNSET:
            field_dict["schedule_target"] = schedule_target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_assign_role_rootly_task_params_escalation_policy_target import (
            AutoAssignRoleRootlyTaskParamsEscalationPolicyTarget,
        )
        from ..models.auto_assign_role_rootly_task_params_group_target import AutoAssignRoleRootlyTaskParamsGroupTarget
        from ..models.auto_assign_role_rootly_task_params_schedule_target import (
            AutoAssignRoleRootlyTaskParamsScheduleTarget,
        )
        from ..models.auto_assign_role_rootly_task_params_service_target import (
            AutoAssignRoleRootlyTaskParamsServiceTarget,
        )
        from ..models.auto_assign_role_rootly_task_params_user_target import AutoAssignRoleRootlyTaskParamsUserTarget

        d = dict(src_dict)
        incident_role_id = d.pop("incident_role_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | AutoAssignRoleRootlyTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_auto_assign_role_rootly_task_params_task_type(_task_type)

        _escalation_policy_target = d.pop("escalation_policy_target", UNSET)
        escalation_policy_target: Unset | AutoAssignRoleRootlyTaskParamsEscalationPolicyTarget
        if isinstance(_escalation_policy_target, Unset):
            escalation_policy_target = UNSET
        else:
            escalation_policy_target = AutoAssignRoleRootlyTaskParamsEscalationPolicyTarget.from_dict(
                _escalation_policy_target
            )

        _service_target = d.pop("service_target", UNSET)
        service_target: Unset | AutoAssignRoleRootlyTaskParamsServiceTarget
        if isinstance(_service_target, Unset):
            service_target = UNSET
        else:
            service_target = AutoAssignRoleRootlyTaskParamsServiceTarget.from_dict(_service_target)

        _user_target = d.pop("user_target", UNSET)
        user_target: Unset | AutoAssignRoleRootlyTaskParamsUserTarget
        if isinstance(_user_target, Unset):
            user_target = UNSET
        else:
            user_target = AutoAssignRoleRootlyTaskParamsUserTarget.from_dict(_user_target)

        _group_target = d.pop("group_target", UNSET)
        group_target: Unset | AutoAssignRoleRootlyTaskParamsGroupTarget
        if isinstance(_group_target, Unset):
            group_target = UNSET
        else:
            group_target = AutoAssignRoleRootlyTaskParamsGroupTarget.from_dict(_group_target)

        _schedule_target = d.pop("schedule_target", UNSET)
        schedule_target: Unset | AutoAssignRoleRootlyTaskParamsScheduleTarget
        if isinstance(_schedule_target, Unset):
            schedule_target = UNSET
        else:
            schedule_target = AutoAssignRoleRootlyTaskParamsScheduleTarget.from_dict(_schedule_target)

        auto_assign_role_rootly_task_params = cls(
            incident_role_id=incident_role_id,
            task_type=task_type,
            escalation_policy_target=escalation_policy_target,
            service_target=service_target,
            user_target=user_target,
            group_target=group_target,
            schedule_target=schedule_target,
        )

        auto_assign_role_rootly_task_params.additional_properties = d
        return auto_assign_role_rootly_task_params

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
