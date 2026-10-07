from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_workflow_data import UpdateWorkflowData


T = TypeVar("T", bound="UpdateWorkflow")


@_attrs_define
class UpdateWorkflow:
    """
    Attributes:
        data (UpdateWorkflowData):
    """

    data: UpdateWorkflowData

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
        from ..models.update_workflow_data import UpdateWorkflowData

        d = dict(src_dict)
        data = UpdateWorkflowData.from_dict(d.pop("data"))

        update_workflow = cls(
            data=data,
        )

        return update_workflow
