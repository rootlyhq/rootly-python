from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_opsgenie_alert_task_params_priority import (
    UpdateOpsgenieAlertTaskParamsPriority,
    check_update_opsgenie_alert_task_params_priority,
)
from ..models.update_opsgenie_alert_task_params_task_type import (
    UpdateOpsgenieAlertTaskParamsTaskType,
    check_update_opsgenie_alert_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_opsgenie_alert_task_params_completion import UpdateOpsgenieAlertTaskParamsCompletion


T = TypeVar("T", bound="UpdateOpsgenieAlertTaskParams")


@_attrs_define
class UpdateOpsgenieAlertTaskParams:
    """
    Attributes:
        alert_id (str): Opsgenie Alert ID
        priority (UpdateOpsgenieAlertTaskParamsPriority):
        completion (UpdateOpsgenieAlertTaskParamsCompletion):
        task_type (Union[Unset, UpdateOpsgenieAlertTaskParamsTaskType]):
        message (Union[Unset, str]): Message of the alert
        description (Union[Unset, str]): Description field of the alert that is generally used to provide a detailed
            information about the alert
    """

    alert_id: str
    priority: UpdateOpsgenieAlertTaskParamsPriority
    completion: "UpdateOpsgenieAlertTaskParamsCompletion"
    task_type: Unset | UpdateOpsgenieAlertTaskParamsTaskType = UNSET
    message: Unset | str = UNSET
    description: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_id = self.alert_id

        priority: str = self.priority

        completion = self.completion.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        message = self.message

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_id": alert_id,
                "priority": priority,
                "completion": completion,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if message is not UNSET:
            field_dict["message"] = message
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_opsgenie_alert_task_params_completion import UpdateOpsgenieAlertTaskParamsCompletion

        d = dict(src_dict)
        alert_id = d.pop("alert_id")

        priority = check_update_opsgenie_alert_task_params_priority(d.pop("priority"))

        completion = UpdateOpsgenieAlertTaskParamsCompletion.from_dict(d.pop("completion"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateOpsgenieAlertTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_opsgenie_alert_task_params_task_type(_task_type)

        message = d.pop("message", UNSET)

        description = d.pop("description", UNSET)

        update_opsgenie_alert_task_params = cls(
            alert_id=alert_id,
            priority=priority,
            completion=completion,
            task_type=task_type,
            message=message,
            description=description,
        )

        update_opsgenie_alert_task_params.additional_properties = d
        return update_opsgenie_alert_task_params

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
