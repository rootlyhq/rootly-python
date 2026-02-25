from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_status_task_params_status import (
    UpdateStatusTaskParamsStatus,
    check_update_status_task_params_status,
)
from ..models.update_status_task_params_task_type import (
    UpdateStatusTaskParamsTaskType,
    check_update_status_task_params_task_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateStatusTaskParams")


@_attrs_define
class UpdateStatusTaskParams:
    """
    Attributes:
        status (UpdateStatusTaskParamsStatus):
        task_type (Union[Unset, UpdateStatusTaskParamsTaskType]):
        inactivity_timeout (Union[Unset, str]): In format '1 hour', '1 day', etc Example: 1 hour.
    """

    status: UpdateStatusTaskParamsStatus
    task_type: Unset | UpdateStatusTaskParamsTaskType = UNSET
    inactivity_timeout: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str = self.status

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        inactivity_timeout = self.inactivity_timeout

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if inactivity_timeout is not UNSET:
            field_dict["inactivity_timeout"] = inactivity_timeout

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = check_update_status_task_params_status(d.pop("status"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdateStatusTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_status_task_params_task_type(_task_type)

        inactivity_timeout = d.pop("inactivity_timeout", UNSET)

        update_status_task_params = cls(
            status=status,
            task_type=task_type,
            inactivity_timeout=inactivity_timeout,
        )

        update_status_task_params.additional_properties = d
        return update_status_task_params

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
