from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_workflow_task_params_attribute_to_query_by import (
    TriggerWorkflowTaskParamsAttributeToQueryBy,
    check_trigger_workflow_task_params_attribute_to_query_by,
)
from ..models.trigger_workflow_task_params_kind import (
    TriggerWorkflowTaskParamsKind,
    check_trigger_workflow_task_params_kind,
)
from ..models.trigger_workflow_task_params_task_type import (
    TriggerWorkflowTaskParamsTaskType,
    check_trigger_workflow_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trigger_workflow_task_params_resource import TriggerWorkflowTaskParamsResource
    from ..models.trigger_workflow_task_params_workflow import TriggerWorkflowTaskParamsWorkflow


T = TypeVar("T", bound="TriggerWorkflowTaskParams")


@_attrs_define
class TriggerWorkflowTaskParams:
    """
    Attributes:
        kind (TriggerWorkflowTaskParamsKind):  Default: 'incident'.
        attribute_to_query_by (TriggerWorkflowTaskParamsAttributeToQueryBy): ["(incident) kind can only match [:id,
            :slug, :sequential_id, :pagerduty_incident_id, :opsgenie_incident_id, :victor_ops_incident_id, :jira_issue_id,
            :asana_task_id, :shortcut_task_id, :linear_issue_id, :zendesk_ticket_id, :motion_task_id, :trello_card_id,
            :airtable_record_id, :shortcut_story_id, :github_issue_id, :freshservice_ticket_id, :freshservice_task_id,
            :clickup_task_id]", "(post_mortem) kind can only match [:id]", "(action_item) kind can only match [:id,
            :jira_issue_id, :asana_task_id, :shortcut_task_id, :linear_issue_id, :zendesk_ticket_id, :motion_task_id,
            :trello_card_id, :airtable_record_id, :shortcut_story_id, :github_issue_id, :freshservice_ticket_id,
            :freshservice_task_id, :clickup_task_id]", "(pulse) kind can only match [:id]", "(alert) kind can only match
            [:id]"] Default: 'id'.
        resource (TriggerWorkflowTaskParamsResource):
        workflow (TriggerWorkflowTaskParamsWorkflow):
        task_type (Union[Unset, TriggerWorkflowTaskParamsTaskType]):
        check_workflow_conditions (Union[Unset, bool]):
    """

    resource: "TriggerWorkflowTaskParamsResource"
    workflow: "TriggerWorkflowTaskParamsWorkflow"
    kind: TriggerWorkflowTaskParamsKind = "incident"
    attribute_to_query_by: TriggerWorkflowTaskParamsAttributeToQueryBy = "id"
    task_type: Unset | TriggerWorkflowTaskParamsTaskType = UNSET
    check_workflow_conditions: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        attribute_to_query_by: str = self.attribute_to_query_by

        resource = self.resource.to_dict()

        workflow = self.workflow.to_dict()

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        check_workflow_conditions = self.check_workflow_conditions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "attribute_to_query_by": attribute_to_query_by,
                "resource": resource,
                "workflow": workflow,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if check_workflow_conditions is not UNSET:
            field_dict["check_workflow_conditions"] = check_workflow_conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_workflow_task_params_resource import TriggerWorkflowTaskParamsResource
        from ..models.trigger_workflow_task_params_workflow import TriggerWorkflowTaskParamsWorkflow

        d = dict(src_dict)
        kind = check_trigger_workflow_task_params_kind(d.pop("kind"))

        attribute_to_query_by = check_trigger_workflow_task_params_attribute_to_query_by(d.pop("attribute_to_query_by"))

        resource = TriggerWorkflowTaskParamsResource.from_dict(d.pop("resource"))

        workflow = TriggerWorkflowTaskParamsWorkflow.from_dict(d.pop("workflow"))

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | TriggerWorkflowTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_trigger_workflow_task_params_task_type(_task_type)

        check_workflow_conditions = d.pop("check_workflow_conditions", UNSET)

        trigger_workflow_task_params = cls(
            kind=kind,
            attribute_to_query_by=attribute_to_query_by,
            resource=resource,
            workflow=workflow,
            task_type=task_type,
            check_workflow_conditions=check_workflow_conditions,
        )

        trigger_workflow_task_params.additional_properties = d
        return trigger_workflow_task_params

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
