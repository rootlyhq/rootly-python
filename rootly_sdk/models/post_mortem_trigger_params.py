from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_mortem_trigger_params_incident_condition import (
    PostMortemTriggerParamsIncidentCondition,
    check_post_mortem_trigger_params_incident_condition,
)
from ..models.post_mortem_trigger_params_incident_condition_acknowledged_at_type_1 import (
    PostMortemTriggerParamsIncidentConditionAcknowledgedAtType1,
    check_post_mortem_trigger_params_incident_condition_acknowledged_at_type_1,
)
from ..models.post_mortem_trigger_params_incident_condition_cause import (
    PostMortemTriggerParamsIncidentConditionCause,
    check_post_mortem_trigger_params_incident_condition_cause,
)
from ..models.post_mortem_trigger_params_incident_condition_detected_at_type_1 import (
    PostMortemTriggerParamsIncidentConditionDetectedAtType1,
    check_post_mortem_trigger_params_incident_condition_detected_at_type_1,
)
from ..models.post_mortem_trigger_params_incident_condition_environment import (
    PostMortemTriggerParamsIncidentConditionEnvironment,
    check_post_mortem_trigger_params_incident_condition_environment,
)
from ..models.post_mortem_trigger_params_incident_condition_functionality import (
    PostMortemTriggerParamsIncidentConditionFunctionality,
    check_post_mortem_trigger_params_incident_condition_functionality,
)
from ..models.post_mortem_trigger_params_incident_condition_group import (
    PostMortemTriggerParamsIncidentConditionGroup,
    check_post_mortem_trigger_params_incident_condition_group,
)
from ..models.post_mortem_trigger_params_incident_condition_incident_roles import (
    PostMortemTriggerParamsIncidentConditionIncidentRoles,
    check_post_mortem_trigger_params_incident_condition_incident_roles,
)
from ..models.post_mortem_trigger_params_incident_condition_incident_type import (
    PostMortemTriggerParamsIncidentConditionIncidentType,
    check_post_mortem_trigger_params_incident_condition_incident_type,
)
from ..models.post_mortem_trigger_params_incident_condition_kind import (
    PostMortemTriggerParamsIncidentConditionKind,
    check_post_mortem_trigger_params_incident_condition_kind,
)
from ..models.post_mortem_trigger_params_incident_condition_mitigated_at_type_1 import (
    PostMortemTriggerParamsIncidentConditionMitigatedAtType1,
    check_post_mortem_trigger_params_incident_condition_mitigated_at_type_1,
)
from ..models.post_mortem_trigger_params_incident_condition_resolved_at_type_1 import (
    PostMortemTriggerParamsIncidentConditionResolvedAtType1,
    check_post_mortem_trigger_params_incident_condition_resolved_at_type_1,
)
from ..models.post_mortem_trigger_params_incident_condition_service import (
    PostMortemTriggerParamsIncidentConditionService,
    check_post_mortem_trigger_params_incident_condition_service,
)
from ..models.post_mortem_trigger_params_incident_condition_severity import (
    PostMortemTriggerParamsIncidentConditionSeverity,
    check_post_mortem_trigger_params_incident_condition_severity,
)
from ..models.post_mortem_trigger_params_incident_condition_started_at_type_1 import (
    PostMortemTriggerParamsIncidentConditionStartedAtType1,
    check_post_mortem_trigger_params_incident_condition_started_at_type_1,
)
from ..models.post_mortem_trigger_params_incident_condition_status import (
    PostMortemTriggerParamsIncidentConditionStatus,
    check_post_mortem_trigger_params_incident_condition_status,
)
from ..models.post_mortem_trigger_params_incident_condition_sub_status import (
    PostMortemTriggerParamsIncidentConditionSubStatus,
    check_post_mortem_trigger_params_incident_condition_sub_status,
)
from ..models.post_mortem_trigger_params_incident_condition_summary_type_1 import (
    PostMortemTriggerParamsIncidentConditionSummaryType1,
    check_post_mortem_trigger_params_incident_condition_summary_type_1,
)
from ..models.post_mortem_trigger_params_incident_condition_visibility import (
    PostMortemTriggerParamsIncidentConditionVisibility,
    check_post_mortem_trigger_params_incident_condition_visibility,
)
from ..models.post_mortem_trigger_params_incident_conditional_inactivity_type_1 import (
    PostMortemTriggerParamsIncidentConditionalInactivityType1,
    check_post_mortem_trigger_params_incident_conditional_inactivity_type_1,
)
from ..models.post_mortem_trigger_params_incident_kinds_item import (
    PostMortemTriggerParamsIncidentKindsItem,
    check_post_mortem_trigger_params_incident_kinds_item,
)
from ..models.post_mortem_trigger_params_incident_post_mortem_condition import (
    PostMortemTriggerParamsIncidentPostMortemCondition,
    check_post_mortem_trigger_params_incident_post_mortem_condition,
)
from ..models.post_mortem_trigger_params_incident_post_mortem_condition_cause import (
    PostMortemTriggerParamsIncidentPostMortemConditionCause,
    check_post_mortem_trigger_params_incident_post_mortem_condition_cause,
)
from ..models.post_mortem_trigger_params_incident_post_mortem_condition_status import (
    PostMortemTriggerParamsIncidentPostMortemConditionStatus,
    check_post_mortem_trigger_params_incident_post_mortem_condition_status,
)
from ..models.post_mortem_trigger_params_incident_post_mortem_statuses_item import (
    PostMortemTriggerParamsIncidentPostMortemStatusesItem,
    check_post_mortem_trigger_params_incident_post_mortem_statuses_item,
)
from ..models.post_mortem_trigger_params_incident_statuses_item import (
    PostMortemTriggerParamsIncidentStatusesItem,
    check_post_mortem_trigger_params_incident_statuses_item,
)
from ..models.post_mortem_trigger_params_trigger_type import (
    PostMortemTriggerParamsTriggerType,
    check_post_mortem_trigger_params_trigger_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostMortemTriggerParams")


@_attrs_define
class PostMortemTriggerParams:
    """
    Attributes:
        trigger_type (PostMortemTriggerParamsTriggerType):
        triggers (Union[Unset, list[str]]):
        incident_visibilities (Union[Unset, list[bool]]):
        incident_kinds (Union[Unset, list[PostMortemTriggerParamsIncidentKindsItem]]):
        incident_statuses (Union[Unset, list[PostMortemTriggerParamsIncidentStatusesItem]]):
        incident_inactivity_duration (Union[None, Unset, str]):
        incident_condition (Union[Unset, PostMortemTriggerParamsIncidentCondition]):  Default: 'ALL'.
        incident_condition_visibility (Union[Unset, PostMortemTriggerParamsIncidentConditionVisibility]):  Default:
            'ANY'.
        incident_condition_kind (Union[Unset, PostMortemTriggerParamsIncidentConditionKind]):  Default: 'IS'.
        incident_condition_status (Union[Unset, PostMortemTriggerParamsIncidentConditionStatus]):  Default: 'ANY'.
        incident_condition_sub_status (Union[Unset, PostMortemTriggerParamsIncidentConditionSubStatus]):  Default:
            'ANY'.
        incident_condition_environment (Union[Unset, PostMortemTriggerParamsIncidentConditionEnvironment]):  Default:
            'ANY'.
        incident_condition_severity (Union[Unset, PostMortemTriggerParamsIncidentConditionSeverity]):  Default: 'ANY'.
        incident_condition_incident_type (Union[Unset, PostMortemTriggerParamsIncidentConditionIncidentType]):  Default:
            'ANY'.
        incident_condition_incident_roles (Union[Unset, PostMortemTriggerParamsIncidentConditionIncidentRoles]):
            Default: 'ANY'.
        incident_condition_service (Union[Unset, PostMortemTriggerParamsIncidentConditionService]):  Default: 'ANY'.
        incident_condition_functionality (Union[Unset, PostMortemTriggerParamsIncidentConditionFunctionality]):
            Default: 'ANY'.
        incident_condition_group (Union[Unset, PostMortemTriggerParamsIncidentConditionGroup]):  Default: 'ANY'.
        incident_condition_cause (Union[Unset, PostMortemTriggerParamsIncidentConditionCause]):  Default: 'ANY'.
        incident_post_mortem_condition_cause (Union[Unset, PostMortemTriggerParamsIncidentPostMortemConditionCause]):
            [DEPRECATED] Use incident_condition_cause instead Default: 'ANY'.
        incident_condition_summary (Union[None, PostMortemTriggerParamsIncidentConditionSummaryType1, Unset]):
        incident_condition_started_at (Union[None, PostMortemTriggerParamsIncidentConditionStartedAtType1, Unset]):
        incident_condition_detected_at (Union[None, PostMortemTriggerParamsIncidentConditionDetectedAtType1, Unset]):
        incident_condition_acknowledged_at (Union[None, PostMortemTriggerParamsIncidentConditionAcknowledgedAtType1,
            Unset]):
        incident_condition_mitigated_at (Union[None, PostMortemTriggerParamsIncidentConditionMitigatedAtType1, Unset]):
        incident_condition_resolved_at (Union[None, PostMortemTriggerParamsIncidentConditionResolvedAtType1, Unset]):
        incident_conditional_inactivity (Union[None, PostMortemTriggerParamsIncidentConditionalInactivityType1, Unset]):
        incident_post_mortem_condition (Union[Unset, PostMortemTriggerParamsIncidentPostMortemCondition]):
        incident_post_mortem_condition_status (Union[Unset, PostMortemTriggerParamsIncidentPostMortemConditionStatus]):
            Default: 'ANY'.
        incident_post_mortem_statuses (Union[Unset, list[PostMortemTriggerParamsIncidentPostMortemStatusesItem]]):
    """

    trigger_type: PostMortemTriggerParamsTriggerType
    triggers: Unset | list[str] = UNSET
    incident_visibilities: Unset | list[bool] = UNSET
    incident_kinds: Unset | list[PostMortemTriggerParamsIncidentKindsItem] = UNSET
    incident_statuses: Unset | list[PostMortemTriggerParamsIncidentStatusesItem] = UNSET
    incident_inactivity_duration: None | Unset | str = UNSET
    incident_condition: Unset | PostMortemTriggerParamsIncidentCondition = "ALL"
    incident_condition_visibility: Unset | PostMortemTriggerParamsIncidentConditionVisibility = "ANY"
    incident_condition_kind: Unset | PostMortemTriggerParamsIncidentConditionKind = "IS"
    incident_condition_status: Unset | PostMortemTriggerParamsIncidentConditionStatus = "ANY"
    incident_condition_sub_status: Unset | PostMortemTriggerParamsIncidentConditionSubStatus = "ANY"
    incident_condition_environment: Unset | PostMortemTriggerParamsIncidentConditionEnvironment = "ANY"
    incident_condition_severity: Unset | PostMortemTriggerParamsIncidentConditionSeverity = "ANY"
    incident_condition_incident_type: Unset | PostMortemTriggerParamsIncidentConditionIncidentType = "ANY"
    incident_condition_incident_roles: Unset | PostMortemTriggerParamsIncidentConditionIncidentRoles = "ANY"
    incident_condition_service: Unset | PostMortemTriggerParamsIncidentConditionService = "ANY"
    incident_condition_functionality: Unset | PostMortemTriggerParamsIncidentConditionFunctionality = "ANY"
    incident_condition_group: Unset | PostMortemTriggerParamsIncidentConditionGroup = "ANY"
    incident_condition_cause: Unset | PostMortemTriggerParamsIncidentConditionCause = "ANY"
    incident_post_mortem_condition_cause: Unset | PostMortemTriggerParamsIncidentPostMortemConditionCause = "ANY"
    incident_condition_summary: None | PostMortemTriggerParamsIncidentConditionSummaryType1 | Unset = UNSET
    incident_condition_started_at: None | PostMortemTriggerParamsIncidentConditionStartedAtType1 | Unset = UNSET
    incident_condition_detected_at: None | PostMortemTriggerParamsIncidentConditionDetectedAtType1 | Unset = UNSET
    incident_condition_acknowledged_at: None | PostMortemTriggerParamsIncidentConditionAcknowledgedAtType1 | Unset = (
        UNSET
    )
    incident_condition_mitigated_at: None | PostMortemTriggerParamsIncidentConditionMitigatedAtType1 | Unset = UNSET
    incident_condition_resolved_at: None | PostMortemTriggerParamsIncidentConditionResolvedAtType1 | Unset = UNSET
    incident_conditional_inactivity: None | PostMortemTriggerParamsIncidentConditionalInactivityType1 | Unset = UNSET
    incident_post_mortem_condition: Unset | PostMortemTriggerParamsIncidentPostMortemCondition = UNSET
    incident_post_mortem_condition_status: Unset | PostMortemTriggerParamsIncidentPostMortemConditionStatus = "ANY"
    incident_post_mortem_statuses: Unset | list[PostMortemTriggerParamsIncidentPostMortemStatusesItem] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger_type: str = self.trigger_type

        triggers: Unset | list[str] = UNSET
        if not isinstance(self.triggers, Unset):
            triggers = self.triggers

        incident_visibilities: Unset | list[bool] = UNSET
        if not isinstance(self.incident_visibilities, Unset):
            incident_visibilities = self.incident_visibilities

        incident_kinds: Unset | list[str] = UNSET
        if not isinstance(self.incident_kinds, Unset):
            incident_kinds = []
            for incident_kinds_item_data in self.incident_kinds:
                incident_kinds_item: str = incident_kinds_item_data
                incident_kinds.append(incident_kinds_item)

        incident_statuses: Unset | list[str] = UNSET
        if not isinstance(self.incident_statuses, Unset):
            incident_statuses = []
            for incident_statuses_item_data in self.incident_statuses:
                incident_statuses_item: str = incident_statuses_item_data
                incident_statuses.append(incident_statuses_item)

        incident_inactivity_duration: None | Unset | str
        if isinstance(self.incident_inactivity_duration, Unset):
            incident_inactivity_duration = UNSET
        else:
            incident_inactivity_duration = self.incident_inactivity_duration

        incident_condition: Unset | str = UNSET
        if not isinstance(self.incident_condition, Unset):
            incident_condition = self.incident_condition

        incident_condition_visibility: Unset | str = UNSET
        if not isinstance(self.incident_condition_visibility, Unset):
            incident_condition_visibility = self.incident_condition_visibility

        incident_condition_kind: Unset | str = UNSET
        if not isinstance(self.incident_condition_kind, Unset):
            incident_condition_kind = self.incident_condition_kind

        incident_condition_status: Unset | str = UNSET
        if not isinstance(self.incident_condition_status, Unset):
            incident_condition_status = self.incident_condition_status

        incident_condition_sub_status: Unset | str = UNSET
        if not isinstance(self.incident_condition_sub_status, Unset):
            incident_condition_sub_status = self.incident_condition_sub_status

        incident_condition_environment: Unset | str = UNSET
        if not isinstance(self.incident_condition_environment, Unset):
            incident_condition_environment = self.incident_condition_environment

        incident_condition_severity: Unset | str = UNSET
        if not isinstance(self.incident_condition_severity, Unset):
            incident_condition_severity = self.incident_condition_severity

        incident_condition_incident_type: Unset | str = UNSET
        if not isinstance(self.incident_condition_incident_type, Unset):
            incident_condition_incident_type = self.incident_condition_incident_type

        incident_condition_incident_roles: Unset | str = UNSET
        if not isinstance(self.incident_condition_incident_roles, Unset):
            incident_condition_incident_roles = self.incident_condition_incident_roles

        incident_condition_service: Unset | str = UNSET
        if not isinstance(self.incident_condition_service, Unset):
            incident_condition_service = self.incident_condition_service

        incident_condition_functionality: Unset | str = UNSET
        if not isinstance(self.incident_condition_functionality, Unset):
            incident_condition_functionality = self.incident_condition_functionality

        incident_condition_group: Unset | str = UNSET
        if not isinstance(self.incident_condition_group, Unset):
            incident_condition_group = self.incident_condition_group

        incident_condition_cause: Unset | str = UNSET
        if not isinstance(self.incident_condition_cause, Unset):
            incident_condition_cause = self.incident_condition_cause

        incident_post_mortem_condition_cause: Unset | str = UNSET
        if not isinstance(self.incident_post_mortem_condition_cause, Unset):
            incident_post_mortem_condition_cause = self.incident_post_mortem_condition_cause

        incident_condition_summary: None | Unset | str
        if isinstance(self.incident_condition_summary, Unset):
            incident_condition_summary = UNSET
        elif isinstance(self.incident_condition_summary, str):
            incident_condition_summary = self.incident_condition_summary
        else:
            incident_condition_summary = self.incident_condition_summary

        incident_condition_started_at: None | Unset | str
        if isinstance(self.incident_condition_started_at, Unset):
            incident_condition_started_at = UNSET
        elif isinstance(self.incident_condition_started_at, str):
            incident_condition_started_at = self.incident_condition_started_at
        else:
            incident_condition_started_at = self.incident_condition_started_at

        incident_condition_detected_at: None | Unset | str
        if isinstance(self.incident_condition_detected_at, Unset):
            incident_condition_detected_at = UNSET
        elif isinstance(self.incident_condition_detected_at, str):
            incident_condition_detected_at = self.incident_condition_detected_at
        else:
            incident_condition_detected_at = self.incident_condition_detected_at

        incident_condition_acknowledged_at: None | Unset | str
        if isinstance(self.incident_condition_acknowledged_at, Unset):
            incident_condition_acknowledged_at = UNSET
        elif isinstance(self.incident_condition_acknowledged_at, str):
            incident_condition_acknowledged_at = self.incident_condition_acknowledged_at
        else:
            incident_condition_acknowledged_at = self.incident_condition_acknowledged_at

        incident_condition_mitigated_at: None | Unset | str
        if isinstance(self.incident_condition_mitigated_at, Unset):
            incident_condition_mitigated_at = UNSET
        elif isinstance(self.incident_condition_mitigated_at, str):
            incident_condition_mitigated_at = self.incident_condition_mitigated_at
        else:
            incident_condition_mitigated_at = self.incident_condition_mitigated_at

        incident_condition_resolved_at: None | Unset | str
        if isinstance(self.incident_condition_resolved_at, Unset):
            incident_condition_resolved_at = UNSET
        elif isinstance(self.incident_condition_resolved_at, str):
            incident_condition_resolved_at = self.incident_condition_resolved_at
        else:
            incident_condition_resolved_at = self.incident_condition_resolved_at

        incident_conditional_inactivity: None | Unset | str
        if isinstance(self.incident_conditional_inactivity, Unset):
            incident_conditional_inactivity = UNSET
        elif isinstance(self.incident_conditional_inactivity, str):
            incident_conditional_inactivity = self.incident_conditional_inactivity
        else:
            incident_conditional_inactivity = self.incident_conditional_inactivity

        incident_post_mortem_condition: Unset | str = UNSET
        if not isinstance(self.incident_post_mortem_condition, Unset):
            incident_post_mortem_condition = self.incident_post_mortem_condition

        incident_post_mortem_condition_status: Unset | str = UNSET
        if not isinstance(self.incident_post_mortem_condition_status, Unset):
            incident_post_mortem_condition_status = self.incident_post_mortem_condition_status

        incident_post_mortem_statuses: Unset | list[str] = UNSET
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

        incident_kinds = []
        _incident_kinds = d.pop("incident_kinds", UNSET)
        for incident_kinds_item_data in _incident_kinds or []:
            incident_kinds_item = check_post_mortem_trigger_params_incident_kinds_item(incident_kinds_item_data)

            incident_kinds.append(incident_kinds_item)

        incident_statuses = []
        _incident_statuses = d.pop("incident_statuses", UNSET)
        for incident_statuses_item_data in _incident_statuses or []:
            incident_statuses_item = check_post_mortem_trigger_params_incident_statuses_item(
                incident_statuses_item_data
            )

            incident_statuses.append(incident_statuses_item)

        def _parse_incident_inactivity_duration(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        incident_inactivity_duration = _parse_incident_inactivity_duration(d.pop("incident_inactivity_duration", UNSET))

        _incident_condition = d.pop("incident_condition", UNSET)
        incident_condition: Unset | PostMortemTriggerParamsIncidentCondition
        if isinstance(_incident_condition, Unset):
            incident_condition = UNSET
        else:
            incident_condition = check_post_mortem_trigger_params_incident_condition(_incident_condition)

        _incident_condition_visibility = d.pop("incident_condition_visibility", UNSET)
        incident_condition_visibility: Unset | PostMortemTriggerParamsIncidentConditionVisibility
        if isinstance(_incident_condition_visibility, Unset):
            incident_condition_visibility = UNSET
        else:
            incident_condition_visibility = check_post_mortem_trigger_params_incident_condition_visibility(
                _incident_condition_visibility
            )

        _incident_condition_kind = d.pop("incident_condition_kind", UNSET)
        incident_condition_kind: Unset | PostMortemTriggerParamsIncidentConditionKind
        if isinstance(_incident_condition_kind, Unset):
            incident_condition_kind = UNSET
        else:
            incident_condition_kind = check_post_mortem_trigger_params_incident_condition_kind(_incident_condition_kind)

        _incident_condition_status = d.pop("incident_condition_status", UNSET)
        incident_condition_status: Unset | PostMortemTriggerParamsIncidentConditionStatus
        if isinstance(_incident_condition_status, Unset):
            incident_condition_status = UNSET
        else:
            incident_condition_status = check_post_mortem_trigger_params_incident_condition_status(
                _incident_condition_status
            )

        _incident_condition_sub_status = d.pop("incident_condition_sub_status", UNSET)
        incident_condition_sub_status: Unset | PostMortemTriggerParamsIncidentConditionSubStatus
        if isinstance(_incident_condition_sub_status, Unset):
            incident_condition_sub_status = UNSET
        else:
            incident_condition_sub_status = check_post_mortem_trigger_params_incident_condition_sub_status(
                _incident_condition_sub_status
            )

        _incident_condition_environment = d.pop("incident_condition_environment", UNSET)
        incident_condition_environment: Unset | PostMortemTriggerParamsIncidentConditionEnvironment
        if isinstance(_incident_condition_environment, Unset):
            incident_condition_environment = UNSET
        else:
            incident_condition_environment = check_post_mortem_trigger_params_incident_condition_environment(
                _incident_condition_environment
            )

        _incident_condition_severity = d.pop("incident_condition_severity", UNSET)
        incident_condition_severity: Unset | PostMortemTriggerParamsIncidentConditionSeverity
        if isinstance(_incident_condition_severity, Unset):
            incident_condition_severity = UNSET
        else:
            incident_condition_severity = check_post_mortem_trigger_params_incident_condition_severity(
                _incident_condition_severity
            )

        _incident_condition_incident_type = d.pop("incident_condition_incident_type", UNSET)
        incident_condition_incident_type: Unset | PostMortemTriggerParamsIncidentConditionIncidentType
        if isinstance(_incident_condition_incident_type, Unset):
            incident_condition_incident_type = UNSET
        else:
            incident_condition_incident_type = check_post_mortem_trigger_params_incident_condition_incident_type(
                _incident_condition_incident_type
            )

        _incident_condition_incident_roles = d.pop("incident_condition_incident_roles", UNSET)
        incident_condition_incident_roles: Unset | PostMortemTriggerParamsIncidentConditionIncidentRoles
        if isinstance(_incident_condition_incident_roles, Unset):
            incident_condition_incident_roles = UNSET
        else:
            incident_condition_incident_roles = check_post_mortem_trigger_params_incident_condition_incident_roles(
                _incident_condition_incident_roles
            )

        _incident_condition_service = d.pop("incident_condition_service", UNSET)
        incident_condition_service: Unset | PostMortemTriggerParamsIncidentConditionService
        if isinstance(_incident_condition_service, Unset):
            incident_condition_service = UNSET
        else:
            incident_condition_service = check_post_mortem_trigger_params_incident_condition_service(
                _incident_condition_service
            )

        _incident_condition_functionality = d.pop("incident_condition_functionality", UNSET)
        incident_condition_functionality: Unset | PostMortemTriggerParamsIncidentConditionFunctionality
        if isinstance(_incident_condition_functionality, Unset):
            incident_condition_functionality = UNSET
        else:
            incident_condition_functionality = check_post_mortem_trigger_params_incident_condition_functionality(
                _incident_condition_functionality
            )

        _incident_condition_group = d.pop("incident_condition_group", UNSET)
        incident_condition_group: Unset | PostMortemTriggerParamsIncidentConditionGroup
        if isinstance(_incident_condition_group, Unset):
            incident_condition_group = UNSET
        else:
            incident_condition_group = check_post_mortem_trigger_params_incident_condition_group(
                _incident_condition_group
            )

        _incident_condition_cause = d.pop("incident_condition_cause", UNSET)
        incident_condition_cause: Unset | PostMortemTriggerParamsIncidentConditionCause
        if isinstance(_incident_condition_cause, Unset):
            incident_condition_cause = UNSET
        else:
            incident_condition_cause = check_post_mortem_trigger_params_incident_condition_cause(
                _incident_condition_cause
            )

        _incident_post_mortem_condition_cause = d.pop("incident_post_mortem_condition_cause", UNSET)
        incident_post_mortem_condition_cause: Unset | PostMortemTriggerParamsIncidentPostMortemConditionCause
        if isinstance(_incident_post_mortem_condition_cause, Unset):
            incident_post_mortem_condition_cause = UNSET
        else:
            incident_post_mortem_condition_cause = (
                check_post_mortem_trigger_params_incident_post_mortem_condition_cause(
                    _incident_post_mortem_condition_cause
                )
            )

        def _parse_incident_condition_summary(
            data: object,
        ) -> None | PostMortemTriggerParamsIncidentConditionSummaryType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                incident_condition_summary_type_1 = check_post_mortem_trigger_params_incident_condition_summary_type_1(
                    data
                )

                return incident_condition_summary_type_1
            except:  # noqa: E722
                pass
            return cast(None | PostMortemTriggerParamsIncidentConditionSummaryType1 | Unset, data)

        incident_condition_summary = _parse_incident_condition_summary(d.pop("incident_condition_summary", UNSET))

        def _parse_incident_condition_started_at(
            data: object,
        ) -> None | PostMortemTriggerParamsIncidentConditionStartedAtType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                incident_condition_started_at_type_1 = (
                    check_post_mortem_trigger_params_incident_condition_started_at_type_1(data)
                )

                return incident_condition_started_at_type_1
            except:  # noqa: E722
                pass
            return cast(None | PostMortemTriggerParamsIncidentConditionStartedAtType1 | Unset, data)

        incident_condition_started_at = _parse_incident_condition_started_at(
            d.pop("incident_condition_started_at", UNSET)
        )

        def _parse_incident_condition_detected_at(
            data: object,
        ) -> None | PostMortemTriggerParamsIncidentConditionDetectedAtType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                incident_condition_detected_at_type_1 = (
                    check_post_mortem_trigger_params_incident_condition_detected_at_type_1(data)
                )

                return incident_condition_detected_at_type_1
            except:  # noqa: E722
                pass
            return cast(None | PostMortemTriggerParamsIncidentConditionDetectedAtType1 | Unset, data)

        incident_condition_detected_at = _parse_incident_condition_detected_at(
            d.pop("incident_condition_detected_at", UNSET)
        )

        def _parse_incident_condition_acknowledged_at(
            data: object,
        ) -> None | PostMortemTriggerParamsIncidentConditionAcknowledgedAtType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                incident_condition_acknowledged_at_type_1 = (
                    check_post_mortem_trigger_params_incident_condition_acknowledged_at_type_1(data)
                )

                return incident_condition_acknowledged_at_type_1
            except:  # noqa: E722
                pass
            return cast(None | PostMortemTriggerParamsIncidentConditionAcknowledgedAtType1 | Unset, data)

        incident_condition_acknowledged_at = _parse_incident_condition_acknowledged_at(
            d.pop("incident_condition_acknowledged_at", UNSET)
        )

        def _parse_incident_condition_mitigated_at(
            data: object,
        ) -> None | PostMortemTriggerParamsIncidentConditionMitigatedAtType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                incident_condition_mitigated_at_type_1 = (
                    check_post_mortem_trigger_params_incident_condition_mitigated_at_type_1(data)
                )

                return incident_condition_mitigated_at_type_1
            except:  # noqa: E722
                pass
            return cast(None | PostMortemTriggerParamsIncidentConditionMitigatedAtType1 | Unset, data)

        incident_condition_mitigated_at = _parse_incident_condition_mitigated_at(
            d.pop("incident_condition_mitigated_at", UNSET)
        )

        def _parse_incident_condition_resolved_at(
            data: object,
        ) -> None | PostMortemTriggerParamsIncidentConditionResolvedAtType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                incident_condition_resolved_at_type_1 = (
                    check_post_mortem_trigger_params_incident_condition_resolved_at_type_1(data)
                )

                return incident_condition_resolved_at_type_1
            except:  # noqa: E722
                pass
            return cast(None | PostMortemTriggerParamsIncidentConditionResolvedAtType1 | Unset, data)

        incident_condition_resolved_at = _parse_incident_condition_resolved_at(
            d.pop("incident_condition_resolved_at", UNSET)
        )

        def _parse_incident_conditional_inactivity(
            data: object,
        ) -> None | PostMortemTriggerParamsIncidentConditionalInactivityType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                incident_conditional_inactivity_type_1 = (
                    check_post_mortem_trigger_params_incident_conditional_inactivity_type_1(data)
                )

                return incident_conditional_inactivity_type_1
            except:  # noqa: E722
                pass
            return cast(None | PostMortemTriggerParamsIncidentConditionalInactivityType1 | Unset, data)

        incident_conditional_inactivity = _parse_incident_conditional_inactivity(
            d.pop("incident_conditional_inactivity", UNSET)
        )

        _incident_post_mortem_condition = d.pop("incident_post_mortem_condition", UNSET)
        incident_post_mortem_condition: Unset | PostMortemTriggerParamsIncidentPostMortemCondition
        if isinstance(_incident_post_mortem_condition, Unset):
            incident_post_mortem_condition = UNSET
        else:
            incident_post_mortem_condition = check_post_mortem_trigger_params_incident_post_mortem_condition(
                _incident_post_mortem_condition
            )

        _incident_post_mortem_condition_status = d.pop("incident_post_mortem_condition_status", UNSET)
        incident_post_mortem_condition_status: Unset | PostMortemTriggerParamsIncidentPostMortemConditionStatus
        if isinstance(_incident_post_mortem_condition_status, Unset):
            incident_post_mortem_condition_status = UNSET
        else:
            incident_post_mortem_condition_status = (
                check_post_mortem_trigger_params_incident_post_mortem_condition_status(
                    _incident_post_mortem_condition_status
                )
            )

        incident_post_mortem_statuses = []
        _incident_post_mortem_statuses = d.pop("incident_post_mortem_statuses", UNSET)
        for incident_post_mortem_statuses_item_data in _incident_post_mortem_statuses or []:
            incident_post_mortem_statuses_item = check_post_mortem_trigger_params_incident_post_mortem_statuses_item(
                incident_post_mortem_statuses_item_data
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
