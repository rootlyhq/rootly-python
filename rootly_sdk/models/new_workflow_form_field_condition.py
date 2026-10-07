from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.new_workflow_form_field_condition_data import NewWorkflowFormFieldConditionData


T = TypeVar("T", bound="NewWorkflowFormFieldCondition")


@_attrs_define
class NewWorkflowFormFieldCondition:
    """
    Attributes:
        data (NewWorkflowFormFieldConditionData):
    """

    data: NewWorkflowFormFieldConditionData

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
        from ..models.new_workflow_form_field_condition_data import NewWorkflowFormFieldConditionData

        d = dict(src_dict)
        data = NewWorkflowFormFieldConditionData.from_dict(d.pop("data"))

        new_workflow_form_field_condition = cls(
            data=data,
        )

        return new_workflow_form_field_condition
