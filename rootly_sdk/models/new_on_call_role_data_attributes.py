from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.new_on_call_role_data_attributes_alert_fields_permissions_item import (
    NewOnCallRoleDataAttributesAlertFieldsPermissionsItem,
    check_new_on_call_role_data_attributes_alert_fields_permissions_item,
)
from ..models.new_on_call_role_data_attributes_alert_groups_permissions_item import (
    NewOnCallRoleDataAttributesAlertGroupsPermissionsItem,
    check_new_on_call_role_data_attributes_alert_groups_permissions_item,
)
from ..models.new_on_call_role_data_attributes_alert_routing_rules_permissions_item import (
    NewOnCallRoleDataAttributesAlertRoutingRulesPermissionsItem,
    check_new_on_call_role_data_attributes_alert_routing_rules_permissions_item,
)
from ..models.new_on_call_role_data_attributes_alert_sources_permissions_item import (
    NewOnCallRoleDataAttributesAlertSourcesPermissionsItem,
    check_new_on_call_role_data_attributes_alert_sources_permissions_item,
)
from ..models.new_on_call_role_data_attributes_alert_urgency_permissions_item import (
    NewOnCallRoleDataAttributesAlertUrgencyPermissionsItem,
    check_new_on_call_role_data_attributes_alert_urgency_permissions_item,
)
from ..models.new_on_call_role_data_attributes_alerts_permissions_item import (
    NewOnCallRoleDataAttributesAlertsPermissionsItem,
    check_new_on_call_role_data_attributes_alerts_permissions_item,
)
from ..models.new_on_call_role_data_attributes_api_keys_permissions_item import (
    NewOnCallRoleDataAttributesApiKeysPermissionsItem,
    check_new_on_call_role_data_attributes_api_keys_permissions_item,
)
from ..models.new_on_call_role_data_attributes_audits_permissions_item import (
    NewOnCallRoleDataAttributesAuditsPermissionsItem,
    check_new_on_call_role_data_attributes_audits_permissions_item,
)
from ..models.new_on_call_role_data_attributes_contacts_permissions_item import (
    NewOnCallRoleDataAttributesContactsPermissionsItem,
    check_new_on_call_role_data_attributes_contacts_permissions_item,
)
from ..models.new_on_call_role_data_attributes_escalation_policies_permissions_item import (
    NewOnCallRoleDataAttributesEscalationPoliciesPermissionsItem,
    check_new_on_call_role_data_attributes_escalation_policies_permissions_item,
)
from ..models.new_on_call_role_data_attributes_groups_permissions_item import (
    NewOnCallRoleDataAttributesGroupsPermissionsItem,
    check_new_on_call_role_data_attributes_groups_permissions_item,
)
from ..models.new_on_call_role_data_attributes_heartbeats_permissions_item import (
    NewOnCallRoleDataAttributesHeartbeatsPermissionsItem,
    check_new_on_call_role_data_attributes_heartbeats_permissions_item,
)
from ..models.new_on_call_role_data_attributes_integrations_permissions_item import (
    NewOnCallRoleDataAttributesIntegrationsPermissionsItem,
    check_new_on_call_role_data_attributes_integrations_permissions_item,
)
from ..models.new_on_call_role_data_attributes_invitations_permissions_item import (
    NewOnCallRoleDataAttributesInvitationsPermissionsItem,
    check_new_on_call_role_data_attributes_invitations_permissions_item,
)
from ..models.new_on_call_role_data_attributes_live_call_routing_permissions_item import (
    NewOnCallRoleDataAttributesLiveCallRoutingPermissionsItem,
    check_new_on_call_role_data_attributes_live_call_routing_permissions_item,
)
from ..models.new_on_call_role_data_attributes_on_call_readiness_report_permissions_item import (
    NewOnCallRoleDataAttributesOnCallReadinessReportPermissionsItem,
    check_new_on_call_role_data_attributes_on_call_readiness_report_permissions_item,
)
from ..models.new_on_call_role_data_attributes_on_call_roles_permissions_item import (
    NewOnCallRoleDataAttributesOnCallRolesPermissionsItem,
    check_new_on_call_role_data_attributes_on_call_roles_permissions_item,
)
from ..models.new_on_call_role_data_attributes_schedule_override_permissions_item import (
    NewOnCallRoleDataAttributesScheduleOverridePermissionsItem,
    check_new_on_call_role_data_attributes_schedule_override_permissions_item,
)
from ..models.new_on_call_role_data_attributes_schedules_permissions_item import (
    NewOnCallRoleDataAttributesSchedulesPermissionsItem,
    check_new_on_call_role_data_attributes_schedules_permissions_item,
)
from ..models.new_on_call_role_data_attributes_services_permissions_item import (
    NewOnCallRoleDataAttributesServicesPermissionsItem,
    check_new_on_call_role_data_attributes_services_permissions_item,
)
from ..models.new_on_call_role_data_attributes_webhooks_permissions_item import (
    NewOnCallRoleDataAttributesWebhooksPermissionsItem,
    check_new_on_call_role_data_attributes_webhooks_permissions_item,
)
from ..models.new_on_call_role_data_attributes_workflows_permissions_item import (
    NewOnCallRoleDataAttributesWorkflowsPermissionsItem,
    check_new_on_call_role_data_attributes_workflows_permissions_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewOnCallRoleDataAttributes")


@_attrs_define
class NewOnCallRoleDataAttributes:
    """
    Attributes:
        name (str): The role name.
        system_role (str | Unset): The kind of role (user and custom type roles are only editable) Default: 'custom'.
        alert_fields_permissions (list[NewOnCallRoleDataAttributesAlertFieldsPermissionsItem] | Unset):
        alert_groups_permissions (list[NewOnCallRoleDataAttributesAlertGroupsPermissionsItem] | Unset):
        alert_routing_rules_permissions (list[NewOnCallRoleDataAttributesAlertRoutingRulesPermissionsItem] | Unset):
        on_call_readiness_report_permissions (list[NewOnCallRoleDataAttributesOnCallReadinessReportPermissionsItem] |
            Unset):
        on_call_roles_permissions (list[NewOnCallRoleDataAttributesOnCallRolesPermissionsItem] | Unset):
        alert_sources_permissions (list[NewOnCallRoleDataAttributesAlertSourcesPermissionsItem] | Unset):
        alert_urgency_permissions (list[NewOnCallRoleDataAttributesAlertUrgencyPermissionsItem] | Unset):
        alerts_permissions (list[NewOnCallRoleDataAttributesAlertsPermissionsItem] | Unset):
        api_keys_permissions (list[NewOnCallRoleDataAttributesApiKeysPermissionsItem] | Unset):
        audits_permissions (list[NewOnCallRoleDataAttributesAuditsPermissionsItem] | Unset):
        contacts_permissions (list[NewOnCallRoleDataAttributesContactsPermissionsItem] | Unset):
        escalation_policies_permissions (list[NewOnCallRoleDataAttributesEscalationPoliciesPermissionsItem] | Unset):
        groups_permissions (list[NewOnCallRoleDataAttributesGroupsPermissionsItem] | Unset):
        heartbeats_permissions (list[NewOnCallRoleDataAttributesHeartbeatsPermissionsItem] | Unset):
        integrations_permissions (list[NewOnCallRoleDataAttributesIntegrationsPermissionsItem] | Unset):
        invitations_permissions (list[NewOnCallRoleDataAttributesInvitationsPermissionsItem] | Unset):
        live_call_routing_permissions (list[NewOnCallRoleDataAttributesLiveCallRoutingPermissionsItem] | Unset):
        schedule_override_permissions (list[NewOnCallRoleDataAttributesScheduleOverridePermissionsItem] | Unset):
        schedules_permissions (list[NewOnCallRoleDataAttributesSchedulesPermissionsItem] | Unset):
        services_permissions (list[NewOnCallRoleDataAttributesServicesPermissionsItem] | Unset):
        webhooks_permissions (list[NewOnCallRoleDataAttributesWebhooksPermissionsItem] | Unset):
        workflows_permissions (list[NewOnCallRoleDataAttributesWorkflowsPermissionsItem] | Unset):
    """

    name: str
    system_role: str | Unset = "custom"
    alert_fields_permissions: list[NewOnCallRoleDataAttributesAlertFieldsPermissionsItem] | Unset = UNSET
    alert_groups_permissions: list[NewOnCallRoleDataAttributesAlertGroupsPermissionsItem] | Unset = UNSET
    alert_routing_rules_permissions: list[NewOnCallRoleDataAttributesAlertRoutingRulesPermissionsItem] | Unset = UNSET
    on_call_readiness_report_permissions: (
        list[NewOnCallRoleDataAttributesOnCallReadinessReportPermissionsItem] | Unset
    ) = UNSET
    on_call_roles_permissions: list[NewOnCallRoleDataAttributesOnCallRolesPermissionsItem] | Unset = UNSET
    alert_sources_permissions: list[NewOnCallRoleDataAttributesAlertSourcesPermissionsItem] | Unset = UNSET
    alert_urgency_permissions: list[NewOnCallRoleDataAttributesAlertUrgencyPermissionsItem] | Unset = UNSET
    alerts_permissions: list[NewOnCallRoleDataAttributesAlertsPermissionsItem] | Unset = UNSET
    api_keys_permissions: list[NewOnCallRoleDataAttributesApiKeysPermissionsItem] | Unset = UNSET
    audits_permissions: list[NewOnCallRoleDataAttributesAuditsPermissionsItem] | Unset = UNSET
    contacts_permissions: list[NewOnCallRoleDataAttributesContactsPermissionsItem] | Unset = UNSET
    escalation_policies_permissions: list[NewOnCallRoleDataAttributesEscalationPoliciesPermissionsItem] | Unset = UNSET
    groups_permissions: list[NewOnCallRoleDataAttributesGroupsPermissionsItem] | Unset = UNSET
    heartbeats_permissions: list[NewOnCallRoleDataAttributesHeartbeatsPermissionsItem] | Unset = UNSET
    integrations_permissions: list[NewOnCallRoleDataAttributesIntegrationsPermissionsItem] | Unset = UNSET
    invitations_permissions: list[NewOnCallRoleDataAttributesInvitationsPermissionsItem] | Unset = UNSET
    live_call_routing_permissions: list[NewOnCallRoleDataAttributesLiveCallRoutingPermissionsItem] | Unset = UNSET
    schedule_override_permissions: list[NewOnCallRoleDataAttributesScheduleOverridePermissionsItem] | Unset = UNSET
    schedules_permissions: list[NewOnCallRoleDataAttributesSchedulesPermissionsItem] | Unset = UNSET
    services_permissions: list[NewOnCallRoleDataAttributesServicesPermissionsItem] | Unset = UNSET
    webhooks_permissions: list[NewOnCallRoleDataAttributesWebhooksPermissionsItem] | Unset = UNSET
    workflows_permissions: list[NewOnCallRoleDataAttributesWorkflowsPermissionsItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        system_role = self.system_role

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

        field_dict.update(
            {
                "name": name,
            }
        )
        if system_role is not UNSET:
            field_dict["system_role"] = system_role
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
        if alert_sources_permissions is not UNSET:
            field_dict["alert_sources_permissions"] = alert_sources_permissions
        if alert_urgency_permissions is not UNSET:
            field_dict["alert_urgency_permissions"] = alert_urgency_permissions
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

        system_role = d.pop("system_role", UNSET)

        _alert_fields_permissions = d.pop("alert_fields_permissions", UNSET)
        alert_fields_permissions: list[NewOnCallRoleDataAttributesAlertFieldsPermissionsItem] | Unset = UNSET
        if _alert_fields_permissions is not UNSET:
            alert_fields_permissions = []
            for alert_fields_permissions_item_data in _alert_fields_permissions:
                alert_fields_permissions_item = check_new_on_call_role_data_attributes_alert_fields_permissions_item(
                    alert_fields_permissions_item_data
                )

                alert_fields_permissions.append(alert_fields_permissions_item)

        _alert_groups_permissions = d.pop("alert_groups_permissions", UNSET)
        alert_groups_permissions: list[NewOnCallRoleDataAttributesAlertGroupsPermissionsItem] | Unset = UNSET
        if _alert_groups_permissions is not UNSET:
            alert_groups_permissions = []
            for alert_groups_permissions_item_data in _alert_groups_permissions:
                alert_groups_permissions_item = check_new_on_call_role_data_attributes_alert_groups_permissions_item(
                    alert_groups_permissions_item_data
                )

                alert_groups_permissions.append(alert_groups_permissions_item)

        _alert_routing_rules_permissions = d.pop("alert_routing_rules_permissions", UNSET)
        alert_routing_rules_permissions: list[NewOnCallRoleDataAttributesAlertRoutingRulesPermissionsItem] | Unset = (
            UNSET
        )
        if _alert_routing_rules_permissions is not UNSET:
            alert_routing_rules_permissions = []
            for alert_routing_rules_permissions_item_data in _alert_routing_rules_permissions:
                alert_routing_rules_permissions_item = (
                    check_new_on_call_role_data_attributes_alert_routing_rules_permissions_item(
                        alert_routing_rules_permissions_item_data
                    )
                )

                alert_routing_rules_permissions.append(alert_routing_rules_permissions_item)

        _on_call_readiness_report_permissions = d.pop("on_call_readiness_report_permissions", UNSET)
        on_call_readiness_report_permissions: (
            list[NewOnCallRoleDataAttributesOnCallReadinessReportPermissionsItem] | Unset
        ) = UNSET
        if _on_call_readiness_report_permissions is not UNSET:
            on_call_readiness_report_permissions = []
            for on_call_readiness_report_permissions_item_data in _on_call_readiness_report_permissions:
                on_call_readiness_report_permissions_item = (
                    check_new_on_call_role_data_attributes_on_call_readiness_report_permissions_item(
                        on_call_readiness_report_permissions_item_data
                    )
                )

                on_call_readiness_report_permissions.append(on_call_readiness_report_permissions_item)

        _on_call_roles_permissions = d.pop("on_call_roles_permissions", UNSET)
        on_call_roles_permissions: list[NewOnCallRoleDataAttributesOnCallRolesPermissionsItem] | Unset = UNSET
        if _on_call_roles_permissions is not UNSET:
            on_call_roles_permissions = []
            for on_call_roles_permissions_item_data in _on_call_roles_permissions:
                on_call_roles_permissions_item = check_new_on_call_role_data_attributes_on_call_roles_permissions_item(
                    on_call_roles_permissions_item_data
                )

                on_call_roles_permissions.append(on_call_roles_permissions_item)

        _alert_sources_permissions = d.pop("alert_sources_permissions", UNSET)
        alert_sources_permissions: list[NewOnCallRoleDataAttributesAlertSourcesPermissionsItem] | Unset = UNSET
        if _alert_sources_permissions is not UNSET:
            alert_sources_permissions = []
            for alert_sources_permissions_item_data in _alert_sources_permissions:
                alert_sources_permissions_item = check_new_on_call_role_data_attributes_alert_sources_permissions_item(
                    alert_sources_permissions_item_data
                )

                alert_sources_permissions.append(alert_sources_permissions_item)

        _alert_urgency_permissions = d.pop("alert_urgency_permissions", UNSET)
        alert_urgency_permissions: list[NewOnCallRoleDataAttributesAlertUrgencyPermissionsItem] | Unset = UNSET
        if _alert_urgency_permissions is not UNSET:
            alert_urgency_permissions = []
            for alert_urgency_permissions_item_data in _alert_urgency_permissions:
                alert_urgency_permissions_item = check_new_on_call_role_data_attributes_alert_urgency_permissions_item(
                    alert_urgency_permissions_item_data
                )

                alert_urgency_permissions.append(alert_urgency_permissions_item)

        _alerts_permissions = d.pop("alerts_permissions", UNSET)
        alerts_permissions: list[NewOnCallRoleDataAttributesAlertsPermissionsItem] | Unset = UNSET
        if _alerts_permissions is not UNSET:
            alerts_permissions = []
            for alerts_permissions_item_data in _alerts_permissions:
                alerts_permissions_item = check_new_on_call_role_data_attributes_alerts_permissions_item(
                    alerts_permissions_item_data
                )

                alerts_permissions.append(alerts_permissions_item)

        _api_keys_permissions = d.pop("api_keys_permissions", UNSET)
        api_keys_permissions: list[NewOnCallRoleDataAttributesApiKeysPermissionsItem] | Unset = UNSET
        if _api_keys_permissions is not UNSET:
            api_keys_permissions = []
            for api_keys_permissions_item_data in _api_keys_permissions:
                api_keys_permissions_item = check_new_on_call_role_data_attributes_api_keys_permissions_item(
                    api_keys_permissions_item_data
                )

                api_keys_permissions.append(api_keys_permissions_item)

        _audits_permissions = d.pop("audits_permissions", UNSET)
        audits_permissions: list[NewOnCallRoleDataAttributesAuditsPermissionsItem] | Unset = UNSET
        if _audits_permissions is not UNSET:
            audits_permissions = []
            for audits_permissions_item_data in _audits_permissions:
                audits_permissions_item = check_new_on_call_role_data_attributes_audits_permissions_item(
                    audits_permissions_item_data
                )

                audits_permissions.append(audits_permissions_item)

        _contacts_permissions = d.pop("contacts_permissions", UNSET)
        contacts_permissions: list[NewOnCallRoleDataAttributesContactsPermissionsItem] | Unset = UNSET
        if _contacts_permissions is not UNSET:
            contacts_permissions = []
            for contacts_permissions_item_data in _contacts_permissions:
                contacts_permissions_item = check_new_on_call_role_data_attributes_contacts_permissions_item(
                    contacts_permissions_item_data
                )

                contacts_permissions.append(contacts_permissions_item)

        _escalation_policies_permissions = d.pop("escalation_policies_permissions", UNSET)
        escalation_policies_permissions: list[NewOnCallRoleDataAttributesEscalationPoliciesPermissionsItem] | Unset = (
            UNSET
        )
        if _escalation_policies_permissions is not UNSET:
            escalation_policies_permissions = []
            for escalation_policies_permissions_item_data in _escalation_policies_permissions:
                escalation_policies_permissions_item = (
                    check_new_on_call_role_data_attributes_escalation_policies_permissions_item(
                        escalation_policies_permissions_item_data
                    )
                )

                escalation_policies_permissions.append(escalation_policies_permissions_item)

        _groups_permissions = d.pop("groups_permissions", UNSET)
        groups_permissions: list[NewOnCallRoleDataAttributesGroupsPermissionsItem] | Unset = UNSET
        if _groups_permissions is not UNSET:
            groups_permissions = []
            for groups_permissions_item_data in _groups_permissions:
                groups_permissions_item = check_new_on_call_role_data_attributes_groups_permissions_item(
                    groups_permissions_item_data
                )

                groups_permissions.append(groups_permissions_item)

        _heartbeats_permissions = d.pop("heartbeats_permissions", UNSET)
        heartbeats_permissions: list[NewOnCallRoleDataAttributesHeartbeatsPermissionsItem] | Unset = UNSET
        if _heartbeats_permissions is not UNSET:
            heartbeats_permissions = []
            for heartbeats_permissions_item_data in _heartbeats_permissions:
                heartbeats_permissions_item = check_new_on_call_role_data_attributes_heartbeats_permissions_item(
                    heartbeats_permissions_item_data
                )

                heartbeats_permissions.append(heartbeats_permissions_item)

        _integrations_permissions = d.pop("integrations_permissions", UNSET)
        integrations_permissions: list[NewOnCallRoleDataAttributesIntegrationsPermissionsItem] | Unset = UNSET
        if _integrations_permissions is not UNSET:
            integrations_permissions = []
            for integrations_permissions_item_data in _integrations_permissions:
                integrations_permissions_item = check_new_on_call_role_data_attributes_integrations_permissions_item(
                    integrations_permissions_item_data
                )

                integrations_permissions.append(integrations_permissions_item)

        _invitations_permissions = d.pop("invitations_permissions", UNSET)
        invitations_permissions: list[NewOnCallRoleDataAttributesInvitationsPermissionsItem] | Unset = UNSET
        if _invitations_permissions is not UNSET:
            invitations_permissions = []
            for invitations_permissions_item_data in _invitations_permissions:
                invitations_permissions_item = check_new_on_call_role_data_attributes_invitations_permissions_item(
                    invitations_permissions_item_data
                )

                invitations_permissions.append(invitations_permissions_item)

        _live_call_routing_permissions = d.pop("live_call_routing_permissions", UNSET)
        live_call_routing_permissions: list[NewOnCallRoleDataAttributesLiveCallRoutingPermissionsItem] | Unset = UNSET
        if _live_call_routing_permissions is not UNSET:
            live_call_routing_permissions = []
            for live_call_routing_permissions_item_data in _live_call_routing_permissions:
                live_call_routing_permissions_item = (
                    check_new_on_call_role_data_attributes_live_call_routing_permissions_item(
                        live_call_routing_permissions_item_data
                    )
                )

                live_call_routing_permissions.append(live_call_routing_permissions_item)

        _schedule_override_permissions = d.pop("schedule_override_permissions", UNSET)
        schedule_override_permissions: list[NewOnCallRoleDataAttributesScheduleOverridePermissionsItem] | Unset = UNSET
        if _schedule_override_permissions is not UNSET:
            schedule_override_permissions = []
            for schedule_override_permissions_item_data in _schedule_override_permissions:
                schedule_override_permissions_item = (
                    check_new_on_call_role_data_attributes_schedule_override_permissions_item(
                        schedule_override_permissions_item_data
                    )
                )

                schedule_override_permissions.append(schedule_override_permissions_item)

        _schedules_permissions = d.pop("schedules_permissions", UNSET)
        schedules_permissions: list[NewOnCallRoleDataAttributesSchedulesPermissionsItem] | Unset = UNSET
        if _schedules_permissions is not UNSET:
            schedules_permissions = []
            for schedules_permissions_item_data in _schedules_permissions:
                schedules_permissions_item = check_new_on_call_role_data_attributes_schedules_permissions_item(
                    schedules_permissions_item_data
                )

                schedules_permissions.append(schedules_permissions_item)

        _services_permissions = d.pop("services_permissions", UNSET)
        services_permissions: list[NewOnCallRoleDataAttributesServicesPermissionsItem] | Unset = UNSET
        if _services_permissions is not UNSET:
            services_permissions = []
            for services_permissions_item_data in _services_permissions:
                services_permissions_item = check_new_on_call_role_data_attributes_services_permissions_item(
                    services_permissions_item_data
                )

                services_permissions.append(services_permissions_item)

        _webhooks_permissions = d.pop("webhooks_permissions", UNSET)
        webhooks_permissions: list[NewOnCallRoleDataAttributesWebhooksPermissionsItem] | Unset = UNSET
        if _webhooks_permissions is not UNSET:
            webhooks_permissions = []
            for webhooks_permissions_item_data in _webhooks_permissions:
                webhooks_permissions_item = check_new_on_call_role_data_attributes_webhooks_permissions_item(
                    webhooks_permissions_item_data
                )

                webhooks_permissions.append(webhooks_permissions_item)

        _workflows_permissions = d.pop("workflows_permissions", UNSET)
        workflows_permissions: list[NewOnCallRoleDataAttributesWorkflowsPermissionsItem] | Unset = UNSET
        if _workflows_permissions is not UNSET:
            workflows_permissions = []
            for workflows_permissions_item_data in _workflows_permissions:
                workflows_permissions_item = check_new_on_call_role_data_attributes_workflows_permissions_item(
                    workflows_permissions_item_data
                )

                workflows_permissions.append(workflows_permissions_item)

        new_on_call_role_data_attributes = cls(
            name=name,
            system_role=system_role,
            alert_fields_permissions=alert_fields_permissions,
            alert_groups_permissions=alert_groups_permissions,
            alert_routing_rules_permissions=alert_routing_rules_permissions,
            on_call_readiness_report_permissions=on_call_readiness_report_permissions,
            on_call_roles_permissions=on_call_roles_permissions,
            alert_sources_permissions=alert_sources_permissions,
            alert_urgency_permissions=alert_urgency_permissions,
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

        return new_on_call_role_data_attributes
