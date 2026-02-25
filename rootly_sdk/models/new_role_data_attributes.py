from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

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
from ..models.new_role_data_attributes_status_pages_permissions_item import (
    NewRoleDataAttributesStatusPagesPermissionsItem,
    check_new_role_data_attributes_status_pages_permissions_item,
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
        incident_permission_set_id (Union[None, Unset, str]): Associated incident permissions set.
        alerts_permissions (Union[Unset, list[NewRoleDataAttributesAlertsPermissionsItem]]):
        api_keys_permissions (Union[Unset, list[NewRoleDataAttributesApiKeysPermissionsItem]]):
        audits_permissions (Union[Unset, list[NewRoleDataAttributesAuditsPermissionsItem]]):
        billing_permissions (Union[Unset, list[NewRoleDataAttributesBillingPermissionsItem]]):
        environments_permissions (Union[Unset, list[NewRoleDataAttributesEnvironmentsPermissionsItem]]):
        form_fields_permissions (Union[Unset, list[NewRoleDataAttributesFormFieldsPermissionsItem]]):
        functionalities_permissions (Union[Unset, list[NewRoleDataAttributesFunctionalitiesPermissionsItem]]):
        groups_permissions (Union[Unset, list[NewRoleDataAttributesGroupsPermissionsItem]]):
        incident_causes_permissions (Union[Unset, list[NewRoleDataAttributesIncidentCausesPermissionsItem]]):
        incident_feedbacks_permissions (Union[Unset, list[NewRoleDataAttributesIncidentFeedbacksPermissionsItem]]):
        incident_roles_permissions (Union[Unset, list[NewRoleDataAttributesIncidentRolesPermissionsItem]]):
        incident_types_permissions (Union[Unset, list[NewRoleDataAttributesIncidentTypesPermissionsItem]]):
        incidents_permissions (Union[Unset, list[NewRoleDataAttributesIncidentsPermissionsItem]]):
        integrations_permissions (Union[Unset, list[NewRoleDataAttributesIntegrationsPermissionsItem]]):
        invitations_permissions (Union[Unset, list[NewRoleDataAttributesInvitationsPermissionsItem]]):
        playbooks_permissions (Union[Unset, list[NewRoleDataAttributesPlaybooksPermissionsItem]]):
        private_incidents_permissions (Union[Unset, list[NewRoleDataAttributesPrivateIncidentsPermissionsItem]]):
        pulses_permissions (Union[Unset, list[NewRoleDataAttributesPulsesPermissionsItem]]):
        retrospective_permissions (Union[Unset, list[NewRoleDataAttributesRetrospectivePermissionsItem]]):
        roles_permissions (Union[Unset, list[NewRoleDataAttributesRolesPermissionsItem]]):
        secrets_permissions (Union[Unset, list[NewRoleDataAttributesSecretsPermissionsItem]]):
        services_permissions (Union[Unset, list[NewRoleDataAttributesServicesPermissionsItem]]):
        severities_permissions (Union[Unset, list[NewRoleDataAttributesSeveritiesPermissionsItem]]):
        status_pages_permissions (Union[Unset, list[NewRoleDataAttributesStatusPagesPermissionsItem]]):
        webhooks_permissions (Union[Unset, list[NewRoleDataAttributesWebhooksPermissionsItem]]):
        workflows_permissions (Union[Unset, list[NewRoleDataAttributesWorkflowsPermissionsItem]]):
    """

    name: str
    incident_permission_set_id: Union[None, Unset, str] = UNSET
    alerts_permissions: Union[Unset, list[NewRoleDataAttributesAlertsPermissionsItem]] = UNSET
    api_keys_permissions: Union[Unset, list[NewRoleDataAttributesApiKeysPermissionsItem]] = UNSET
    audits_permissions: Union[Unset, list[NewRoleDataAttributesAuditsPermissionsItem]] = UNSET
    billing_permissions: Union[Unset, list[NewRoleDataAttributesBillingPermissionsItem]] = UNSET
    environments_permissions: Union[Unset, list[NewRoleDataAttributesEnvironmentsPermissionsItem]] = UNSET
    form_fields_permissions: Union[Unset, list[NewRoleDataAttributesFormFieldsPermissionsItem]] = UNSET
    functionalities_permissions: Union[Unset, list[NewRoleDataAttributesFunctionalitiesPermissionsItem]] = UNSET
    groups_permissions: Union[Unset, list[NewRoleDataAttributesGroupsPermissionsItem]] = UNSET
    incident_causes_permissions: Union[Unset, list[NewRoleDataAttributesIncidentCausesPermissionsItem]] = UNSET
    incident_feedbacks_permissions: Union[Unset, list[NewRoleDataAttributesIncidentFeedbacksPermissionsItem]] = UNSET
    incident_roles_permissions: Union[Unset, list[NewRoleDataAttributesIncidentRolesPermissionsItem]] = UNSET
    incident_types_permissions: Union[Unset, list[NewRoleDataAttributesIncidentTypesPermissionsItem]] = UNSET
    incidents_permissions: Union[Unset, list[NewRoleDataAttributesIncidentsPermissionsItem]] = UNSET
    integrations_permissions: Union[Unset, list[NewRoleDataAttributesIntegrationsPermissionsItem]] = UNSET
    invitations_permissions: Union[Unset, list[NewRoleDataAttributesInvitationsPermissionsItem]] = UNSET
    playbooks_permissions: Union[Unset, list[NewRoleDataAttributesPlaybooksPermissionsItem]] = UNSET
    private_incidents_permissions: Union[Unset, list[NewRoleDataAttributesPrivateIncidentsPermissionsItem]] = UNSET
    pulses_permissions: Union[Unset, list[NewRoleDataAttributesPulsesPermissionsItem]] = UNSET
    retrospective_permissions: Union[Unset, list[NewRoleDataAttributesRetrospectivePermissionsItem]] = UNSET
    roles_permissions: Union[Unset, list[NewRoleDataAttributesRolesPermissionsItem]] = UNSET
    secrets_permissions: Union[Unset, list[NewRoleDataAttributesSecretsPermissionsItem]] = UNSET
    services_permissions: Union[Unset, list[NewRoleDataAttributesServicesPermissionsItem]] = UNSET
    severities_permissions: Union[Unset, list[NewRoleDataAttributesSeveritiesPermissionsItem]] = UNSET
    status_pages_permissions: Union[Unset, list[NewRoleDataAttributesStatusPagesPermissionsItem]] = UNSET
    webhooks_permissions: Union[Unset, list[NewRoleDataAttributesWebhooksPermissionsItem]] = UNSET
    workflows_permissions: Union[Unset, list[NewRoleDataAttributesWorkflowsPermissionsItem]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        incident_permission_set_id: Union[None, Unset, str]
        if isinstance(self.incident_permission_set_id, Unset):
            incident_permission_set_id = UNSET
        else:
            incident_permission_set_id = self.incident_permission_set_id

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

        billing_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.billing_permissions, Unset):
            billing_permissions = []
            for billing_permissions_item_data in self.billing_permissions:
                billing_permissions_item: str = billing_permissions_item_data
                billing_permissions.append(billing_permissions_item)

        environments_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.environments_permissions, Unset):
            environments_permissions = []
            for environments_permissions_item_data in self.environments_permissions:
                environments_permissions_item: str = environments_permissions_item_data
                environments_permissions.append(environments_permissions_item)

        form_fields_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.form_fields_permissions, Unset):
            form_fields_permissions = []
            for form_fields_permissions_item_data in self.form_fields_permissions:
                form_fields_permissions_item: str = form_fields_permissions_item_data
                form_fields_permissions.append(form_fields_permissions_item)

        functionalities_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.functionalities_permissions, Unset):
            functionalities_permissions = []
            for functionalities_permissions_item_data in self.functionalities_permissions:
                functionalities_permissions_item: str = functionalities_permissions_item_data
                functionalities_permissions.append(functionalities_permissions_item)

        groups_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.groups_permissions, Unset):
            groups_permissions = []
            for groups_permissions_item_data in self.groups_permissions:
                groups_permissions_item: str = groups_permissions_item_data
                groups_permissions.append(groups_permissions_item)

        incident_causes_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.incident_causes_permissions, Unset):
            incident_causes_permissions = []
            for incident_causes_permissions_item_data in self.incident_causes_permissions:
                incident_causes_permissions_item: str = incident_causes_permissions_item_data
                incident_causes_permissions.append(incident_causes_permissions_item)

        incident_feedbacks_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.incident_feedbacks_permissions, Unset):
            incident_feedbacks_permissions = []
            for incident_feedbacks_permissions_item_data in self.incident_feedbacks_permissions:
                incident_feedbacks_permissions_item: str = incident_feedbacks_permissions_item_data
                incident_feedbacks_permissions.append(incident_feedbacks_permissions_item)

        incident_roles_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.incident_roles_permissions, Unset):
            incident_roles_permissions = []
            for incident_roles_permissions_item_data in self.incident_roles_permissions:
                incident_roles_permissions_item: str = incident_roles_permissions_item_data
                incident_roles_permissions.append(incident_roles_permissions_item)

        incident_types_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.incident_types_permissions, Unset):
            incident_types_permissions = []
            for incident_types_permissions_item_data in self.incident_types_permissions:
                incident_types_permissions_item: str = incident_types_permissions_item_data
                incident_types_permissions.append(incident_types_permissions_item)

        incidents_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.incidents_permissions, Unset):
            incidents_permissions = []
            for incidents_permissions_item_data in self.incidents_permissions:
                incidents_permissions_item: str = incidents_permissions_item_data
                incidents_permissions.append(incidents_permissions_item)

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

        playbooks_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.playbooks_permissions, Unset):
            playbooks_permissions = []
            for playbooks_permissions_item_data in self.playbooks_permissions:
                playbooks_permissions_item: str = playbooks_permissions_item_data
                playbooks_permissions.append(playbooks_permissions_item)

        private_incidents_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.private_incidents_permissions, Unset):
            private_incidents_permissions = []
            for private_incidents_permissions_item_data in self.private_incidents_permissions:
                private_incidents_permissions_item: str = private_incidents_permissions_item_data
                private_incidents_permissions.append(private_incidents_permissions_item)

        pulses_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.pulses_permissions, Unset):
            pulses_permissions = []
            for pulses_permissions_item_data in self.pulses_permissions:
                pulses_permissions_item: str = pulses_permissions_item_data
                pulses_permissions.append(pulses_permissions_item)

        retrospective_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.retrospective_permissions, Unset):
            retrospective_permissions = []
            for retrospective_permissions_item_data in self.retrospective_permissions:
                retrospective_permissions_item: str = retrospective_permissions_item_data
                retrospective_permissions.append(retrospective_permissions_item)

        roles_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.roles_permissions, Unset):
            roles_permissions = []
            for roles_permissions_item_data in self.roles_permissions:
                roles_permissions_item: str = roles_permissions_item_data
                roles_permissions.append(roles_permissions_item)

        secrets_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.secrets_permissions, Unset):
            secrets_permissions = []
            for secrets_permissions_item_data in self.secrets_permissions:
                secrets_permissions_item: str = secrets_permissions_item_data
                secrets_permissions.append(secrets_permissions_item)

        services_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.services_permissions, Unset):
            services_permissions = []
            for services_permissions_item_data in self.services_permissions:
                services_permissions_item: str = services_permissions_item_data
                services_permissions.append(services_permissions_item)

        severities_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.severities_permissions, Unset):
            severities_permissions = []
            for severities_permissions_item_data in self.severities_permissions:
                severities_permissions_item: str = severities_permissions_item_data
                severities_permissions.append(severities_permissions_item)

        status_pages_permissions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.status_pages_permissions, Unset):
            status_pages_permissions = []
            for status_pages_permissions_item_data in self.status_pages_permissions:
                status_pages_permissions_item: str = status_pages_permissions_item_data
                status_pages_permissions.append(status_pages_permissions_item)

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_incident_permission_set_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        incident_permission_set_id = _parse_incident_permission_set_id(d.pop("incident_permission_set_id", UNSET))

        alerts_permissions = []
        _alerts_permissions = d.pop("alerts_permissions", UNSET)
        for alerts_permissions_item_data in _alerts_permissions or []:
            alerts_permissions_item = check_new_role_data_attributes_alerts_permissions_item(
                alerts_permissions_item_data
            )

            alerts_permissions.append(alerts_permissions_item)

        api_keys_permissions = []
        _api_keys_permissions = d.pop("api_keys_permissions", UNSET)
        for api_keys_permissions_item_data in _api_keys_permissions or []:
            api_keys_permissions_item = check_new_role_data_attributes_api_keys_permissions_item(
                api_keys_permissions_item_data
            )

            api_keys_permissions.append(api_keys_permissions_item)

        audits_permissions = []
        _audits_permissions = d.pop("audits_permissions", UNSET)
        for audits_permissions_item_data in _audits_permissions or []:
            audits_permissions_item = check_new_role_data_attributes_audits_permissions_item(
                audits_permissions_item_data
            )

            audits_permissions.append(audits_permissions_item)

        billing_permissions = []
        _billing_permissions = d.pop("billing_permissions", UNSET)
        for billing_permissions_item_data in _billing_permissions or []:
            billing_permissions_item = check_new_role_data_attributes_billing_permissions_item(
                billing_permissions_item_data
            )

            billing_permissions.append(billing_permissions_item)

        environments_permissions = []
        _environments_permissions = d.pop("environments_permissions", UNSET)
        for environments_permissions_item_data in _environments_permissions or []:
            environments_permissions_item = check_new_role_data_attributes_environments_permissions_item(
                environments_permissions_item_data
            )

            environments_permissions.append(environments_permissions_item)

        form_fields_permissions = []
        _form_fields_permissions = d.pop("form_fields_permissions", UNSET)
        for form_fields_permissions_item_data in _form_fields_permissions or []:
            form_fields_permissions_item = check_new_role_data_attributes_form_fields_permissions_item(
                form_fields_permissions_item_data
            )

            form_fields_permissions.append(form_fields_permissions_item)

        functionalities_permissions = []
        _functionalities_permissions = d.pop("functionalities_permissions", UNSET)
        for functionalities_permissions_item_data in _functionalities_permissions or []:
            functionalities_permissions_item = check_new_role_data_attributes_functionalities_permissions_item(
                functionalities_permissions_item_data
            )

            functionalities_permissions.append(functionalities_permissions_item)

        groups_permissions = []
        _groups_permissions = d.pop("groups_permissions", UNSET)
        for groups_permissions_item_data in _groups_permissions or []:
            groups_permissions_item = check_new_role_data_attributes_groups_permissions_item(
                groups_permissions_item_data
            )

            groups_permissions.append(groups_permissions_item)

        incident_causes_permissions = []
        _incident_causes_permissions = d.pop("incident_causes_permissions", UNSET)
        for incident_causes_permissions_item_data in _incident_causes_permissions or []:
            incident_causes_permissions_item = check_new_role_data_attributes_incident_causes_permissions_item(
                incident_causes_permissions_item_data
            )

            incident_causes_permissions.append(incident_causes_permissions_item)

        incident_feedbacks_permissions = []
        _incident_feedbacks_permissions = d.pop("incident_feedbacks_permissions", UNSET)
        for incident_feedbacks_permissions_item_data in _incident_feedbacks_permissions or []:
            incident_feedbacks_permissions_item = check_new_role_data_attributes_incident_feedbacks_permissions_item(
                incident_feedbacks_permissions_item_data
            )

            incident_feedbacks_permissions.append(incident_feedbacks_permissions_item)

        incident_roles_permissions = []
        _incident_roles_permissions = d.pop("incident_roles_permissions", UNSET)
        for incident_roles_permissions_item_data in _incident_roles_permissions or []:
            incident_roles_permissions_item = check_new_role_data_attributes_incident_roles_permissions_item(
                incident_roles_permissions_item_data
            )

            incident_roles_permissions.append(incident_roles_permissions_item)

        incident_types_permissions = []
        _incident_types_permissions = d.pop("incident_types_permissions", UNSET)
        for incident_types_permissions_item_data in _incident_types_permissions or []:
            incident_types_permissions_item = check_new_role_data_attributes_incident_types_permissions_item(
                incident_types_permissions_item_data
            )

            incident_types_permissions.append(incident_types_permissions_item)

        incidents_permissions = []
        _incidents_permissions = d.pop("incidents_permissions", UNSET)
        for incidents_permissions_item_data in _incidents_permissions or []:
            incidents_permissions_item = check_new_role_data_attributes_incidents_permissions_item(
                incidents_permissions_item_data
            )

            incidents_permissions.append(incidents_permissions_item)

        integrations_permissions = []
        _integrations_permissions = d.pop("integrations_permissions", UNSET)
        for integrations_permissions_item_data in _integrations_permissions or []:
            integrations_permissions_item = check_new_role_data_attributes_integrations_permissions_item(
                integrations_permissions_item_data
            )

            integrations_permissions.append(integrations_permissions_item)

        invitations_permissions = []
        _invitations_permissions = d.pop("invitations_permissions", UNSET)
        for invitations_permissions_item_data in _invitations_permissions or []:
            invitations_permissions_item = check_new_role_data_attributes_invitations_permissions_item(
                invitations_permissions_item_data
            )

            invitations_permissions.append(invitations_permissions_item)

        playbooks_permissions = []
        _playbooks_permissions = d.pop("playbooks_permissions", UNSET)
        for playbooks_permissions_item_data in _playbooks_permissions or []:
            playbooks_permissions_item = check_new_role_data_attributes_playbooks_permissions_item(
                playbooks_permissions_item_data
            )

            playbooks_permissions.append(playbooks_permissions_item)

        private_incidents_permissions = []
        _private_incidents_permissions = d.pop("private_incidents_permissions", UNSET)
        for private_incidents_permissions_item_data in _private_incidents_permissions or []:
            private_incidents_permissions_item = check_new_role_data_attributes_private_incidents_permissions_item(
                private_incidents_permissions_item_data
            )

            private_incidents_permissions.append(private_incidents_permissions_item)

        pulses_permissions = []
        _pulses_permissions = d.pop("pulses_permissions", UNSET)
        for pulses_permissions_item_data in _pulses_permissions or []:
            pulses_permissions_item = check_new_role_data_attributes_pulses_permissions_item(
                pulses_permissions_item_data
            )

            pulses_permissions.append(pulses_permissions_item)

        retrospective_permissions = []
        _retrospective_permissions = d.pop("retrospective_permissions", UNSET)
        for retrospective_permissions_item_data in _retrospective_permissions or []:
            retrospective_permissions_item = check_new_role_data_attributes_retrospective_permissions_item(
                retrospective_permissions_item_data
            )

            retrospective_permissions.append(retrospective_permissions_item)

        roles_permissions = []
        _roles_permissions = d.pop("roles_permissions", UNSET)
        for roles_permissions_item_data in _roles_permissions or []:
            roles_permissions_item = check_new_role_data_attributes_roles_permissions_item(roles_permissions_item_data)

            roles_permissions.append(roles_permissions_item)

        secrets_permissions = []
        _secrets_permissions = d.pop("secrets_permissions", UNSET)
        for secrets_permissions_item_data in _secrets_permissions or []:
            secrets_permissions_item = check_new_role_data_attributes_secrets_permissions_item(
                secrets_permissions_item_data
            )

            secrets_permissions.append(secrets_permissions_item)

        services_permissions = []
        _services_permissions = d.pop("services_permissions", UNSET)
        for services_permissions_item_data in _services_permissions or []:
            services_permissions_item = check_new_role_data_attributes_services_permissions_item(
                services_permissions_item_data
            )

            services_permissions.append(services_permissions_item)

        severities_permissions = []
        _severities_permissions = d.pop("severities_permissions", UNSET)
        for severities_permissions_item_data in _severities_permissions or []:
            severities_permissions_item = check_new_role_data_attributes_severities_permissions_item(
                severities_permissions_item_data
            )

            severities_permissions.append(severities_permissions_item)

        status_pages_permissions = []
        _status_pages_permissions = d.pop("status_pages_permissions", UNSET)
        for status_pages_permissions_item_data in _status_pages_permissions or []:
            status_pages_permissions_item = check_new_role_data_attributes_status_pages_permissions_item(
                status_pages_permissions_item_data
            )

            status_pages_permissions.append(status_pages_permissions_item)

        webhooks_permissions = []
        _webhooks_permissions = d.pop("webhooks_permissions", UNSET)
        for webhooks_permissions_item_data in _webhooks_permissions or []:
            webhooks_permissions_item = check_new_role_data_attributes_webhooks_permissions_item(
                webhooks_permissions_item_data
            )

            webhooks_permissions.append(webhooks_permissions_item)

        workflows_permissions = []
        _workflows_permissions = d.pop("workflows_permissions", UNSET)
        for workflows_permissions_item_data in _workflows_permissions or []:
            workflows_permissions_item = check_new_role_data_attributes_workflows_permissions_item(
                workflows_permissions_item_data
            )

            workflows_permissions.append(workflows_permissions_item)

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
        )

        return new_role_data_attributes
