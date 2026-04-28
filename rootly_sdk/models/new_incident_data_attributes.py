from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        title (None | str | Unset): The title of the incident. We will autogenerate one if null
        kind (NewIncidentDataAttributesKind | Unset): The kind of the incident Default: 'normal'.
        parent_incident_id (None | str | Unset): ID of parent incident
        duplicate_incident_id (None | str | Unset): ID of duplicated incident
        private (bool | None | Unset): Create an incident as private. Once an incident is made as private it cannot be
            undone Default: False.
        summary (None | str | Unset): The summary of the incident
        user_id (None | str | Unset): User ID of the creator of the incident. Default to the user attached to the Api
            Key
        severity_id (None | str | Unset): The Severity ID to attach to the incident
        public_title (None | str | Unset): The public title of the incident
        alert_ids (list[str] | None | Unset): The Alert IDs to attach to the incident
        environment_ids (list[str] | None | Unset): The Environment IDs to attach to the incident
        incident_type_ids (list[str] | None | Unset): The Incident Type IDs to attach to the incident
        service_ids (list[str] | None | Unset): The Service IDs to attach to the incident
        functionality_ids (list[str] | None | Unset): The Functionality IDs to attach to the incident
        group_ids (list[str] | None | Unset): The Team IDs to attach to the incident
        cause_ids (list[str] | None | Unset): The Cause IDs to attach to the incident
        muted_service_ids (list[str] | None | Unset): The Service IDs to mute alerts for during maintenance. Alerts for
            these services will still be triggered and attached to the incident, but won't page responders.
        labels (NewIncidentDataAttributesLabelsType0 | None | Unset): Labels to attach to the incidents. eg:
            {"platform":"osx", "version": "1.29"}
        slack_channel_name (None | str | Unset): Slack channel name
        slack_channel_id (None | str | Unset): Slack channel id
        slack_channel_url (None | str | Unset): Slack channel url
        slack_channel_archived (bool | None | Unset): Whether the Slack channel is archived
        google_drive_parent_id (None | str | Unset): Google Drive parent folder ID
        google_drive_url (None | str | Unset): Google Drive URL
        jira_issue_key (None | str | Unset): Jira issue key
        jira_issue_id (None | str | Unset): Jira issue ID
        jira_issue_url (None | str | Unset): Jira issue URL
        notify_emails (list[str] | None | Unset): Emails you want to notify
        status (NewIncidentDataAttributesStatus | Unset): The status of the incident
        url (str | Unset): The url to the incident
        scheduled_for (None | str | Unset): Date of when the maintenance begins
        scheduled_until (None | str | Unset): Date of when the maintenance ends
        in_triage_at (None | str | Unset): Date of triage
        started_at (None | str | Unset): Date of start
        detected_at (None | str | Unset): Date of detection
        acknowledged_at (None | str | Unset): Date of acknowledgment
        mitigated_at (None | str | Unset): Date of mitigation
        resolved_at (None | str | Unset): Date of resolution
        closed_at (None | str | Unset): Date of closure
        cancelled_at (None | str | Unset): Date of cancellation
    """

    title: None | str | Unset = UNSET
    kind: NewIncidentDataAttributesKind | Unset = "normal"
    parent_incident_id: None | str | Unset = UNSET
    duplicate_incident_id: None | str | Unset = UNSET
    private: bool | None | Unset = False
    summary: None | str | Unset = UNSET
    user_id: None | str | Unset = UNSET
    severity_id: None | str | Unset = UNSET
    public_title: None | str | Unset = UNSET
    alert_ids: list[str] | None | Unset = UNSET
    environment_ids: list[str] | None | Unset = UNSET
    incident_type_ids: list[str] | None | Unset = UNSET
    service_ids: list[str] | None | Unset = UNSET
    functionality_ids: list[str] | None | Unset = UNSET
    group_ids: list[str] | None | Unset = UNSET
    cause_ids: list[str] | None | Unset = UNSET
    muted_service_ids: list[str] | None | Unset = UNSET
    labels: NewIncidentDataAttributesLabelsType0 | None | Unset = UNSET
    slack_channel_name: None | str | Unset = UNSET
    slack_channel_id: None | str | Unset = UNSET
    slack_channel_url: None | str | Unset = UNSET
    slack_channel_archived: bool | None | Unset = UNSET
    google_drive_parent_id: None | str | Unset = UNSET
    google_drive_url: None | str | Unset = UNSET
    jira_issue_key: None | str | Unset = UNSET
    jira_issue_id: None | str | Unset = UNSET
    jira_issue_url: None | str | Unset = UNSET
    notify_emails: list[str] | None | Unset = UNSET
    status: NewIncidentDataAttributesStatus | Unset = UNSET
    url: str | Unset = UNSET
    scheduled_for: None | str | Unset = UNSET
    scheduled_until: None | str | Unset = UNSET
    in_triage_at: None | str | Unset = UNSET
    started_at: None | str | Unset = UNSET
    detected_at: None | str | Unset = UNSET
    acknowledged_at: None | str | Unset = UNSET
    mitigated_at: None | str | Unset = UNSET
    resolved_at: None | str | Unset = UNSET
    closed_at: None | str | Unset = UNSET
    cancelled_at: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_incident_data_attributes_labels_type_0 import NewIncidentDataAttributesLabelsType0

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        parent_incident_id: None | str | Unset
        if isinstance(self.parent_incident_id, Unset):
            parent_incident_id = UNSET
        else:
            parent_incident_id = self.parent_incident_id

        duplicate_incident_id: None | str | Unset
        if isinstance(self.duplicate_incident_id, Unset):
            duplicate_incident_id = UNSET
        else:
            duplicate_incident_id = self.duplicate_incident_id

        private: bool | None | Unset
        if isinstance(self.private, Unset):
            private = UNSET
        else:
            private = self.private

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        severity_id: None | str | Unset
        if isinstance(self.severity_id, Unset):
            severity_id = UNSET
        else:
            severity_id = self.severity_id

        public_title: None | str | Unset
        if isinstance(self.public_title, Unset):
            public_title = UNSET
        else:
            public_title = self.public_title

        alert_ids: list[str] | None | Unset
        if isinstance(self.alert_ids, Unset):
            alert_ids = UNSET
        elif isinstance(self.alert_ids, list):
            alert_ids = self.alert_ids

        else:
            alert_ids = self.alert_ids

        environment_ids: list[str] | None | Unset
        if isinstance(self.environment_ids, Unset):
            environment_ids = UNSET
        elif isinstance(self.environment_ids, list):
            environment_ids = self.environment_ids

        else:
            environment_ids = self.environment_ids

        incident_type_ids: list[str] | None | Unset
        if isinstance(self.incident_type_ids, Unset):
            incident_type_ids = UNSET
        elif isinstance(self.incident_type_ids, list):
            incident_type_ids = self.incident_type_ids

        else:
            incident_type_ids = self.incident_type_ids

        service_ids: list[str] | None | Unset
        if isinstance(self.service_ids, Unset):
            service_ids = UNSET
        elif isinstance(self.service_ids, list):
            service_ids = self.service_ids

        else:
            service_ids = self.service_ids

        functionality_ids: list[str] | None | Unset
        if isinstance(self.functionality_ids, Unset):
            functionality_ids = UNSET
        elif isinstance(self.functionality_ids, list):
            functionality_ids = self.functionality_ids

        else:
            functionality_ids = self.functionality_ids

        group_ids: list[str] | None | Unset
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        cause_ids: list[str] | None | Unset
        if isinstance(self.cause_ids, Unset):
            cause_ids = UNSET
        elif isinstance(self.cause_ids, list):
            cause_ids = self.cause_ids

        else:
            cause_ids = self.cause_ids

        muted_service_ids: list[str] | None | Unset
        if isinstance(self.muted_service_ids, Unset):
            muted_service_ids = UNSET
        elif isinstance(self.muted_service_ids, list):
            muted_service_ids = self.muted_service_ids

        else:
            muted_service_ids = self.muted_service_ids

        labels: dict[str, Any] | None | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, NewIncidentDataAttributesLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        slack_channel_name: None | str | Unset
        if isinstance(self.slack_channel_name, Unset):
            slack_channel_name = UNSET
        else:
            slack_channel_name = self.slack_channel_name

        slack_channel_id: None | str | Unset
        if isinstance(self.slack_channel_id, Unset):
            slack_channel_id = UNSET
        else:
            slack_channel_id = self.slack_channel_id

        slack_channel_url: None | str | Unset
        if isinstance(self.slack_channel_url, Unset):
            slack_channel_url = UNSET
        else:
            slack_channel_url = self.slack_channel_url

        slack_channel_archived: bool | None | Unset
        if isinstance(self.slack_channel_archived, Unset):
            slack_channel_archived = UNSET
        else:
            slack_channel_archived = self.slack_channel_archived

        google_drive_parent_id: None | str | Unset
        if isinstance(self.google_drive_parent_id, Unset):
            google_drive_parent_id = UNSET
        else:
            google_drive_parent_id = self.google_drive_parent_id

        google_drive_url: None | str | Unset
        if isinstance(self.google_drive_url, Unset):
            google_drive_url = UNSET
        else:
            google_drive_url = self.google_drive_url

        jira_issue_key: None | str | Unset
        if isinstance(self.jira_issue_key, Unset):
            jira_issue_key = UNSET
        else:
            jira_issue_key = self.jira_issue_key

        jira_issue_id: None | str | Unset
        if isinstance(self.jira_issue_id, Unset):
            jira_issue_id = UNSET
        else:
            jira_issue_id = self.jira_issue_id

        jira_issue_url: None | str | Unset
        if isinstance(self.jira_issue_url, Unset):
            jira_issue_url = UNSET
        else:
            jira_issue_url = self.jira_issue_url

        notify_emails: list[str] | None | Unset
        if isinstance(self.notify_emails, Unset):
            notify_emails = UNSET
        elif isinstance(self.notify_emails, list):
            notify_emails = self.notify_emails

        else:
            notify_emails = self.notify_emails

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        url = self.url

        scheduled_for: None | str | Unset
        if isinstance(self.scheduled_for, Unset):
            scheduled_for = UNSET
        else:
            scheduled_for = self.scheduled_for

        scheduled_until: None | str | Unset
        if isinstance(self.scheduled_until, Unset):
            scheduled_until = UNSET
        else:
            scheduled_until = self.scheduled_until

        in_triage_at: None | str | Unset
        if isinstance(self.in_triage_at, Unset):
            in_triage_at = UNSET
        else:
            in_triage_at = self.in_triage_at

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        detected_at: None | str | Unset
        if isinstance(self.detected_at, Unset):
            detected_at = UNSET
        else:
            detected_at = self.detected_at

        acknowledged_at: None | str | Unset
        if isinstance(self.acknowledged_at, Unset):
            acknowledged_at = UNSET
        else:
            acknowledged_at = self.acknowledged_at

        mitigated_at: None | str | Unset
        if isinstance(self.mitigated_at, Unset):
            mitigated_at = UNSET
        else:
            mitigated_at = self.mitigated_at

        resolved_at: None | str | Unset
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        else:
            resolved_at = self.resolved_at

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        else:
            closed_at = self.closed_at

        cancelled_at: None | str | Unset
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

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: NewIncidentDataAttributesKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_new_incident_data_attributes_kind(_kind)

        def _parse_parent_incident_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_incident_id = _parse_parent_incident_id(d.pop("parent_incident_id", UNSET))

        def _parse_duplicate_incident_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        duplicate_incident_id = _parse_duplicate_incident_id(d.pop("duplicate_incident_id", UNSET))

        def _parse_private(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        private = _parse_private(d.pop("private", UNSET))

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_severity_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        severity_id = _parse_severity_id(d.pop("severity_id", UNSET))

        def _parse_public_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_title = _parse_public_title(d.pop("public_title", UNSET))

        def _parse_alert_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alert_ids_type_0 = cast(list[str], data)

                return alert_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        alert_ids = _parse_alert_ids(d.pop("alert_ids", UNSET))

        def _parse_environment_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                environment_ids_type_0 = cast(list[str], data)

                return environment_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        environment_ids = _parse_environment_ids(d.pop("environment_ids", UNSET))

        def _parse_incident_type_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                incident_type_ids_type_0 = cast(list[str], data)

                return incident_type_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        incident_type_ids = _parse_incident_type_ids(d.pop("incident_type_ids", UNSET))

        def _parse_service_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                service_ids_type_0 = cast(list[str], data)

                return service_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        service_ids = _parse_service_ids(d.pop("service_ids", UNSET))

        def _parse_functionality_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                functionality_ids_type_0 = cast(list[str], data)

                return functionality_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        functionality_ids = _parse_functionality_ids(d.pop("functionality_ids", UNSET))

        def _parse_group_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = cast(list[str], data)

                return group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        def _parse_cause_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cause_ids_type_0 = cast(list[str], data)

                return cause_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        cause_ids = _parse_cause_ids(d.pop("cause_ids", UNSET))

        def _parse_muted_service_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                muted_service_ids_type_0 = cast(list[str], data)

                return muted_service_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        muted_service_ids = _parse_muted_service_ids(d.pop("muted_service_ids", UNSET))

        def _parse_labels(data: object) -> NewIncidentDataAttributesLabelsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = NewIncidentDataAttributesLabelsType0.from_dict(data)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewIncidentDataAttributesLabelsType0 | None | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_slack_channel_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slack_channel_name = _parse_slack_channel_name(d.pop("slack_channel_name", UNSET))

        def _parse_slack_channel_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slack_channel_id = _parse_slack_channel_id(d.pop("slack_channel_id", UNSET))

        def _parse_slack_channel_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slack_channel_url = _parse_slack_channel_url(d.pop("slack_channel_url", UNSET))

        def _parse_slack_channel_archived(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        slack_channel_archived = _parse_slack_channel_archived(d.pop("slack_channel_archived", UNSET))

        def _parse_google_drive_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        google_drive_parent_id = _parse_google_drive_parent_id(d.pop("google_drive_parent_id", UNSET))

        def _parse_google_drive_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        google_drive_url = _parse_google_drive_url(d.pop("google_drive_url", UNSET))

        def _parse_jira_issue_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jira_issue_key = _parse_jira_issue_key(d.pop("jira_issue_key", UNSET))

        def _parse_jira_issue_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jira_issue_id = _parse_jira_issue_id(d.pop("jira_issue_id", UNSET))

        def _parse_jira_issue_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jira_issue_url = _parse_jira_issue_url(d.pop("jira_issue_url", UNSET))

        def _parse_notify_emails(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notify_emails_type_0 = cast(list[str], data)

                return notify_emails_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        notify_emails = _parse_notify_emails(d.pop("notify_emails", UNSET))

        _status = d.pop("status", UNSET)
        status: NewIncidentDataAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_new_incident_data_attributes_status(_status)

        url = d.pop("url", UNSET)

        def _parse_scheduled_for(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheduled_for = _parse_scheduled_for(d.pop("scheduled_for", UNSET))

        def _parse_scheduled_until(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheduled_until = _parse_scheduled_until(d.pop("scheduled_until", UNSET))

        def _parse_in_triage_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        in_triage_at = _parse_in_triage_at(d.pop("in_triage_at", UNSET))

        def _parse_started_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_detected_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detected_at = _parse_detected_at(d.pop("detected_at", UNSET))

        def _parse_acknowledged_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acknowledged_at = _parse_acknowledged_at(d.pop("acknowledged_at", UNSET))

        def _parse_mitigated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mitigated_at = _parse_mitigated_at(d.pop("mitigated_at", UNSET))

        def _parse_resolved_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at", UNSET))

        def _parse_closed_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        closed_at = _parse_closed_at(d.pop("closed_at", UNSET))

        def _parse_cancelled_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

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
