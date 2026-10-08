from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.update_workflow_action_item_form_field_condition_data import (
        UpdateWorkflowActionItemFormFieldConditionData,
    )


T = TypeVar("T", bound="UpdateWorkflowActionItemFormFieldCondition")


@_attrs_define
class UpdateWorkflowActionItemFormFieldCondition:
    """
    Attributes:
        data (UpdateWorkflowActionItemFormFieldConditionData):
    """

    data: UpdateWorkflowActionItemFormFieldConditionData

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
        from ..models.update_workflow_action_item_form_field_condition_data import (
            UpdateWorkflowActionItemFormFieldConditionData,
        )

        d = dict(src_dict)
        data = UpdateWorkflowActionItemFormFieldConditionData.from_dict(d.pop("data"))

        update_workflow_action_item_form_field_condition = cls(
            data=data,
        )

        return update_workflow_action_item_form_field_condition
