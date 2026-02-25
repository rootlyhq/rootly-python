from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_workflow_custom_field_selection_data_attributes_incident_condition import (
    UpdateWorkflowCustomFieldSelectionDataAttributesIncidentCondition,
    check_update_workflow_custom_field_selection_data_attributes_incident_condition,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWorkflowCustomFieldSelectionDataAttributes")


@_attrs_define
class UpdateWorkflowCustomFieldSelectionDataAttributes:
    """
    Attributes:
        incident_condition (Union[Unset, UpdateWorkflowCustomFieldSelectionDataAttributesIncidentCondition]): The
            trigger condition Default: 'ANY'.
        values (Union[Unset, list[str]]):
        selected_option_ids (Union[Unset, list[int]]):
    """

    incident_condition: Unset | UpdateWorkflowCustomFieldSelectionDataAttributesIncidentCondition = "ANY"
    values: Unset | list[str] = UNSET
    selected_option_ids: Unset | list[int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        incident_condition: Unset | str = UNSET
        if not isinstance(self.incident_condition, Unset):
            incident_condition = self.incident_condition

        values: Unset | list[str] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        selected_option_ids: Unset | list[int] = UNSET
        if not isinstance(self.selected_option_ids, Unset):
            selected_option_ids = self.selected_option_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if incident_condition is not UNSET:
            field_dict["incident_condition"] = incident_condition
        if values is not UNSET:
            field_dict["values"] = values
        if selected_option_ids is not UNSET:
            field_dict["selected_option_ids"] = selected_option_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _incident_condition = d.pop("incident_condition", UNSET)
        incident_condition: Unset | UpdateWorkflowCustomFieldSelectionDataAttributesIncidentCondition
        if isinstance(_incident_condition, Unset):
            incident_condition = UNSET
        else:
            incident_condition = check_update_workflow_custom_field_selection_data_attributes_incident_condition(
                _incident_condition
            )

        values = cast(list[str], d.pop("values", UNSET))

        selected_option_ids = cast(list[int], d.pop("selected_option_ids", UNSET))

        update_workflow_custom_field_selection_data_attributes = cls(
            incident_condition=incident_condition,
            values=values,
            selected_option_ids=selected_option_ids,
        )

        return update_workflow_custom_field_selection_data_attributes
