from collections.abc import Mapping
from typing import Any, TypeVar, Union

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
        system_role (Union[Unset, str]): The kind of role (user and custom type roles are only editable) Default:
            'custom'.
        alert_fields_permissions (Union[Unset, list[NewOnCallRoleDataAttributesAlertFieldsPermissionsItem]]):
        alert_groups_permissions (Union[Unset, list[NewOnCallRoleDataAttributesAlertGroupsPermissionsItem]]):
        alert_routing_rules_permissions (Union[Unset,
            list[NewOnCallRoleDataAttributesAlertRoutingRulesPermissionsItem]]):
        on_call_readiness_report_permissions (Union[Unset,
            list[NewOnCallRoleDataAttributesOnCallReadinessReportPermissionsItem]]):
        on_call_roles_permissions (Union[Unset, list[NewOnCallRoleDataAttributesOnCallRolesPermissionsItem]]):
        alert_sources_permissions (Union[Unset, list[NewOnCallRoleDataAttributesAlertSourcesPermissionsItem]]):
        alert_urgency_permissions (Union[Unset, list[NewOnCallRoleDataAttributesAlertUrgencyPermissionsItem]]):
        alerts_permissions (Union[Unset, list[NewOnCallRoleDataAttributesAlertsPermissionsItem]]):
        api_keys_permissions (Union[Unset, list[NewOnCallRoleDataAttributesApiKeysPermissionsItem]]):
        audits_permissions (Union[Unset, list[NewOnCallRoleDataAttributesAuditsPermissionsItem]]):
        contacts_permissions (Union[Unset, list[NewOnCallRoleDataAttributesContactsPermissionsItem]]):
        escalation_policies_permissions (Union[Unset,
            list[NewOnCallRoleDataAttributesEscalationPoliciesPermissionsItem]]):
        groups_permissions (Union[Unset, list[NewOnCallRoleDataAttributesGroupsPermissionsItem]]):
        heartbeats_permissions (Union[Unset, list[NewOnCallRoleDataAttributesHeartbeatsPermissionsItem]]):
        integrations_permissions (Union[Unset, list[NewOnCallRoleDataAttributesIntegrationsPermissionsItem]]):
        invitations_permissions (Union[Unset, list[NewOnCallRoleDataAttributesInvitationsPermissionsItem]]):
        live_call_routing_permissions (Union[Unset, list[NewOnCallRoleDataAttributesLiveCallRoutingPermissionsItem]]):
        schedule_override_permissions (Union[Unset, list[NewOnCallRoleDataAttributesScheduleOverridePermissionsItem]]):
        schedules_permissions (Union[Unset, list[NewOnCallRoleDataAttributesSchedulesPermissionsItem]]):
        services_permissions (Union[Unset, list[NewOnCallRoleDataAttributesServicesPermissionsItem]]):
        webhooks_permissions (Union[Unset, list[NewOnCallRoleDataAttributesWebhooksPermissionsItem]]):
        workflows_permissions (Union[Unset, list[NewOnCallRoleDataAttributesWorkflowsPermissionsItem]]):
    """

    name: str
    system_role: Union[Unset, str] = "custom"
    alert_fields_permissions: Union[Unset, list[NewOnCallRoleDataAttributesAlertFieldsPermissionsItem]] = UNSET
    alert_groups_permissions: Union[Unset, list[NewOnCallRoleDataAttributesAlertGroupsPermissionsItem]] = UNSET
    alert_routing_rules_permissions: Union[Unset, list[NewOnCallRoleDataAttributesAlertRoutingRulesPermissionsItem]] = (
        UNSET
    )
    on_call_readiness_report_permissions: Union[
        Unset, list[NewOnCallRoleDataAttributesOnCallReadinessReportPermissionsItem]
    ] = UNSET
    on_call_roles_permissions: Union[Unset, list[NewOnCallRoleDataAttributesOnCallRolesPermissionsItem]] = UNSET
    alert_sources_permissions: Union[Unset, list[NewOnCallRoleDataAttributesAlertSourcesPermissionsItem]] = UNSET
    alert_urgency_permissions: Union[Unset, list[NewOnCallRoleDataAttributesAlertUrgencyPermissionsItem]] = UNSET
    alerts_permissions: Union[Unset, list[NewOnCallRoleDataAttributesAlertsPermissionsItem]] = UNSET
    api_keys_permissions: Union[Unset, list[NewOnCallRoleDataAttributesApiKeysPermissionsItem]] = UNSET
    audits_permissions: Union[Unset, list[NewOnCallRoleDataAttributesAuditsPermissionsItem]] = UNSET
    contacts_permissions: Union[Unset, list[NewOnCallRoleDataAttributesContactsPermissionsItem]] = UNSET
    escalation_policies_permissions: Union[
        Unset, list[NewOnCallRoleDataAttributesEscalationPoliciesPermissionsItem]
    ] = UNSET
    groups_permissions: Union[Unset, list[NewOnCallRoleDataAttributesGroupsPermissionsItem]] = UNSET
    heartbeats_permissions: Union[Unset, list[NewOnCallRoleDataAttributesHeartbeatsPermissionsItem]] = UNSET
    integrations_permissions: Union[Unset, list[NewOnCallRoleDataAttributesIntegrationsPermissionsItem]] = UNSET
    invitations_permissions: Union[Unset, list[NewOnCallRoleDataAttributesInvitationsPermissionsItem]] = UNSET
    live_call_routing_permissions: Union[Unset, list[NewOnCallRoleDataAttributesLiveCallRoutingPermissionsItem]] = UNSET
    schedule_override_permissions: Union[Unset, list[NewOnCallRoleDataAttributesScheduleOverridePermissionsItem]] = (
        UNSET
    )
    schedules_permissions: Union[Unset, list[NewOnCallRoleDataAttributesSchedulesPermissionsItem]] = UNSET
    services_permissions: Union[Unset, list[NewOnCallRoleDataAttributesServicesPermissionsItem]] = UNSET
    webhooks_permissions: Union[Unset, list[NewOnCallRoleDataAttributesWebhooksPermissionsItem]] = UNSET
    workflows_permissions: Union[Unset, list[NewOnCallRoleDataAttributesWorkflowsPermissionsItem]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        system_role = self.system_role

        alert_fields_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.alert_fields_permissions, Unset):
            alert_fields_permissions = []
            for alert_fields_permissions_item_data in self.alert_fields_permissions:
                alert_fields_permissions_item: str = alert_fields_permissions_item_data
                alert_fields_permissions.append(alert_fields_permissions_item)

        alert_groups_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.alert_groups_permissions, Unset):
            alert_groups_permissions = []
            for alert_groups_permissions_item_data in self.alert_groups_permissions:
                alert_groups_permissions_item: str = alert_groups_permissions_item_data
                alert_groups_permissions.append(alert_groups_permissions_item)

        alert_routing_rules_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.alert_routing_rules_permissions, Unset):
            alert_routing_rules_permissions = []
            for alert_routing_rules_permissions_item_data in self.alert_routing_rules_permissions:
                alert_routing_rules_permissions_item: str = alert_routing_rules_permissions_item_data
                alert_routing_rules_permissions.append(alert_routing_rules_permissions_item)

        on_call_readiness_report_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.on_call_readiness_report_permissions, Unset):
            on_call_readiness_report_permissions = []
            for on_call_readiness_report_permissions_item_data in self.on_call_readiness_report_permissions:
                on_call_readiness_report_permissions_item: str = on_call_readiness_report_permissions_item_data
                on_call_readiness_report_permissions.append(on_call_readiness_report_permissions_item)

        on_call_roles_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.on_call_roles_permissions, Unset):
            on_call_roles_permissions = []
            for on_call_roles_permissions_item_data in self.on_call_roles_permissions:
                on_call_roles_permissions_item: str = on_call_roles_permissions_item_data
                on_call_roles_permissions.append(on_call_roles_permissions_item)

        alert_sources_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.alert_sources_permissions, Unset):
            alert_sources_permissions = []
            for alert_sources_permissions_item_data in self.alert_sources_permissions:
                alert_sources_permissions_item: str = alert_sources_permissions_item_data
                alert_sources_permissions.append(alert_sources_permissions_item)

        alert_urgency_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.alert_urgency_permissions, Unset):
            alert_urgency_permissions = []
            for alert_urgency_permissions_item_data in self.alert_urgency_permissions:
                alert_urgency_permissions_item: str = alert_urgency_permissions_item_data
                alert_urgency_permissions.append(alert_urgency_permissions_item)

        alerts_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.alerts_permissions, Unset):
            alerts_permissions = []
            for alerts_permissions_item_data in self.alerts_permissions:
                alerts_permissions_item: str = alerts_permissions_item_data
                alerts_permissions.append(alerts_permissions_item)

        api_keys_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.api_keys_permissions, Unset):
            api_keys_permissions = []
            for api_keys_permissions_item_data in self.api_keys_permissions:
                api_keys_permissions_item: str = api_keys_permissions_item_data
                api_keys_permissions.append(api_keys_permissions_item)

        audits_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.audits_permissions, Unset):
            audits_permissions = []
            for audits_permissions_item_data in self.audits_permissions:
                audits_permissions_item: str = audits_permissions_item_data
                audits_permissions.append(audits_permissions_item)

        contacts_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.contacts_permissions, Unset):
            contacts_permissions = []
            for contacts_permissions_item_data in self.contacts_permissions:
                contacts_permissions_item: str = contacts_permissions_item_data
                contacts_permissions.append(contacts_permissions_item)

        escalation_policies_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.escalation_policies_permissions, Unset):
            escalation_policies_permissions = []
            for escalation_policies_permissions_item_data in self.escalation_policies_permissions:
                escalation_policies_permissions_item: str = escalation_policies_permissions_item_data
                escalation_policies_permissions.append(escalation_policies_permissions_item)

        groups_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.groups_permissions, Unset):
            groups_permissions = []
            for groups_permissions_item_data in self.groups_permissions:
                groups_permissions_item: str = groups_permissions_item_data
                groups_permissions.append(groups_permissions_item)

        heartbeats_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.heartbeats_permissions, Unset):
            heartbeats_permissions = []
            for heartbeats_permissions_item_data in self.heartbeats_permissions:
                heartbeats_permissions_item: str = heartbeats_permissions_item_data
                heartbeats_permissions.append(heartbeats_permissions_item)

        integrations_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.integrations_permissions, Unset):
            integrations_permissions = []
            for integrations_permissions_item_data in self.integrations_permissions:
                integrations_permissions_item: str = integrations_permissions_item_data
                integrations_permissions.append(integrations_permissions_item)

        invitations_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.invitations_permissions, Unset):
            invitations_permissions = []
            for invitations_permissions_item_data in self.invitations_permissions:
                invitations_permissions_item: str = invitations_permissions_item_data
                invitations_permissions.append(invitations_permissions_item)

        live_call_routing_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.live_call_routing_permissions, Unset):
            live_call_routing_permissions = []
            for live_call_routing_permissions_item_data in self.live_call_routing_permissions:
                live_call_routing_permissions_item: str = live_call_routing_permissions_item_data
                live_call_routing_permissions.append(live_call_routing_permissions_item)

        schedule_override_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.schedule_override_permissions, Unset):
            schedule_override_permissions = []
            for schedule_override_permissions_item_data in self.schedule_override_permissions:
                schedule_override_permissions_item: str = schedule_override_permissions_item_data
                schedule_override_permissions.append(schedule_override_permissions_item)

        schedules_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.schedules_permissions, Unset):
            schedules_permissions = []
            for schedules_permissions_item_data in self.schedules_permissions:
                schedules_permissions_item: str = schedules_permissions_item_data
                schedules_permissions.append(schedules_permissions_item)

        services_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.services_permissions, Unset):
            services_permissions = []
            for services_permissions_item_data in self.services_permissions:
                services_permissions_item: str = services_permissions_item_data
                services_permissions.append(services_permissions_item)

        webhooks_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.webhooks_permissions, Unset):
            webhooks_permissions = []
            for webhooks_permissions_item_data in self.webhooks_permissions:
                webhooks_permissions_item: str = webhooks_permissions_item_data
                webhooks_permissions.append(webhooks_permissions_item)

        workflows_permissions: Union[Unset, list[str]] = UNSET
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

        alert_fields_permissions = []
        _alert_fields_permissions = d.pop("alert_fields_permissions", UNSET)
        for alert_fields_permissions_item_data in _alert_fields_permissions or []:
            alert_fields_permissions_item = check_new_on_call_role_data_attributes_alert_fields_permissions_item(
                alert_fields_permissions_item_data
            )

            alert_fields_permissions.append(alert_fields_permissions_item)

        alert_groups_permissions = []
        _alert_groups_permissions = d.pop("alert_groups_permissions", UNSET)
        for alert_groups_permissions_item_data in _alert_groups_permissions or []:
            alert_groups_permissions_item = check_new_on_call_role_data_attributes_alert_groups_permissions_item(
                alert_groups_permissions_item_data
            )

            alert_groups_permissions.append(alert_groups_permissions_item)

        alert_routing_rules_permissions = []
        _alert_routing_rules_permissions = d.pop("alert_routing_rules_permissions", UNSET)
        for alert_routing_rules_permissions_item_data in _alert_routing_rules_permissions or []:
            alert_routing_rules_permissions_item = (
                check_new_on_call_role_data_attributes_alert_routing_rules_permissions_item(
                    alert_routing_rules_permissions_item_data
                )
            )

            alert_routing_rules_permissions.append(alert_routing_rules_permissions_item)

        on_call_readiness_report_permissions = []
        _on_call_readiness_report_permissions = d.pop("on_call_readiness_report_permissions", UNSET)
        for on_call_readiness_report_permissions_item_data in _on_call_readiness_report_permissions or []:
            on_call_readiness_report_permissions_item = (
                check_new_on_call_role_data_attributes_on_call_readiness_report_permissions_item(
                    on_call_readiness_report_permissions_item_data
                )
            )

            on_call_readiness_report_permissions.append(on_call_readiness_report_permissions_item)

        on_call_roles_permissions = []
        _on_call_roles_permissions = d.pop("on_call_roles_permissions", UNSET)
        for on_call_roles_permissions_item_data in _on_call_roles_permissions or []:
            on_call_roles_permissions_item = check_new_on_call_role_data_attributes_on_call_roles_permissions_item(
                on_call_roles_permissions_item_data
            )

            on_call_roles_permissions.append(on_call_roles_permissions_item)

        alert_sources_permissions = []
        _alert_sources_permissions = d.pop("alert_sources_permissions", UNSET)
        for alert_sources_permissions_item_data in _alert_sources_permissions or []:
            alert_sources_permissions_item = check_new_on_call_role_data_attributes_alert_sources_permissions_item(
                alert_sources_permissions_item_data
            )

            alert_sources_permissions.append(alert_sources_permissions_item)

        alert_urgency_permissions = []
        _alert_urgency_permissions = d.pop("alert_urgency_permissions", UNSET)
        for alert_urgency_permissions_item_data in _alert_urgency_permissions or []:
            alert_urgency_permissions_item = check_new_on_call_role_data_attributes_alert_urgency_permissions_item(
                alert_urgency_permissions_item_data
            )

            alert_urgency_permissions.append(alert_urgency_permissions_item)

        alerts_permissions = []
        _alerts_permissions = d.pop("alerts_permissions", UNSET)
        for alerts_permissions_item_data in _alerts_permissions or []:
            alerts_permissions_item = check_new_on_call_role_data_attributes_alerts_permissions_item(
                alerts_permissions_item_data
            )

            alerts_permissions.append(alerts_permissions_item)

        api_keys_permissions = []
        _api_keys_permissions = d.pop("api_keys_permissions", UNSET)
        for api_keys_permissions_item_data in _api_keys_permissions or []:
            api_keys_permissions_item = check_new_on_call_role_data_attributes_api_keys_permissions_item(
                api_keys_permissions_item_data
            )

            api_keys_permissions.append(api_keys_permissions_item)

        audits_permissions = []
        _audits_permissions = d.pop("audits_permissions", UNSET)
        for audits_permissions_item_data in _audits_permissions or []:
            audits_permissions_item = check_new_on_call_role_data_attributes_audits_permissions_item(
                audits_permissions_item_data
            )

            audits_permissions.append(audits_permissions_item)

        contacts_permissions = []
        _contacts_permissions = d.pop("contacts_permissions", UNSET)
        for contacts_permissions_item_data in _contacts_permissions or []:
            contacts_permissions_item = check_new_on_call_role_data_attributes_contacts_permissions_item(
                contacts_permissions_item_data
            )

            contacts_permissions.append(contacts_permissions_item)

        escalation_policies_permissions = []
        _escalation_policies_permissions = d.pop("escalation_policies_permissions", UNSET)
        for escalation_policies_permissions_item_data in _escalation_policies_permissions or []:
            escalation_policies_permissions_item = (
                check_new_on_call_role_data_attributes_escalation_policies_permissions_item(
                    escalation_policies_permissions_item_data
                )
            )

            escalation_policies_permissions.append(escalation_policies_permissions_item)

        groups_permissions = []
        _groups_permissions = d.pop("groups_permissions", UNSET)
        for groups_permissions_item_data in _groups_permissions or []:
            groups_permissions_item = check_new_on_call_role_data_attributes_groups_permissions_item(
                groups_permissions_item_data
            )

            groups_permissions.append(groups_permissions_item)

        heartbeats_permissions = []
        _heartbeats_permissions = d.pop("heartbeats_permissions", UNSET)
        for heartbeats_permissions_item_data in _heartbeats_permissions or []:
            heartbeats_permissions_item = check_new_on_call_role_data_attributes_heartbeats_permissions_item(
                heartbeats_permissions_item_data
            )

            heartbeats_permissions.append(heartbeats_permissions_item)

        integrations_permissions = []
        _integrations_permissions = d.pop("integrations_permissions", UNSET)
        for integrations_permissions_item_data in _integrations_permissions or []:
            integrations_permissions_item = check_new_on_call_role_data_attributes_integrations_permissions_item(
                integrations_permissions_item_data
            )

            integrations_permissions.append(integrations_permissions_item)

        invitations_permissions = []
        _invitations_permissions = d.pop("invitations_permissions", UNSET)
        for invitations_permissions_item_data in _invitations_permissions or []:
            invitations_permissions_item = check_new_on_call_role_data_attributes_invitations_permissions_item(
                invitations_permissions_item_data
            )

            invitations_permissions.append(invitations_permissions_item)

        live_call_routing_permissions = []
        _live_call_routing_permissions = d.pop("live_call_routing_permissions", UNSET)
        for live_call_routing_permissions_item_data in _live_call_routing_permissions or []:
            live_call_routing_permissions_item = (
                check_new_on_call_role_data_attributes_live_call_routing_permissions_item(
                    live_call_routing_permissions_item_data
                )
            )

            live_call_routing_permissions.append(live_call_routing_permissions_item)

        schedule_override_permissions = []
        _schedule_override_permissions = d.pop("schedule_override_permissions", UNSET)
        for schedule_override_permissions_item_data in _schedule_override_permissions or []:
            schedule_override_permissions_item = (
                check_new_on_call_role_data_attributes_schedule_override_permissions_item(
                    schedule_override_permissions_item_data
                )
            )

            schedule_override_permissions.append(schedule_override_permissions_item)

        schedules_permissions = []
        _schedules_permissions = d.pop("schedules_permissions", UNSET)
        for schedules_permissions_item_data in _schedules_permissions or []:
            schedules_permissions_item = check_new_on_call_role_data_attributes_schedules_permissions_item(
                schedules_permissions_item_data
            )

            schedules_permissions.append(schedules_permissions_item)

        services_permissions = []
        _services_permissions = d.pop("services_permissions", UNSET)
        for services_permissions_item_data in _services_permissions or []:
            services_permissions_item = check_new_on_call_role_data_attributes_services_permissions_item(
                services_permissions_item_data
            )

            services_permissions.append(services_permissions_item)

        webhooks_permissions = []
        _webhooks_permissions = d.pop("webhooks_permissions", UNSET)
        for webhooks_permissions_item_data in _webhooks_permissions or []:
            webhooks_permissions_item = check_new_on_call_role_data_attributes_webhooks_permissions_item(
                webhooks_permissions_item_data
            )

            webhooks_permissions.append(webhooks_permissions_item)

        workflows_permissions = []
        _workflows_permissions = d.pop("workflows_permissions", UNSET)
        for workflows_permissions_item_data in _workflows_permissions or []:
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
