from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_role_task_params_task_type import AddRoleTaskParamsTaskType, check_add_role_task_params_task_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_role_task_params_assigned_to_user import AddRoleTaskParamsAssignedToUser


T = TypeVar("T", bound="AddRoleTaskParams")


@_attrs_define
class AddRoleTaskParams:
    """
    Attributes:
        incident_role_id (str): The role id to add to the incident
        task_type (Union[Unset, AddRoleTaskParamsTaskType]):
        assigned_to_user_id (Union[Unset, str]): [DEPRECATED] Use assigned_to_user attribute instead. The user id this
            role is assigned to
        assigned_to_user (Union[Unset, AddRoleTaskParamsAssignedToUser]):  The user this role is assigned to
    """

    incident_role_id: str
    task_type: Unset | AddRoleTaskParamsTaskType = UNSET
    assigned_to_user_id: Unset | str = UNSET
    assigned_to_user: Union[Unset, "AddRoleTaskParamsAssignedToUser"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_role_id = self.incident_role_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        assigned_to_user_id = self.assigned_to_user_id

        assigned_to_user: Unset | dict[str, Any] = UNSET
        if not isinstance(self.assigned_to_user, Unset):
            assigned_to_user = self.assigned_to_user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_role_id": incident_role_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if assigned_to_user_id is not UNSET:
            field_dict["assigned_to_user_id"] = assigned_to_user_id
        if assigned_to_user is not UNSET:
            field_dict["assigned_to_user"] = assigned_to_user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_role_task_params_assigned_to_user import AddRoleTaskParamsAssignedToUser

        d = dict(src_dict)
        incident_role_id = d.pop("incident_role_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | AddRoleTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_add_role_task_params_task_type(_task_type)

        assigned_to_user_id = d.pop("assigned_to_user_id", UNSET)

        _assigned_to_user = d.pop("assigned_to_user", UNSET)
        assigned_to_user: Unset | AddRoleTaskParamsAssignedToUser
        if isinstance(_assigned_to_user, Unset):
            assigned_to_user = UNSET
        else:
            assigned_to_user = AddRoleTaskParamsAssignedToUser.from_dict(_assigned_to_user)

        add_role_task_params = cls(
            incident_role_id=incident_role_id,
            task_type=task_type,
            assigned_to_user_id=assigned_to_user_id,
            assigned_to_user=assigned_to_user,
        )

        add_role_task_params.additional_properties = d
        return add_role_task_params

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
