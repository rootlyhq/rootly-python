from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_item_trigger_params_incident_action_item_condition import (
    ActionItemTriggerParamsIncidentActionItemCondition,
    check_action_item_trigger_params_incident_action_item_condition,
)
from ..models.action_item_trigger_params_incident_action_item_condition_group import (
    ActionItemTriggerParamsIncidentActionItemConditionGroup,
    check_action_item_trigger_params_incident_action_item_condition_group,
)
from ..models.action_item_trigger_params_incident_action_item_condition_kind import (
    ActionItemTriggerParamsIncidentActionItemConditionKind,
    check_action_item_trigger_params_incident_action_item_condition_kind,
)
from ..models.action_item_trigger_params_incident_action_item_condition_priority import (
    ActionItemTriggerParamsIncidentActionItemConditionPriority,
    check_action_item_trigger_params_incident_action_item_condition_priority,
)
from ..models.action_item_trigger_params_incident_action_item_condition_status import (
    ActionItemTriggerParamsIncidentActionItemConditionStatus,
    check_action_item_trigger_params_incident_action_item_condition_status,
)
from ..models.action_item_trigger_params_incident_action_item_kinds_item import (
    ActionItemTriggerParamsIncidentActionItemKindsItem,
    check_action_item_trigger_params_incident_action_item_kinds_item,
)
from ..models.action_item_trigger_params_incident_action_item_priorities_item import (
    ActionItemTriggerParamsIncidentActionItemPrioritiesItem,
    check_action_item_trigger_params_incident_action_item_priorities_item,
)
from ..models.action_item_trigger_params_incident_action_item_statuses_item import (
    ActionItemTriggerParamsIncidentActionItemStatusesItem,
    check_action_item_trigger_params_incident_action_item_statuses_item,
)
from ..models.action_item_trigger_params_incident_condition import (
    ActionItemTriggerParamsIncidentCondition,
    check_action_item_trigger_params_incident_condition,
)
from ..models.action_item_trigger_params_incident_condition_acknowledged_at_type_1 import (
    ActionItemTriggerParamsIncidentConditionAcknowledgedAtType1,
    check_action_item_trigger_params_incident_condition_acknowledged_at_type_1,
)
from ..models.action_item_trigger_params_incident_condition_detected_at_type_1 import (
    ActionItemTriggerParamsIncidentConditionDetectedAtType1,
    check_action_item_trigger_params_incident_condition_detected_at_type_1,
)
from ..models.action_item_trigger_params_incident_condition_environment import (
    ActionItemTriggerParamsIncidentConditionEnvironment,
    check_action_item_trigger_params_incident_condition_environment,
)
from ..models.action_item_trigger_params_incident_condition_functionality import (
    ActionItemTriggerParamsIncidentConditionFunctionality,
    check_action_item_trigger_params_incident_condition_functionality,
)
from ..models.action_item_trigger_params_incident_condition_group import (
    ActionItemTriggerParamsIncidentConditionGroup,
    check_action_item_trigger_params_incident_condition_group,
)
from ..models.action_item_trigger_params_incident_condition_incident_roles import (
    ActionItemTriggerParamsIncidentConditionIncidentRoles,
    check_action_item_trigger_params_incident_condition_incident_roles,
)
from ..models.action_item_trigger_params_incident_condition_incident_type import (
    ActionItemTriggerParamsIncidentConditionIncidentType,
    check_action_item_trigger_params_incident_condition_incident_type,
)
from ..models.action_item_trigger_params_incident_condition_kind import (
    ActionItemTriggerParamsIncidentConditionKind,
    check_action_item_trigger_params_incident_condition_kind,
)
from ..models.action_item_trigger_params_incident_condition_mitigated_at_type_1 import (
    ActionItemTriggerParamsIncidentConditionMitigatedAtType1,
    check_action_item_trigger_params_incident_condition_mitigated_at_type_1,
)
from ..models.action_item_trigger_params_incident_condition_resolved_at_type_1 import (
    ActionItemTriggerParamsIncidentConditionResolvedAtType1,
    check_action_item_trigger_params_incident_condition_resolved_at_type_1,
)
from ..models.action_item_trigger_params_incident_condition_service import (
    ActionItemTriggerParamsIncidentConditionService,
    check_action_item_trigger_params_incident_condition_service,
)
from ..models.action_item_trigger_params_incident_condition_severity import (
    ActionItemTriggerParamsIncidentConditionSeverity,
    check_action_item_trigger_params_incident_condition_severity,
)
from ..models.action_item_trigger_params_incident_condition_started_at_type_1 import (
    ActionItemTriggerParamsIncidentConditionStartedAtType1,
    check_action_item_trigger_params_incident_condition_started_at_type_1,
)
from ..models.action_item_trigger_params_incident_condition_status import (
    ActionItemTriggerParamsIncidentConditionStatus,
    check_action_item_trigger_params_incident_condition_status,
)
from ..models.action_item_trigger_params_incident_condition_sub_status import (
    ActionItemTriggerParamsIncidentConditionSubStatus,
    check_action_item_trigger_params_incident_condition_sub_status,
)
from ..models.action_item_trigger_params_incident_condition_summary_type_1 import (
    ActionItemTriggerParamsIncidentConditionSummaryType1,
    check_action_item_trigger_params_incident_condition_summary_type_1,
)
from ..models.action_item_trigger_params_incident_condition_visibility import (
    ActionItemTriggerParamsIncidentConditionVisibility,
    check_action_item_trigger_params_incident_condition_visibility,
)
from ..models.action_item_trigger_params_incident_conditional_inactivity_type_1 import (
    ActionItemTriggerParamsIncidentConditionalInactivityType1,
    check_action_item_trigger_params_incident_conditional_inactivity_type_1,
)
from ..models.action_item_trigger_params_incident_kinds_item import (
    ActionItemTriggerParamsIncidentKindsItem,
    check_action_item_trigger_params_incident_kinds_item,
)
from ..models.action_item_trigger_params_incident_statuses_item import (
    ActionItemTriggerParamsIncidentStatusesItem,
    check_action_item_trigger_params_incident_statuses_item,
)
from ..models.action_item_trigger_params_trigger_type import (
    ActionItemTriggerParamsTriggerType,
    check_action_item_trigger_params_trigger_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionItemTriggerParams")


@_attrs_define
class ActionItemTriggerParams:
    """
    Attributes:
        trigger_type (ActionItemTriggerParamsTriggerType):
        triggers (list[str] | Unset):
        incident_visibilities (list[bool] | Unset):
        incident_kinds (list[ActionItemTriggerParamsIncidentKindsItem] | Unset):
        incident_statuses (list[ActionItemTriggerParamsIncidentStatusesItem] | Unset):
        incident_inactivity_duration (None | str | Unset):
        incident_condition (ActionItemTriggerParamsIncidentCondition | Unset):  Default: 'ALL'.
        incident_condition_visibility (ActionItemTriggerParamsIncidentConditionVisibility | Unset):  Default: 'ANY'.
        incident_condition_kind (ActionItemTriggerParamsIncidentConditionKind | Unset):  Default: 'IS'.
        incident_condition_status (ActionItemTriggerParamsIncidentConditionStatus | Unset):  Default: 'ANY'.
        incident_condition_sub_status (ActionItemTriggerParamsIncidentConditionSubStatus | Unset):  Default: 'ANY'.
        incident_condition_environment (ActionItemTriggerParamsIncidentConditionEnvironment | Unset):  Default: 'ANY'.
        incident_condition_severity (ActionItemTriggerParamsIncidentConditionSeverity | Unset):  Default: 'ANY'.
        incident_condition_incident_type (ActionItemTriggerParamsIncidentConditionIncidentType | Unset):  Default:
            'ANY'.
        incident_condition_incident_roles (ActionItemTriggerParamsIncidentConditionIncidentRoles | Unset):  Default:
            'ANY'.
        incident_condition_service (ActionItemTriggerParamsIncidentConditionService | Unset):  Default: 'ANY'.
        incident_condition_functionality (ActionItemTriggerParamsIncidentConditionFunctionality | Unset):  Default:
            'ANY'.
        incident_condition_group (ActionItemTriggerParamsIncidentConditionGroup | Unset):  Default: 'ANY'.
        incident_condition_summary (ActionItemTriggerParamsIncidentConditionSummaryType1 | None | Unset):
        incident_condition_started_at (ActionItemTriggerParamsIncidentConditionStartedAtType1 | None | Unset):
        incident_condition_detected_at (ActionItemTriggerParamsIncidentConditionDetectedAtType1 | None | Unset):
        incident_condition_acknowledged_at (ActionItemTriggerParamsIncidentConditionAcknowledgedAtType1 | None | Unset):
        incident_condition_mitigated_at (ActionItemTriggerParamsIncidentConditionMitigatedAtType1 | None | Unset):
        incident_condition_resolved_at (ActionItemTriggerParamsIncidentConditionResolvedAtType1 | None | Unset):
        incident_conditional_inactivity (ActionItemTriggerParamsIncidentConditionalInactivityType1 | None | Unset):
        incident_action_item_condition (ActionItemTriggerParamsIncidentActionItemCondition | Unset):
        incident_action_item_condition_kind (ActionItemTriggerParamsIncidentActionItemConditionKind | Unset):  Default:
            'ANY'.
        incident_action_item_kinds (list[ActionItemTriggerParamsIncidentActionItemKindsItem] | Unset):
        incident_action_item_condition_status (ActionItemTriggerParamsIncidentActionItemConditionStatus | Unset):
            Default: 'ANY'.
        incident_action_item_statuses (list[ActionItemTriggerParamsIncidentActionItemStatusesItem] | Unset):
        incident_action_item_condition_priority (ActionItemTriggerParamsIncidentActionItemConditionPriority | Unset):
            Default: 'ANY'.
        incident_action_item_priorities (list[ActionItemTriggerParamsIncidentActionItemPrioritiesItem] | Unset):
        incident_action_item_condition_group (ActionItemTriggerParamsIncidentActionItemConditionGroup | Unset):
            Default: 'ANY'.
        incident_action_item_group_ids (list[str] | Unset):
    """

    trigger_type: ActionItemTriggerParamsTriggerType
    triggers: list[str] | Unset = UNSET
    incident_visibilities: list[bool] | Unset = UNSET
    incident_kinds: list[ActionItemTriggerParamsIncidentKindsItem] | Unset = UNSET
    incident_statuses: list[ActionItemTriggerParamsIncidentStatusesItem] | Unset = UNSET
    incident_inactivity_duration: None | str | Unset = UNSET
    incident_condition: ActionItemTriggerParamsIncidentCondition | Unset = "ALL"
    incident_condition_visibility: ActionItemTriggerParamsIncidentConditionVisibility | Unset = "ANY"
    incident_condition_kind: ActionItemTriggerParamsIncidentConditionKind | Unset = "IS"
    incident_condition_status: ActionItemTriggerParamsIncidentConditionStatus | Unset = "ANY"
    incident_condition_sub_status: ActionItemTriggerParamsIncidentConditionSubStatus | Unset = "ANY"
    incident_condition_environment: ActionItemTriggerParamsIncidentConditionEnvironment | Unset = "ANY"
    incident_condition_severity: ActionItemTriggerParamsIncidentConditionSeverity | Unset = "ANY"
    incident_condition_incident_type: ActionItemTriggerParamsIncidentConditionIncidentType | Unset = "ANY"
    incident_condition_incident_roles: ActionItemTriggerParamsIncidentConditionIncidentRoles | Unset = "ANY"
    incident_condition_service: ActionItemTriggerParamsIncidentConditionService | Unset = "ANY"
    incident_condition_functionality: ActionItemTriggerParamsIncidentConditionFunctionality | Unset = "ANY"
    incident_condition_group: ActionItemTriggerParamsIncidentConditionGroup | Unset = "ANY"
    incident_condition_summary: ActionItemTriggerParamsIncidentConditionSummaryType1 | None | Unset = UNSET
    incident_condition_started_at: ActionItemTriggerParamsIncidentConditionStartedAtType1 | None | Unset = UNSET
    incident_condition_detected_at: ActionItemTriggerParamsIncidentConditionDetectedAtType1 | None | Unset = UNSET
    incident_condition_acknowledged_at: ActionItemTriggerParamsIncidentConditionAcknowledgedAtType1 | None | Unset = (
        UNSET
    )
    incident_condition_mitigated_at: ActionItemTriggerParamsIncidentConditionMitigatedAtType1 | None | Unset = UNSET
    incident_condition_resolved_at: ActionItemTriggerParamsIncidentConditionResolvedAtType1 | None | Unset = UNSET
    incident_conditional_inactivity: ActionItemTriggerParamsIncidentConditionalInactivityType1 | None | Unset = UNSET
    incident_action_item_condition: ActionItemTriggerParamsIncidentActionItemCondition | Unset = UNSET
    incident_action_item_condition_kind: ActionItemTriggerParamsIncidentActionItemConditionKind | Unset = "ANY"
    incident_action_item_kinds: list[ActionItemTriggerParamsIncidentActionItemKindsItem] | Unset = UNSET
    incident_action_item_condition_status: ActionItemTriggerParamsIncidentActionItemConditionStatus | Unset = "ANY"
    incident_action_item_statuses: list[ActionItemTriggerParamsIncidentActionItemStatusesItem] | Unset = UNSET
    incident_action_item_condition_priority: ActionItemTriggerParamsIncidentActionItemConditionPriority | Unset = "ANY"
    incident_action_item_priorities: list[ActionItemTriggerParamsIncidentActionItemPrioritiesItem] | Unset = UNSET
    incident_action_item_condition_group: ActionItemTriggerParamsIncidentActionItemConditionGroup | Unset = "ANY"
    incident_action_item_group_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger_type: str = self.trigger_type

        triggers: list[str] | Unset = UNSET
        if not isinstance(self.triggers, Unset):
            triggers = self.triggers

        incident_visibilities: list[bool] | Unset = UNSET
        if not isinstance(self.incident_visibilities, Unset):
            incident_visibilities = self.incident_visibilities

        incident_kinds: list[str] | Unset = UNSET
        if not isinstance(self.incident_kinds, Unset):
            incident_kinds = []
            for incident_kinds_item_data in self.incident_kinds:
                incident_kinds_item: str = incident_kinds_item_data
                incident_kinds.append(incident_kinds_item)

        incident_statuses: list[str] | Unset = UNSET
        if not isinstance(self.incident_statuses, Unset):
            incident_statuses = []
            for incident_statuses_item_data in self.incident_statuses:
                incident_statuses_item: str = incident_statuses_item_data
                incident_statuses.append(incident_statuses_item)

        incident_inactivity_duration: None | str | Unset
        if isinstance(self.incident_inactivity_duration, Unset):
            incident_inactivity_duration = UNSET
        else:
            incident_inactivity_duration = self.incident_inactivity_duration

        incident_condition: str | Unset = UNSET
        if not isinstance(self.incident_condition, Unset):
            incident_condition = self.incident_condition

        incident_condition_visibility: str | Unset = UNSET
        if not isinstance(self.incident_condition_visibility, Unset):
            incident_condition_visibility = self.incident_condition_visibility

        incident_condition_kind: str | Unset = UNSET
        if not isinstance(self.incident_condition_kind, Unset):
            incident_condition_kind = self.incident_condition_kind

        incident_condition_status: str | Unset = UNSET
        if not isinstance(self.incident_condition_status, Unset):
            incident_condition_status = self.incident_condition_status

        incident_condition_sub_status: str | Unset = UNSET
        if not isinstance(self.incident_condition_sub_status, Unset):
            incident_condition_sub_status = self.incident_condition_sub_status

        incident_condition_environment: str | Unset = UNSET
        if not isinstance(self.incident_condition_environment, Unset):
            incident_condition_environment = self.incident_condition_environment

        incident_condition_severity: str | Unset = UNSET
        if not isinstance(self.incident_condition_severity, Unset):
            incident_condition_severity = self.incident_condition_severity

        incident_condition_incident_type: str | Unset = UNSET
        if not isinstance(self.incident_condition_incident_type, Unset):
            incident_condition_incident_type = self.incident_condition_incident_type

        incident_condition_incident_roles: str | Unset = UNSET
        if not isinstance(self.incident_condition_incident_roles, Unset):
            incident_condition_incident_roles = self.incident_condition_incident_roles

        incident_condition_service: str | Unset = UNSET
        if not isinstance(self.incident_condition_service, Unset):
            incident_condition_service = self.incident_condition_service

        incident_condition_functionality: str | Unset = UNSET
        if not isinstance(self.incident_condition_functionality, Unset):
            incident_condition_functionality = self.incident_condition_functionality

        incident_condition_group: str | Unset = UNSET
        if not isinstance(self.incident_condition_group, Unset):
            incident_condition_group = self.incident_condition_group

        incident_condition_summary: None | str | Unset
        if isinstance(self.incident_condition_summary, Unset):
            incident_condition_summary = UNSET
        elif isinstance(self.incident_condition_summary, str):
            incident_condition_summary = self.incident_condition_summary
        else:
            incident_condition_summary = self.incident_condition_summary

        incident_condition_started_at: None | str | Unset
        if isinstance(self.incident_condition_started_at, Unset):
            incident_condition_started_at = UNSET
        elif isinstance(self.incident_condition_started_at, str):
            incident_condition_started_at = self.incident_condition_started_at
        else:
            incident_condition_started_at = self.incident_condition_started_at

        incident_condition_detected_at: None | str | Unset
        if isinstance(self.incident_condition_detected_at, Unset):
            incident_condition_detected_at = UNSET
        elif isinstance(self.incident_condition_detected_at, str):
            incident_condition_detected_at = self.incident_condition_detected_at
        else:
            incident_condition_detected_at = self.incident_condition_detected_at

        incident_condition_acknowledged_at: None | str | Unset
        if isinstance(self.incident_condition_acknowledged_at, Unset):
            incident_condition_acknowledged_at = UNSET
        elif isinstance(self.incident_condition_acknowledged_at, str):
            incident_condition_acknowledged_at = self.incident_condition_acknowledged_at
        else:
            incident_condition_acknowledged_at = self.incident_condition_acknowledged_at

        incident_condition_mitigated_at: None | str | Unset
        if isinstance(self.incident_condition_mitigated_at, Unset):
            incident_condition_mitigated_at = UNSET
        elif isinstance(self.incident_condition_mitigated_at, str):
            incident_condition_mitigated_at = self.incident_condition_mitigated_at
        else:
            incident_condition_mitigated_at = self.incident_condition_mitigated_at

        incident_condition_resolved_at: None | str | Unset
        if isinstance(self.incident_condition_resolved_at, Unset):
            incident_condition_resolved_at = UNSET
        elif isinstance(self.incident_condition_resolved_at, str):
            incident_condition_resolved_at = self.incident_condition_resolved_at
        else:
            incident_condition_resolved_at = self.incident_condition_resolved_at

        incident_conditional_inactivity: None | str | Unset
        if isinstance(self.incident_conditional_inactivity, Unset):
            incident_conditional_inactivity = UNSET
        elif isinstance(self.incident_conditional_inactivity, str):
            incident_conditional_inactivity = self.incident_conditional_inactivity
        else:
            incident_conditional_inactivity = self.incident_conditional_inactivity

        incident_action_item_condition: str | Unset = UNSET
        if not isinstance(self.incident_action_item_condition, Unset):
            incident_action_item_condition = self.incident_action_item_condition

        incident_action_item_condition_kind: str | Unset = UNSET
        if not isinstance(self.incident_action_item_condition_kind, Unset):
            incident_action_item_condition_kind = self.incident_action_item_condition_kind

        incident_action_item_kinds: list[str] | Unset = UNSET
        if not isinstance(self.incident_action_item_kinds, Unset):
            incident_action_item_kinds = []
            for incident_action_item_kinds_item_data in self.incident_action_item_kinds:
                incident_action_item_kinds_item: str = incident_action_item_kinds_item_data
                incident_action_item_kinds.append(incident_action_item_kinds_item)

        incident_action_item_condition_status: str | Unset = UNSET
        if not isinstance(self.incident_action_item_condition_status, Unset):
            incident_action_item_condition_status = self.incident_action_item_condition_status

        incident_action_item_statuses: list[str] | Unset = UNSET
        if not isinstance(self.incident_action_item_statuses, Unset):
            incident_action_item_statuses = []
            for incident_action_item_statuses_item_data in self.incident_action_item_statuses:
                incident_action_item_statuses_item: str = incident_action_item_statuses_item_data
                incident_action_item_statuses.append(incident_action_item_statuses_item)

        incident_action_item_condition_priority: str | Unset = UNSET
        if not isinstance(self.incident_action_item_condition_priority, Unset):
            incident_action_item_condition_priority = self.incident_action_item_condition_priority

        incident_action_item_priorities: list[str] | Unset = UNSET
        if not isinstance(self.incident_action_item_priorities, Unset):
            incident_action_item_priorities = []
            for incident_action_item_priorities_item_data in self.incident_action_item_priorities:
                incident_action_item_priorities_item: str = incident_action_item_priorities_item_data
                incident_action_item_priorities.append(incident_action_item_priorities_item)

        incident_action_item_condition_group: str | Unset = UNSET
        if not isinstance(self.incident_action_item_condition_group, Unset):
            incident_action_item_condition_group = self.incident_action_item_condition_group

        incident_action_item_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.incident_action_item_group_ids, Unset):
            incident_action_item_group_ids = self.incident_action_item_group_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trigger_type": trigger_type,
            }
        )
        if triggers is not UNSET:
            field_dict["triggers"] = triggers
        if incident_visibilities is not UNSET:
            field_dict["incident_visibilities"] = incident_visibilities
        if incident_kinds is not UNSET:
            field_dict["incident_kinds"] = incident_kinds
        if incident_statuses is not UNSET:
            field_dict["incident_statuses"] = incident_statuses
        if incident_inactivity_duration is not UNSET:
            field_dict["incident_inactivity_duration"] = incident_inactivity_duration
        if incident_condition is not UNSET:
            field_dict["incident_condition"] = incident_condition
        if incident_condition_visibility is not UNSET:
            field_dict["incident_condition_visibility"] = incident_condition_visibility
        if incident_condition_kind is not UNSET:
            field_dict["incident_condition_kind"] = incident_condition_kind
        if incident_condition_status is not UNSET:
            field_dict["incident_condition_status"] = incident_condition_status
        if incident_condition_sub_status is not UNSET:
            field_dict["incident_condition_sub_status"] = incident_condition_sub_status
        if incident_condition_environment is not UNSET:
            field_dict["incident_condition_environment"] = incident_condition_environment
        if incident_condition_severity is not UNSET:
            field_dict["incident_condition_severity"] = incident_condition_severity
        if incident_condition_incident_type is not UNSET:
            field_dict["incident_condition_incident_type"] = incident_condition_incident_type
        if incident_condition_incident_roles is not UNSET:
            field_dict["incident_condition_incident_roles"] = incident_condition_incident_roles
        if incident_condition_service is not UNSET:
            field_dict["incident_condition_service"] = incident_condition_service
        if incident_condition_functionality is not UNSET:
            field_dict["incident_condition_functionality"] = incident_condition_functionality
        if incident_condition_group is not UNSET:
            field_dict["incident_condition_group"] = incident_condition_group
        if incident_condition_summary is not UNSET:
            field_dict["incident_condition_summary"] = incident_condition_summary
        if incident_condition_started_at is not UNSET:
            field_dict["incident_condition_started_at"] = incident_condition_started_at
        if incident_condition_detected_at is not UNSET:
            field_dict["incident_condition_detected_at"] = incident_condition_detected_at
        if incident_condition_acknowledged_at is not UNSET:
            field_dict["incident_condition_acknowledged_at"] = incident_condition_acknowledged_at
        if incident_condition_mitigated_at is not UNSET:
            field_dict["incident_condition_mitigated_at"] = incident_condition_mitigated_at
        if incident_condition_resolved_at is not UNSET:
            field_dict["incident_condition_resolved_at"] = incident_condition_resolved_at
        if incident_conditional_inactivity is not UNSET:
            field_dict["incident_conditional_inactivity"] = incident_conditional_inactivity
        if incident_action_item_condition is not UNSET:
            field_dict["incident_action_item_condition"] = incident_action_item_condition
        if incident_action_item_condition_kind is not UNSET:
            field_dict["incident_action_item_condition_kind"] = incident_action_item_condition_kind
        if incident_action_item_kinds is not UNSET:
            field_dict["incident_action_item_kinds"] = incident_action_item_kinds
        if incident_action_item_condition_status is not UNSET:
            field_dict["incident_action_item_condition_status"] = incident_action_item_condition_status
        if incident_action_item_statuses is not UNSET:
            field_dict["incident_action_item_statuses"] = incident_action_item_statuses
        if incident_action_item_condition_priority is not UNSET:
            field_dict["incident_action_item_condition_priority"] = incident_action_item_condition_priority
        if incident_action_item_priorities is not UNSET:
            field_dict["incident_action_item_priorities"] = incident_action_item_priorities
        if incident_action_item_condition_group is not UNSET:
            field_dict["incident_action_item_condition_group"] = incident_action_item_condition_group
        if incident_action_item_group_ids is not UNSET:
            field_dict["incident_action_item_group_ids"] = incident_action_item_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trigger_type = check_action_item_trigger_params_trigger_type(d.pop("trigger_type"))

        triggers = cast(list[str], d.pop("triggers", UNSET))

        incident_visibilities = cast(list[bool], d.pop("incident_visibilities", UNSET))

        _incident_kinds = d.pop("incident_kinds", UNSET)
        incident_kinds: list[ActionItemTriggerParamsIncidentKindsItem] | Unset = UNSET
        if _incident_kinds is not UNSET:
            incident_kinds = []
            for incident_kinds_item_data in _incident_kinds:
                incident_kinds_item = check_action_item_trigger_params_incident_kinds_item(incident_kinds_item_data)

                incident_kinds.append(incident_kinds_item)

        _incident_statuses = d.pop("incident_statuses", UNSET)
        incident_statuses: list[ActionItemTriggerParamsIncidentStatusesItem] | Unset = UNSET
        if _incident_statuses is not UNSET:
            incident_statuses = []
            for incident_statuses_item_data in _incident_statuses:
                incident_statuses_item = check_action_item_trigger_params_incident_statuses_item(
                    incident_statuses_item_data
                )

                incident_statuses.append(incident_statuses_item)

        def _parse_incident_inactivity_duration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        incident_inactivity_duration = _parse_incident_inactivity_duration(d.pop("incident_inactivity_duration", UNSET))

        _incident_condition = d.pop("incident_condition", UNSET)
        incident_condition: ActionItemTriggerParamsIncidentCondition | Unset
        if isinstance(_incident_condition, Unset):
            incident_condition = UNSET
        else:
            incident_condition = check_action_item_trigger_params_incident_condition(_incident_condition)

        _incident_condition_visibility = d.pop("incident_condition_visibility", UNSET)
        incident_condition_visibility: ActionItemTriggerParamsIncidentConditionVisibility | Unset
        if isinstance(_incident_condition_visibility, Unset):
            incident_condition_visibility = UNSET
        else:
            incident_condition_visibility = check_action_item_trigger_params_incident_condition_visibility(
                _incident_condition_visibility
            )

        _incident_condition_kind = d.pop("incident_condition_kind", UNSET)
        incident_condition_kind: ActionItemTriggerParamsIncidentConditionKind | Unset
        if isinstance(_incident_condition_kind, Unset):
            incident_condition_kind = UNSET
        else:
            incident_condition_kind = check_action_item_trigger_params_incident_condition_kind(_incident_condition_kind)

        _incident_condition_status = d.pop("incident_condition_status", UNSET)
        incident_condition_status: ActionItemTriggerParamsIncidentConditionStatus | Unset
        if isinstance(_incident_condition_status, Unset):
            incident_condition_status = UNSET
        else:
            incident_condition_status = check_action_item_trigger_params_incident_condition_status(
                _incident_condition_status
            )

        _incident_condition_sub_status = d.pop("incident_condition_sub_status", UNSET)
        incident_condition_sub_status: ActionItemTriggerParamsIncidentConditionSubStatus | Unset
        if isinstance(_incident_condition_sub_status, Unset):
            incident_condition_sub_status = UNSET
        else:
            incident_condition_sub_status = check_action_item_trigger_params_incident_condition_sub_status(
                _incident_condition_sub_status
            )

        _incident_condition_environment = d.pop("incident_condition_environment", UNSET)
        incident_condition_environment: ActionItemTriggerParamsIncidentConditionEnvironment | Unset
        if isinstance(_incident_condition_environment, Unset):
            incident_condition_environment = UNSET
        else:
            incident_condition_environment = check_action_item_trigger_params_incident_condition_environment(
                _incident_condition_environment
            )

        _incident_condition_severity = d.pop("incident_condition_severity", UNSET)
        incident_condition_severity: ActionItemTriggerParamsIncidentConditionSeverity | Unset
        if isinstance(_incident_condition_severity, Unset):
            incident_condition_severity = UNSET
        else:
            incident_condition_severity = check_action_item_trigger_params_incident_condition_severity(
                _incident_condition_severity
            )

        _incident_condition_incident_type = d.pop("incident_condition_incident_type", UNSET)
        incident_condition_incident_type: ActionItemTriggerParamsIncidentConditionIncidentType | Unset
        if isinstance(_incident_condition_incident_type, Unset):
            incident_condition_incident_type = UNSET
        else:
            incident_condition_incident_type = check_action_item_trigger_params_incident_condition_incident_type(
                _incident_condition_incident_type
            )

        _incident_condition_incident_roles = d.pop("incident_condition_incident_roles", UNSET)
        incident_condition_incident_roles: ActionItemTriggerParamsIncidentConditionIncidentRoles | Unset
        if isinstance(_incident_condition_incident_roles, Unset):
            incident_condition_incident_roles = UNSET
        else:
            incident_condition_incident_roles = check_action_item_trigger_params_incident_condition_incident_roles(
                _incident_condition_incident_roles
            )

        _incident_condition_service = d.pop("incident_condition_service", UNSET)
        incident_condition_service: ActionItemTriggerParamsIncidentConditionService | Unset
        if isinstance(_incident_condition_service, Unset):
            incident_condition_service = UNSET
        else:
            incident_condition_service = check_action_item_trigger_params_incident_condition_service(
                _incident_condition_service
            )

        _incident_condition_functionality = d.pop("incident_condition_functionality", UNSET)
        incident_condition_functionality: ActionItemTriggerParamsIncidentConditionFunctionality | Unset
        if isinstance(_incident_condition_functionality, Unset):
            incident_condition_functionality = UNSET
        else:
            incident_condition_functionality = check_action_item_trigger_params_incident_condition_functionality(
                _incident_condition_functionality
            )

        _incident_condition_group = d.pop("incident_condition_group", UNSET)
        incident_condition_group: ActionItemTriggerParamsIncidentConditionGroup | Unset
        if isinstance(_incident_condition_group, Unset):
            incident_condition_group = UNSET
        else:
            incident_condition_group = check_action_item_trigger_params_incident_condition_group(
                _incident_condition_group
            )

        def _parse_incident_condition_summary(
            data: object,
        ) -> ActionItemTriggerParamsIncidentConditionSummaryType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                incident_condition_summary_type_1 = check_action_item_trigger_params_incident_condition_summary_type_1(
                    data
                )

                return incident_condition_summary_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionItemTriggerParamsIncidentConditionSummaryType1 | None | Unset, data)

        incident_condition_summary = _parse_incident_condition_summary(d.pop("incident_condition_summary", UNSET))

        def _parse_incident_condition_started_at(
            data: object,
        ) -> ActionItemTriggerParamsIncidentConditionStartedAtType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                incident_condition_started_at_type_1 = (
                    check_action_item_trigger_params_incident_condition_started_at_type_1(data)
                )

                return incident_condition_started_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionItemTriggerParamsIncidentConditionStartedAtType1 | None | Unset, data)

        incident_condition_started_at = _parse_incident_condition_started_at(
            d.pop("incident_condition_started_at", UNSET)
        )

        def _parse_incident_condition_detected_at(
            data: object,
        ) -> ActionItemTriggerParamsIncidentConditionDetectedAtType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                incident_condition_detected_at_type_1 = (
                    check_action_item_trigger_params_incident_condition_detected_at_type_1(data)
                )

                return incident_condition_detected_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionItemTriggerParamsIncidentConditionDetectedAtType1 | None | Unset, data)

        incident_condition_detected_at = _parse_incident_condition_detected_at(
            d.pop("incident_condition_detected_at", UNSET)
        )

        def _parse_incident_condition_acknowledged_at(
            data: object,
        ) -> ActionItemTriggerParamsIncidentConditionAcknowledgedAtType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                incident_condition_acknowledged_at_type_1 = (
                    check_action_item_trigger_params_incident_condition_acknowledged_at_type_1(data)
                )

                return incident_condition_acknowledged_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionItemTriggerParamsIncidentConditionAcknowledgedAtType1 | None | Unset, data)

        incident_condition_acknowledged_at = _parse_incident_condition_acknowledged_at(
            d.pop("incident_condition_acknowledged_at", UNSET)
        )

        def _parse_incident_condition_mitigated_at(
            data: object,
        ) -> ActionItemTriggerParamsIncidentConditionMitigatedAtType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                incident_condition_mitigated_at_type_1 = (
                    check_action_item_trigger_params_incident_condition_mitigated_at_type_1(data)
                )

                return incident_condition_mitigated_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionItemTriggerParamsIncidentConditionMitigatedAtType1 | None | Unset, data)

        incident_condition_mitigated_at = _parse_incident_condition_mitigated_at(
            d.pop("incident_condition_mitigated_at", UNSET)
        )

        def _parse_incident_condition_resolved_at(
            data: object,
        ) -> ActionItemTriggerParamsIncidentConditionResolvedAtType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                incident_condition_resolved_at_type_1 = (
                    check_action_item_trigger_params_incident_condition_resolved_at_type_1(data)
                )

                return incident_condition_resolved_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionItemTriggerParamsIncidentConditionResolvedAtType1 | None | Unset, data)

        incident_condition_resolved_at = _parse_incident_condition_resolved_at(
            d.pop("incident_condition_resolved_at", UNSET)
        )

        def _parse_incident_conditional_inactivity(
            data: object,
        ) -> ActionItemTriggerParamsIncidentConditionalInactivityType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                incident_conditional_inactivity_type_1 = (
                    check_action_item_trigger_params_incident_conditional_inactivity_type_1(data)
                )

                return incident_conditional_inactivity_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionItemTriggerParamsIncidentConditionalInactivityType1 | None | Unset, data)

        incident_conditional_inactivity = _parse_incident_conditional_inactivity(
            d.pop("incident_conditional_inactivity", UNSET)
        )

        _incident_action_item_condition = d.pop("incident_action_item_condition", UNSET)
        incident_action_item_condition: ActionItemTriggerParamsIncidentActionItemCondition | Unset
        if isinstance(_incident_action_item_condition, Unset):
            incident_action_item_condition = UNSET
        else:
            incident_action_item_condition = check_action_item_trigger_params_incident_action_item_condition(
                _incident_action_item_condition
            )

        _incident_action_item_condition_kind = d.pop("incident_action_item_condition_kind", UNSET)
        incident_action_item_condition_kind: ActionItemTriggerParamsIncidentActionItemConditionKind | Unset
        if isinstance(_incident_action_item_condition_kind, Unset):
            incident_action_item_condition_kind = UNSET
        else:
            incident_action_item_condition_kind = check_action_item_trigger_params_incident_action_item_condition_kind(
                _incident_action_item_condition_kind
            )

        _incident_action_item_kinds = d.pop("incident_action_item_kinds", UNSET)
        incident_action_item_kinds: list[ActionItemTriggerParamsIncidentActionItemKindsItem] | Unset = UNSET
        if _incident_action_item_kinds is not UNSET:
            incident_action_item_kinds = []
            for incident_action_item_kinds_item_data in _incident_action_item_kinds:
                incident_action_item_kinds_item = check_action_item_trigger_params_incident_action_item_kinds_item(
                    incident_action_item_kinds_item_data
                )

                incident_action_item_kinds.append(incident_action_item_kinds_item)

        _incident_action_item_condition_status = d.pop("incident_action_item_condition_status", UNSET)
        incident_action_item_condition_status: ActionItemTriggerParamsIncidentActionItemConditionStatus | Unset
        if isinstance(_incident_action_item_condition_status, Unset):
            incident_action_item_condition_status = UNSET
        else:
            incident_action_item_condition_status = (
                check_action_item_trigger_params_incident_action_item_condition_status(
                    _incident_action_item_condition_status
                )
            )

        _incident_action_item_statuses = d.pop("incident_action_item_statuses", UNSET)
        incident_action_item_statuses: list[ActionItemTriggerParamsIncidentActionItemStatusesItem] | Unset = UNSET
        if _incident_action_item_statuses is not UNSET:
            incident_action_item_statuses = []
            for incident_action_item_statuses_item_data in _incident_action_item_statuses:
                incident_action_item_statuses_item = (
                    check_action_item_trigger_params_incident_action_item_statuses_item(
                        incident_action_item_statuses_item_data
                    )
                )

                incident_action_item_statuses.append(incident_action_item_statuses_item)

        _incident_action_item_condition_priority = d.pop("incident_action_item_condition_priority", UNSET)
        incident_action_item_condition_priority: ActionItemTriggerParamsIncidentActionItemConditionPriority | Unset
        if isinstance(_incident_action_item_condition_priority, Unset):
            incident_action_item_condition_priority = UNSET
        else:
            incident_action_item_condition_priority = (
                check_action_item_trigger_params_incident_action_item_condition_priority(
                    _incident_action_item_condition_priority
                )
            )

        _incident_action_item_priorities = d.pop("incident_action_item_priorities", UNSET)
        incident_action_item_priorities: list[ActionItemTriggerParamsIncidentActionItemPrioritiesItem] | Unset = UNSET
        if _incident_action_item_priorities is not UNSET:
            incident_action_item_priorities = []
            for incident_action_item_priorities_item_data in _incident_action_item_priorities:
                incident_action_item_priorities_item = (
                    check_action_item_trigger_params_incident_action_item_priorities_item(
                        incident_action_item_priorities_item_data
                    )
                )

                incident_action_item_priorities.append(incident_action_item_priorities_item)

        _incident_action_item_condition_group = d.pop("incident_action_item_condition_group", UNSET)
        incident_action_item_condition_group: ActionItemTriggerParamsIncidentActionItemConditionGroup | Unset
        if isinstance(_incident_action_item_condition_group, Unset):
            incident_action_item_condition_group = UNSET
        else:
            incident_action_item_condition_group = (
                check_action_item_trigger_params_incident_action_item_condition_group(
                    _incident_action_item_condition_group
                )
            )

        incident_action_item_group_ids = cast(list[str], d.pop("incident_action_item_group_ids", UNSET))

        action_item_trigger_params = cls(
            trigger_type=trigger_type,
            triggers=triggers,
            incident_visibilities=incident_visibilities,
            incident_kinds=incident_kinds,
            incident_statuses=incident_statuses,
            incident_inactivity_duration=incident_inactivity_duration,
            incident_condition=incident_condition,
            incident_condition_visibility=incident_condition_visibility,
            incident_condition_kind=incident_condition_kind,
            incident_condition_status=incident_condition_status,
            incident_condition_sub_status=incident_condition_sub_status,
            incident_condition_environment=incident_condition_environment,
            incident_condition_severity=incident_condition_severity,
            incident_condition_incident_type=incident_condition_incident_type,
            incident_condition_incident_roles=incident_condition_incident_roles,
            incident_condition_service=incident_condition_service,
            incident_condition_functionality=incident_condition_functionality,
            incident_condition_group=incident_condition_group,
            incident_condition_summary=incident_condition_summary,
            incident_condition_started_at=incident_condition_started_at,
            incident_condition_detected_at=incident_condition_detected_at,
            incident_condition_acknowledged_at=incident_condition_acknowledged_at,
            incident_condition_mitigated_at=incident_condition_mitigated_at,
            incident_condition_resolved_at=incident_condition_resolved_at,
            incident_conditional_inactivity=incident_conditional_inactivity,
            incident_action_item_condition=incident_action_item_condition,
            incident_action_item_condition_kind=incident_action_item_condition_kind,
            incident_action_item_kinds=incident_action_item_kinds,
            incident_action_item_condition_status=incident_action_item_condition_status,
            incident_action_item_statuses=incident_action_item_statuses,
            incident_action_item_condition_priority=incident_action_item_condition_priority,
            incident_action_item_priorities=incident_action_item_priorities,
            incident_action_item_condition_group=incident_action_item_condition_group,
            incident_action_item_group_ids=incident_action_item_group_ids,
        )

        action_item_trigger_params.additional_properties = d
        return action_item_trigger_params

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
