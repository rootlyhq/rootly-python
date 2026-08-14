from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_run_status import WorkflowRunStatus, check_workflow_run_status
from ..models.workflow_run_triggered_by import WorkflowRunTriggeredBy, check_workflow_run_triggered_by
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_run_context import WorkflowRunContext


T = TypeVar("T", bound="WorkflowRun")


@_attrs_define
class WorkflowRun:
    """
    Attributes:
        workflow_id (str):
        status (WorkflowRunStatus):
        triggered_by (WorkflowRunTriggeredBy):
        status_message (Union[None, Unset, str]):
        started_at (Union[None, Unset, str]):
        completed_at (Union[None, Unset, str]):
        failed_at (Union[None, Unset, str]):
        canceled_at (Union[None, Unset, str]):
        incident_id (Union[None, Unset, str]):
        post_mortem_id (Union[None, Unset, str]):
        action_item_id (Union[None, Unset, str]):
        alert_id (Union[None, Unset, str]):
        pulse_id (Union[None, Unset, str]):
        context (Union[Unset, WorkflowRunContext]):
    """

    workflow_id: str
    status: WorkflowRunStatus
    triggered_by: WorkflowRunTriggeredBy
    status_message: None | Unset | str = UNSET
    started_at: None | Unset | str = UNSET
    completed_at: None | Unset | str = UNSET
    failed_at: None | Unset | str = UNSET
    canceled_at: None | Unset | str = UNSET
    incident_id: None | Unset | str = UNSET
    post_mortem_id: None | Unset | str = UNSET
    action_item_id: None | Unset | str = UNSET
    alert_id: None | Unset | str = UNSET
    pulse_id: None | Unset | str = UNSET
    context: Union[Unset, "WorkflowRunContext"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_id = self.workflow_id

        status: str = self.status

        triggered_by: str = self.triggered_by

        status_message: None | Unset | str
        if isinstance(self.status_message, Unset):
            status_message = UNSET
        else:
            status_message = self.status_message

        started_at: None | Unset | str
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        completed_at: None | Unset | str
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = self.completed_at

        failed_at: None | Unset | str
        if isinstance(self.failed_at, Unset):
            failed_at = UNSET
        else:
            failed_at = self.failed_at

        canceled_at: None | Unset | str
        if isinstance(self.canceled_at, Unset):
            canceled_at = UNSET
        else:
            canceled_at = self.canceled_at

        incident_id: None | Unset | str
        if isinstance(self.incident_id, Unset):
            incident_id = UNSET
        else:
            incident_id = self.incident_id

        post_mortem_id: None | Unset | str
        if isinstance(self.post_mortem_id, Unset):
            post_mortem_id = UNSET
        else:
            post_mortem_id = self.post_mortem_id

        action_item_id: None | Unset | str
        if isinstance(self.action_item_id, Unset):
            action_item_id = UNSET
        else:
            action_item_id = self.action_item_id

        alert_id: None | Unset | str
        if isinstance(self.alert_id, Unset):
            alert_id = UNSET
        else:
            alert_id = self.alert_id

        pulse_id: None | Unset | str
        if isinstance(self.pulse_id, Unset):
            pulse_id = UNSET
        else:
            pulse_id = self.pulse_id

        context: Unset | dict[str, Any] = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "workflow_id": workflow_id,
                "status": status,
                "triggered_by": triggered_by,
            }
        )
        if status_message is not UNSET:
            field_dict["status_message"] = status_message
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if failed_at is not UNSET:
            field_dict["failed_at"] = failed_at
        if canceled_at is not UNSET:
            field_dict["canceled_at"] = canceled_at
        if incident_id is not UNSET:
            field_dict["incident_id"] = incident_id
        if post_mortem_id is not UNSET:
            field_dict["post_mortem_id"] = post_mortem_id
        if action_item_id is not UNSET:
            field_dict["action_item_id"] = action_item_id
        if alert_id is not UNSET:
            field_dict["alert_id"] = alert_id
        if pulse_id is not UNSET:
            field_dict["pulse_id"] = pulse_id
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_run_context import WorkflowRunContext

        d = dict(src_dict)
        workflow_id = d.pop("workflow_id")

        status = check_workflow_run_status(d.pop("status"))

        triggered_by = check_workflow_run_triggered_by(d.pop("triggered_by"))

        def _parse_status_message(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        status_message = _parse_status_message(d.pop("status_message", UNSET))

        def _parse_started_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_completed_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        def _parse_failed_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        failed_at = _parse_failed_at(d.pop("failed_at", UNSET))

        def _parse_canceled_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        canceled_at = _parse_canceled_at(d.pop("canceled_at", UNSET))

        def _parse_incident_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        incident_id = _parse_incident_id(d.pop("incident_id", UNSET))

        def _parse_post_mortem_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        post_mortem_id = _parse_post_mortem_id(d.pop("post_mortem_id", UNSET))

        def _parse_action_item_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        action_item_id = _parse_action_item_id(d.pop("action_item_id", UNSET))

        def _parse_alert_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        alert_id = _parse_alert_id(d.pop("alert_id", UNSET))

        def _parse_pulse_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        pulse_id = _parse_pulse_id(d.pop("pulse_id", UNSET))

        _context = d.pop("context", UNSET)
        context: Unset | WorkflowRunContext
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = WorkflowRunContext.from_dict(_context)

        workflow_run = cls(
            workflow_id=workflow_id,
            status=status,
            triggered_by=triggered_by,
            status_message=status_message,
            started_at=started_at,
            completed_at=completed_at,
            failed_at=failed_at,
            canceled_at=canceled_at,
            incident_id=incident_id,
            post_mortem_id=post_mortem_id,
            action_item_id=action_item_id,
            alert_id=alert_id,
            pulse_id=pulse_id,
            context=context,
        )

        workflow_run.additional_properties = d
        return workflow_run

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
