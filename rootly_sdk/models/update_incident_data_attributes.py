from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.update_incident_data_attributes_kind import (
    UpdateIncidentDataAttributesKind,
    check_update_incident_data_attributes_kind,
)
from ..models.update_incident_data_attributes_status import (
    UpdateIncidentDataAttributesStatus,
    check_update_incident_data_attributes_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_incident_data_attributes_labels_type_0 import UpdateIncidentDataAttributesLabelsType0


T = TypeVar("T", bound="UpdateIncidentDataAttributes")


@_attrs_define
class UpdateIncidentDataAttributes:
    """
    Attributes:
        title (Union[None, Unset, str]): The title of the incident
        kind (Union[Unset, UpdateIncidentDataAttributesKind]): The kind of the incident Default: 'normal'.
        parent_incident_id (Union[None, Unset, str]): ID of parent incident
        duplicate_incident_id (Union[None, Unset, str]): ID of duplicated incident
        summary (Union[None, Unset, str]): The summary of the incident
        status (Union[Unset, UpdateIncidentDataAttributesStatus]): The status of the incident
        private (Union[None, Unset, bool]): Convert the incident as private. Once an incident is updated as private it
            cannot be undone Default: False.
        severity_id (Union[None, Unset, str]): The Severity ID to attach to the incident
        public_title (Union[None, Unset, str]): The public title of the incident
        alert_ids (Union[None, Unset, list[str]]): The Alert IDs to attach to the incident
        environment_ids (Union[None, Unset, list[str]]): The Environment IDs to attach to the incident
        incident_type_ids (Union[None, Unset, list[str]]): The Incident Type IDs to attach to the incident
        service_ids (Union[None, Unset, list[str]]): The Service IDs to attach to the incident
        functionality_ids (Union[None, Unset, list[str]]): The Functionality IDs to attach to the incident
        muted_service_ids (Union[None, Unset, list[str]]): The Service IDs to mute alerts for during maintenance. Alerts
            for these services will still be triggered and attached to the incident, but won't page responders.
        group_ids (Union[None, Unset, list[str]]): The Team IDs to attach to the incident
        cause_ids (Union[None, Unset, list[str]]): The Cause IDs to attach to the incident
        labels (Union['UpdateIncidentDataAttributesLabelsType0', None, Unset]): Labels to attach to the incidents. eg:
            {"platform":"osx", "version": "1.29"}
        slack_channel_id (Union[None, Unset, str]): Slack channel id
        slack_channel_name (Union[None, Unset, str]): Slack channel name
        slack_channel_url (Union[None, Unset, str]): Slack channel url
        slack_channel_archived (Union[None, Unset, bool]): Whether the Slack channel is archived
        google_drive_parent_id (Union[None, Unset, str]): Google Drive parent folder ID
        google_drive_url (Union[None, Unset, str]): Google Drive URL
        jira_issue_key (Union[None, Unset, str]): Jira issue key
        jira_issue_id (Union[None, Unset, str]): Jira issue ID
        jira_issue_url (Union[None, Unset, str]): Jira issue URL
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
        mitigation_message (Union[None, Unset, str]): How was the incident mitigated?
        resolution_message (Union[None, Unset, str]): How was the incident resolved?
        cancellation_message (Union[None, Unset, str]): Why was the incident cancelled?
    """

    title: Union[None, Unset, str] = UNSET
    kind: Union[Unset, UpdateIncidentDataAttributesKind] = "normal"
    parent_incident_id: Union[None, Unset, str] = UNSET
    duplicate_incident_id: Union[None, Unset, str] = UNSET
    summary: Union[None, Unset, str] = UNSET
    status: Union[Unset, UpdateIncidentDataAttributesStatus] = UNSET
    private: Union[None, Unset, bool] = False
    severity_id: Union[None, Unset, str] = UNSET
    public_title: Union[None, Unset, str] = UNSET
    alert_ids: Union[None, Unset, list[str]] = UNSET
    environment_ids: Union[None, Unset, list[str]] = UNSET
    incident_type_ids: Union[None, Unset, list[str]] = UNSET
    service_ids: Union[None, Unset, list[str]] = UNSET
    functionality_ids: Union[None, Unset, list[str]] = UNSET
    muted_service_ids: Union[None, Unset, list[str]] = UNSET
    group_ids: Union[None, Unset, list[str]] = UNSET
    cause_ids: Union[None, Unset, list[str]] = UNSET
    labels: Union["UpdateIncidentDataAttributesLabelsType0", None, Unset] = UNSET
    slack_channel_id: Union[None, Unset, str] = UNSET
    slack_channel_name: Union[None, Unset, str] = UNSET
    slack_channel_url: Union[None, Unset, str] = UNSET
    slack_channel_archived: Union[None, Unset, bool] = UNSET
    google_drive_parent_id: Union[None, Unset, str] = UNSET
    google_drive_url: Union[None, Unset, str] = UNSET
    jira_issue_key: Union[None, Unset, str] = UNSET
    jira_issue_id: Union[None, Unset, str] = UNSET
    jira_issue_url: Union[None, Unset, str] = UNSET
    scheduled_for: Union[None, Unset, str] = UNSET
    scheduled_until: Union[None, Unset, str] = UNSET
    in_triage_at: Union[None, Unset, str] = UNSET
    started_at: Union[None, Unset, str] = UNSET
    detected_at: Union[None, Unset, str] = UNSET
    acknowledged_at: Union[None, Unset, str] = UNSET
    mitigated_at: Union[None, Unset, str] = UNSET
    resolved_at: Union[None, Unset, str] = UNSET
    closed_at: Union[None, Unset, str] = UNSET
    cancelled_at: Union[None, Unset, str] = UNSET
    mitigation_message: Union[None, Unset, str] = UNSET
    resolution_message: Union[None, Unset, str] = UNSET
    cancellation_message: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_incident_data_attributes_labels_type_0 import UpdateIncidentDataAttributesLabelsType0

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        parent_incident_id: Union[None, Unset, str]
        if isinstance(self.parent_incident_id, Unset):
            parent_incident_id = UNSET
        else:
            parent_incident_id = self.parent_incident_id

        duplicate_incident_id: Union[None, Unset, str]
        if isinstance(self.duplicate_incident_id, Unset):
            duplicate_incident_id = UNSET
        else:
            duplicate_incident_id = self.duplicate_incident_id

        summary: Union[None, Unset, str]
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        private: Union[None, Unset, bool]
        if isinstance(self.private, Unset):
            private = UNSET
        else:
            private = self.private

        severity_id: Union[None, Unset, str]
        if isinstance(self.severity_id, Unset):
            severity_id = UNSET
        else:
            severity_id = self.severity_id

        public_title: Union[None, Unset, str]
        if isinstance(self.public_title, Unset):
            public_title = UNSET
        else:
            public_title = self.public_title

        alert_ids: Union[None, Unset, list[str]]
        if isinstance(self.alert_ids, Unset):
            alert_ids = UNSET
        elif isinstance(self.alert_ids, list):
            alert_ids = self.alert_ids

        else:
            alert_ids = self.alert_ids

        environment_ids: Union[None, Unset, list[str]]
        if isinstance(self.environment_ids, Unset):
            environment_ids = UNSET
        elif isinstance(self.environment_ids, list):
            environment_ids = self.environment_ids

        else:
            environment_ids = self.environment_ids

        incident_type_ids: Union[None, Unset, list[str]]
        if isinstance(self.incident_type_ids, Unset):
            incident_type_ids = UNSET
        elif isinstance(self.incident_type_ids, list):
            incident_type_ids = self.incident_type_ids

        else:
            incident_type_ids = self.incident_type_ids

        service_ids: Union[None, Unset, list[str]]
        if isinstance(self.service_ids, Unset):
            service_ids = UNSET
        elif isinstance(self.service_ids, list):
            service_ids = self.service_ids

        else:
            service_ids = self.service_ids

        functionality_ids: Union[None, Unset, list[str]]
        if isinstance(self.functionality_ids, Unset):
            functionality_ids = UNSET
        elif isinstance(self.functionality_ids, list):
            functionality_ids = self.functionality_ids

        else:
            functionality_ids = self.functionality_ids

        muted_service_ids: Union[None, Unset, list[str]]
        if isinstance(self.muted_service_ids, Unset):
            muted_service_ids = UNSET
        elif isinstance(self.muted_service_ids, list):
            muted_service_ids = self.muted_service_ids

        else:
            muted_service_ids = self.muted_service_ids

        group_ids: Union[None, Unset, list[str]]
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        cause_ids: Union[None, Unset, list[str]]
        if isinstance(self.cause_ids, Unset):
            cause_ids = UNSET
        elif isinstance(self.cause_ids, list):
            cause_ids = self.cause_ids

        else:
            cause_ids = self.cause_ids

        labels: Union[None, Unset, dict[str, Any]]
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, UpdateIncidentDataAttributesLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        slack_channel_id: Union[None, Unset, str]
        if isinstance(self.slack_channel_id, Unset):
            slack_channel_id = UNSET
        else:
            slack_channel_id = self.slack_channel_id

        slack_channel_name: Union[None, Unset, str]
        if isinstance(self.slack_channel_name, Unset):
            slack_channel_name = UNSET
        else:
            slack_channel_name = self.slack_channel_name

        slack_channel_url: Union[None, Unset, str]
        if isinstance(self.slack_channel_url, Unset):
            slack_channel_url = UNSET
        else:
            slack_channel_url = self.slack_channel_url

        slack_channel_archived: Union[None, Unset, bool]
        if isinstance(self.slack_channel_archived, Unset):
            slack_channel_archived = UNSET
        else:
            slack_channel_archived = self.slack_channel_archived

        google_drive_parent_id: Union[None, Unset, str]
        if isinstance(self.google_drive_parent_id, Unset):
            google_drive_parent_id = UNSET
        else:
            google_drive_parent_id = self.google_drive_parent_id

        google_drive_url: Union[None, Unset, str]
        if isinstance(self.google_drive_url, Unset):
            google_drive_url = UNSET
        else:
            google_drive_url = self.google_drive_url

        jira_issue_key: Union[None, Unset, str]
        if isinstance(self.jira_issue_key, Unset):
            jira_issue_key = UNSET
        else:
            jira_issue_key = self.jira_issue_key

        jira_issue_id: Union[None, Unset, str]
        if isinstance(self.jira_issue_id, Unset):
            jira_issue_id = UNSET
        else:
            jira_issue_id = self.jira_issue_id

        jira_issue_url: Union[None, Unset, str]
        if isinstance(self.jira_issue_url, Unset):
            jira_issue_url = UNSET
        else:
            jira_issue_url = self.jira_issue_url

        scheduled_for: Union[None, Unset, str]
        if isinstance(self.scheduled_for, Unset):
            scheduled_for = UNSET
        else:
            scheduled_for = self.scheduled_for

        scheduled_until: Union[None, Unset, str]
        if isinstance(self.scheduled_until, Unset):
            scheduled_until = UNSET
        else:
            scheduled_until = self.scheduled_until

        in_triage_at: Union[None, Unset, str]
        if isinstance(self.in_triage_at, Unset):
            in_triage_at = UNSET
        else:
            in_triage_at = self.in_triage_at

        started_at: Union[None, Unset, str]
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        else:
            started_at = self.started_at

        detected_at: Union[None, Unset, str]
        if isinstance(self.detected_at, Unset):
            detected_at = UNSET
        else:
            detected_at = self.detected_at

        acknowledged_at: Union[None, Unset, str]
        if isinstance(self.acknowledged_at, Unset):
            acknowledged_at = UNSET
        else:
            acknowledged_at = self.acknowledged_at

        mitigated_at: Union[None, Unset, str]
        if isinstance(self.mitigated_at, Unset):
            mitigated_at = UNSET
        else:
            mitigated_at = self.mitigated_at

        resolved_at: Union[None, Unset, str]
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        else:
            resolved_at = self.resolved_at

        closed_at: Union[None, Unset, str]
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        else:
            closed_at = self.closed_at

        cancelled_at: Union[None, Unset, str]
        if isinstance(self.cancelled_at, Unset):
            cancelled_at = UNSET
        else:
            cancelled_at = self.cancelled_at

        mitigation_message: Union[None, Unset, str]
        if isinstance(self.mitigation_message, Unset):
            mitigation_message = UNSET
        else:
            mitigation_message = self.mitigation_message

        resolution_message: Union[None, Unset, str]
        if isinstance(self.resolution_message, Unset):
            resolution_message = UNSET
        else:
            resolution_message = self.resolution_message

        cancellation_message: Union[None, Unset, str]
        if isinstance(self.cancellation_message, Unset):
            cancellation_message = UNSET
        else:
            cancellation_message = self.cancellation_message

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
        if summary is not UNSET:
            field_dict["summary"] = summary
        if status is not UNSET:
            field_dict["status"] = status
        if private is not UNSET:
            field_dict["private"] = private
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
        if muted_service_ids is not UNSET:
            field_dict["muted_service_ids"] = muted_service_ids
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if cause_ids is not UNSET:
            field_dict["cause_ids"] = cause_ids
        if labels is not UNSET:
            field_dict["labels"] = labels
        if slack_channel_id is not UNSET:
            field_dict["slack_channel_id"] = slack_channel_id
        if slack_channel_name is not UNSET:
            field_dict["slack_channel_name"] = slack_channel_name
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
        if mitigation_message is not UNSET:
            field_dict["mitigation_message"] = mitigation_message
        if resolution_message is not UNSET:
            field_dict["resolution_message"] = resolution_message
        if cancellation_message is not UNSET:
            field_dict["cancellation_message"] = cancellation_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_incident_data_attributes_labels_type_0 import UpdateIncidentDataAttributesLabelsType0

        d = dict(src_dict)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, UpdateIncidentDataAttributesKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_update_incident_data_attributes_kind(_kind)

        def _parse_parent_incident_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_incident_id = _parse_parent_incident_id(d.pop("parent_incident_id", UNSET))

        def _parse_duplicate_incident_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        duplicate_incident_id = _parse_duplicate_incident_id(d.pop("duplicate_incident_id", UNSET))

        def _parse_summary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        summary = _parse_summary(d.pop("summary", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, UpdateIncidentDataAttributesStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_incident_data_attributes_status(_status)

        def _parse_private(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        private = _parse_private(d.pop("private", UNSET))

        def _parse_severity_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        severity_id = _parse_severity_id(d.pop("severity_id", UNSET))

        def _parse_public_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        public_title = _parse_public_title(d.pop("public_title", UNSET))

        def _parse_alert_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        alert_ids = _parse_alert_ids(d.pop("alert_ids", UNSET))

        def _parse_environment_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        environment_ids = _parse_environment_ids(d.pop("environment_ids", UNSET))

        def _parse_incident_type_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        incident_type_ids = _parse_incident_type_ids(d.pop("incident_type_ids", UNSET))

        def _parse_service_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        service_ids = _parse_service_ids(d.pop("service_ids", UNSET))

        def _parse_functionality_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        functionality_ids = _parse_functionality_ids(d.pop("functionality_ids", UNSET))

        def _parse_muted_service_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        muted_service_ids = _parse_muted_service_ids(d.pop("muted_service_ids", UNSET))

        def _parse_group_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        def _parse_cause_ids(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        cause_ids = _parse_cause_ids(d.pop("cause_ids", UNSET))

        def _parse_labels(data: object) -> Union["UpdateIncidentDataAttributesLabelsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = UpdateIncidentDataAttributesLabelsType0.from_dict(data)

                return labels_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UpdateIncidentDataAttributesLabelsType0", None, Unset], data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_slack_channel_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slack_channel_id = _parse_slack_channel_id(d.pop("slack_channel_id", UNSET))

        def _parse_slack_channel_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slack_channel_name = _parse_slack_channel_name(d.pop("slack_channel_name", UNSET))

        def _parse_slack_channel_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slack_channel_url = _parse_slack_channel_url(d.pop("slack_channel_url", UNSET))

        def _parse_slack_channel_archived(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        slack_channel_archived = _parse_slack_channel_archived(d.pop("slack_channel_archived", UNSET))

        def _parse_google_drive_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        google_drive_parent_id = _parse_google_drive_parent_id(d.pop("google_drive_parent_id", UNSET))

        def _parse_google_drive_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        google_drive_url = _parse_google_drive_url(d.pop("google_drive_url", UNSET))

        def _parse_jira_issue_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        jira_issue_key = _parse_jira_issue_key(d.pop("jira_issue_key", UNSET))

        def _parse_jira_issue_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        jira_issue_id = _parse_jira_issue_id(d.pop("jira_issue_id", UNSET))

        def _parse_jira_issue_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        jira_issue_url = _parse_jira_issue_url(d.pop("jira_issue_url", UNSET))

        def _parse_scheduled_for(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scheduled_for = _parse_scheduled_for(d.pop("scheduled_for", UNSET))

        def _parse_scheduled_until(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scheduled_until = _parse_scheduled_until(d.pop("scheduled_until", UNSET))

        def _parse_in_triage_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        in_triage_at = _parse_in_triage_at(d.pop("in_triage_at", UNSET))

        def _parse_started_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_detected_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        detected_at = _parse_detected_at(d.pop("detected_at", UNSET))

        def _parse_acknowledged_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        acknowledged_at = _parse_acknowledged_at(d.pop("acknowledged_at", UNSET))

        def _parse_mitigated_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mitigated_at = _parse_mitigated_at(d.pop("mitigated_at", UNSET))

        def _parse_resolved_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at", UNSET))

        def _parse_closed_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        closed_at = _parse_closed_at(d.pop("closed_at", UNSET))

        def _parse_cancelled_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cancelled_at = _parse_cancelled_at(d.pop("cancelled_at", UNSET))

        def _parse_mitigation_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mitigation_message = _parse_mitigation_message(d.pop("mitigation_message", UNSET))

        def _parse_resolution_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        resolution_message = _parse_resolution_message(d.pop("resolution_message", UNSET))

        def _parse_cancellation_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cancellation_message = _parse_cancellation_message(d.pop("cancellation_message", UNSET))

        update_incident_data_attributes = cls(
            title=title,
            kind=kind,
            parent_incident_id=parent_incident_id,
            duplicate_incident_id=duplicate_incident_id,
            summary=summary,
            status=status,
            private=private,
            severity_id=severity_id,
            public_title=public_title,
            alert_ids=alert_ids,
            environment_ids=environment_ids,
            incident_type_ids=incident_type_ids,
            service_ids=service_ids,
            functionality_ids=functionality_ids,
            muted_service_ids=muted_service_ids,
            group_ids=group_ids,
            cause_ids=cause_ids,
            labels=labels,
            slack_channel_id=slack_channel_id,
            slack_channel_name=slack_channel_name,
            slack_channel_url=slack_channel_url,
            slack_channel_archived=slack_channel_archived,
            google_drive_parent_id=google_drive_parent_id,
            google_drive_url=google_drive_url,
            jira_issue_key=jira_issue_key,
            jira_issue_id=jira_issue_id,
            jira_issue_url=jira_issue_url,
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
            mitigation_message=mitigation_message,
            resolution_message=resolution_message,
            cancellation_message=cancellation_message,
        )

        return update_incident_data_attributes
