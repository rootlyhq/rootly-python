from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_event_action import AlertEventAction, check_alert_event_action
from ..models.alert_event_kind import AlertEventKind, check_alert_event_kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_event_escalation_target_type_0 import AlertEventEscalationTargetType0
    from ..models.alert_event_incident_type_0 import AlertEventIncidentType0
    from ..models.alert_event_schedule_type_0 import AlertEventScheduleType0
    from ..models.alert_event_user import AlertEventUser
    from ..models.slack_channel import SlackChannel


T = TypeVar("T", bound="AlertEvent")


@_attrs_define
class AlertEvent:
    """
    Attributes:
        alert_id (str): ID of the alert this event belongs to.
        kind (AlertEventKind):
        action (AlertEventAction):
        source (str):
        created_at (str):
        updated_at (str):
        user_id (Union[None, Unset, int]): Author of the note.
        details (Union[None, Unset, str]): Note message.
        user (Union[Unset, AlertEventUser]):
        incident (Union['AlertEventIncidentType0', None, Unset]):
        schedule (Union['AlertEventScheduleType0', None, Unset]):
        escalation_level (Union[None, Unset, int]):
        escalation_target_type (Union[None, Unset, str]): e.g. EscalationPolicy, User.
        escalation_target (Union['AlertEventEscalationTargetType0', None, Unset]): JSON:API-wrapped escalation target
            (User or EscalationPolicy).
        slack_channel (Union[Unset, SlackChannel]):
        incident_ids (Union[None, Unset, list[str]]):
    """

    alert_id: str
    kind: AlertEventKind
    action: AlertEventAction
    source: str
    created_at: str
    updated_at: str
    user_id: Union[None, Unset, int] = UNSET
    details: Union[None, Unset, str] = UNSET
    user: Union[Unset, "AlertEventUser"] = UNSET
    incident: Union["AlertEventIncidentType0", None, Unset] = UNSET
    schedule: Union["AlertEventScheduleType0", None, Unset] = UNSET
    escalation_level: Union[None, Unset, int] = UNSET
    escalation_target_type: Union[None, Unset, str] = UNSET
    escalation_target: Union["AlertEventEscalationTargetType0", None, Unset] = UNSET
    slack_channel: Union[Unset, "SlackChannel"] = UNSET
    incident_ids: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.alert_event_escalation_target_type_0 import AlertEventEscalationTargetType0
        from ..models.alert_event_incident_type_0 import AlertEventIncidentType0
        from ..models.alert_event_schedule_type_0 import AlertEventScheduleType0

        alert_id = self.alert_id

        kind: str = self.kind

        action: str = self.action

        source = self.source

        created_at = self.created_at

        updated_at = self.updated_at

        user_id: Union[None, Unset, int]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        details: Union[None, Unset, str]
        if isinstance(self.details, Unset):
            details = UNSET
        else:
            details = self.details

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        incident: Union[None, Unset, dict[str, Any]]
        if isinstance(self.incident, Unset):
            incident = UNSET
        elif isinstance(self.incident, AlertEventIncidentType0):
            incident = self.incident.to_dict()
        else:
            incident = self.incident

        schedule: Union[None, Unset, dict[str, Any]]
        if isinstance(self.schedule, Unset):
            schedule = UNSET
        elif isinstance(self.schedule, AlertEventScheduleType0):
            schedule = self.schedule.to_dict()
        else:
            schedule = self.schedule

        escalation_level: Union[None, Unset, int]
        if isinstance(self.escalation_level, Unset):
            escalation_level = UNSET
        else:
            escalation_level = self.escalation_level

        escalation_target_type: Union[None, Unset, str]
        if isinstance(self.escalation_target_type, Unset):
            escalation_target_type = UNSET
        else:
            escalation_target_type = self.escalation_target_type

        escalation_target: Union[None, Unset, dict[str, Any]]
        if isinstance(self.escalation_target, Unset):
            escalation_target = UNSET
        elif isinstance(self.escalation_target, AlertEventEscalationTargetType0):
            escalation_target = self.escalation_target.to_dict()
        else:
            escalation_target = self.escalation_target

        slack_channel: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.slack_channel, Unset):
            slack_channel = self.slack_channel.to_dict()

        incident_ids: Union[None, Unset, list[str]]
        if isinstance(self.incident_ids, Unset):
            incident_ids = UNSET
        elif isinstance(self.incident_ids, list):
            incident_ids = self.incident_ids

        else:
            incident_ids = self.incident_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_id": alert_id,
                "kind": kind,
                "action": action,
                "source": source,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if details is not UNSET:
            field_dict["details"] = details
        if user is not UNSET:
            field_dict["user"] = user
        if incident is not UNSET:
            field_dict["incident"] = incident
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if escalation_level is not UNSET:
            field_dict["escalation_level"] = escalation_level
        if escalation_target_type is not UNSET:
            field_dict["escalation_target_type"] = escalation_target_type
        if escalation_target is not UNSET:
            field_dict["escalation_target"] = escalation_target
        if slack_channel is not UNSET:
            field_dict["slack_channel"] = slack_channel
        if incident_ids is not UNSET:
            field_dict["incident_ids"] = incident_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alert_event_escalation_target_type_0 import AlertEventEscalationTargetType0
        from ..models.alert_event_incident_type_0 import AlertEventIncidentType0
        from ..models.alert_event_schedule_type_0 import AlertEventScheduleType0
        from ..models.alert_event_user import AlertEventUser
        from ..models.slack_channel import SlackChannel

        d = dict(src_dict)
        alert_id = d.pop("alert_id")

        kind = check_alert_event_kind(d.pop("kind"))

        action = check_alert_event_action(d.pop("action"))

        source = d.pop("source")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_user_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_details(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        details = _parse_details(d.pop("details", UNSET))

        _user = d.pop("user", UNSET)
        user: Union[Unset, AlertEventUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = AlertEventUser.from_dict(_user)

        def _parse_incident(data: object) -> Union["AlertEventIncidentType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                incident_type_0 = AlertEventIncidentType0.from_dict(data)

                return incident_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AlertEventIncidentType0", None, Unset], data)

        incident = _parse_incident(d.pop("incident", UNSET))

        def _parse_schedule(data: object) -> Union["AlertEventScheduleType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schedule_type_0 = AlertEventScheduleType0.from_dict(data)

                return schedule_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AlertEventScheduleType0", None, Unset], data)

        schedule = _parse_schedule(d.pop("schedule", UNSET))

        def _parse_escalation_level(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        escalation_level = _parse_escalation_level(d.pop("escalation_level", UNSET))

        def _parse_escalation_target_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        escalation_target_type = _parse_escalation_target_type(d.pop("escalation_target_type", UNSET))

        def _parse_escalation_target(data: object) -> Union["AlertEventEscalationTargetType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                escalation_target_type_0 = AlertEventEscalationTargetType0.from_dict(data)

                return escalation_target_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AlertEventEscalationTargetType0", None, Unset], data)

        escalation_target = _parse_escalation_target(d.pop("escalation_target", UNSET))

        _slack_channel = d.pop("slack_channel", UNSET)
        slack_channel: Union[Unset, SlackChannel]
        if isinstance(_slack_channel, Unset):
            slack_channel = UNSET
        else:
            slack_channel = SlackChannel.from_dict(_slack_channel)

        def _parse_incident_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                incident_ids_type_0 = cast(list[str], data)

                return incident_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        incident_ids = _parse_incident_ids(d.pop("incident_ids", UNSET))

        alert_event = cls(
            alert_id=alert_id,
            kind=kind,
            action=action,
            source=source,
            created_at=created_at,
            updated_at=updated_at,
            user_id=user_id,
            details=details,
            user=user,
            incident=incident,
            schedule=schedule,
            escalation_level=escalation_level,
            escalation_target_type=escalation_target_type,
            escalation_target=escalation_target,
            slack_channel=slack_channel,
            incident_ids=incident_ids,
        )

        alert_event.additional_properties = d
        return alert_event

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
