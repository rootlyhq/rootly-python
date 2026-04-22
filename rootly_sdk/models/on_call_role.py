from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.on_call_role_alert_fields_permissions_item import (
    OnCallRoleAlertFieldsPermissionsItem,
    check_on_call_role_alert_fields_permissions_item,
)
from ..models.on_call_role_alert_groups_permissions_item import (
    OnCallRoleAlertGroupsPermissionsItem,
    check_on_call_role_alert_groups_permissions_item,
)
from ..models.on_call_role_alert_routing_rules_permissions_item import (
    OnCallRoleAlertRoutingRulesPermissionsItem,
    check_on_call_role_alert_routing_rules_permissions_item,
)
from ..models.on_call_role_alert_sources_permissions_item import (
    OnCallRoleAlertSourcesPermissionsItem,
    check_on_call_role_alert_sources_permissions_item,
)
from ..models.on_call_role_alert_urgency_permissions_item import (
    OnCallRoleAlertUrgencyPermissionsItem,
    check_on_call_role_alert_urgency_permissions_item,
)
from ..models.on_call_role_alerts_permissions_item import (
    OnCallRoleAlertsPermissionsItem,
    check_on_call_role_alerts_permissions_item,
)
from ..models.on_call_role_api_keys_permissions_item import (
    OnCallRoleApiKeysPermissionsItem,
    check_on_call_role_api_keys_permissions_item,
)
from ..models.on_call_role_audits_permissions_item import (
    OnCallRoleAuditsPermissionsItem,
    check_on_call_role_audits_permissions_item,
)
from ..models.on_call_role_contacts_permissions_item import (
    OnCallRoleContactsPermissionsItem,
    check_on_call_role_contacts_permissions_item,
)
from ..models.on_call_role_escalation_policies_permissions_item import (
    OnCallRoleEscalationPoliciesPermissionsItem,
    check_on_call_role_escalation_policies_permissions_item,
)
from ..models.on_call_role_groups_permissions_item import (
    OnCallRoleGroupsPermissionsItem,
    check_on_call_role_groups_permissions_item,
)
from ..models.on_call_role_heartbeats_permissions_item import (
    OnCallRoleHeartbeatsPermissionsItem,
    check_on_call_role_heartbeats_permissions_item,
)
from ..models.on_call_role_integrations_permissions_item import (
    OnCallRoleIntegrationsPermissionsItem,
    check_on_call_role_integrations_permissions_item,
)
from ..models.on_call_role_invitations_permissions_item import (
    OnCallRoleInvitationsPermissionsItem,
    check_on_call_role_invitations_permissions_item,
)
from ..models.on_call_role_live_call_routing_permissions_item import (
    OnCallRoleLiveCallRoutingPermissionsItem,
    check_on_call_role_live_call_routing_permissions_item,
)
from ..models.on_call_role_on_call_readiness_report_permissions_item import (
    OnCallRoleOnCallReadinessReportPermissionsItem,
    check_on_call_role_on_call_readiness_report_permissions_item,
)
from ..models.on_call_role_on_call_roles_permissions_item import (
    OnCallRoleOnCallRolesPermissionsItem,
    check_on_call_role_on_call_roles_permissions_item,
)
from ..models.on_call_role_schedule_override_permissions_item import (
    OnCallRoleScheduleOverridePermissionsItem,
    check_on_call_role_schedule_override_permissions_item,
)
from ..models.on_call_role_schedules_permissions_item import (
    OnCallRoleSchedulesPermissionsItem,
    check_on_call_role_schedules_permissions_item,
)
from ..models.on_call_role_services_permissions_item import (
    OnCallRoleServicesPermissionsItem,
    check_on_call_role_services_permissions_item,
)
from ..models.on_call_role_webhooks_permissions_item import (
    OnCallRoleWebhooksPermissionsItem,
    check_on_call_role_webhooks_permissions_item,
)
from ..models.on_call_role_workflows_permissions_item import (
    OnCallRoleWorkflowsPermissionsItem,
    check_on_call_role_workflows_permissions_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OnCallRole")


@_attrs_define
class OnCallRole:
    """
    Attributes:
        name (str): The role name.
        created_at (str):
        updated_at (str):
        slug (str | Unset): The role slug.
        system_role (str | Unset): The kind of role Default: 'custom'.
        alert_sources_permissions (list[OnCallRoleAlertSourcesPermissionsItem] | Unset):
        alert_urgency_permissions (list[OnCallRoleAlertUrgencyPermissionsItem] | Unset):
        alert_fields_permissions (list[OnCallRoleAlertFieldsPermissionsItem] | Unset):
        alert_groups_permissions (list[OnCallRoleAlertGroupsPermissionsItem] | Unset):
        alert_routing_rules_permissions (list[OnCallRoleAlertRoutingRulesPermissionsItem] | Unset):
        on_call_readiness_report_permissions (list[OnCallRoleOnCallReadinessReportPermissionsItem] | Unset):
        on_call_roles_permissions (list[OnCallRoleOnCallRolesPermissionsItem] | Unset):
        alerts_permissions (list[OnCallRoleAlertsPermissionsItem] | Unset):
        api_keys_permissions (list[OnCallRoleApiKeysPermissionsItem] | Unset):
        audits_permissions (list[OnCallRoleAuditsPermissionsItem] | Unset):
        contacts_permissions (list[OnCallRoleContactsPermissionsItem] | Unset):
        escalation_policies_permissions (list[OnCallRoleEscalationPoliciesPermissionsItem] | Unset):
        groups_permissions (list[OnCallRoleGroupsPermissionsItem] | Unset):
        heartbeats_permissions (list[OnCallRoleHeartbeatsPermissionsItem] | Unset):
        integrations_permissions (list[OnCallRoleIntegrationsPermissionsItem] | Unset):
        invitations_permissions (list[OnCallRoleInvitationsPermissionsItem] | Unset):
        live_call_routing_permissions (list[OnCallRoleLiveCallRoutingPermissionsItem] | Unset):
        schedule_override_permissions (list[OnCallRoleScheduleOverridePermissionsItem] | Unset):
        schedules_permissions (list[OnCallRoleSchedulesPermissionsItem] | Unset):
        services_permissions (list[OnCallRoleServicesPermissionsItem] | Unset):
        webhooks_permissions (list[OnCallRoleWebhooksPermissionsItem] | Unset):
        workflows_permissions (list[OnCallRoleWorkflowsPermissionsItem] | Unset):
    """

    name: str
    created_at: str
    updated_at: str
    slug: str | Unset = UNSET
    system_role: str | Unset = "custom"
    alert_sources_permissions: list[OnCallRoleAlertSourcesPermissionsItem] | Unset = UNSET
    alert_urgency_permissions: list[OnCallRoleAlertUrgencyPermissionsItem] | Unset = UNSET
    alert_fields_permissions: list[OnCallRoleAlertFieldsPermissionsItem] | Unset = UNSET
    alert_groups_permissions: list[OnCallRoleAlertGroupsPermissionsItem] | Unset = UNSET
    alert_routing_rules_permissions: list[OnCallRoleAlertRoutingRulesPermissionsItem] | Unset = UNSET
    on_call_readiness_report_permissions: list[OnCallRoleOnCallReadinessReportPermissionsItem] | Unset = UNSET
    on_call_roles_permissions: list[OnCallRoleOnCallRolesPermissionsItem] | Unset = UNSET
    alerts_permissions: list[OnCallRoleAlertsPermissionsItem] | Unset = UNSET
    api_keys_permissions: list[OnCallRoleApiKeysPermissionsItem] | Unset = UNSET
    audits_permissions: list[OnCallRoleAuditsPermissionsItem] | Unset = UNSET
    contacts_permissions: list[OnCallRoleContactsPermissionsItem] | Unset = UNSET
    escalation_policies_permissions: list[OnCallRoleEscalationPoliciesPermissionsItem] | Unset = UNSET
    groups_permissions: list[OnCallRoleGroupsPermissionsItem] | Unset = UNSET
    heartbeats_permissions: list[OnCallRoleHeartbeatsPermissionsItem] | Unset = UNSET
    integrations_permissions: list[OnCallRoleIntegrationsPermissionsItem] | Unset = UNSET
    invitations_permissions: list[OnCallRoleInvitationsPermissionsItem] | Unset = UNSET
    live_call_routing_permissions: list[OnCallRoleLiveCallRoutingPermissionsItem] | Unset = UNSET
    schedule_override_permissions: list[OnCallRoleScheduleOverridePermissionsItem] | Unset = UNSET
    schedules_permissions: list[OnCallRoleSchedulesPermissionsItem] | Unset = UNSET
    services_permissions: list[OnCallRoleServicesPermissionsItem] | Unset = UNSET
    webhooks_permissions: list[OnCallRoleWebhooksPermissionsItem] | Unset = UNSET
    workflows_permissions: list[OnCallRoleWorkflowsPermissionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        system_role = self.system_role

        alert_sources_permissions: list[str] | Unset = UNSET
        if not isinstance(self.alert_sources_permissions, Unset):
            alert_sources_permissions = []
            for alert_sources_permissions_item_data in self.alert_sources_permissions:
                alert_sources_permissions_item: str = alert_sources_permissions_item_data
                alert_sources_permissions.append(alert_sources_permissions_item)

        alert_urgency_permissions: list[str] | Unset = UNSET
        if not isinstance(self.alert_urgency_permissions, Unset):
            alert_urgency_permissions = []
            for alert_urgency_permissions_item_data in self.alert_urgency_permissions:
                alert_urgency_permissions_item: str = alert_urgency_permissions_item_data
                alert_urgency_permissions.append(alert_urgency_permissions_item)

        alert_fields_permissions: list[str] | Unset = UNSET
        if not isinstance(self.alert_fields_permissions, Unset):
            alert_fields_permissions = []
            for alert_fields_permissions_item_data in self.alert_fields_permissions:
                alert_fields_permissions_item: str = alert_fields_permissions_item_data
                alert_fields_permissions.append(alert_fields_permissions_item)

        alert_groups_permissions: list[str] | Unset = UNSET
        if not isinstance(self.alert_groups_permissions, Unset):
            alert_groups_permissions = []
            for alert_groups_permissions_item_data in self.alert_groups_permissions:
                alert_groups_permissions_item: str = alert_groups_permissions_item_data
                alert_groups_permissions.append(alert_groups_permissions_item)

        alert_routing_rules_permissions: list[str] | Unset = UNSET
        if not isinstance(self.alert_routing_rules_permissions, Unset):
            alert_routing_rules_permissions = []
            for alert_routing_rules_permissions_item_data in self.alert_routing_rules_permissions:
                alert_routing_rules_permissions_item: str = alert_routing_rules_permissions_item_data
                alert_routing_rules_permissions.append(alert_routing_rules_permissions_item)

        on_call_readiness_report_permissions: list[str] | Unset = UNSET
        if not isinstance(self.on_call_readiness_report_permissions, Unset):
            on_call_readiness_report_permissions = []
            for on_call_readiness_report_permissions_item_data in self.on_call_readiness_report_permissions:
                on_call_readiness_report_permissions_item: str = on_call_readiness_report_permissions_item_data
                on_call_readiness_report_permissions.append(on_call_readiness_report_permissions_item)

        on_call_roles_permissions: list[str] | Unset = UNSET
        if not isinstance(self.on_call_roles_permissions, Unset):
            on_call_roles_permissions = []
            for on_call_roles_permissions_item_data in self.on_call_roles_permissions:
                on_call_roles_permissions_item: str = on_call_roles_permissions_item_data
                on_call_roles_permissions.append(on_call_roles_permissions_item)

        alerts_permissions: list[str] | Unset = UNSET
        if not isinstance(self.alerts_permissions, Unset):
            alerts_permissions = []
            for alerts_permissions_item_data in self.alerts_permissions:
                alerts_permissions_item: str = alerts_permissions_item_data
                alerts_permissions.append(alerts_permissions_item)

        api_keys_permissions: list[str] | Unset = UNSET
        if not isinstance(self.api_keys_permissions, Unset):
            api_keys_permissions = []
            for api_keys_permissions_item_data in self.api_keys_permissions:
                api_keys_permissions_item: str = api_keys_permissions_item_data
                api_keys_permissions.append(api_keys_permissions_item)

        audits_permissions: list[str] | Unset = UNSET
        if not isinstance(self.audits_permissions, Unset):
            audits_permissions = []
            for audits_permissions_item_data in self.audits_permissions:
                audits_permissions_item: str = audits_permissions_item_data
                audits_permissions.append(audits_permissions_item)

        contacts_permissions: list[str] | Unset = UNSET
        if not isinstance(self.contacts_permissions, Unset):
            contacts_permissions = []
            for contacts_permissions_item_data in self.contacts_permissions:
                contacts_permissions_item: str = contacts_permissions_item_data
                contacts_permissions.append(contacts_permissions_item)

        escalation_policies_permissions: list[str] | Unset = UNSET
        if not isinstance(self.escalation_policies_permissions, Unset):
            escalation_policies_permissions = []
            for escalation_policies_permissions_item_data in self.escalation_policies_permissions:
                escalation_policies_permissions_item: str = escalation_policies_permissions_item_data
                escalation_policies_permissions.append(escalation_policies_permissions_item)

        groups_permissions: list[str] | Unset = UNSET
        if not isinstance(self.groups_permissions, Unset):
            groups_permissions = []
            for groups_permissions_item_data in self.groups_permissions:
                groups_permissions_item: str = groups_permissions_item_data
                groups_permissions.append(groups_permissions_item)

        heartbeats_permissions: list[str] | Unset = UNSET
        if not isinstance(self.heartbeats_permissions, Unset):
            heartbeats_permissions = []
            for heartbeats_permissions_item_data in self.heartbeats_permissions:
                heartbeats_permissions_item: str = heartbeats_permissions_item_data
                heartbeats_permissions.append(heartbeats_permissions_item)

        integrations_permissions: list[str] | Unset = UNSET
        if not isinstance(self.integrations_permissions, Unset):
            integrations_permissions = []
            for integrations_permissions_item_data in self.integrations_permissions:
                integrations_permissions_item: str = integrations_permissions_item_data
                integrations_permissions.append(integrations_permissions_item)

        invitations_permissions: list[str] | Unset = UNSET
        if not isinstance(self.invitations_permissions, Unset):
            invitations_permissions = []
            for invitations_permissions_item_data in self.invitations_permissions:
                invitations_permissions_item: str = invitations_permissions_item_data
                invitations_permissions.append(invitations_permissions_item)

        live_call_routing_permissions: list[str] | Unset = UNSET
        if not isinstance(self.live_call_routing_permissions, Unset):
            live_call_routing_permissions = []
            for live_call_routing_permissions_item_data in self.live_call_routing_permissions:
                live_call_routing_permissions_item: str = live_call_routing_permissions_item_data
                live_call_routing_permissions.append(live_call_routing_permissions_item)

        schedule_override_permissions: list[str] | Unset = UNSET
        if not isinstance(self.schedule_override_permissions, Unset):
            schedule_override_permissions = []
            for schedule_override_permissions_item_data in self.schedule_override_permissions:
                schedule_override_permissions_item: str = schedule_override_permissions_item_data
                schedule_override_permissions.append(schedule_override_permissions_item)

        schedules_permissions: list[str] | Unset = UNSET
        if not isinstance(self.schedules_permissions, Unset):
            schedules_permissions = []
            for schedules_permissions_item_data in self.schedules_permissions:
                schedules_permissions_item: str = schedules_permissions_item_data
                schedules_permissions.append(schedules_permissions_item)

        services_permissions: list[str] | Unset = UNSET
        if not isinstance(self.services_permissions, Unset):
            services_permissions = []
            for services_permissions_item_data in self.services_permissions:
                services_permissions_item: str = services_permissions_item_data
                services_permissions.append(services_permissions_item)

        webhooks_permissions: list[str] | Unset = UNSET
        if not isinstance(self.webhooks_permissions, Unset):
            webhooks_permissions = []
            for webhooks_permissions_item_data in self.webhooks_permissions:
                webhooks_permissions_item: str = webhooks_permissions_item_data
                webhooks_permissions.append(webhooks_permissions_item)

        workflows_permissions: list[str] | Unset = UNSET
        if not isinstance(self.workflows_permissions, Unset):
            workflows_permissions = []
            for workflows_permissions_item_data in self.workflows_permissions:
                workflows_permissions_item: str = workflows_permissions_item_data
                workflows_permissions.append(workflows_permissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if system_role is not UNSET:
            field_dict["system_role"] = system_role
        if alert_sources_permissions is not UNSET:
            field_dict["alert_sources_permissions"] = alert_sources_permissions
        if alert_urgency_permissions is not UNSET:
            field_dict["alert_urgency_permissions"] = alert_urgency_permissions
        if alert_fields_permissions is not UNSET:
            field_dict["alert_fields_permissions"] = alert_fields_permissions
        if alert_groups_permissions is not UNSET:
            field_dict["alert_groups_permissions"] = alert_groups_permissions
        if alert_routing_rules_permissions is not UNSET:
            field_dict["alert_routing_rules_permissions"] = alert_routing_rules_permissions
        if on_call_readiness_report_permissions is not UNSET:
            field_dict["on_call_readiness_report_permissions"] = on_call_readiness_report_permissions
        if on_call_roles_permissions is not UNSET:
            field_dict["on_call_roles_permissions"] = on_call_roles_permissions
        if alerts_permissions is not UNSET:
            field_dict["alerts_permissions"] = alerts_permissions
        if api_keys_permissions is not UNSET:
            field_dict["api_keys_permissions"] = api_keys_permissions
        if audits_permissions is not UNSET:
            field_dict["audits_permissions"] = audits_permissions
        if contacts_permissions is not UNSET:
            field_dict["contacts_permissions"] = contacts_permissions
        if escalation_policies_permissions is not UNSET:
            field_dict["escalation_policies_permissions"] = escalation_policies_permissions
        if groups_permissions is not UNSET:
            field_dict["groups_permissions"] = groups_permissions
        if heartbeats_permissions is not UNSET:
            field_dict["heartbeats_permissions"] = heartbeats_permissions
        if integrations_permissions is not UNSET:
            field_dict["integrations_permissions"] = integrations_permissions
        if invitations_permissions is not UNSET:
            field_dict["invitations_permissions"] = invitations_permissions
        if live_call_routing_permissions is not UNSET:
            field_dict["live_call_routing_permissions"] = live_call_routing_permissions
        if schedule_override_permissions is not UNSET:
            field_dict["schedule_override_permissions"] = schedule_override_permissions
        if schedules_permissions is not UNSET:
            field_dict["schedules_permissions"] = schedules_permissions
        if services_permissions is not UNSET:
            field_dict["services_permissions"] = services_permissions
        if webhooks_permissions is not UNSET:
            field_dict["webhooks_permissions"] = webhooks_permissions
        if workflows_permissions is not UNSET:
            field_dict["workflows_permissions"] = workflows_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        system_role = d.pop("system_role", UNSET)

        _alert_sources_permissions = d.pop("alert_sources_permissions", UNSET)
        alert_sources_permissions: list[OnCallRoleAlertSourcesPermissionsItem] | Unset = UNSET
        if _alert_sources_permissions is not UNSET:
            alert_sources_permissions = []
            for alert_sources_permissions_item_data in _alert_sources_permissions:
                alert_sources_permissions_item = check_on_call_role_alert_sources_permissions_item(
                    alert_sources_permissions_item_data
                )

                alert_sources_permissions.append(alert_sources_permissions_item)

        _alert_urgency_permissions = d.pop("alert_urgency_permissions", UNSET)
        alert_urgency_permissions: list[OnCallRoleAlertUrgencyPermissionsItem] | Unset = UNSET
        if _alert_urgency_permissions is not UNSET:
            alert_urgency_permissions = []
            for alert_urgency_permissions_item_data in _alert_urgency_permissions:
                alert_urgency_permissions_item = check_on_call_role_alert_urgency_permissions_item(
                    alert_urgency_permissions_item_data
                )

                alert_urgency_permissions.append(alert_urgency_permissions_item)

        _alert_fields_permissions = d.pop("alert_fields_permissions", UNSET)
        alert_fields_permissions: list[OnCallRoleAlertFieldsPermissionsItem] | Unset = UNSET
        if _alert_fields_permissions is not UNSET:
            alert_fields_permissions = []
            for alert_fields_permissions_item_data in _alert_fields_permissions:
                alert_fields_permissions_item = check_on_call_role_alert_fields_permissions_item(
                    alert_fields_permissions_item_data
                )

                alert_fields_permissions.append(alert_fields_permissions_item)

        _alert_groups_permissions = d.pop("alert_groups_permissions", UNSET)
        alert_groups_permissions: list[OnCallRoleAlertGroupsPermissionsItem] | Unset = UNSET
        if _alert_groups_permissions is not UNSET:
            alert_groups_permissions = []
            for alert_groups_permissions_item_data in _alert_groups_permissions:
                alert_groups_permissions_item = check_on_call_role_alert_groups_permissions_item(
                    alert_groups_permissions_item_data
                )

                alert_groups_permissions.append(alert_groups_permissions_item)

        _alert_routing_rules_permissions = d.pop("alert_routing_rules_permissions", UNSET)
        alert_routing_rules_permissions: list[OnCallRoleAlertRoutingRulesPermissionsItem] | Unset = UNSET
        if _alert_routing_rules_permissions is not UNSET:
            alert_routing_rules_permissions = []
            for alert_routing_rules_permissions_item_data in _alert_routing_rules_permissions:
                alert_routing_rules_permissions_item = check_on_call_role_alert_routing_rules_permissions_item(
                    alert_routing_rules_permissions_item_data
                )

                alert_routing_rules_permissions.append(alert_routing_rules_permissions_item)

        _on_call_readiness_report_permissions = d.pop("on_call_readiness_report_permissions", UNSET)
        on_call_readiness_report_permissions: list[OnCallRoleOnCallReadinessReportPermissionsItem] | Unset = UNSET
        if _on_call_readiness_report_permissions is not UNSET:
            on_call_readiness_report_permissions = []
            for on_call_readiness_report_permissions_item_data in _on_call_readiness_report_permissions:
                on_call_readiness_report_permissions_item = (
                    check_on_call_role_on_call_readiness_report_permissions_item(
                        on_call_readiness_report_permissions_item_data
                    )
                )

                on_call_readiness_report_permissions.append(on_call_readiness_report_permissions_item)

        _on_call_roles_permissions = d.pop("on_call_roles_permissions", UNSET)
        on_call_roles_permissions: list[OnCallRoleOnCallRolesPermissionsItem] | Unset = UNSET
        if _on_call_roles_permissions is not UNSET:
            on_call_roles_permissions = []
            for on_call_roles_permissions_item_data in _on_call_roles_permissions:
                on_call_roles_permissions_item = check_on_call_role_on_call_roles_permissions_item(
                    on_call_roles_permissions_item_data
                )

                on_call_roles_permissions.append(on_call_roles_permissions_item)

        _alerts_permissions = d.pop("alerts_permissions", UNSET)
        alerts_permissions: list[OnCallRoleAlertsPermissionsItem] | Unset = UNSET
        if _alerts_permissions is not UNSET:
            alerts_permissions = []
            for alerts_permissions_item_data in _alerts_permissions:
                alerts_permissions_item = check_on_call_role_alerts_permissions_item(alerts_permissions_item_data)

                alerts_permissions.append(alerts_permissions_item)

        _api_keys_permissions = d.pop("api_keys_permissions", UNSET)
        api_keys_permissions: list[OnCallRoleApiKeysPermissionsItem] | Unset = UNSET
        if _api_keys_permissions is not UNSET:
            api_keys_permissions = []
            for api_keys_permissions_item_data in _api_keys_permissions:
                api_keys_permissions_item = check_on_call_role_api_keys_permissions_item(api_keys_permissions_item_data)

                api_keys_permissions.append(api_keys_permissions_item)

        _audits_permissions = d.pop("audits_permissions", UNSET)
        audits_permissions: list[OnCallRoleAuditsPermissionsItem] | Unset = UNSET
        if _audits_permissions is not UNSET:
            audits_permissions = []
            for audits_permissions_item_data in _audits_permissions:
                audits_permissions_item = check_on_call_role_audits_permissions_item(audits_permissions_item_data)

                audits_permissions.append(audits_permissions_item)

        _contacts_permissions = d.pop("contacts_permissions", UNSET)
        contacts_permissions: list[OnCallRoleContactsPermissionsItem] | Unset = UNSET
        if _contacts_permissions is not UNSET:
            contacts_permissions = []
            for contacts_permissions_item_data in _contacts_permissions:
                contacts_permissions_item = check_on_call_role_contacts_permissions_item(contacts_permissions_item_data)

                contacts_permissions.append(contacts_permissions_item)

        _escalation_policies_permissions = d.pop("escalation_policies_permissions", UNSET)
        escalation_policies_permissions: list[OnCallRoleEscalationPoliciesPermissionsItem] | Unset = UNSET
        if _escalation_policies_permissions is not UNSET:
            escalation_policies_permissions = []
            for escalation_policies_permissions_item_data in _escalation_policies_permissions:
                escalation_policies_permissions_item = check_on_call_role_escalation_policies_permissions_item(
                    escalation_policies_permissions_item_data
                )

                escalation_policies_permissions.append(escalation_policies_permissions_item)

        _groups_permissions = d.pop("groups_permissions", UNSET)
        groups_permissions: list[OnCallRoleGroupsPermissionsItem] | Unset = UNSET
        if _groups_permissions is not UNSET:
            groups_permissions = []
            for groups_permissions_item_data in _groups_permissions:
                groups_permissions_item = check_on_call_role_groups_permissions_item(groups_permissions_item_data)

                groups_permissions.append(groups_permissions_item)

        _heartbeats_permissions = d.pop("heartbeats_permissions", UNSET)
        heartbeats_permissions: list[OnCallRoleHeartbeatsPermissionsItem] | Unset = UNSET
        if _heartbeats_permissions is not UNSET:
            heartbeats_permissions = []
            for heartbeats_permissions_item_data in _heartbeats_permissions:
                heartbeats_permissions_item = check_on_call_role_heartbeats_permissions_item(
                    heartbeats_permissions_item_data
                )

                heartbeats_permissions.append(heartbeats_permissions_item)

        _integrations_permissions = d.pop("integrations_permissions", UNSET)
        integrations_permissions: list[OnCallRoleIntegrationsPermissionsItem] | Unset = UNSET
        if _integrations_permissions is not UNSET:
            integrations_permissions = []
            for integrations_permissions_item_data in _integrations_permissions:
                integrations_permissions_item = check_on_call_role_integrations_permissions_item(
                    integrations_permissions_item_data
                )

                integrations_permissions.append(integrations_permissions_item)

        _invitations_permissions = d.pop("invitations_permissions", UNSET)
        invitations_permissions: list[OnCallRoleInvitationsPermissionsItem] | Unset = UNSET
        if _invitations_permissions is not UNSET:
            invitations_permissions = []
            for invitations_permissions_item_data in _invitations_permissions:
                invitations_permissions_item = check_on_call_role_invitations_permissions_item(
                    invitations_permissions_item_data
                )

                invitations_permissions.append(invitations_permissions_item)

        _live_call_routing_permissions = d.pop("live_call_routing_permissions", UNSET)
        live_call_routing_permissions: list[OnCallRoleLiveCallRoutingPermissionsItem] | Unset = UNSET
        if _live_call_routing_permissions is not UNSET:
            live_call_routing_permissions = []
            for live_call_routing_permissions_item_data in _live_call_routing_permissions:
                live_call_routing_permissions_item = check_on_call_role_live_call_routing_permissions_item(
                    live_call_routing_permissions_item_data
                )

                live_call_routing_permissions.append(live_call_routing_permissions_item)

        _schedule_override_permissions = d.pop("schedule_override_permissions", UNSET)
        schedule_override_permissions: list[OnCallRoleScheduleOverridePermissionsItem] | Unset = UNSET
        if _schedule_override_permissions is not UNSET:
            schedule_override_permissions = []
            for schedule_override_permissions_item_data in _schedule_override_permissions:
                schedule_override_permissions_item = check_on_call_role_schedule_override_permissions_item(
                    schedule_override_permissions_item_data
                )

                schedule_override_permissions.append(schedule_override_permissions_item)

        _schedules_permissions = d.pop("schedules_permissions", UNSET)
        schedules_permissions: list[OnCallRoleSchedulesPermissionsItem] | Unset = UNSET
        if _schedules_permissions is not UNSET:
            schedules_permissions = []
            for schedules_permissions_item_data in _schedules_permissions:
                schedules_permissions_item = check_on_call_role_schedules_permissions_item(
                    schedules_permissions_item_data
                )

                schedules_permissions.append(schedules_permissions_item)

        _services_permissions = d.pop("services_permissions", UNSET)
        services_permissions: list[OnCallRoleServicesPermissionsItem] | Unset = UNSET
        if _services_permissions is not UNSET:
            services_permissions = []
            for services_permissions_item_data in _services_permissions:
                services_permissions_item = check_on_call_role_services_permissions_item(services_permissions_item_data)

                services_permissions.append(services_permissions_item)

        _webhooks_permissions = d.pop("webhooks_permissions", UNSET)
        webhooks_permissions: list[OnCallRoleWebhooksPermissionsItem] | Unset = UNSET
        if _webhooks_permissions is not UNSET:
            webhooks_permissions = []
            for webhooks_permissions_item_data in _webhooks_permissions:
                webhooks_permissions_item = check_on_call_role_webhooks_permissions_item(webhooks_permissions_item_data)

                webhooks_permissions.append(webhooks_permissions_item)

        _workflows_permissions = d.pop("workflows_permissions", UNSET)
        workflows_permissions: list[OnCallRoleWorkflowsPermissionsItem] | Unset = UNSET
        if _workflows_permissions is not UNSET:
            workflows_permissions = []
            for workflows_permissions_item_data in _workflows_permissions:
                workflows_permissions_item = check_on_call_role_workflows_permissions_item(
                    workflows_permissions_item_data
                )

                workflows_permissions.append(workflows_permissions_item)

        on_call_role = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            system_role=system_role,
            alert_sources_permissions=alert_sources_permissions,
            alert_urgency_permissions=alert_urgency_permissions,
            alert_fields_permissions=alert_fields_permissions,
            alert_groups_permissions=alert_groups_permissions,
            alert_routing_rules_permissions=alert_routing_rules_permissions,
            on_call_readiness_report_permissions=on_call_readiness_report_permissions,
            on_call_roles_permissions=on_call_roles_permissions,
            alerts_permissions=alerts_permissions,
            api_keys_permissions=api_keys_permissions,
            audits_permissions=audits_permissions,
            contacts_permissions=contacts_permissions,
            escalation_policies_permissions=escalation_policies_permissions,
            groups_permissions=groups_permissions,
            heartbeats_permissions=heartbeats_permissions,
            integrations_permissions=integrations_permissions,
            invitations_permissions=invitations_permissions,
            live_call_routing_permissions=live_call_routing_permissions,
            schedule_override_permissions=schedule_override_permissions,
            schedules_permissions=schedules_permissions,
            services_permissions=services_permissions,
            webhooks_permissions=webhooks_permissions,
            workflows_permissions=workflows_permissions,
        )

        on_call_role.additional_properties = d
        return on_call_role

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
