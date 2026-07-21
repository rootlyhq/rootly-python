from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.post_mortem_trigger_params_incident_condition import check_post_mortem_trigger_params_incident_condition
from ..models.post_mortem_trigger_params_incident_condition import PostMortemTriggerParamsIncidentCondition
from ..models.post_mortem_trigger_params_incident_condition_acknowledged_at import (
    check_post_mortem_trigger_params_incident_condition_acknowledged_at,
)
from ..models.post_mortem_trigger_params_incident_condition_acknowledged_at import (
    PostMortemTriggerParamsIncidentConditionAcknowledgedAt,
)
from ..models.post_mortem_trigger_params_incident_condition_cause import (
    check_post_mortem_trigger_params_incident_condition_cause,
)
from ..models.post_mortem_trigger_params_incident_condition_cause import PostMortemTriggerParamsIncidentConditionCause
from ..models.post_mortem_trigger_params_incident_condition_detected_at import (
    check_post_mortem_trigger_params_incident_condition_detected_at,
)
from ..models.post_mortem_trigger_params_incident_condition_detected_at import (
    PostMortemTriggerParamsIncidentConditionDetectedAt,
)
from ..models.post_mortem_trigger_params_incident_condition_environment import (
    check_post_mortem_trigger_params_incident_condition_environment,
)
from ..models.post_mortem_trigger_params_incident_condition_environment import (
    PostMortemTriggerParamsIncidentConditionEnvironment,
)
from ..models.post_mortem_trigger_params_incident_condition_functionality import (
    check_post_mortem_trigger_params_incident_condition_functionality,
)
from ..models.post_mortem_trigger_params_incident_condition_functionality import (
    PostMortemTriggerParamsIncidentConditionFunctionality,
)
from ..models.post_mortem_trigger_params_incident_condition_group import (
    check_post_mortem_trigger_params_incident_condition_group,
)
from ..models.post_mortem_trigger_params_incident_condition_group import PostMortemTriggerParamsIncidentConditionGroup
from ..models.post_mortem_trigger_params_incident_condition_incident_roles import (
    check_post_mortem_trigger_params_incident_condition_incident_roles,
)
from ..models.post_mortem_trigger_params_incident_condition_incident_roles import (
    PostMortemTriggerParamsIncidentConditionIncidentRoles,
)
from ..models.post_mortem_trigger_params_incident_condition_incident_type import (
    check_post_mortem_trigger_params_incident_condition_incident_type,
)
from ..models.post_mortem_trigger_params_incident_condition_incident_type import (
    PostMortemTriggerParamsIncidentConditionIncidentType,
)
from ..models.post_mortem_trigger_params_incident_condition_kind import (
    check_post_mortem_trigger_params_incident_condition_kind,
)
from ..models.post_mortem_trigger_params_incident_condition_kind import PostMortemTriggerParamsIncidentConditionKind
from ..models.post_mortem_trigger_params_incident_condition_label import (
    check_post_mortem_trigger_params_incident_condition_label,
)
from ..models.post_mortem_trigger_params_incident_condition_label import PostMortemTriggerParamsIncidentConditionLabel
from ..models.post_mortem_trigger_params_incident_condition_mitigated_at import (
    check_post_mortem_trigger_params_incident_condition_mitigated_at,
)
from ..models.post_mortem_trigger_params_incident_condition_mitigated_at import (
    PostMortemTriggerParamsIncidentConditionMitigatedAt,
)
from ..models.post_mortem_trigger_params_incident_condition_resolved_at import (
    check_post_mortem_trigger_params_incident_condition_resolved_at,
)
from ..models.post_mortem_trigger_params_incident_condition_resolved_at import (
    PostMortemTriggerParamsIncidentConditionResolvedAt,
)
from ..models.post_mortem_trigger_params_incident_condition_service import (
    check_post_mortem_trigger_params_incident_condition_service,
)
from ..models.post_mortem_trigger_params_incident_condition_service import (
    PostMortemTriggerParamsIncidentConditionService,
)
from ..models.post_mortem_trigger_params_incident_condition_severity import (
    check_post_mortem_trigger_params_incident_condition_severity,
)
from ..models.post_mortem_trigger_params_incident_condition_severity import (
    PostMortemTriggerParamsIncidentConditionSeverity,
)
from ..models.post_mortem_trigger_params_incident_condition_started_at import (
    check_post_mortem_trigger_params_incident_condition_started_at,
)
from ..models.post_mortem_trigger_params_incident_condition_started_at import (
    PostMortemTriggerParamsIncidentConditionStartedAt,
)
from ..models.post_mortem_trigger_params_incident_condition_status import (
    check_post_mortem_trigger_params_incident_condition_status,
)
from ..models.post_mortem_trigger_params_incident_condition_status import PostMortemTriggerParamsIncidentConditionStatus
from ..models.post_mortem_trigger_params_incident_condition_sub_status import (
    check_post_mortem_trigger_params_incident_condition_sub_status,
)
from ..models.post_mortem_trigger_params_incident_condition_sub_status import (
    PostMortemTriggerParamsIncidentConditionSubStatus,
)
from ..models.post_mortem_trigger_params_incident_condition_summary import (
    check_post_mortem_trigger_params_incident_condition_summary,
)
from ..models.post_mortem_trigger_params_incident_condition_summary import (
    PostMortemTriggerParamsIncidentConditionSummary,
)
from ..models.post_mortem_trigger_params_incident_condition_visibility import (
    check_post_mortem_trigger_params_incident_condition_visibility,
)
from ..models.post_mortem_trigger_params_incident_condition_visibility import (
    PostMortemTriggerParamsIncidentConditionVisibility,
)
from ..models.post_mortem_trigger_params_incident_conditional_inactivity import (
    check_post_mortem_trigger_params_incident_conditional_inactivity,
)
from ..models.post_mortem_trigger_params_incident_conditional_inactivity import (
    PostMortemTriggerParamsIncidentConditionalInactivity,
)
from ..models.post_mortem_trigger_params_incident_kinds_item import check_post_mortem_trigger_params_incident_kinds_item
from ..models.post_mortem_trigger_params_incident_kinds_item import PostMortemTriggerParamsIncidentKindsItem
from ..models.post_mortem_trigger_params_incident_post_mortem_condition import (
    check_post_mortem_trigger_params_incident_post_mortem_condition,
)
from ..models.post_mortem_trigger_params_incident_post_mortem_condition import (
    PostMortemTriggerParamsIncidentPostMortemCondition,
)
from ..models.post_mortem_trigger_params_incident_post_mortem_condition_cause import (
    check_post_mortem_trigger_params_incident_post_mortem_condition_cause,
)
from ..models.post_mortem_trigger_params_incident_post_mortem_condition_cause import (
    PostMortemTriggerParamsIncidentPostMortemConditionCause,
)
from ..models.post_mortem_trigger_params_incident_post_mortem_condition_status import (
    check_post_mortem_trigger_params_incident_post_mortem_condition_status,
)
from ..models.post_mortem_trigger_params_incident_post_mortem_condition_status import (
    PostMortemTriggerParamsIncidentPostMortemConditionStatus,
)
from ..models.post_mortem_trigger_params_incident_post_mortem_statuses_item import (
    check_post_mortem_trigger_params_incident_post_mortem_statuses_item,
)
from ..models.post_mortem_trigger_params_incident_post_mortem_statuses_item import (
    PostMortemTriggerParamsIncidentPostMortemStatusesItem,
)
from ..models.post_mortem_trigger_params_incident_statuses_item import (
    check_post_mortem_trigger_params_incident_statuses_item,
)
from ..models.post_mortem_trigger_params_incident_statuses_item import PostMortemTriggerParamsIncidentStatusesItem
from ..models.post_mortem_trigger_params_trigger_type import check_post_mortem_trigger_params_trigger_type
from ..models.post_mortem_trigger_params_trigger_type import PostMortemTriggerParamsTriggerType
from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="PostMortemTriggerParams")


@_attrs_define
class PostMortemTriggerParams:
    """
    Attributes:
        trigger_type (PostMortemTriggerParamsTriggerType):
        triggers (list[str] | Unset):
        incident_visibilities (list[bool] | Unset):
        incident_kinds (list[PostMortemTriggerParamsIncidentKindsItem] | Unset):
        incident_statuses (list[PostMortemTriggerParamsIncidentStatusesItem] | Unset):
        incident_inactivity_duration (None | str | Unset): ex. 10 min, 1h, 3 days, 2 weeks
        incident_condition (PostMortemTriggerParamsIncidentCondition | Unset):  Default: 'ALL'.
        incident_condition_visibility (PostMortemTriggerParamsIncidentConditionVisibility | Unset):  Default: 'ANY'.
        incident_condition_kind (PostMortemTriggerParamsIncidentConditionKind | Unset):  Default: 'IS'.
        incident_condition_status (PostMortemTriggerParamsIncidentConditionStatus | Unset):  Default: 'ANY'.
        incident_condition_sub_status (PostMortemTriggerParamsIncidentConditionSubStatus | Unset):  Default: 'ANY'.
        incident_condition_environment (PostMortemTriggerParamsIncidentConditionEnvironment | Unset):  Default: 'ANY'.
        incident_condition_severity (PostMortemTriggerParamsIncidentConditionSeverity | Unset):  Default: 'ANY'.
        incident_condition_incident_type (PostMortemTriggerParamsIncidentConditionIncidentType | Unset):  Default:
            'ANY'.
        incident_condition_incident_roles (PostMortemTriggerParamsIncidentConditionIncidentRoles | Unset):  Default:
            'ANY'.
        incident_condition_service (PostMortemTriggerParamsIncidentConditionService | Unset):  Default: 'ANY'.
        incident_condition_functionality (PostMortemTriggerParamsIncidentConditionFunctionality | Unset):  Default:
            'ANY'.
        incident_condition_group (PostMortemTriggerParamsIncidentConditionGroup | Unset):  Default: 'ANY'.
        incident_condition_cause (PostMortemTriggerParamsIncidentConditionCause | Unset):  Default: 'ANY'.
        incident_condition_label (PostMortemTriggerParamsIncidentConditionLabel | Unset):  Default: 'ANY'.
        incident_condition_label_use_regexp (bool | Unset):  Default: False.
        incident_labels (list[str] | Unset):
        incident_post_mortem_condition_cause (PostMortemTriggerParamsIncidentPostMortemConditionCause | Unset):
            [DEPRECATED] Use incident_condition_cause instead Default: 'ANY'.
        incident_condition_summary (PostMortemTriggerParamsIncidentConditionSummary | Unset):
        incident_condition_started_at (PostMortemTriggerParamsIncidentConditionStartedAt | Unset):
        incident_condition_detected_at (PostMortemTriggerParamsIncidentConditionDetectedAt | Unset):
        incident_condition_acknowledged_at (PostMortemTriggerParamsIncidentConditionAcknowledgedAt | Unset):
        incident_condition_mitigated_at (PostMortemTriggerParamsIncidentConditionMitigatedAt | Unset):
        incident_condition_resolved_at (PostMortemTriggerParamsIncidentConditionResolvedAt | Unset):
        incident_conditional_inactivity (PostMortemTriggerParamsIncidentConditionalInactivity | Unset):
        incident_post_mortem_condition (PostMortemTriggerParamsIncidentPostMortemCondition | Unset):
        incident_post_mortem_condition_status (PostMortemTriggerParamsIncidentPostMortemConditionStatus | Unset):
            Default: 'ANY'.
        incident_post_mortem_statuses (list[PostMortemTriggerParamsIncidentPostMortemStatusesItem] | Unset):
    """

    trigger_type: PostMortemTriggerParamsTriggerType
    triggers: list[str] | Unset = UNSET
    incident_visibilities: list[bool] | Unset = UNSET
    incident_kinds: list[PostMortemTriggerParamsIncidentKindsItem] | Unset = UNSET
    incident_statuses: list[PostMortemTriggerParamsIncidentStatusesItem] | Unset = UNSET
    incident_inactivity_duration: None | str | Unset = UNSET
    incident_condition: PostMortemTriggerParamsIncidentCondition | Unset = "ALL"
    incident_condition_visibility: PostMortemTriggerParamsIncidentConditionVisibility | Unset = "ANY"
    incident_condition_kind: PostMortemTriggerParamsIncidentConditionKind | Unset = "IS"
    incident_condition_status: PostMortemTriggerParamsIncidentConditionStatus | Unset = "ANY"
    incident_condition_sub_status: PostMortemTriggerParamsIncidentConditionSubStatus | Unset = "ANY"
    incident_condition_environment: PostMortemTriggerParamsIncidentConditionEnvironment | Unset = "ANY"
    incident_condition_severity: PostMortemTriggerParamsIncidentConditionSeverity | Unset = "ANY"
    incident_condition_incident_type: PostMortemTriggerParamsIncidentConditionIncidentType | Unset = "ANY"
    incident_condition_incident_roles: PostMortemTriggerParamsIncidentConditionIncidentRoles | Unset = "ANY"
    incident_condition_service: PostMortemTriggerParamsIncidentConditionService | Unset = "ANY"
    incident_condition_functionality: PostMortemTriggerParamsIncidentConditionFunctionality | Unset = "ANY"
    incident_condition_group: PostMortemTriggerParamsIncidentConditionGroup | Unset = "ANY"
    incident_condition_cause: PostMortemTriggerParamsIncidentConditionCause | Unset = "ANY"
    incident_condition_label: PostMortemTriggerParamsIncidentConditionLabel | Unset = "ANY"
    incident_condition_label_use_regexp: bool | Unset = False
    incident_labels: list[str] | Unset = UNSET
    incident_post_mortem_condition_cause: PostMortemTriggerParamsIncidentPostMortemConditionCause | Unset = "ANY"
    incident_condition_summary: PostMortemTriggerParamsIncidentConditionSummary | Unset = UNSET
    incident_condition_started_at: PostMortemTriggerParamsIncidentConditionStartedAt | Unset = UNSET
    incident_condition_detected_at: PostMortemTriggerParamsIncidentConditionDetectedAt | Unset = UNSET
    incident_condition_acknowledged_at: PostMortemTriggerParamsIncidentConditionAcknowledgedAt | Unset = UNSET
    incident_condition_mitigated_at: PostMortemTriggerParamsIncidentConditionMitigatedAt | Unset = UNSET
    incident_condition_resolved_at: PostMortemTriggerParamsIncidentConditionResolvedAt | Unset = UNSET
    incident_conditional_inactivity: PostMortemTriggerParamsIncidentConditionalInactivity | Unset = UNSET
    incident_post_mortem_condition: PostMortemTriggerParamsIncidentPostMortemCondition | Unset = UNSET
    incident_post_mortem_condition_status: PostMortemTriggerParamsIncidentPostMortemConditionStatus | Unset = "ANY"
    incident_post_mortem_statuses: list[PostMortemTriggerParamsIncidentPostMortemStatusesItem] | Unset = UNSET
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

        incident_condition_cause: str | Unset = UNSET
        if not isinstance(self.incident_condition_cause, Unset):
            incident_condition_cause = self.incident_condition_cause

        incident_condition_label: str | Unset = UNSET
        if not isinstance(self.incident_condition_label, Unset):
            incident_condition_label = self.incident_condition_label

        incident_condition_label_use_regexp = self.incident_condition_label_use_regexp

        incident_labels: list[str] | Unset = UNSET
        if not isinstance(self.incident_labels, Unset):
            incident_labels = self.incident_labels

        incident_post_mortem_condition_cause: str | Unset = UNSET
        if not isinstance(self.incident_post_mortem_condition_cause, Unset):
            incident_post_mortem_condition_cause = self.incident_post_mortem_condition_cause

        incident_condition_summary: str | Unset = UNSET
        if not isinstance(self.incident_condition_summary, Unset):
            incident_condition_summary = self.incident_condition_summary

        incident_condition_started_at: str | Unset = UNSET
        if not isinstance(self.incident_condition_started_at, Unset):
            incident_condition_started_at = self.incident_condition_started_at

        incident_condition_detected_at: str | Unset = UNSET
        if not isinstance(self.incident_condition_detected_at, Unset):
            incident_condition_detected_at = self.incident_condition_detected_at

        incident_condition_acknowledged_at: str | Unset = UNSET
        if not isinstance(self.incident_condition_acknowledged_at, Unset):
            incident_condition_acknowledged_at = self.incident_condition_acknowledged_at

        incident_condition_mitigated_at: str | Unset = UNSET
        if not isinstance(self.incident_condition_mitigated_at, Unset):
            incident_condition_mitigated_at = self.incident_condition_mitigated_at

        incident_condition_resolved_at: str | Unset = UNSET
        if not isinstance(self.incident_condition_resolved_at, Unset):
            incident_condition_resolved_at = self.incident_condition_resolved_at

        incident_conditional_inactivity: str | Unset = UNSET
        if not isinstance(self.incident_conditional_inactivity, Unset):
            incident_conditional_inactivity = self.incident_conditional_inactivity

        incident_post_mortem_condition: str | Unset = UNSET
        if not isinstance(self.incident_post_mortem_condition, Unset):
            incident_post_mortem_condition = self.incident_post_mortem_condition

        incident_post_mortem_condition_status: str | Unset = UNSET
        if not isinstance(self.incident_post_mortem_condition_status, Unset):
            incident_post_mortem_condition_status = self.incident_post_mortem_condition_status

        incident_post_mortem_statuses: list[str] | Unset = UNSET
        if not isinstance(self.incident_post_mortem_statuses, Unset):
            incident_post_mortem_statuses = []
            for incident_post_mortem_statuses_item_data in self.incident_post_mortem_statuses:
                incident_post_mortem_statuses_item: str = incident_post_mortem_statuses_item_data
                incident_post_mortem_statuses.append(incident_post_mortem_statuses_item)

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
        if incident_condition_cause is not UNSET:
            field_dict["incident_condition_cause"] = incident_condition_cause
        if incident_condition_label is not UNSET:
            field_dict["incident_condition_label"] = incident_condition_label
        if incident_condition_label_use_regexp is not UNSET:
            field_dict["incident_condition_label_use_regexp"] = incident_condition_label_use_regexp
        if incident_labels is not UNSET:
            field_dict["incident_labels"] = incident_labels
        if incident_post_mortem_condition_cause is not UNSET:
            field_dict["incident_post_mortem_condition_cause"] = incident_post_mortem_condition_cause
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
        if incident_post_mortem_condition is not UNSET:
            field_dict["incident_post_mortem_condition"] = incident_post_mortem_condition
        if incident_post_mortem_condition_status is not UNSET:
            field_dict["incident_post_mortem_condition_status"] = incident_post_mortem_condition_status
        if incident_post_mortem_statuses is not UNSET:
            field_dict["incident_post_mortem_statuses"] = incident_post_mortem_statuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trigger_type = check_post_mortem_trigger_params_trigger_type(d.pop("trigger_type"))

        triggers = cast(list[str], d.pop("triggers", UNSET))

        incident_visibilities = cast(list[bool], d.pop("incident_visibilities", UNSET))

        _incident_kinds = d.pop("incident_kinds", UNSET)
        incident_kinds: list[PostMortemTriggerParamsIncidentKindsItem] | Unset = UNSET
        if _incident_kinds is not UNSET:
            incident_kinds = []
            for incident_kinds_item_data in _incident_kinds:
                incident_kinds_item = check_post_mortem_trigger_params_incident_kinds_item(incident_kinds_item_data)

                incident_kinds.append(incident_kinds_item)

        _incident_statuses = d.pop("incident_statuses", UNSET)
        incident_statuses: list[PostMortemTriggerParamsIncidentStatusesItem] | Unset = UNSET
        if _incident_statuses is not UNSET:
            incident_statuses = []
            for incident_statuses_item_data in _incident_statuses:
                incident_statuses_item = check_post_mortem_trigger_params_incident_statuses_item(
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
        incident_condition: PostMortemTriggerParamsIncidentCondition | Unset
        if isinstance(_incident_condition, Unset):
            incident_condition = UNSET
        else:
            incident_condition = check_post_mortem_trigger_params_incident_condition(_incident_condition)

        _incident_condition_visibility = d.pop("incident_condition_visibility", UNSET)
        incident_condition_visibility: PostMortemTriggerParamsIncidentConditionVisibility | Unset
        if isinstance(_incident_condition_visibility, Unset):
            incident_condition_visibility = UNSET
        else:
            incident_condition_visibility = check_post_mortem_trigger_params_incident_condition_visibility(
                _incident_condition_visibility
            )

        _incident_condition_kind = d.pop("incident_condition_kind", UNSET)
        incident_condition_kind: PostMortemTriggerParamsIncidentConditionKind | Unset
        if isinstance(_incident_condition_kind, Unset):
            incident_condition_kind = UNSET
        else:
            incident_condition_kind = check_post_mortem_trigger_params_incident_condition_kind(_incident_condition_kind)

        _incident_condition_status = d.pop("incident_condition_status", UNSET)
        incident_condition_status: PostMortemTriggerParamsIncidentConditionStatus | Unset
        if isinstance(_incident_condition_status, Unset):
            incident_condition_status = UNSET
        else:
            incident_condition_status = check_post_mortem_trigger_params_incident_condition_status(
                _incident_condition_status
            )

        _incident_condition_sub_status = d.pop("incident_condition_sub_status", UNSET)
        incident_condition_sub_status: PostMortemTriggerParamsIncidentConditionSubStatus | Unset
        if isinstance(_incident_condition_sub_status, Unset):
            incident_condition_sub_status = UNSET
        else:
            incident_condition_sub_status = check_post_mortem_trigger_params_incident_condition_sub_status(
                _incident_condition_sub_status
            )

        _incident_condition_environment = d.pop("incident_condition_environment", UNSET)
        incident_condition_environment: PostMortemTriggerParamsIncidentConditionEnvironment | Unset
        if isinstance(_incident_condition_environment, Unset):
            incident_condition_environment = UNSET
        else:
            incident_condition_environment = check_post_mortem_trigger_params_incident_condition_environment(
                _incident_condition_environment
            )

        _incident_condition_severity = d.pop("incident_condition_severity", UNSET)
        incident_condition_severity: PostMortemTriggerParamsIncidentConditionSeverity | Unset
        if isinstance(_incident_condition_severity, Unset):
            incident_condition_severity = UNSET
        else:
            incident_condition_severity = check_post_mortem_trigger_params_incident_condition_severity(
                _incident_condition_severity
            )

        _incident_condition_incident_type = d.pop("incident_condition_incident_type", UNSET)
        incident_condition_incident_type: PostMortemTriggerParamsIncidentConditionIncidentType | Unset
        if isinstance(_incident_condition_incident_type, Unset):
            incident_condition_incident_type = UNSET
        else:
            incident_condition_incident_type = check_post_mortem_trigger_params_incident_condition_incident_type(
                _incident_condition_incident_type
            )

        _incident_condition_incident_roles = d.pop("incident_condition_incident_roles", UNSET)
        incident_condition_incident_roles: PostMortemTriggerParamsIncidentConditionIncidentRoles | Unset
        if isinstance(_incident_condition_incident_roles, Unset):
            incident_condition_incident_roles = UNSET
        else:
            incident_condition_incident_roles = check_post_mortem_trigger_params_incident_condition_incident_roles(
                _incident_condition_incident_roles
            )

        _incident_condition_service = d.pop("incident_condition_service", UNSET)
        incident_condition_service: PostMortemTriggerParamsIncidentConditionService | Unset
        if isinstance(_incident_condition_service, Unset):
            incident_condition_service = UNSET
        else:
            incident_condition_service = check_post_mortem_trigger_params_incident_condition_service(
                _incident_condition_service
            )

        _incident_condition_functionality = d.pop("incident_condition_functionality", UNSET)
        incident_condition_functionality: PostMortemTriggerParamsIncidentConditionFunctionality | Unset
        if isinstance(_incident_condition_functionality, Unset):
            incident_condition_functionality = UNSET
        else:
            incident_condition_functionality = check_post_mortem_trigger_params_incident_condition_functionality(
                _incident_condition_functionality
            )

        _incident_condition_group = d.pop("incident_condition_group", UNSET)
        incident_condition_group: PostMortemTriggerParamsIncidentConditionGroup | Unset
        if isinstance(_incident_condition_group, Unset):
            incident_condition_group = UNSET
        else:
            incident_condition_group = check_post_mortem_trigger_params_incident_condition_group(
                _incident_condition_group
            )

        _incident_condition_cause = d.pop("incident_condition_cause", UNSET)
        incident_condition_cause: PostMortemTriggerParamsIncidentConditionCause | Unset
        if isinstance(_incident_condition_cause, Unset):
            incident_condition_cause = UNSET
        else:
            incident_condition_cause = check_post_mortem_trigger_params_incident_condition_cause(
                _incident_condition_cause
            )

        _incident_condition_label = d.pop("incident_condition_label", UNSET)
        incident_condition_label: PostMortemTriggerParamsIncidentConditionLabel | Unset
        if isinstance(_incident_condition_label, Unset):
            incident_condition_label = UNSET
        else:
            incident_condition_label = check_post_mortem_trigger_params_incident_condition_label(
                _incident_condition_label
            )

        incident_condition_label_use_regexp = d.pop("incident_condition_label_use_regexp", UNSET)

        incident_labels = cast(list[str], d.pop("incident_labels", UNSET))

        _incident_post_mortem_condition_cause = d.pop("incident_post_mortem_condition_cause", UNSET)
        incident_post_mortem_condition_cause: PostMortemTriggerParamsIncidentPostMortemConditionCause | Unset
        if isinstance(_incident_post_mortem_condition_cause, Unset):
            incident_post_mortem_condition_cause = UNSET
        else:
            incident_post_mortem_condition_cause = (
                check_post_mortem_trigger_params_incident_post_mortem_condition_cause(
                    _incident_post_mortem_condition_cause
                )
            )

        _incident_condition_summary = d.pop("incident_condition_summary", UNSET)
        incident_condition_summary: PostMortemTriggerParamsIncidentConditionSummary | Unset
        if isinstance(_incident_condition_summary, Unset):
            incident_condition_summary = UNSET
        else:
            incident_condition_summary = check_post_mortem_trigger_params_incident_condition_summary(
                _incident_condition_summary
            )

        _incident_condition_started_at = d.pop("incident_condition_started_at", UNSET)
        incident_condition_started_at: PostMortemTriggerParamsIncidentConditionStartedAt | Unset
        if isinstance(_incident_condition_started_at, Unset):
            incident_condition_started_at = UNSET
        else:
            incident_condition_started_at = check_post_mortem_trigger_params_incident_condition_started_at(
                _incident_condition_started_at
            )

        _incident_condition_detected_at = d.pop("incident_condition_detected_at", UNSET)
        incident_condition_detected_at: PostMortemTriggerParamsIncidentConditionDetectedAt | Unset
        if isinstance(_incident_condition_detected_at, Unset):
            incident_condition_detected_at = UNSET
        else:
            incident_condition_detected_at = check_post_mortem_trigger_params_incident_condition_detected_at(
                _incident_condition_detected_at
            )

        _incident_condition_acknowledged_at = d.pop("incident_condition_acknowledged_at", UNSET)
        incident_condition_acknowledged_at: PostMortemTriggerParamsIncidentConditionAcknowledgedAt | Unset
        if isinstance(_incident_condition_acknowledged_at, Unset):
            incident_condition_acknowledged_at = UNSET
        else:
            incident_condition_acknowledged_at = check_post_mortem_trigger_params_incident_condition_acknowledged_at(
                _incident_condition_acknowledged_at
            )

        _incident_condition_mitigated_at = d.pop("incident_condition_mitigated_at", UNSET)
        incident_condition_mitigated_at: PostMortemTriggerParamsIncidentConditionMitigatedAt | Unset
        if isinstance(_incident_condition_mitigated_at, Unset):
            incident_condition_mitigated_at = UNSET
        else:
            incident_condition_mitigated_at = check_post_mortem_trigger_params_incident_condition_mitigated_at(
                _incident_condition_mitigated_at
            )

        _incident_condition_resolved_at = d.pop("incident_condition_resolved_at", UNSET)
        incident_condition_resolved_at: PostMortemTriggerParamsIncidentConditionResolvedAt | Unset
        if isinstance(_incident_condition_resolved_at, Unset):
            incident_condition_resolved_at = UNSET
        else:
            incident_condition_resolved_at = check_post_mortem_trigger_params_incident_condition_resolved_at(
                _incident_condition_resolved_at
            )

        _incident_conditional_inactivity = d.pop("incident_conditional_inactivity", UNSET)
        incident_conditional_inactivity: PostMortemTriggerParamsIncidentConditionalInactivity | Unset
        if isinstance(_incident_conditional_inactivity, Unset):
            incident_conditional_inactivity = UNSET
        else:
            incident_conditional_inactivity = check_post_mortem_trigger_params_incident_conditional_inactivity(
                _incident_conditional_inactivity
            )

        _incident_post_mortem_condition = d.pop("incident_post_mortem_condition", UNSET)
        incident_post_mortem_condition: PostMortemTriggerParamsIncidentPostMortemCondition | Unset
        if isinstance(_incident_post_mortem_condition, Unset):
            incident_post_mortem_condition = UNSET
        else:
            incident_post_mortem_condition = check_post_mortem_trigger_params_incident_post_mortem_condition(
                _incident_post_mortem_condition
            )

        _incident_post_mortem_condition_status = d.pop("incident_post_mortem_condition_status", UNSET)
        incident_post_mortem_condition_status: PostMortemTriggerParamsIncidentPostMortemConditionStatus | Unset
        if isinstance(_incident_post_mortem_condition_status, Unset):
            incident_post_mortem_condition_status = UNSET
        else:
            incident_post_mortem_condition_status = (
                check_post_mortem_trigger_params_incident_post_mortem_condition_status(
                    _incident_post_mortem_condition_status
                )
            )

        _incident_post_mortem_statuses = d.pop("incident_post_mortem_statuses", UNSET)
        incident_post_mortem_statuses: list[PostMortemTriggerParamsIncidentPostMortemStatusesItem] | Unset = UNSET
        if _incident_post_mortem_statuses is not UNSET:
            incident_post_mortem_statuses = []
            for incident_post_mortem_statuses_item_data in _incident_post_mortem_statuses:
                incident_post_mortem_statuses_item = (
                    check_post_mortem_trigger_params_incident_post_mortem_statuses_item(
                        incident_post_mortem_statuses_item_data
                    )
                )

                incident_post_mortem_statuses.append(incident_post_mortem_statuses_item)

        post_mortem_trigger_params = cls(
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
            incident_condition_cause=incident_condition_cause,
            incident_condition_label=incident_condition_label,
            incident_condition_label_use_regexp=incident_condition_label_use_regexp,
            incident_labels=incident_labels,
            incident_post_mortem_condition_cause=incident_post_mortem_condition_cause,
            incident_condition_summary=incident_condition_summary,
            incident_condition_started_at=incident_condition_started_at,
            incident_condition_detected_at=incident_condition_detected_at,
            incident_condition_acknowledged_at=incident_condition_acknowledged_at,
            incident_condition_mitigated_at=incident_condition_mitigated_at,
            incident_condition_resolved_at=incident_condition_resolved_at,
            incident_conditional_inactivity=incident_conditional_inactivity,
            incident_post_mortem_condition=incident_post_mortem_condition,
            incident_post_mortem_condition_status=incident_post_mortem_condition_status,
            incident_post_mortem_statuses=incident_post_mortem_statuses,
        )

        post_mortem_trigger_params.additional_properties = d
        return post_mortem_trigger_params

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
