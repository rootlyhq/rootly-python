from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.new_workflow_form_field_condition_data_attributes_incident_condition import (
    NewWorkflowFormFieldConditionDataAttributesIncidentCondition,
    check_new_workflow_form_field_condition_data_attributes_incident_condition,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewWorkflowFormFieldConditionDataAttributes")


@_attrs_define
class NewWorkflowFormFieldConditionDataAttributes:
    """
    Attributes:
        form_field_id (str): The custom field for this condition
        incident_condition (NewWorkflowFormFieldConditionDataAttributesIncidentCondition): The trigger condition
            Default: 'ANY'.
        workflow_id (Union[Unset, str]): The workflow for this condition
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

    form_field_id: str
    incident_condition: NewWorkflowFormFieldConditionDataAttributesIncidentCondition = "ANY"
    workflow_id: Union[Unset, str] = UNSET
    values: Union[Unset, list[str]] = UNSET
    selected_catalog_entity_ids: Union[Unset, list[str]] = UNSET
    selected_functionality_ids: Union[Unset, list[str]] = UNSET
    selected_group_ids: Union[Unset, list[str]] = UNSET
    selected_option_ids: Union[Unset, list[str]] = UNSET
    selected_service_ids: Union[Unset, list[str]] = UNSET
    selected_user_ids: Union[Unset, list[int]] = UNSET
    selected_cause_ids: Union[Unset, list[str]] = UNSET
    selected_environment_ids: Union[Unset, list[str]] = UNSET
    selected_incident_type_ids: Union[Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        form_field_id = self.form_field_id

        incident_condition: str = self.incident_condition

        workflow_id = self.workflow_id

        values: Union[Unset, list[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        selected_catalog_entity_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_catalog_entity_ids, Unset):
            selected_catalog_entity_ids = self.selected_catalog_entity_ids

        selected_functionality_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_functionality_ids, Unset):
            selected_functionality_ids = self.selected_functionality_ids

        selected_group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_group_ids, Unset):
            selected_group_ids = self.selected_group_ids

        selected_option_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_option_ids, Unset):
            selected_option_ids = self.selected_option_ids

        selected_service_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_service_ids, Unset):
            selected_service_ids = self.selected_service_ids

        selected_user_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.selected_user_ids, Unset):
            selected_user_ids = self.selected_user_ids

        selected_cause_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_cause_ids, Unset):
            selected_cause_ids = self.selected_cause_ids

        selected_environment_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_environment_ids, Unset):
            selected_environment_ids = self.selected_environment_ids

        selected_incident_type_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.selected_incident_type_ids, Unset):
            selected_incident_type_ids = self.selected_incident_type_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "form_field_id": form_field_id,
                "incident_condition": incident_condition,
            }
        )
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id
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
        form_field_id = d.pop("form_field_id")

        incident_condition = check_new_workflow_form_field_condition_data_attributes_incident_condition(
            d.pop("incident_condition")
        )

        workflow_id = d.pop("workflow_id", UNSET)

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

        new_workflow_form_field_condition_data_attributes = cls(
            form_field_id=form_field_id,
            incident_condition=incident_condition,
            workflow_id=workflow_id,
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

        return new_workflow_form_field_condition_data_attributes
