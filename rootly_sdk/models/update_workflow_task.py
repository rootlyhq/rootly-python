from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_workflow_task_data import UpdateWorkflowTaskData


T = TypeVar("T", bound="UpdateWorkflowTask")


@_attrs_define
class UpdateWorkflowTask:
    """
    Attributes:
        data (UpdateWorkflowTaskData):
    """

    data: "UpdateWorkflowTaskData"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.update_workflow_task_data import UpdateWorkflowTaskData

        d = src_dict.copy()
        data = UpdateWorkflowTaskData.from_dict(d.pop("data"))

        update_workflow_task = cls(
            data=data,
        )

        update_workflow_task.additional_properties = d
        return update_workflow_task

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
