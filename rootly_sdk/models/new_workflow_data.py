from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_workflow_data_type import NewWorkflowDataType, check_new_workflow_data_type

if TYPE_CHECKING:
    from ..models.new_workflow_data_attributes import NewWorkflowDataAttributes


T = TypeVar("T", bound="NewWorkflowData")


@_attrs_define
class NewWorkflowData:
    """
    Attributes:
        type_ (NewWorkflowDataType):
        attributes (NewWorkflowDataAttributes):
    """

    type_: NewWorkflowDataType
    attributes: NewWorkflowDataAttributes

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_workflow_data_attributes import NewWorkflowDataAttributes

        d = dict(src_dict)
        type_ = check_new_workflow_data_type(d.pop("type"))

        attributes = NewWorkflowDataAttributes.from_dict(d.pop("attributes"))

        new_workflow_data = cls(
            type_=type_,
            attributes=attributes,
        )

        return new_workflow_data
