from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_workflow_form_field_condition_data_attributes_incident_condition import (
    UpdateWorkflowFormFieldConditionDataAttributesIncidentCondition,
    check_update_workflow_form_field_condition_data_attributes_incident_condition,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWorkflowFormFieldConditionDataAttributes")


@_attrs_define
class UpdateWorkflowFormFieldConditionDataAttributes:
    """
    Attributes:
        incident_condition (Union[Unset, UpdateWorkflowFormFieldConditionDataAttributesIncidentCondition]): The trigger
            condition Default: 'ANY'.
        values (Union[Unset, list[str]]):
        selected_catalog_entity_ids (Union[Unset, list[str]]):
        selected_functionality_ids (Union[Unset, list[str]]):
        selected_group_ids (Union[Unset, list[str]]):
        selected_option_ids (Union[Unset, list[str]]):
        selected_service_ids (Union[Unset, list[str]]):
        selected_user_ids (Union[Unset, list[int]]):
        selected_cause_ids (Union[Unset, list[str]]):
        selected_environment_ids (Union[Unset, list[str]]):
        selected_incident_type_ids (Union[Unset, list[str]]):
    """

    incident_condition: Unset | UpdateWorkflowFormFieldConditionDataAttributesIncidentCondition = "ANY"
    values: Unset | list[str] = UNSET
    selected_catalog_entity_ids: Unset | list[str] = UNSET
    selected_functionality_ids: Unset | list[str] = UNSET
    selected_group_ids: Unset | list[str] = UNSET
    selected_option_ids: Unset | list[str] = UNSET
    selected_service_ids: Unset | list[str] = UNSET
    selected_user_ids: Unset | list[int] = UNSET
    selected_cause_ids: Unset | list[str] = UNSET
    selected_environment_ids: Unset | list[str] = UNSET
    selected_incident_type_ids: Unset | list[str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        incident_condition: Unset | str = UNSET
        if not isinstance(self.incident_condition, Unset):
            incident_condition = self.incident_condition

        values: Unset | list[str] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        selected_catalog_entity_ids: Unset | list[str] = UNSET
        if not isinstance(self.selected_catalog_entity_ids, Unset):
            selected_catalog_entity_ids = self.selected_catalog_entity_ids

        selected_functionality_ids: Unset | list[str] = UNSET
        if not isinstance(self.selected_functionality_ids, Unset):
            selected_functionality_ids = self.selected_functionality_ids

        selected_group_ids: Unset | list[str] = UNSET
        if not isinstance(self.selected_group_ids, Unset):
            selected_group_ids = self.selected_group_ids

        selected_option_ids: Unset | list[str] = UNSET
        if not isinstance(self.selected_option_ids, Unset):
            selected_option_ids = self.selected_option_ids

        selected_service_ids: Unset | list[str] = UNSET
        if not isinstance(self.selected_service_ids, Unset):
            selected_service_ids = self.selected_service_ids

        selected_user_ids: Unset | list[int] = UNSET
        if not isinstance(self.selected_user_ids, Unset):
            selected_user_ids = self.selected_user_ids

        selected_cause_ids: Unset | list[str] = UNSET
        if not isinstance(self.selected_cause_ids, Unset):
            selected_cause_ids = self.selected_cause_ids

        selected_environment_ids: Unset | list[str] = UNSET
        if not isinstance(self.selected_environment_ids, Unset):
            selected_environment_ids = self.selected_environment_ids

        selected_incident_type_ids: Unset | list[str] = UNSET
        if not isinstance(self.selected_incident_type_ids, Unset):
            selected_incident_type_ids = self.selected_incident_type_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if incident_condition is not UNSET:
            field_dict["incident_condition"] = incident_condition
        if values is not UNSET:
            field_dict["values"] = values
        if selected_catalog_entity_ids is not UNSET:
            field_dict["selected_catalog_entity_ids"] = selected_catalog_entity_ids
        if selected_functionality_ids is not UNSET:
            field_dict["selected_functionality_ids"] = selected_functionality_ids
        if selected_group_ids is not UNSET:
            field_dict["selected_group_ids"] = selected_group_ids
        if selected_option_ids is not UNSET:
            field_dict["selected_option_ids"] = selected_option_ids
        if selected_service_ids is not UNSET:
            field_dict["selected_service_ids"] = selected_service_ids
        if selected_user_ids is not UNSET:
            field_dict["selected_user_ids"] = selected_user_ids
        if selected_cause_ids is not UNSET:
            field_dict["selected_cause_ids"] = selected_cause_ids
        if selected_environment_ids is not UNSET:
            field_dict["selected_environment_ids"] = selected_environment_ids
        if selected_incident_type_ids is not UNSET:
            field_dict["selected_incident_type_ids"] = selected_incident_type_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _incident_condition = d.pop("incident_condition", UNSET)
        incident_condition: Unset | UpdateWorkflowFormFieldConditionDataAttributesIncidentCondition
        if isinstance(_incident_condition, Unset):
            incident_condition = UNSET
        else:
            incident_condition = check_update_workflow_form_field_condition_data_attributes_incident_condition(
                _incident_condition
            )

        values = cast(list[str], d.pop("values", UNSET))

        selected_catalog_entity_ids = cast(list[str], d.pop("selected_catalog_entity_ids", UNSET))

        selected_functionality_ids = cast(list[str], d.pop("selected_functionality_ids", UNSET))

        selected_group_ids = cast(list[str], d.pop("selected_group_ids", UNSET))

        selected_option_ids = cast(list[str], d.pop("selected_option_ids", UNSET))

        selected_service_ids = cast(list[str], d.pop("selected_service_ids", UNSET))

        selected_user_ids = cast(list[int], d.pop("selected_user_ids", UNSET))

        selected_cause_ids = cast(list[str], d.pop("selected_cause_ids", UNSET))

        selected_environment_ids = cast(list[str], d.pop("selected_environment_ids", UNSET))

        selected_incident_type_ids = cast(list[str], d.pop("selected_incident_type_ids", UNSET))

        update_workflow_form_field_condition_data_attributes = cls(
            incident_condition=incident_condition,
            values=values,
            selected_catalog_entity_ids=selected_catalog_entity_ids,
            selected_functionality_ids=selected_functionality_ids,
            selected_group_ids=selected_group_ids,
            selected_option_ids=selected_option_ids,
            selected_service_ids=selected_service_ids,
            selected_user_ids=selected_user_ids,
            selected_cause_ids=selected_cause_ids,
            selected_environment_ids=selected_environment_ids,
            selected_incident_type_ids=selected_incident_type_ids,
        )

        return update_workflow_form_field_condition_data_attributes
