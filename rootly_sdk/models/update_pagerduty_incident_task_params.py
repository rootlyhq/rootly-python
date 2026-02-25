from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_pagerduty_incident_task_params_status import (
    UpdatePagerdutyIncidentTaskParamsStatus,
    check_update_pagerduty_incident_task_params_status,
)
from ..models.update_pagerduty_incident_task_params_task_type import (
    UpdatePagerdutyIncidentTaskParamsTaskType,
    check_update_pagerduty_incident_task_params_task_type,
)
from ..models.update_pagerduty_incident_task_params_urgency import (
    UpdatePagerdutyIncidentTaskParamsUrgency,
    check_update_pagerduty_incident_task_params_urgency,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePagerdutyIncidentTaskParams")


@_attrs_define
class UpdatePagerdutyIncidentTaskParams:
    """
    Attributes:
        pagerduty_incident_id (str): Pagerduty incident id
        task_type (Union[Unset, UpdatePagerdutyIncidentTaskParamsTaskType]):
        title (Union[Unset, str]): Title to update to
        status (Union[Unset, UpdatePagerdutyIncidentTaskParamsStatus]):
        resolution (Union[Unset, str]): A message outlining the incident's resolution in PagerDuty
        escalation_level (Union[Unset, int]): Escalation level of policy attached to incident Example: 1.
        urgency (Union[Unset, UpdatePagerdutyIncidentTaskParamsUrgency]): PagerDuty incident urgency, selecting auto
            will let Rootly auto map our incident severity
        priority (Union[Unset, str]): PagerDuty incident priority, selecting auto will let Rootly auto map our incident
            severity
    """

    pagerduty_incident_id: str
    task_type: Unset | UpdatePagerdutyIncidentTaskParamsTaskType = UNSET
    title: Unset | str = UNSET
    status: Unset | UpdatePagerdutyIncidentTaskParamsStatus = UNSET
    resolution: Unset | str = UNSET
    escalation_level: Unset | int = UNSET
    urgency: Unset | UpdatePagerdutyIncidentTaskParamsUrgency = UNSET
    priority: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagerduty_incident_id = self.pagerduty_incident_id

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        title = self.title

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        resolution = self.resolution

        escalation_level = self.escalation_level

        urgency: Unset | str = UNSET
        if not isinstance(self.urgency, Unset):
            urgency = self.urgency

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pagerduty_incident_id": pagerduty_incident_id,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if escalation_level is not UNSET:
            field_dict["escalation_level"] = escalation_level
        if urgency is not UNSET:
            field_dict["urgency"] = urgency
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pagerduty_incident_id = d.pop("pagerduty_incident_id")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | UpdatePagerdutyIncidentTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_update_pagerduty_incident_task_params_task_type(_task_type)

        title = d.pop("title", UNSET)

        _status = d.pop("status", UNSET)
        status: Unset | UpdatePagerdutyIncidentTaskParamsStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_pagerduty_incident_task_params_status(_status)

        resolution = d.pop("resolution", UNSET)

        escalation_level = d.pop("escalation_level", UNSET)

        _urgency = d.pop("urgency", UNSET)
        urgency: Unset | UpdatePagerdutyIncidentTaskParamsUrgency
        if isinstance(_urgency, Unset):
            urgency = UNSET
        else:
            urgency = check_update_pagerduty_incident_task_params_urgency(_urgency)

        priority = d.pop("priority", UNSET)

        update_pagerduty_incident_task_params = cls(
            pagerduty_incident_id=pagerduty_incident_id,
            task_type=task_type,
            title=title,
            status=status,
            resolution=resolution,
            escalation_level=escalation_level,
            urgency=urgency,
            priority=priority,
        )

        update_pagerduty_incident_task_params.additional_properties = d
        return update_pagerduty_incident_task_params

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
