from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.print_task_params_task_type import PrintTaskParamsTaskType, check_print_task_params_task_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="PrintTaskParams")


@_attrs_define
class PrintTaskParams:
    """
    Attributes:
        message (str): The message to print
        task_type (Union[Unset, PrintTaskParamsTaskType]):
    """

    message: str
    task_type: Unset | PrintTaskParamsTaskType = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | PrintTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_print_task_params_task_type(_task_type)

        print_task_params = cls(
            message=message,
            task_type=task_type,
        )

        print_task_params.additional_properties = d
        return print_task_params

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
