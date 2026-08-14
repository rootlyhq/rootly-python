from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.new_incident_data_attributes_kind import (
    NewIncidentDataAttributesKind,
    check_new_incident_data_attributes_kind,
)
from ..models.new_incident_data_attributes_status import (
    NewIncidentDataAttributesStatus,
    check_new_incident_data_attributes_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_incident_data_attributes_labels_type_0 import NewIncidentDataAttributesLabelsType0


T = TypeVar("T", bound="NewIncidentDataAttributes")


@_attrs_define
class NewIncidentDataAttributes:
    """
    Attributes:
        title (Union[None, Unset, str]): The title of the incident. We will autogenerate one if null
        kind (Union[Unset, NewIncidentDataAttributesKind]): The kind of the incident Default: 'normal'.
        parent_incident_id (Union[None, Unset, str]): ID of parent incident
        duplicate_incident_id (Union[None, Unset, str]): ID of duplicated incident
        private (Union[None, Unset, bool]): Create an incident as private. Once an incident is made as private it cannot
            be undone Default: False.
        summary (Union[None, Unset, str]): The summary of the incident
        user_id (Union[None, Unset, str]): User ID of the creator of the incident. Default to the user attached to the
            Api Key
        severity_id (Union[None, Unset, str]): The Severity ID to attach to the incident
        public_title (Union[None, Unset, str]): The public title of the incident
        alert_ids (Union[None, Unset, list[str]]): The Alert IDs to attach to the incident
        environment_ids (Union[None, Unset, list[str]]): The Environment IDs to attach to the incident
        incident_type_ids (Union[None, Unset, list[str]]): The Incident Type IDs to attach to the incident
        service_ids (Union[None, Unset, list[str]]): The Service IDs to attach to the incident
        functionality_ids (Union[None, Unset, list[str]]): The Functionality IDs to attach to the incident
        group_ids (Union[None, Unset, list[str]]): The Team IDs to attach to the incident
        cause_ids (Union[None, Unset, list[str]]): The Cause IDs to attach to the incident
        muted_service_ids (Union[None, Unset, list[str]]): The Service IDs to mute alerts for during maintenance. Alerts
            for these services will still be triggered and attached to the incident, but won't page responders.
        labels (Union['NewIncidentDataAttributesLabelsType0', None, Unset]): Labels to attach to the incidents. eg:
            {"platform":"osx", "version": "1.29"}
        slack_channel_name (Union[None, Unset, str]): Slack channel name
        slack_channel_id (Union[None, Unset, str]): Slack channel id
        slack_channel_url (Union[None, Unset, str]): Slack channel url
        slack_channel_archived (Union[None, Unset, bool]): Whether the Slack channel is archived
        google_drive_parent_id (Union[None, Unset, str]): Google Drive parent folder ID
        google_drive_url (Union[None, Unset, str]): Google Drive URL
        jira_issue_key (Union[None, Unset, str]): Jira issue key
        jira_issue_id (Union[None, Unset, str]): Jira issue ID
        jira_issue_url (Union[None, Unset, str]): Jira issue URL
        notify_emails (Union[None, Unset, list[str]]): Emails you want to notify
        status (Union[Unset, NewIncidentDataAttributesStatus]): The status of the incident
        url (Union[Unset, str]): The url to the incident
        scheduled_for (Union[None, Unset, str]): Date of when the maintenance begins
        scheduled_until (Union[None, Unset, str]): Date of when the maintenance ends
        in_triage_at (Union[None, Unset, str]): Date of triage
        started_at (Union[None, Unset, str]): Date of start
        detected_at (Union[None, Unset, str]): Date of detection
        acknowledged_at (Union[None, Unset, str]): Date of acknowledgment
        mitigated_at (Union[None, Unset, str]): Date of mitigation
        resolved_at (Union[None, Unset, str]): Date of resolution
        closed_at (Union[None, Unset, str]): Date of closure
        cancelled_at (Union[None, Unset, str]): Date of cancellation
    """

    title: None | Unset | str = UNSET
    kind: Unset | NewIncidentDataAttributesKind = "normal"
    parent_incident_id: None | Unset | str = UNSET
    duplicate_incident_id: None | Unset | str = UNSET
    private: None | Unset | bool = False
    summary: None | Unset | str = UNSET
    user_id: None | Unset | str = UNSET
    severity_id: None | Unset | str = UNSET
    public_title: None | Unset | str = UNSET
    alert_ids: None | Unset | list[str] = UNSET
    environment_ids: None | Unset | list[str] = UNSET
    incident_type_ids: None | Unset | list[str] = UNSET
    service_ids: None | Unset | list[str] = UNSET
    functionality_ids: None | Unset | list[str] = UNSET
    group_ids: None | Unset | list[str] = UNSET
    cause_ids: None | Unset | list[str] = UNSET
    muted_service_ids: None | Unset | list[str] = UNSET
    labels: Union["NewIncidentDataAttributesLabelsType0", None, Unset] = UNSET
    slack_channel_name: None | Unset | str = UNSET
    slack_channel_id: None | Unset | str = UNSET
    slack_channel_url: None | Unset | str = UNSET
    slack_channel_archived: None | Unset | bool = UNSET
    google_drive_parent_id: None | Unset | str = UNSET
    google_drive_url: None | Unset | str = UNSET
    jira_issue_key: None | Unset | str = UNSET
    jira_issue_id: None | Unset | str = UNSET
    jira_issue_url: None | Unset | str = UNSET
    notify_emails: None | Unset | list[str] = UNSET
    status: Unset | NewIncidentDataAttributesStatus = UNSET
    url: Unset | str = UNSET
    scheduled_for: None | Unset | str = UNSET
    scheduled_until: None | Unset | str = UNSET
    in_triage_at: None | Unset | str = UNSET
    started_at: None | Unset | str = UNSET
    detected_at: None | Unset | str = UNSET
    acknowledged_at: None | Unset | str = UNSET
    mitigated_at: None | Unset | str = UNSET
    resolved_at: None | Unset | str = UNSET
    closed_at: None | Unset | str = UNSET
    cancelled_at: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_incident_data_attributes_labels_type_0 import NewIncidentDataAttributesLabelsType0

        title: None | Unset | str
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        kind: Unset | str = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        parent_incident_id: None | Unset | str
        if isinstance(self.parent_incident_id, Unset):
            parent_incident_id = UNSET
        else:
            parent_incident_id = self.parent_incident_id

        duplicate_incident_id: None | Unset | str
        if isinstance(self.duplicate_incident_id, Unset):
            duplicate_incident_id = UNSET
        else:
            duplicate_incident_id = self.duplicate_incident_id

        private: None | Unset | bool
        if isinstance(self.private, Unset):
            private = UNSET
        else:
            private = self.private

        summary: None | Unset | str
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        user_id: None | Unset | str
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        severity_id: None | Unset | str
        if isinstance(self.severity_id, Unset):
            severity_id = UNSET
        else:
            severity_id = self.severity_id

        public_title: None | Unset | str
        if isinstance(self.public_title, Unset):
            public_title = UNSET
        else:
            public_title = self.public_title

        alert_ids: None | Unset | list[str]
        if isinstance(self.alert_ids, Unset):
            alert_ids = UNSET
        elif isinstance(self.alert_ids, list):
            alert_ids = self.alert_ids

        else:
            alert_ids = self.alert_ids

        environment_ids: None | Unset | list[str]
        if isinstance(self.environment_ids, Unset):
            environment_ids = UNSET
        elif isinstance(self.environment_ids, list):
            environment_ids = self.environment_ids

        else:
            environment_ids = self.environment_ids

        incident_type_ids: None | Unset | list[str]
        if isinstance(self.incident_type_ids, Unset):
            incident_type_ids = UNSET
        elif isinstance(self.incident_type_ids, list):
            incident_type_ids = self.incident_type_ids

        else:
            incident_type_ids = self.incident_type_ids

        service_ids: None | Unset | list[str]
        if isinstance(self.service_ids, Unset):
            service_ids = UNSET
        elif isinstance(self.service_ids, list):
            service_ids = self.service_ids

        else:
            service_ids = self.service_ids

        functionality_ids: None | Unset | list[str]
        if isinstance(self.functionality_ids, Unset):
            functionality_ids = UNSET
        elif isinstance(self.functionality_ids, list):
            functionality_ids = self.functionality_ids

        else:
            functionality_ids = self.functionality_ids

        group_ids: None | Unset | list[str]
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        cause_ids: None | Unset | list[str]
        if isinstance(self.cause_ids, Unset):
            cause_ids = UNSET
        elif isinstance(self.cause_ids, list):
            cause_ids = self.cause_ids

        else:
            cause_ids = self.cause_ids

        muted_service_ids: None | Unset | list[str]
        if isinstance(self.muted_service_ids, Unset):
            muted_service_ids = UNSET
        elif isinstance(self.muted_service_ids, list):
            muted_service_ids = self.muted_service_ids

        else:
            muted_service_ids = self.muted_service_ids

        labels: None | Unset | dict[str, Any]
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, NewIncidentDataAttributesLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        slack_channel_name: None | Unset | str
        if isinstance(self.slack_channel_name, Unset):
            slack_channel_name = UNSET
        else:
            slack_channel_name = self.slack_channel_name

        slack_channel_id: None | Unset | str
        if isinstance(self.slack_channel_id, Unset):
            slack_channel_id = UNSET
        else:
            slack_channel_id = self.slack_channel_id

        slack_channel_url: None | Unset | str
        if isinstance(self.slack_channel_url, Unset):
            slack_channel_url = UNSET
        else:
            slack_channel_url = self.slack_channel_url

        slack_channel_archived: None | Unset | bool
        if isinstance(self.slack_channel_archived, Unset):
            slack_channel_archived = UNSET
        else:
            slack_channel_archived = self.slack_channel_archived

        google_drive_parent_id: None | Unset | str
        if isinstance(self.google_drive_parent_id, Unset):
            google_drive_parent_id = UNSET
        else:
            google_drive_parent_id = self.google_drive_parent_id

        google_drive_url: None | Unset | str
        if isinstance(self.google_drive_url, Unset):
            google_drive_url = UNSET
        else:
            google_drive_url = self.google_drive_url

        jira_issue_key: None | Unset | str
        if isinstance(self.jira_issue_key, Unset):
            jira_issue_key = UNSET
        else:
            jira_issue_key = self.jira_issue_key

        jira_issue_id: None | Unset | str
        if isinstance(self.jira_issue_id, Unset):
            jira_issue_id = UNSET
        else:
            jira_issue_id = self.jira_issue_id

        jira_issue_url: None | Unset | str
        if isinstance(self.jira_issue_url, Unset):
            jira_issue_url = UNSET
        else:
            jira_issue_url = self.jira_issue_url

        notify_emails: None | Unset | list[str]
        if isinstance(self.notify_emails, Unset):
            notify_emails = UNSET
        elif isinstance(self.notify_emails, list):
            notify_emails = self.notify_emails

        else:
            notify_emails = self.notify_emails

        status: Unset | str = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        url = self.url

        scheduled_for: None | Unset | str
        if isinstance(self.scheduled_for, Unset):
            scheduled_for = UNSET
        else:
            scheduled_for = self.scheduled_for

        scheduled_until: None | Unset | str
        if isinstance(self.scheduled_until, Unset):
            scheduled_until = UNSET
        else:
            scheduled_until = self.scheduled_until

        in_triage_at: None | Unset | str
        if isinstance(self.in_triage_at, Unset):
            in_triage_at = UNSET
        else:
            in_triage_at = self.in_triage_at

        started_at: None | Unset | str
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        detected_at: None | Unset | str
        if isinstance(self.detected_at, Unset):
            detected_at = UNSET
        else:
            detected_at = self.detected_at

        acknowledged_at: None | Unset | str
        if isinstance(self.acknowledged_at, Unset):
            acknowledged_at = UNSET
        else:
            acknowledged_at = self.acknowledged_at

        mitigated_at: None | Unset | str
        if isinstance(self.mitigated_at, Unset):
            mitigated_at = UNSET
        else:
            mitigated_at = self.mitigated_at

        resolved_at: None | Unset | str
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        else:
            resolved_at = self.resolved_at

        closed_at: None | Unset | str
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        else:
            closed_at = self.closed_at

        cancelled_at: None | Unset | str
        if isinstance(self.cancelled_at, Unset):
            cancelled_at = UNSET
        else:
            cancelled_at = self.cancelled_at

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if kind is not UNSET:
            field_dict["kind"] = kind
        if parent_incident_id is not UNSET:
            field_dict["parent_incident_id"] = parent_incident_id
        if duplicate_incident_id is not UNSET:
            field_dict["duplicate_incident_id"] = duplicate_incident_id
        if private is not UNSET:
            field_dict["private"] = private
        if summary is not UNSET:
            field_dict["summary"] = summary
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if severity_id is not UNSET:
            field_dict["severity_id"] = severity_id
        if public_title is not UNSET:
            field_dict["public_title"] = public_title
        if alert_ids is not UNSET:
            field_dict["alert_ids"] = alert_ids
        if environment_ids is not UNSET:
            field_dict["environment_ids"] = environment_ids
        if incident_type_ids is not UNSET:
            field_dict["incident_type_ids"] = incident_type_ids
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if functionality_ids is not UNSET:
            field_dict["functionality_ids"] = functionality_ids
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if cause_ids is not UNSET:
            field_dict["cause_ids"] = cause_ids
        if muted_service_ids is not UNSET:
            field_dict["muted_service_ids"] = muted_service_ids
        if labels is not UNSET:
            field_dict["labels"] = labels
        if slack_channel_name is not UNSET:
            field_dict["slack_channel_name"] = slack_channel_name
        if slack_channel_id is not UNSET:
            field_dict["slack_channel_id"] = slack_channel_id
        if slack_channel_url is not UNSET:
            field_dict["slack_channel_url"] = slack_channel_url
        if slack_channel_archived is not UNSET:
            field_dict["slack_channel_archived"] = slack_channel_archived
        if google_drive_parent_id is not UNSET:
            field_dict["google_drive_parent_id"] = google_drive_parent_id
        if google_drive_url is not UNSET:
            field_dict["google_drive_url"] = google_drive_url
        if jira_issue_key is not UNSET:
            field_dict["jira_issue_key"] = jira_issue_key
        if jira_issue_id is not UNSET:
            field_dict["jira_issue_id"] = jira_issue_id
        if jira_issue_url is not UNSET:
            field_dict["jira_issue_url"] = jira_issue_url
        if notify_emails is not UNSET:
            field_dict["notify_emails"] = notify_emails
        if status is not UNSET:
            field_dict["status"] = status
        if url is not UNSET:
            field_dict["url"] = url
        if scheduled_for is not UNSET:
            field_dict["scheduled_for"] = scheduled_for
        if scheduled_until is not UNSET:
            field_dict["scheduled_until"] = scheduled_until
        if in_triage_at is not UNSET:
            field_dict["in_triage_at"] = in_triage_at
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if detected_at is not UNSET:
            field_dict["detected_at"] = detected_at
        if acknowledged_at is not UNSET:
            field_dict["acknowledged_at"] = acknowledged_at
        if mitigated_at is not UNSET:
            field_dict["mitigated_at"] = mitigated_at
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_incident_data_attributes_labels_type_0 import NewIncidentDataAttributesLabelsType0

        d = dict(src_dict)

        def _parse_title(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        title = _parse_title(d.pop("title", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: Unset | NewIncidentDataAttributesKind
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_new_incident_data_attributes_kind(_kind)

        def _parse_parent_incident_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        parent_incident_id = _parse_parent_incident_id(d.pop("parent_incident_id", UNSET))

        def _parse_duplicate_incident_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        duplicate_incident_id = _parse_duplicate_incident_id(d.pop("duplicate_incident_id", UNSET))

        def _parse_private(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        private = _parse_private(d.pop("private", UNSET))

        def _parse_summary(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_user_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_severity_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        severity_id = _parse_severity_id(d.pop("severity_id", UNSET))

        def _parse_public_title(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        public_title = _parse_public_title(d.pop("public_title", UNSET))

        def _parse_alert_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alert_ids_type_0 = cast(list[str], data)

                return alert_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        alert_ids = _parse_alert_ids(d.pop("alert_ids", UNSET))

        def _parse_environment_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                environment_ids_type_0 = cast(list[str], data)

                return environment_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        environment_ids = _parse_environment_ids(d.pop("environment_ids", UNSET))

        def _parse_incident_type_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                incident_type_ids_type_0 = cast(list[str], data)

                return incident_type_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        incident_type_ids = _parse_incident_type_ids(d.pop("incident_type_ids", UNSET))

        def _parse_service_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                service_ids_type_0 = cast(list[str], data)

                return service_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        service_ids = _parse_service_ids(d.pop("service_ids", UNSET))

        def _parse_functionality_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                functionality_ids_type_0 = cast(list[str], data)

                return functionality_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        functionality_ids = _parse_functionality_ids(d.pop("functionality_ids", UNSET))

        def _parse_group_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = cast(list[str], data)

                return group_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        def _parse_cause_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cause_ids_type_0 = cast(list[str], data)

                return cause_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        cause_ids = _parse_cause_ids(d.pop("cause_ids", UNSET))

        def _parse_muted_service_ids(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                muted_service_ids_type_0 = cast(list[str], data)

                return muted_service_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        muted_service_ids = _parse_muted_service_ids(d.pop("muted_service_ids", UNSET))

        def _parse_labels(data: object) -> Union["NewIncidentDataAttributesLabelsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = NewIncidentDataAttributesLabelsType0.from_dict(data)

                return labels_type_0
            except:  # noqa: E722
                pass
            return cast(Union["NewIncidentDataAttributesLabelsType0", None, Unset], data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_slack_channel_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slack_channel_name = _parse_slack_channel_name(d.pop("slack_channel_name", UNSET))

        def _parse_slack_channel_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slack_channel_id = _parse_slack_channel_id(d.pop("slack_channel_id", UNSET))

        def _parse_slack_channel_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slack_channel_url = _parse_slack_channel_url(d.pop("slack_channel_url", UNSET))

        def _parse_slack_channel_archived(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        slack_channel_archived = _parse_slack_channel_archived(d.pop("slack_channel_archived", UNSET))

        def _parse_google_drive_parent_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        google_drive_parent_id = _parse_google_drive_parent_id(d.pop("google_drive_parent_id", UNSET))

        def _parse_google_drive_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        google_drive_url = _parse_google_drive_url(d.pop("google_drive_url", UNSET))

        def _parse_jira_issue_key(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        jira_issue_key = _parse_jira_issue_key(d.pop("jira_issue_key", UNSET))

        def _parse_jira_issue_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        jira_issue_id = _parse_jira_issue_id(d.pop("jira_issue_id", UNSET))

        def _parse_jira_issue_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        jira_issue_url = _parse_jira_issue_url(d.pop("jira_issue_url", UNSET))

        def _parse_notify_emails(data: object) -> None | Unset | list[str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notify_emails_type_0 = cast(list[str], data)

                return notify_emails_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list[str], data)

        notify_emails = _parse_notify_emails(d.pop("notify_emails", UNSET))

        _status = d.pop("status", UNSET)
        status: Unset | NewIncidentDataAttributesStatus
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_new_incident_data_attributes_status(_status)

        url = d.pop("url", UNSET)

        def _parse_scheduled_for(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        scheduled_for = _parse_scheduled_for(d.pop("scheduled_for", UNSET))

        def _parse_scheduled_until(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        scheduled_until = _parse_scheduled_until(d.pop("scheduled_until", UNSET))

        def _parse_in_triage_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        in_triage_at = _parse_in_triage_at(d.pop("in_triage_at", UNSET))

        def _parse_started_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_detected_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        detected_at = _parse_detected_at(d.pop("detected_at", UNSET))

        def _parse_acknowledged_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        acknowledged_at = _parse_acknowledged_at(d.pop("acknowledged_at", UNSET))

        def _parse_mitigated_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        mitigated_at = _parse_mitigated_at(d.pop("mitigated_at", UNSET))

        def _parse_resolved_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at", UNSET))

        def _parse_closed_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        closed_at = _parse_closed_at(d.pop("closed_at", UNSET))

        def _parse_cancelled_at(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        cancelled_at = _parse_cancelled_at(d.pop("cancelled_at", UNSET))

        new_incident_data_attributes = cls(
            title=title,
            kind=kind,
            parent_incident_id=parent_incident_id,
            duplicate_incident_id=duplicate_incident_id,
            private=private,
            summary=summary,
            user_id=user_id,
            severity_id=severity_id,
            public_title=public_title,
            alert_ids=alert_ids,
            environment_ids=environment_ids,
            incident_type_ids=incident_type_ids,
            service_ids=service_ids,
            functionality_ids=functionality_ids,
            group_ids=group_ids,
            cause_ids=cause_ids,
            muted_service_ids=muted_service_ids,
            labels=labels,
            slack_channel_name=slack_channel_name,
            slack_channel_id=slack_channel_id,
            slack_channel_url=slack_channel_url,
            slack_channel_archived=slack_channel_archived,
            google_drive_parent_id=google_drive_parent_id,
            google_drive_url=google_drive_url,
            jira_issue_key=jira_issue_key,
            jira_issue_id=jira_issue_id,
            jira_issue_url=jira_issue_url,
            notify_emails=notify_emails,
            status=status,
            url=url,
            scheduled_for=scheduled_for,
            scheduled_until=scheduled_until,
            in_triage_at=in_triage_at,
            started_at=started_at,
            detected_at=detected_at,
            acknowledged_at=acknowledged_at,
            mitigated_at=mitigated_at,
            resolved_at=resolved_at,
            closed_at=closed_at,
            cancelled_at=cancelled_at,
        )

        return new_incident_data_attributes
