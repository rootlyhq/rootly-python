from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_role_data_attributes_alerts_permissions_item import (
    NewRoleDataAttributesAlertsPermissionsItem,
    check_new_role_data_attributes_alerts_permissions_item,
)
from ..models.new_role_data_attributes_api_keys_permissions_item import (
    NewRoleDataAttributesApiKeysPermissionsItem,
    check_new_role_data_attributes_api_keys_permissions_item,
)
from ..models.new_role_data_attributes_audits_permissions_item import (
    NewRoleDataAttributesAuditsPermissionsItem,
    check_new_role_data_attributes_audits_permissions_item,
)
from ..models.new_role_data_attributes_billing_permissions_item import (
    NewRoleDataAttributesBillingPermissionsItem,
    check_new_role_data_attributes_billing_permissions_item,
)
from ..models.new_role_data_attributes_catalogs_permissions_item import (
    NewRoleDataAttributesCatalogsPermissionsItem,
    check_new_role_data_attributes_catalogs_permissions_item,
)
from ..models.new_role_data_attributes_communication_permissions_item import (
    NewRoleDataAttributesCommunicationPermissionsItem,
    check_new_role_data_attributes_communication_permissions_item,
)
from ..models.new_role_data_attributes_edge_connector_permissions_item import (
    NewRoleDataAttributesEdgeConnectorPermissionsItem,
    check_new_role_data_attributes_edge_connector_permissions_item,
)
from ..models.new_role_data_attributes_environments_permissions_item import (
    NewRoleDataAttributesEnvironmentsPermissionsItem,
    check_new_role_data_attributes_environments_permissions_item,
)
from ..models.new_role_data_attributes_form_fields_permissions_item import (
    NewRoleDataAttributesFormFieldsPermissionsItem,
    check_new_role_data_attributes_form_fields_permissions_item,
)
from ..models.new_role_data_attributes_functionalities_permissions_item import (
    NewRoleDataAttributesFunctionalitiesPermissionsItem,
    check_new_role_data_attributes_functionalities_permissions_item,
)
from ..models.new_role_data_attributes_groups_permissions_item import (
    NewRoleDataAttributesGroupsPermissionsItem,
    check_new_role_data_attributes_groups_permissions_item,
)
from ..models.new_role_data_attributes_incident_causes_permissions_item import (
    NewRoleDataAttributesIncidentCausesPermissionsItem,
    check_new_role_data_attributes_incident_causes_permissions_item,
)
from ..models.new_role_data_attributes_incident_communication_permissions_item import (
    NewRoleDataAttributesIncidentCommunicationPermissionsItem,
    check_new_role_data_attributes_incident_communication_permissions_item,
)
from ..models.new_role_data_attributes_incident_feedbacks_permissions_item import (
    NewRoleDataAttributesIncidentFeedbacksPermissionsItem,
    check_new_role_data_attributes_incident_feedbacks_permissions_item,
)
from ..models.new_role_data_attributes_incident_roles_permissions_item import (
    NewRoleDataAttributesIncidentRolesPermissionsItem,
    check_new_role_data_attributes_incident_roles_permissions_item,
)
from ..models.new_role_data_attributes_incident_types_permissions_item import (
    NewRoleDataAttributesIncidentTypesPermissionsItem,
    check_new_role_data_attributes_incident_types_permissions_item,
)
from ..models.new_role_data_attributes_incidents_permissions_item import (
    NewRoleDataAttributesIncidentsPermissionsItem,
    check_new_role_data_attributes_incidents_permissions_item,
)
from ..models.new_role_data_attributes_integrations_permissions_item import (
    NewRoleDataAttributesIntegrationsPermissionsItem,
    check_new_role_data_attributes_integrations_permissions_item,
)
from ..models.new_role_data_attributes_invitations_permissions_item import (
    NewRoleDataAttributesInvitationsPermissionsItem,
    check_new_role_data_attributes_invitations_permissions_item,
)
from ..models.new_role_data_attributes_paging_permissions_item import (
    NewRoleDataAttributesPagingPermissionsItem,
    check_new_role_data_attributes_paging_permissions_item,
)
from ..models.new_role_data_attributes_playbooks_permissions_item import (
    NewRoleDataAttributesPlaybooksPermissionsItem,
    check_new_role_data_attributes_playbooks_permissions_item,
)
from ..models.new_role_data_attributes_private_incidents_permissions_item import (
    NewRoleDataAttributesPrivateIncidentsPermissionsItem,
    check_new_role_data_attributes_private_incidents_permissions_item,
)
from ..models.new_role_data_attributes_pulses_permissions_item import (
    NewRoleDataAttributesPulsesPermissionsItem,
    check_new_role_data_attributes_pulses_permissions_item,
)
from ..models.new_role_data_attributes_retrospective_permissions_item import (
    NewRoleDataAttributesRetrospectivePermissionsItem,
    check_new_role_data_attributes_retrospective_permissions_item,
)
from ..models.new_role_data_attributes_roles_permissions_item import (
    NewRoleDataAttributesRolesPermissionsItem,
    check_new_role_data_attributes_roles_permissions_item,
)
from ..models.new_role_data_attributes_secrets_permissions_item import (
    NewRoleDataAttributesSecretsPermissionsItem,
    check_new_role_data_attributes_secrets_permissions_item,
)
from ..models.new_role_data_attributes_services_permissions_item import (
    NewRoleDataAttributesServicesPermissionsItem,
    check_new_role_data_attributes_services_permissions_item,
)
from ..models.new_role_data_attributes_severities_permissions_item import (
    NewRoleDataAttributesSeveritiesPermissionsItem,
    check_new_role_data_attributes_severities_permissions_item,
)
from ..models.new_role_data_attributes_slas_permissions_item import (
    NewRoleDataAttributesSlasPermissionsItem,
    check_new_role_data_attributes_slas_permissions_item,
)
from ..models.new_role_data_attributes_status_pages_permissions_item import (
    NewRoleDataAttributesStatusPagesPermissionsItem,
    check_new_role_data_attributes_status_pages_permissions_item,
)
from ..models.new_role_data_attributes_sub_statuses_permissions_item import (
    NewRoleDataAttributesSubStatusesPermissionsItem,
    check_new_role_data_attributes_sub_statuses_permissions_item,
)
from ..models.new_role_data_attributes_webhooks_permissions_item import (
    NewRoleDataAttributesWebhooksPermissionsItem,
    check_new_role_data_attributes_webhooks_permissions_item,
)
from ..models.new_role_data_attributes_workflows_permissions_item import (
    NewRoleDataAttributesWorkflowsPermissionsItem,
    check_new_role_data_attributes_workflows_permissions_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewRoleDataAttributes")


@_attrs_define
class NewRoleDataAttributes:
    """
    Attributes:
        name (str): The role name.
        incident_permission_set_id (None | str | Unset): Associated incident permissions set.
        alerts_permissions (list[NewRoleDataAttributesAlertsPermissionsItem] | Unset):
        api_keys_permissions (list[NewRoleDataAttributesApiKeysPermissionsItem] | Unset):
        audits_permissions (list[NewRoleDataAttributesAuditsPermissionsItem] | Unset):
        billing_permissions (list[NewRoleDataAttributesBillingPermissionsItem] | Unset):
        environments_permissions (list[NewRoleDataAttributesEnvironmentsPermissionsItem] | Unset):
        form_fields_permissions (list[NewRoleDataAttributesFormFieldsPermissionsItem] | Unset):
        functionalities_permissions (list[NewRoleDataAttributesFunctionalitiesPermissionsItem] | Unset):
        groups_permissions (list[NewRoleDataAttributesGroupsPermissionsItem] | Unset):
        incident_causes_permissions (list[NewRoleDataAttributesIncidentCausesPermissionsItem] | Unset):
        incident_feedbacks_permissions (list[NewRoleDataAttributesIncidentFeedbacksPermissionsItem] | Unset):
        incident_roles_permissions (list[NewRoleDataAttributesIncidentRolesPermissionsItem] | Unset):
        incident_types_permissions (list[NewRoleDataAttributesIncidentTypesPermissionsItem] | Unset):
        incidents_permissions (list[NewRoleDataAttributesIncidentsPermissionsItem] | Unset):
        integrations_permissions (list[NewRoleDataAttributesIntegrationsPermissionsItem] | Unset):
        invitations_permissions (list[NewRoleDataAttributesInvitationsPermissionsItem] | Unset):
        playbooks_permissions (list[NewRoleDataAttributesPlaybooksPermissionsItem] | Unset):
        private_incidents_permissions (list[NewRoleDataAttributesPrivateIncidentsPermissionsItem] | Unset):
        pulses_permissions (list[NewRoleDataAttributesPulsesPermissionsItem] | Unset):
        retrospective_permissions (list[NewRoleDataAttributesRetrospectivePermissionsItem] | Unset):
        roles_permissions (list[NewRoleDataAttributesRolesPermissionsItem] | Unset):
        secrets_permissions (list[NewRoleDataAttributesSecretsPermissionsItem] | Unset):
        services_permissions (list[NewRoleDataAttributesServicesPermissionsItem] | Unset):
        severities_permissions (list[NewRoleDataAttributesSeveritiesPermissionsItem] | Unset):
        status_pages_permissions (list[NewRoleDataAttributesStatusPagesPermissionsItem] | Unset):
        webhooks_permissions (list[NewRoleDataAttributesWebhooksPermissionsItem] | Unset):
        workflows_permissions (list[NewRoleDataAttributesWorkflowsPermissionsItem] | Unset):
        catalogs_permissions (list[NewRoleDataAttributesCatalogsPermissionsItem] | Unset):
        sub_statuses_permissions (list[NewRoleDataAttributesSubStatusesPermissionsItem] | Unset):
        edge_connector_permissions (list[NewRoleDataAttributesEdgeConnectorPermissionsItem] | Unset):
        slas_permissions (list[NewRoleDataAttributesSlasPermissionsItem] | Unset):
        paging_permissions (list[NewRoleDataAttributesPagingPermissionsItem] | Unset):
        incident_communication_permissions (list[NewRoleDataAttributesIncidentCommunicationPermissionsItem] | Unset):
        communication_permissions (list[NewRoleDataAttributesCommunicationPermissionsItem] | Unset):
    """

    name: str
    incident_permission_set_id: None | str | Unset = UNSET
    alerts_permissions: list[NewRoleDataAttributesAlertsPermissionsItem] | Unset = UNSET
    api_keys_permissions: list[NewRoleDataAttributesApiKeysPermissionsItem] | Unset = UNSET
    audits_permissions: list[NewRoleDataAttributesAuditsPermissionsItem] | Unset = UNSET
    billing_permissions: list[NewRoleDataAttributesBillingPermissionsItem] | Unset = UNSET
    environments_permissions: list[NewRoleDataAttributesEnvironmentsPermissionsItem] | Unset = UNSET
    form_fields_permissions: list[NewRoleDataAttributesFormFieldsPermissionsItem] | Unset = UNSET
    functionalities_permissions: list[NewRoleDataAttributesFunctionalitiesPermissionsItem] | Unset = UNSET
    groups_permissions: list[NewRoleDataAttributesGroupsPermissionsItem] | Unset = UNSET
    incident_causes_permissions: list[NewRoleDataAttributesIncidentCausesPermissionsItem] | Unset = UNSET
    incident_feedbacks_permissions: list[NewRoleDataAttributesIncidentFeedbacksPermissionsItem] | Unset = UNSET
    incident_roles_permissions: list[NewRoleDataAttributesIncidentRolesPermissionsItem] | Unset = UNSET
    incident_types_permissions: list[NewRoleDataAttributesIncidentTypesPermissionsItem] | Unset = UNSET
    incidents_permissions: list[NewRoleDataAttributesIncidentsPermissionsItem] | Unset = UNSET
    integrations_permissions: list[NewRoleDataAttributesIntegrationsPermissionsItem] | Unset = UNSET
    invitations_permissions: list[NewRoleDataAttributesInvitationsPermissionsItem] | Unset = UNSET
    playbooks_permissions: list[NewRoleDataAttributesPlaybooksPermissionsItem] | Unset = UNSET
    private_incidents_permissions: list[NewRoleDataAttributesPrivateIncidentsPermissionsItem] | Unset = UNSET
    pulses_permissions: list[NewRoleDataAttributesPulsesPermissionsItem] | Unset = UNSET
    retrospective_permissions: list[NewRoleDataAttributesRetrospectivePermissionsItem] | Unset = UNSET
    roles_permissions: list[NewRoleDataAttributesRolesPermissionsItem] | Unset = UNSET
    secrets_permissions: list[NewRoleDataAttributesSecretsPermissionsItem] | Unset = UNSET
    services_permissions: list[NewRoleDataAttributesServicesPermissionsItem] | Unset = UNSET
    severities_permissions: list[NewRoleDataAttributesSeveritiesPermissionsItem] | Unset = UNSET
    status_pages_permissions: list[NewRoleDataAttributesStatusPagesPermissionsItem] | Unset = UNSET
    webhooks_permissions: list[NewRoleDataAttributesWebhooksPermissionsItem] | Unset = UNSET
    workflows_permissions: list[NewRoleDataAttributesWorkflowsPermissionsItem] | Unset = UNSET
    catalogs_permissions: list[NewRoleDataAttributesCatalogsPermissionsItem] | Unset = UNSET
    sub_statuses_permissions: list[NewRoleDataAttributesSubStatusesPermissionsItem] | Unset = UNSET
    edge_connector_permissions: list[NewRoleDataAttributesEdgeConnectorPermissionsItem] | Unset = UNSET
    slas_permissions: list[NewRoleDataAttributesSlasPermissionsItem] | Unset = UNSET
    paging_permissions: list[NewRoleDataAttributesPagingPermissionsItem] | Unset = UNSET
    incident_communication_permissions: list[NewRoleDataAttributesIncidentCommunicationPermissionsItem] | Unset = UNSET
    communication_permissions: list[NewRoleDataAttributesCommunicationPermissionsItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        incident_permission_set_id: None | str | Unset
        if isinstance(self.incident_permission_set_id, Unset):
            incident_permission_set_id = UNSET
        else:
            incident_permission_set_id = self.incident_permission_set_id

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

        billing_permissions: list[str] | Unset = UNSET
        if not isinstance(self.billing_permissions, Unset):
            billing_permissions = []
            for billing_permissions_item_data in self.billing_permissions:
                billing_permissions_item: str = billing_permissions_item_data
                billing_permissions.append(billing_permissions_item)

        environments_permissions: list[str] | Unset = UNSET
        if not isinstance(self.environments_permissions, Unset):
            environments_permissions = []
            for environments_permissions_item_data in self.environments_permissions:
                environments_permissions_item: str = environments_permissions_item_data
                environments_permissions.append(environments_permissions_item)

        form_fields_permissions: list[str] | Unset = UNSET
        if not isinstance(self.form_fields_permissions, Unset):
            form_fields_permissions = []
            for form_fields_permissions_item_data in self.form_fields_permissions:
                form_fields_permissions_item: str = form_fields_permissions_item_data
                form_fields_permissions.append(form_fields_permissions_item)

        functionalities_permissions: list[str] | Unset = UNSET
        if not isinstance(self.functionalities_permissions, Unset):
            functionalities_permissions = []
            for functionalities_permissions_item_data in self.functionalities_permissions:
                functionalities_permissions_item: str = functionalities_permissions_item_data
                functionalities_permissions.append(functionalities_permissions_item)

        groups_permissions: list[str] | Unset = UNSET
        if not isinstance(self.groups_permissions, Unset):
            groups_permissions = []
            for groups_permissions_item_data in self.groups_permissions:
                groups_permissions_item: str = groups_permissions_item_data
                groups_permissions.append(groups_permissions_item)

        incident_causes_permissions: list[str] | Unset = UNSET
        if not isinstance(self.incident_causes_permissions, Unset):
            incident_causes_permissions = []
            for incident_causes_permissions_item_data in self.incident_causes_permissions:
                incident_causes_permissions_item: str = incident_causes_permissions_item_data
                incident_causes_permissions.append(incident_causes_permissions_item)

        incident_feedbacks_permissions: list[str] | Unset = UNSET
        if not isinstance(self.incident_feedbacks_permissions, Unset):
            incident_feedbacks_permissions = []
            for incident_feedbacks_permissions_item_data in self.incident_feedbacks_permissions:
                incident_feedbacks_permissions_item: str = incident_feedbacks_permissions_item_data
                incident_feedbacks_permissions.append(incident_feedbacks_permissions_item)

        incident_roles_permissions: list[str] | Unset = UNSET
        if not isinstance(self.incident_roles_permissions, Unset):
            incident_roles_permissions = []
            for incident_roles_permissions_item_data in self.incident_roles_permissions:
                incident_roles_permissions_item: str = incident_roles_permissions_item_data
                incident_roles_permissions.append(incident_roles_permissions_item)

        incident_types_permissions: list[str] | Unset = UNSET
        if not isinstance(self.incident_types_permissions, Unset):
            incident_types_permissions = []
            for incident_types_permissions_item_data in self.incident_types_permissions:
                incident_types_permissions_item: str = incident_types_permissions_item_data
                incident_types_permissions.append(incident_types_permissions_item)

        incidents_permissions: list[str] | Unset = UNSET
        if not isinstance(self.incidents_permissions, Unset):
            incidents_permissions = []
            for incidents_permissions_item_data in self.incidents_permissions:
                incidents_permissions_item: str = incidents_permissions_item_data
                incidents_permissions.append(incidents_permissions_item)

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

        playbooks_permissions: list[str] | Unset = UNSET
        if not isinstance(self.playbooks_permissions, Unset):
            playbooks_permissions = []
            for playbooks_permissions_item_data in self.playbooks_permissions:
                playbooks_permissions_item: str = playbooks_permissions_item_data
                playbooks_permissions.append(playbooks_permissions_item)

        private_incidents_permissions: list[str] | Unset = UNSET
        if not isinstance(self.private_incidents_permissions, Unset):
            private_incidents_permissions = []
            for private_incidents_permissions_item_data in self.private_incidents_permissions:
                private_incidents_permissions_item: str = private_incidents_permissions_item_data
                private_incidents_permissions.append(private_incidents_permissions_item)

        pulses_permissions: list[str] | Unset = UNSET
        if not isinstance(self.pulses_permissions, Unset):
            pulses_permissions = []
            for pulses_permissions_item_data in self.pulses_permissions:
                pulses_permissions_item: str = pulses_permissions_item_data
                pulses_permissions.append(pulses_permissions_item)

        retrospective_permissions: list[str] | Unset = UNSET
        if not isinstance(self.retrospective_permissions, Unset):
            retrospective_permissions = []
            for retrospective_permissions_item_data in self.retrospective_permissions:
                retrospective_permissions_item: str = retrospective_permissions_item_data
                retrospective_permissions.append(retrospective_permissions_item)

        roles_permissions: list[str] | Unset = UNSET
        if not isinstance(self.roles_permissions, Unset):
            roles_permissions = []
            for roles_permissions_item_data in self.roles_permissions:
                roles_permissions_item: str = roles_permissions_item_data
                roles_permissions.append(roles_permissions_item)

        secrets_permissions: list[str] | Unset = UNSET
        if not isinstance(self.secrets_permissions, Unset):
            secrets_permissions = []
            for secrets_permissions_item_data in self.secrets_permissions:
                secrets_permissions_item: str = secrets_permissions_item_data
                secrets_permissions.append(secrets_permissions_item)

        services_permissions: list[str] | Unset = UNSET
        if not isinstance(self.services_permissions, Unset):
            services_permissions = []
            for services_permissions_item_data in self.services_permissions:
                services_permissions_item: str = services_permissions_item_data
                services_permissions.append(services_permissions_item)

        severities_permissions: list[str] | Unset = UNSET
        if not isinstance(self.severities_permissions, Unset):
            severities_permissions = []
            for severities_permissions_item_data in self.severities_permissions:
                severities_permissions_item: str = severities_permissions_item_data
                severities_permissions.append(severities_permissions_item)

        status_pages_permissions: list[str] | Unset = UNSET
        if not isinstance(self.status_pages_permissions, Unset):
            status_pages_permissions = []
            for status_pages_permissions_item_data in self.status_pages_permissions:
                status_pages_permissions_item: str = status_pages_permissions_item_data
                status_pages_permissions.append(status_pages_permissions_item)

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

        catalogs_permissions: list[str] | Unset = UNSET
        if not isinstance(self.catalogs_permissions, Unset):
            catalogs_permissions = []
            for catalogs_permissions_item_data in self.catalogs_permissions:
                catalogs_permissions_item: str = catalogs_permissions_item_data
                catalogs_permissions.append(catalogs_permissions_item)

        sub_statuses_permissions: list[str] | Unset = UNSET
        if not isinstance(self.sub_statuses_permissions, Unset):
            sub_statuses_permissions = []
            for sub_statuses_permissions_item_data in self.sub_statuses_permissions:
                sub_statuses_permissions_item: str = sub_statuses_permissions_item_data
                sub_statuses_permissions.append(sub_statuses_permissions_item)

        edge_connector_permissions: list[str] | Unset = UNSET
        if not isinstance(self.edge_connector_permissions, Unset):
            edge_connector_permissions = []
            for edge_connector_permissions_item_data in self.edge_connector_permissions:
                edge_connector_permissions_item: str = edge_connector_permissions_item_data
                edge_connector_permissions.append(edge_connector_permissions_item)

        slas_permissions: list[str] | Unset = UNSET
        if not isinstance(self.slas_permissions, Unset):
            slas_permissions = []
            for slas_permissions_item_data in self.slas_permissions:
                slas_permissions_item: str = slas_permissions_item_data
                slas_permissions.append(slas_permissions_item)

        paging_permissions: list[str] | Unset = UNSET
        if not isinstance(self.paging_permissions, Unset):
            paging_permissions = []
            for paging_permissions_item_data in self.paging_permissions:
                paging_permissions_item: str = paging_permissions_item_data
                paging_permissions.append(paging_permissions_item)

        incident_communication_permissions: list[str] | Unset = UNSET
        if not isinstance(self.incident_communication_permissions, Unset):
            incident_communication_permissions = []
            for incident_communication_permissions_item_data in self.incident_communication_permissions:
                incident_communication_permissions_item: str = incident_communication_permissions_item_data
                incident_communication_permissions.append(incident_communication_permissions_item)

        communication_permissions: list[str] | Unset = UNSET
        if not isinstance(self.communication_permissions, Unset):
            communication_permissions = []
            for communication_permissions_item_data in self.communication_permissions:
                communication_permissions_item: str = communication_permissions_item_data
                communication_permissions.append(communication_permissions_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if incident_permission_set_id is not UNSET:
            field_dict["incident_permission_set_id"] = incident_permission_set_id
        if alerts_permissions is not UNSET:
            field_dict["alerts_permissions"] = alerts_permissions
        if api_keys_permissions is not UNSET:
            field_dict["api_keys_permissions"] = api_keys_permissions
        if audits_permissions is not UNSET:
            field_dict["audits_permissions"] = audits_permissions
        if billing_permissions is not UNSET:
            field_dict["billing_permissions"] = billing_permissions
        if environments_permissions is not UNSET:
            field_dict["environments_permissions"] = environments_permissions
        if form_fields_permissions is not UNSET:
            field_dict["form_fields_permissions"] = form_fields_permissions
        if functionalities_permissions is not UNSET:
            field_dict["functionalities_permissions"] = functionalities_permissions
        if groups_permissions is not UNSET:
            field_dict["groups_permissions"] = groups_permissions
        if incident_causes_permissions is not UNSET:
            field_dict["incident_causes_permissions"] = incident_causes_permissions
        if incident_feedbacks_permissions is not UNSET:
            field_dict["incident_feedbacks_permissions"] = incident_feedbacks_permissions
        if incident_roles_permissions is not UNSET:
            field_dict["incident_roles_permissions"] = incident_roles_permissions
        if incident_types_permissions is not UNSET:
            field_dict["incident_types_permissions"] = incident_types_permissions
        if incidents_permissions is not UNSET:
            field_dict["incidents_permissions"] = incidents_permissions
        if integrations_permissions is not UNSET:
            field_dict["integrations_permissions"] = integrations_permissions
        if invitations_permissions is not UNSET:
            field_dict["invitations_permissions"] = invitations_permissions
        if playbooks_permissions is not UNSET:
            field_dict["playbooks_permissions"] = playbooks_permissions
        if private_incidents_permissions is not UNSET:
            field_dict["private_incidents_permissions"] = private_incidents_permissions
        if pulses_permissions is not UNSET:
            field_dict["pulses_permissions"] = pulses_permissions
        if retrospective_permissions is not UNSET:
            field_dict["retrospective_permissions"] = retrospective_permissions
        if roles_permissions is not UNSET:
            field_dict["roles_permissions"] = roles_permissions
        if secrets_permissions is not UNSET:
            field_dict["secrets_permissions"] = secrets_permissions
        if services_permissions is not UNSET:
            field_dict["services_permissions"] = services_permissions
        if severities_permissions is not UNSET:
            field_dict["severities_permissions"] = severities_permissions
        if status_pages_permissions is not UNSET:
            field_dict["status_pages_permissions"] = status_pages_permissions
        if webhooks_permissions is not UNSET:
            field_dict["webhooks_permissions"] = webhooks_permissions
        if workflows_permissions is not UNSET:
            field_dict["workflows_permissions"] = workflows_permissions
        if catalogs_permissions is not UNSET:
            field_dict["catalogs_permissions"] = catalogs_permissions
        if sub_statuses_permissions is not UNSET:
            field_dict["sub_statuses_permissions"] = sub_statuses_permissions
        if edge_connector_permissions is not UNSET:
            field_dict["edge_connector_permissions"] = edge_connector_permissions
        if slas_permissions is not UNSET:
            field_dict["slas_permissions"] = slas_permissions
        if paging_permissions is not UNSET:
            field_dict["paging_permissions"] = paging_permissions
        if incident_communication_permissions is not UNSET:
            field_dict["incident_communication_permissions"] = incident_communication_permissions
        if communication_permissions is not UNSET:
            field_dict["communication_permissions"] = communication_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_incident_permission_set_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        incident_permission_set_id = _parse_incident_permission_set_id(d.pop("incident_permission_set_id", UNSET))

        _alerts_permissions = d.pop("alerts_permissions", UNSET)
        alerts_permissions: list[NewRoleDataAttributesAlertsPermissionsItem] | Unset = UNSET
        if _alerts_permissions is not UNSET:
            alerts_permissions = []
            for alerts_permissions_item_data in _alerts_permissions:
                alerts_permissions_item = check_new_role_data_attributes_alerts_permissions_item(
                    alerts_permissions_item_data
                )

                alerts_permissions.append(alerts_permissions_item)

        _api_keys_permissions = d.pop("api_keys_permissions", UNSET)
        api_keys_permissions: list[NewRoleDataAttributesApiKeysPermissionsItem] | Unset = UNSET
        if _api_keys_permissions is not UNSET:
            api_keys_permissions = []
            for api_keys_permissions_item_data in _api_keys_permissions:
                api_keys_permissions_item = check_new_role_data_attributes_api_keys_permissions_item(
                    api_keys_permissions_item_data
                )

                api_keys_permissions.append(api_keys_permissions_item)

        _audits_permissions = d.pop("audits_permissions", UNSET)
        audits_permissions: list[NewRoleDataAttributesAuditsPermissionsItem] | Unset = UNSET
        if _audits_permissions is not UNSET:
            audits_permissions = []
            for audits_permissions_item_data in _audits_permissions:
                audits_permissions_item = check_new_role_data_attributes_audits_permissions_item(
                    audits_permissions_item_data
                )

                audits_permissions.append(audits_permissions_item)

        _billing_permissions = d.pop("billing_permissions", UNSET)
        billing_permissions: list[NewRoleDataAttributesBillingPermissionsItem] | Unset = UNSET
        if _billing_permissions is not UNSET:
            billing_permissions = []
            for billing_permissions_item_data in _billing_permissions:
                billing_permissions_item = check_new_role_data_attributes_billing_permissions_item(
                    billing_permissions_item_data
                )

                billing_permissions.append(billing_permissions_item)

        _environments_permissions = d.pop("environments_permissions", UNSET)
        environments_permissions: list[NewRoleDataAttributesEnvironmentsPermissionsItem] | Unset = UNSET
        if _environments_permissions is not UNSET:
            environments_permissions = []
            for environments_permissions_item_data in _environments_permissions:
                environments_permissions_item = check_new_role_data_attributes_environments_permissions_item(
                    environments_permissions_item_data
                )

                environments_permissions.append(environments_permissions_item)

        _form_fields_permissions = d.pop("form_fields_permissions", UNSET)
        form_fields_permissions: list[NewRoleDataAttributesFormFieldsPermissionsItem] | Unset = UNSET
        if _form_fields_permissions is not UNSET:
            form_fields_permissions = []
            for form_fields_permissions_item_data in _form_fields_permissions:
                form_fields_permissions_item = check_new_role_data_attributes_form_fields_permissions_item(
                    form_fields_permissions_item_data
                )

                form_fields_permissions.append(form_fields_permissions_item)

        _functionalities_permissions = d.pop("functionalities_permissions", UNSET)
        functionalities_permissions: list[NewRoleDataAttributesFunctionalitiesPermissionsItem] | Unset = UNSET
        if _functionalities_permissions is not UNSET:
            functionalities_permissions = []
            for functionalities_permissions_item_data in _functionalities_permissions:
                functionalities_permissions_item = check_new_role_data_attributes_functionalities_permissions_item(
                    functionalities_permissions_item_data
                )

                functionalities_permissions.append(functionalities_permissions_item)

        _groups_permissions = d.pop("groups_permissions", UNSET)
        groups_permissions: list[NewRoleDataAttributesGroupsPermissionsItem] | Unset = UNSET
        if _groups_permissions is not UNSET:
            groups_permissions = []
            for groups_permissions_item_data in _groups_permissions:
                groups_permissions_item = check_new_role_data_attributes_groups_permissions_item(
                    groups_permissions_item_data
                )

                groups_permissions.append(groups_permissions_item)

        _incident_causes_permissions = d.pop("incident_causes_permissions", UNSET)
        incident_causes_permissions: list[NewRoleDataAttributesIncidentCausesPermissionsItem] | Unset = UNSET
        if _incident_causes_permissions is not UNSET:
            incident_causes_permissions = []
            for incident_causes_permissions_item_data in _incident_causes_permissions:
                incident_causes_permissions_item = check_new_role_data_attributes_incident_causes_permissions_item(
                    incident_causes_permissions_item_data
                )

                incident_causes_permissions.append(incident_causes_permissions_item)

        _incident_feedbacks_permissions = d.pop("incident_feedbacks_permissions", UNSET)
        incident_feedbacks_permissions: list[NewRoleDataAttributesIncidentFeedbacksPermissionsItem] | Unset = UNSET
        if _incident_feedbacks_permissions is not UNSET:
            incident_feedbacks_permissions = []
            for incident_feedbacks_permissions_item_data in _incident_feedbacks_permissions:
                incident_feedbacks_permissions_item = (
                    check_new_role_data_attributes_incident_feedbacks_permissions_item(
                        incident_feedbacks_permissions_item_data
                    )
                )

                incident_feedbacks_permissions.append(incident_feedbacks_permissions_item)

        _incident_roles_permissions = d.pop("incident_roles_permissions", UNSET)
        incident_roles_permissions: list[NewRoleDataAttributesIncidentRolesPermissionsItem] | Unset = UNSET
        if _incident_roles_permissions is not UNSET:
            incident_roles_permissions = []
            for incident_roles_permissions_item_data in _incident_roles_permissions:
                incident_roles_permissions_item = check_new_role_data_attributes_incident_roles_permissions_item(
                    incident_roles_permissions_item_data
                )

                incident_roles_permissions.append(incident_roles_permissions_item)

        _incident_types_permissions = d.pop("incident_types_permissions", UNSET)
        incident_types_permissions: list[NewRoleDataAttributesIncidentTypesPermissionsItem] | Unset = UNSET
        if _incident_types_permissions is not UNSET:
            incident_types_permissions = []
            for incident_types_permissions_item_data in _incident_types_permissions:
                incident_types_permissions_item = check_new_role_data_attributes_incident_types_permissions_item(
                    incident_types_permissions_item_data
                )

                incident_types_permissions.append(incident_types_permissions_item)

        _incidents_permissions = d.pop("incidents_permissions", UNSET)
        incidents_permissions: list[NewRoleDataAttributesIncidentsPermissionsItem] | Unset = UNSET
        if _incidents_permissions is not UNSET:
            incidents_permissions = []
            for incidents_permissions_item_data in _incidents_permissions:
                incidents_permissions_item = check_new_role_data_attributes_incidents_permissions_item(
                    incidents_permissions_item_data
                )

                incidents_permissions.append(incidents_permissions_item)

        _integrations_permissions = d.pop("integrations_permissions", UNSET)
        integrations_permissions: list[NewRoleDataAttributesIntegrationsPermissionsItem] | Unset = UNSET
        if _integrations_permissions is not UNSET:
            integrations_permissions = []
            for integrations_permissions_item_data in _integrations_permissions:
                integrations_permissions_item = check_new_role_data_attributes_integrations_permissions_item(
                    integrations_permissions_item_data
                )

                integrations_permissions.append(integrations_permissions_item)

        _invitations_permissions = d.pop("invitations_permissions", UNSET)
        invitations_permissions: list[NewRoleDataAttributesInvitationsPermissionsItem] | Unset = UNSET
        if _invitations_permissions is not UNSET:
            invitations_permissions = []
            for invitations_permissions_item_data in _invitations_permissions:
                invitations_permissions_item = check_new_role_data_attributes_invitations_permissions_item(
                    invitations_permissions_item_data
                )

                invitations_permissions.append(invitations_permissions_item)

        _playbooks_permissions = d.pop("playbooks_permissions", UNSET)
        playbooks_permissions: list[NewRoleDataAttributesPlaybooksPermissionsItem] | Unset = UNSET
        if _playbooks_permissions is not UNSET:
            playbooks_permissions = []
            for playbooks_permissions_item_data in _playbooks_permissions:
                playbooks_permissions_item = check_new_role_data_attributes_playbooks_permissions_item(
                    playbooks_permissions_item_data
                )

                playbooks_permissions.append(playbooks_permissions_item)

        _private_incidents_permissions = d.pop("private_incidents_permissions", UNSET)
        private_incidents_permissions: list[NewRoleDataAttributesPrivateIncidentsPermissionsItem] | Unset = UNSET
        if _private_incidents_permissions is not UNSET:
            private_incidents_permissions = []
            for private_incidents_permissions_item_data in _private_incidents_permissions:
                private_incidents_permissions_item = check_new_role_data_attributes_private_incidents_permissions_item(
                    private_incidents_permissions_item_data
                )

                private_incidents_permissions.append(private_incidents_permissions_item)

        _pulses_permissions = d.pop("pulses_permissions", UNSET)
        pulses_permissions: list[NewRoleDataAttributesPulsesPermissionsItem] | Unset = UNSET
        if _pulses_permissions is not UNSET:
            pulses_permissions = []
            for pulses_permissions_item_data in _pulses_permissions:
                pulses_permissions_item = check_new_role_data_attributes_pulses_permissions_item(
                    pulses_permissions_item_data
                )

                pulses_permissions.append(pulses_permissions_item)

        _retrospective_permissions = d.pop("retrospective_permissions", UNSET)
        retrospective_permissions: list[NewRoleDataAttributesRetrospectivePermissionsItem] | Unset = UNSET
        if _retrospective_permissions is not UNSET:
            retrospective_permissions = []
            for retrospective_permissions_item_data in _retrospective_permissions:
                retrospective_permissions_item = check_new_role_data_attributes_retrospective_permissions_item(
                    retrospective_permissions_item_data
                )

                retrospective_permissions.append(retrospective_permissions_item)

        _roles_permissions = d.pop("roles_permissions", UNSET)
        roles_permissions: list[NewRoleDataAttributesRolesPermissionsItem] | Unset = UNSET
        if _roles_permissions is not UNSET:
            roles_permissions = []
            for roles_permissions_item_data in _roles_permissions:
                roles_permissions_item = check_new_role_data_attributes_roles_permissions_item(
                    roles_permissions_item_data
                )

                roles_permissions.append(roles_permissions_item)

        _secrets_permissions = d.pop("secrets_permissions", UNSET)
        secrets_permissions: list[NewRoleDataAttributesSecretsPermissionsItem] | Unset = UNSET
        if _secrets_permissions is not UNSET:
            secrets_permissions = []
            for secrets_permissions_item_data in _secrets_permissions:
                secrets_permissions_item = check_new_role_data_attributes_secrets_permissions_item(
                    secrets_permissions_item_data
                )

                secrets_permissions.append(secrets_permissions_item)

        _services_permissions = d.pop("services_permissions", UNSET)
        services_permissions: list[NewRoleDataAttributesServicesPermissionsItem] | Unset = UNSET
        if _services_permissions is not UNSET:
            services_permissions = []
            for services_permissions_item_data in _services_permissions:
                services_permissions_item = check_new_role_data_attributes_services_permissions_item(
                    services_permissions_item_data
                )

                services_permissions.append(services_permissions_item)

        _severities_permissions = d.pop("severities_permissions", UNSET)
        severities_permissions: list[NewRoleDataAttributesSeveritiesPermissionsItem] | Unset = UNSET
        if _severities_permissions is not UNSET:
            severities_permissions = []
            for severities_permissions_item_data in _severities_permissions:
                severities_permissions_item = check_new_role_data_attributes_severities_permissions_item(
                    severities_permissions_item_data
                )

                severities_permissions.append(severities_permissions_item)

        _status_pages_permissions = d.pop("status_pages_permissions", UNSET)
        status_pages_permissions: list[NewRoleDataAttributesStatusPagesPermissionsItem] | Unset = UNSET
        if _status_pages_permissions is not UNSET:
            status_pages_permissions = []
            for status_pages_permissions_item_data in _status_pages_permissions:
                status_pages_permissions_item = check_new_role_data_attributes_status_pages_permissions_item(
                    status_pages_permissions_item_data
                )

                status_pages_permissions.append(status_pages_permissions_item)

        _webhooks_permissions = d.pop("webhooks_permissions", UNSET)
        webhooks_permissions: list[NewRoleDataAttributesWebhooksPermissionsItem] | Unset = UNSET
        if _webhooks_permissions is not UNSET:
            webhooks_permissions = []
            for webhooks_permissions_item_data in _webhooks_permissions:
                webhooks_permissions_item = check_new_role_data_attributes_webhooks_permissions_item(
                    webhooks_permissions_item_data
                )

                webhooks_permissions.append(webhooks_permissions_item)

        _workflows_permissions = d.pop("workflows_permissions", UNSET)
        workflows_permissions: list[NewRoleDataAttributesWorkflowsPermissionsItem] | Unset = UNSET
        if _workflows_permissions is not UNSET:
            workflows_permissions = []
            for workflows_permissions_item_data in _workflows_permissions:
                workflows_permissions_item = check_new_role_data_attributes_workflows_permissions_item(
                    workflows_permissions_item_data
                )

                workflows_permissions.append(workflows_permissions_item)

        _catalogs_permissions = d.pop("catalogs_permissions", UNSET)
        catalogs_permissions: list[NewRoleDataAttributesCatalogsPermissionsItem] | Unset = UNSET
        if _catalogs_permissions is not UNSET:
            catalogs_permissions = []
            for catalogs_permissions_item_data in _catalogs_permissions:
                catalogs_permissions_item = check_new_role_data_attributes_catalogs_permissions_item(
                    catalogs_permissions_item_data
                )

                catalogs_permissions.append(catalogs_permissions_item)

        _sub_statuses_permissions = d.pop("sub_statuses_permissions", UNSET)
        sub_statuses_permissions: list[NewRoleDataAttributesSubStatusesPermissionsItem] | Unset = UNSET
        if _sub_statuses_permissions is not UNSET:
            sub_statuses_permissions = []
            for sub_statuses_permissions_item_data in _sub_statuses_permissions:
                sub_statuses_permissions_item = check_new_role_data_attributes_sub_statuses_permissions_item(
                    sub_statuses_permissions_item_data
                )

                sub_statuses_permissions.append(sub_statuses_permissions_item)

        _edge_connector_permissions = d.pop("edge_connector_permissions", UNSET)
        edge_connector_permissions: list[NewRoleDataAttributesEdgeConnectorPermissionsItem] | Unset = UNSET
        if _edge_connector_permissions is not UNSET:
            edge_connector_permissions = []
            for edge_connector_permissions_item_data in _edge_connector_permissions:
                edge_connector_permissions_item = check_new_role_data_attributes_edge_connector_permissions_item(
                    edge_connector_permissions_item_data
                )

                edge_connector_permissions.append(edge_connector_permissions_item)

        _slas_permissions = d.pop("slas_permissions", UNSET)
        slas_permissions: list[NewRoleDataAttributesSlasPermissionsItem] | Unset = UNSET
        if _slas_permissions is not UNSET:
            slas_permissions = []
            for slas_permissions_item_data in _slas_permissions:
                slas_permissions_item = check_new_role_data_attributes_slas_permissions_item(slas_permissions_item_data)

                slas_permissions.append(slas_permissions_item)

        _paging_permissions = d.pop("paging_permissions", UNSET)
        paging_permissions: list[NewRoleDataAttributesPagingPermissionsItem] | Unset = UNSET
        if _paging_permissions is not UNSET:
            paging_permissions = []
            for paging_permissions_item_data in _paging_permissions:
                paging_permissions_item = check_new_role_data_attributes_paging_permissions_item(
                    paging_permissions_item_data
                )

                paging_permissions.append(paging_permissions_item)

        _incident_communication_permissions = d.pop("incident_communication_permissions", UNSET)
        incident_communication_permissions: list[NewRoleDataAttributesIncidentCommunicationPermissionsItem] | Unset = (
            UNSET
        )
        if _incident_communication_permissions is not UNSET:
            incident_communication_permissions = []
            for incident_communication_permissions_item_data in _incident_communication_permissions:
                incident_communication_permissions_item = (
                    check_new_role_data_attributes_incident_communication_permissions_item(
                        incident_communication_permissions_item_data
                    )
                )

                incident_communication_permissions.append(incident_communication_permissions_item)

        _communication_permissions = d.pop("communication_permissions", UNSET)
        communication_permissions: list[NewRoleDataAttributesCommunicationPermissionsItem] | Unset = UNSET
        if _communication_permissions is not UNSET:
            communication_permissions = []
            for communication_permissions_item_data in _communication_permissions:
                communication_permissions_item = check_new_role_data_attributes_communication_permissions_item(
                    communication_permissions_item_data
                )

                communication_permissions.append(communication_permissions_item)

        new_role_data_attributes = cls(
            name=name,
            incident_permission_set_id=incident_permission_set_id,
            alerts_permissions=alerts_permissions,
            api_keys_permissions=api_keys_permissions,
            audits_permissions=audits_permissions,
            billing_permissions=billing_permissions,
            environments_permissions=environments_permissions,
            form_fields_permissions=form_fields_permissions,
            functionalities_permissions=functionalities_permissions,
            groups_permissions=groups_permissions,
            incident_causes_permissions=incident_causes_permissions,
            incident_feedbacks_permissions=incident_feedbacks_permissions,
            incident_roles_permissions=incident_roles_permissions,
            incident_types_permissions=incident_types_permissions,
            incidents_permissions=incidents_permissions,
            integrations_permissions=integrations_permissions,
            invitations_permissions=invitations_permissions,
            playbooks_permissions=playbooks_permissions,
            private_incidents_permissions=private_incidents_permissions,
            pulses_permissions=pulses_permissions,
            retrospective_permissions=retrospective_permissions,
            roles_permissions=roles_permissions,
            secrets_permissions=secrets_permissions,
            services_permissions=services_permissions,
            severities_permissions=severities_permissions,
            status_pages_permissions=status_pages_permissions,
            webhooks_permissions=webhooks_permissions,
            workflows_permissions=workflows_permissions,
            catalogs_permissions=catalogs_permissions,
            sub_statuses_permissions=sub_statuses_permissions,
            edge_connector_permissions=edge_connector_permissions,
            slas_permissions=slas_permissions,
            paging_permissions=paging_permissions,
            incident_communication_permissions=incident_communication_permissions,
            communication_permissions=communication_permissions,
        )

        return new_role_data_attributes
