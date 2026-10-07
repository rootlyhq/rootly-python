from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_workflow_group_data import NewWorkflowGroupData


T = TypeVar("T", bound="NewWorkflowGroup")


@_attrs_define
class NewWorkflowGroup:
    """
    Attributes:
        data (NewWorkflowGroupData):
    """

    data: NewWorkflowGroupData

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_workflow_group_data import NewWorkflowGroupData

        d = dict(src_dict)
        data = NewWorkflowGroupData.from_dict(d.pop("data"))

        new_workflow_group = cls(
            data=data,
        )

        return new_workflow_group
