from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.role_alerts_permissions_item import RoleAlertsPermissionsItem, check_role_alerts_permissions_item
from ..models.role_api_keys_permissions_item import RoleApiKeysPermissionsItem, check_role_api_keys_permissions_item
from ..models.role_audits_permissions_item import RoleAuditsPermissionsItem, check_role_audits_permissions_item
from ..models.role_billing_permissions_item import RoleBillingPermissionsItem, check_role_billing_permissions_item
from ..models.role_environments_permissions_item import (
    RoleEnvironmentsPermissionsItem,
    check_role_environments_permissions_item,
)
from ..models.role_form_fields_permissions_item import (
    RoleFormFieldsPermissionsItem,
    check_role_form_fields_permissions_item,
)
from ..models.role_functionalities_permissions_item import (
    RoleFunctionalitiesPermissionsItem,
    check_role_functionalities_permissions_item,
)
from ..models.role_groups_permissions_item import RoleGroupsPermissionsItem, check_role_groups_permissions_item
from ..models.role_incident_causes_permissions_item import (
    RoleIncidentCausesPermissionsItem,
    check_role_incident_causes_permissions_item,
)
from ..models.role_incident_feedbacks_permissions_item import (
    RoleIncidentFeedbacksPermissionsItem,
    check_role_incident_feedbacks_permissions_item,
)
from ..models.role_incident_roles_permissions_item import (
    RoleIncidentRolesPermissionsItem,
    check_role_incident_roles_permissions_item,
)
from ..models.role_incident_types_permissions_item import (
    RoleIncidentTypesPermissionsItem,
    check_role_incident_types_permissions_item,
)
from ..models.role_incidents_permissions_item import RoleIncidentsPermissionsItem, check_role_incidents_permissions_item
from ..models.role_integrations_permissions_item import (
    RoleIntegrationsPermissionsItem,
    check_role_integrations_permissions_item,
)
from ..models.role_invitations_permissions_item import (
    RoleInvitationsPermissionsItem,
    check_role_invitations_permissions_item,
)
from ..models.role_playbooks_permissions_item import RolePlaybooksPermissionsItem, check_role_playbooks_permissions_item
from ..models.role_private_incidents_permissions_item import (
    RolePrivateIncidentsPermissionsItem,
    check_role_private_incidents_permissions_item,
)
from ..models.role_pulses_permissions_item import RolePulsesPermissionsItem, check_role_pulses_permissions_item
from ..models.role_retrospective_permissions_item import (
    RoleRetrospectivePermissionsItem,
    check_role_retrospective_permissions_item,
)
from ..models.role_roles_permissions_item import RoleRolesPermissionsItem, check_role_roles_permissions_item
from ..models.role_secrets_permissions_item import RoleSecretsPermissionsItem, check_role_secrets_permissions_item
from ..models.role_services_permissions_item import RoleServicesPermissionsItem, check_role_services_permissions_item
from ..models.role_severities_permissions_item import (
    RoleSeveritiesPermissionsItem,
    check_role_severities_permissions_item,
)
from ..models.role_status_pages_permissions_item import (
    RoleStatusPagesPermissionsItem,
    check_role_status_pages_permissions_item,
)
from ..models.role_webhooks_permissions_item import RoleWebhooksPermissionsItem, check_role_webhooks_permissions_item
from ..models.role_workflows_permissions_item import RoleWorkflowsPermissionsItem, check_role_workflows_permissions_item
from ..types import UNSET, Unset

T = TypeVar("T", bound="Role")


@_attrs_define
class Role:
    """
    Attributes:
        name (str): The role name.
        created_at (str):
        updated_at (str):
        slug (Union[Unset, str]): The role slug.
        incident_permission_set_id (Union[None, Unset, str]): Associated incident permissions set.
        is_deletable (Union[Unset, bool]): Whether the role can be deleted.
        is_editable (Union[Unset, bool]): Whether the role can be edited.
        alerts_permissions (Union[Unset, list[RoleAlertsPermissionsItem]]):
        api_keys_permissions (Union[Unset, list[RoleApiKeysPermissionsItem]]):
        audits_permissions (Union[Unset, list[RoleAuditsPermissionsItem]]):
        billing_permissions (Union[Unset, list[RoleBillingPermissionsItem]]):
        environments_permissions (Union[Unset, list[RoleEnvironmentsPermissionsItem]]):
        form_fields_permissions (Union[Unset, list[RoleFormFieldsPermissionsItem]]):
        functionalities_permissions (Union[Unset, list[RoleFunctionalitiesPermissionsItem]]):
        groups_permissions (Union[Unset, list[RoleGroupsPermissionsItem]]):
        incident_causes_permissions (Union[Unset, list[RoleIncidentCausesPermissionsItem]]):
        incident_feedbacks_permissions (Union[Unset, list[RoleIncidentFeedbacksPermissionsItem]]):
        incident_roles_permissions (Union[Unset, list[RoleIncidentRolesPermissionsItem]]):
        incident_types_permissions (Union[Unset, list[RoleIncidentTypesPermissionsItem]]):
        incidents_permissions (Union[Unset, list[RoleIncidentsPermissionsItem]]):
        integrations_permissions (Union[Unset, list[RoleIntegrationsPermissionsItem]]):
        invitations_permissions (Union[Unset, list[RoleInvitationsPermissionsItem]]):
        playbooks_permissions (Union[Unset, list[RolePlaybooksPermissionsItem]]):
        private_incidents_permissions (Union[Unset, list[RolePrivateIncidentsPermissionsItem]]):
        pulses_permissions (Union[Unset, list[RolePulsesPermissionsItem]]):
        retrospective_permissions (Union[Unset, list[RoleRetrospectivePermissionsItem]]):
        roles_permissions (Union[Unset, list[RoleRolesPermissionsItem]]):
        secrets_permissions (Union[Unset, list[RoleSecretsPermissionsItem]]):
        services_permissions (Union[Unset, list[RoleServicesPermissionsItem]]):
        severities_permissions (Union[Unset, list[RoleSeveritiesPermissionsItem]]):
        status_pages_permissions (Union[Unset, list[RoleStatusPagesPermissionsItem]]):
        webhooks_permissions (Union[Unset, list[RoleWebhooksPermissionsItem]]):
        workflows_permissions (Union[Unset, list[RoleWorkflowsPermissionsItem]]):
    """

    name: str
    created_at: str
    updated_at: str
    slug: Unset | str = UNSET
    incident_permission_set_id: None | Unset | str = UNSET
    is_deletable: Unset | bool = UNSET
    is_editable: Unset | bool = UNSET
    alerts_permissions: Unset | list[RoleAlertsPermissionsItem] = UNSET
    api_keys_permissions: Unset | list[RoleApiKeysPermissionsItem] = UNSET
    audits_permissions: Unset | list[RoleAuditsPermissionsItem] = UNSET
    billing_permissions: Unset | list[RoleBillingPermissionsItem] = UNSET
    environments_permissions: Unset | list[RoleEnvironmentsPermissionsItem] = UNSET
    form_fields_permissions: Unset | list[RoleFormFieldsPermissionsItem] = UNSET
    functionalities_permissions: Unset | list[RoleFunctionalitiesPermissionsItem] = UNSET
    groups_permissions: Unset | list[RoleGroupsPermissionsItem] = UNSET
    incident_causes_permissions: Unset | list[RoleIncidentCausesPermissionsItem] = UNSET
    incident_feedbacks_permissions: Unset | list[RoleIncidentFeedbacksPermissionsItem] = UNSET
    incident_roles_permissions: Unset | list[RoleIncidentRolesPermissionsItem] = UNSET
    incident_types_permissions: Unset | list[RoleIncidentTypesPermissionsItem] = UNSET
    incidents_permissions: Unset | list[RoleIncidentsPermissionsItem] = UNSET
    integrations_permissions: Unset | list[RoleIntegrationsPermissionsItem] = UNSET
    invitations_permissions: Unset | list[RoleInvitationsPermissionsItem] = UNSET
    playbooks_permissions: Unset | list[RolePlaybooksPermissionsItem] = UNSET
    private_incidents_permissions: Unset | list[RolePrivateIncidentsPermissionsItem] = UNSET
    pulses_permissions: Unset | list[RolePulsesPermissionsItem] = UNSET
    retrospective_permissions: Unset | list[RoleRetrospectivePermissionsItem] = UNSET
    roles_permissions: Unset | list[RoleRolesPermissionsItem] = UNSET
    secrets_permissions: Unset | list[RoleSecretsPermissionsItem] = UNSET
    services_permissions: Unset | list[RoleServicesPermissionsItem] = UNSET
    severities_permissions: Unset | list[RoleSeveritiesPermissionsItem] = UNSET
    status_pages_permissions: Unset | list[RoleStatusPagesPermissionsItem] = UNSET
    webhooks_permissions: Unset | list[RoleWebhooksPermissionsItem] = UNSET
    workflows_permissions: Unset | list[RoleWorkflowsPermissionsItem] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        incident_permission_set_id: None | Unset | str
        if isinstance(self.incident_permission_set_id, Unset):
            incident_permission_set_id = UNSET
        else:
            incident_permission_set_id = self.incident_permission_set_id

        is_deletable = self.is_deletable

        is_editable = self.is_editable

        alerts_permissions: Unset | list[str] = UNSET
        if not isinstance(self.alerts_permissions, Unset):
            alerts_permissions = []
            for alerts_permissions_item_data in self.alerts_permissions:
                alerts_permissions_item: str = alerts_permissions_item_data
                alerts_permissions.append(alerts_permissions_item)

        api_keys_permissions: Unset | list[str] = UNSET
        if not isinstance(self.api_keys_permissions, Unset):
            api_keys_permissions = []
            for api_keys_permissions_item_data in self.api_keys_permissions:
                api_keys_permissions_item: str = api_keys_permissions_item_data
                api_keys_permissions.append(api_keys_permissions_item)

        audits_permissions: Unset | list[str] = UNSET
        if not isinstance(self.audits_permissions, Unset):
            audits_permissions = []
            for audits_permissions_item_data in self.audits_permissions:
                audits_permissions_item: str = audits_permissions_item_data
                audits_permissions.append(audits_permissions_item)

        billing_permissions: Unset | list[str] = UNSET
        if not isinstance(self.billing_permissions, Unset):
            billing_permissions = []
            for billing_permissions_item_data in self.billing_permissions:
                billing_permissions_item: str = billing_permissions_item_data
                billing_permissions.append(billing_permissions_item)

        environments_permissions: Unset | list[str] = UNSET
        if not isinstance(self.environments_permissions, Unset):
            environments_permissions = []
            for environments_permissions_item_data in self.environments_permissions:
                environments_permissions_item: str = environments_permissions_item_data
                environments_permissions.append(environments_permissions_item)

        form_fields_permissions: Unset | list[str] = UNSET
        if not isinstance(self.form_fields_permissions, Unset):
            form_fields_permissions = []
            for form_fields_permissions_item_data in self.form_fields_permissions:
                form_fields_permissions_item: str = form_fields_permissions_item_data
                form_fields_permissions.append(form_fields_permissions_item)

        functionalities_permissions: Unset | list[str] = UNSET
        if not isinstance(self.functionalities_permissions, Unset):
            functionalities_permissions = []
            for functionalities_permissions_item_data in self.functionalities_permissions:
                functionalities_permissions_item: str = functionalities_permissions_item_data
                functionalities_permissions.append(functionalities_permissions_item)

        groups_permissions: Unset | list[str] = UNSET
        if not isinstance(self.groups_permissions, Unset):
            groups_permissions = []
            for groups_permissions_item_data in self.groups_permissions:
                groups_permissions_item: str = groups_permissions_item_data
                groups_permissions.append(groups_permissions_item)

        incident_causes_permissions: Unset | list[str] = UNSET
        if not isinstance(self.incident_causes_permissions, Unset):
            incident_causes_permissions = []
            for incident_causes_permissions_item_data in self.incident_causes_permissions:
                incident_causes_permissions_item: str = incident_causes_permissions_item_data
                incident_causes_permissions.append(incident_causes_permissions_item)

        incident_feedbacks_permissions: Unset | list[str] = UNSET
        if not isinstance(self.incident_feedbacks_permissions, Unset):
            incident_feedbacks_permissions = []
            for incident_feedbacks_permissions_item_data in self.incident_feedbacks_permissions:
                incident_feedbacks_permissions_item: str = incident_feedbacks_permissions_item_data
                incident_feedbacks_permissions.append(incident_feedbacks_permissions_item)

        incident_roles_permissions: Unset | list[str] = UNSET
        if not isinstance(self.incident_roles_permissions, Unset):
            incident_roles_permissions = []
            for incident_roles_permissions_item_data in self.incident_roles_permissions:
                incident_roles_permissions_item: str = incident_roles_permissions_item_data
                incident_roles_permissions.append(incident_roles_permissions_item)

        incident_types_permissions: Unset | list[str] = UNSET
        if not isinstance(self.incident_types_permissions, Unset):
            incident_types_permissions = []
            for incident_types_permissions_item_data in self.incident_types_permissions:
                incident_types_permissions_item: str = incident_types_permissions_item_data
                incident_types_permissions.append(incident_types_permissions_item)

        incidents_permissions: Unset | list[str] = UNSET
        if not isinstance(self.incidents_permissions, Unset):
            incidents_permissions = []
            for incidents_permissions_item_data in self.incidents_permissions:
                incidents_permissions_item: str = incidents_permissions_item_data
                incidents_permissions.append(incidents_permissions_item)

        integrations_permissions: Unset | list[str] = UNSET
        if not isinstance(self.integrations_permissions, Unset):
            integrations_permissions = []
            for integrations_permissions_item_data in self.integrations_permissions:
                integrations_permissions_item: str = integrations_permissions_item_data
                integrations_permissions.append(integrations_permissions_item)

        invitations_permissions: Unset | list[str] = UNSET
        if not isinstance(self.invitations_permissions, Unset):
            invitations_permissions = []
            for invitations_permissions_item_data in self.invitations_permissions:
                invitations_permissions_item: str = invitations_permissions_item_data
                invitations_permissions.append(invitations_permissions_item)

        playbooks_permissions: Unset | list[str] = UNSET
        if not isinstance(self.playbooks_permissions, Unset):
            playbooks_permissions = []
            for playbooks_permissions_item_data in self.playbooks_permissions:
                playbooks_permissions_item: str = playbooks_permissions_item_data
                playbooks_permissions.append(playbooks_permissions_item)

        private_incidents_permissions: Unset | list[str] = UNSET
        if not isinstance(self.private_incidents_permissions, Unset):
            private_incidents_permissions = []
            for private_incidents_permissions_item_data in self.private_incidents_permissions:
                private_incidents_permissions_item: str = private_incidents_permissions_item_data
                private_incidents_permissions.append(private_incidents_permissions_item)

        pulses_permissions: Unset | list[str] = UNSET
        if not isinstance(self.pulses_permissions, Unset):
            pulses_permissions = []
            for pulses_permissions_item_data in self.pulses_permissions:
                pulses_permissions_item: str = pulses_permissions_item_data
                pulses_permissions.append(pulses_permissions_item)

        retrospective_permissions: Unset | list[str] = UNSET
        if not isinstance(self.retrospective_permissions, Unset):
            retrospective_permissions = []
            for retrospective_permissions_item_data in self.retrospective_permissions:
                retrospective_permissions_item: str = retrospective_permissions_item_data
                retrospective_permissions.append(retrospective_permissions_item)

        roles_permissions: Unset | list[str] = UNSET
        if not isinstance(self.roles_permissions, Unset):
            roles_permissions = []
            for roles_permissions_item_data in self.roles_permissions:
                roles_permissions_item: str = roles_permissions_item_data
                roles_permissions.append(roles_permissions_item)

        secrets_permissions: Unset | list[str] = UNSET
        if not isinstance(self.secrets_permissions, Unset):
            secrets_permissions = []
            for secrets_permissions_item_data in self.secrets_permissions:
                secrets_permissions_item: str = secrets_permissions_item_data
                secrets_permissions.append(secrets_permissions_item)

        services_permissions: Unset | list[str] = UNSET
        if not isinstance(self.services_permissions, Unset):
            services_permissions = []
            for services_permissions_item_data in self.services_permissions:
                services_permissions_item: str = services_permissions_item_data
                services_permissions.append(services_permissions_item)

        severities_permissions: Unset | list[str] = UNSET
        if not isinstance(self.severities_permissions, Unset):
            severities_permissions = []
            for severities_permissions_item_data in self.severities_permissions:
                severities_permissions_item: str = severities_permissions_item_data
                severities_permissions.append(severities_permissions_item)

        status_pages_permissions: Unset | list[str] = UNSET
        if not isinstance(self.status_pages_permissions, Unset):
            status_pages_permissions = []
            for status_pages_permissions_item_data in self.status_pages_permissions:
                status_pages_permissions_item: str = status_pages_permissions_item_data
                status_pages_permissions.append(status_pages_permissions_item)

        webhooks_permissions: Unset | list[str] = UNSET
        if not isinstance(self.webhooks_permissions, Unset):
            webhooks_permissions = []
            for webhooks_permissions_item_data in self.webhooks_permissions:
                webhooks_permissions_item: str = webhooks_permissions_item_data
                webhooks_permissions.append(webhooks_permissions_item)

        workflows_permissions: Unset | list[str] = UNSET
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
        if incident_permission_set_id is not UNSET:
            field_dict["incident_permission_set_id"] = incident_permission_set_id
        if is_deletable is not UNSET:
            field_dict["is_deletable"] = is_deletable
        if is_editable is not UNSET:
            field_dict["is_editable"] = is_editable
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

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        def _parse_incident_permission_set_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        incident_permission_set_id = _parse_incident_permission_set_id(d.pop("incident_permission_set_id", UNSET))

        is_deletable = d.pop("is_deletable", UNSET)

        is_editable = d.pop("is_editable", UNSET)

        alerts_permissions = []
        _alerts_permissions = d.pop("alerts_permissions", UNSET)
        for alerts_permissions_item_data in _alerts_permissions or []:
            alerts_permissions_item = check_role_alerts_permissions_item(alerts_permissions_item_data)

            alerts_permissions.append(alerts_permissions_item)

        api_keys_permissions = []
        _api_keys_permissions = d.pop("api_keys_permissions", UNSET)
        for api_keys_permissions_item_data in _api_keys_permissions or []:
            api_keys_permissions_item = check_role_api_keys_permissions_item(api_keys_permissions_item_data)

            api_keys_permissions.append(api_keys_permissions_item)

        audits_permissions = []
        _audits_permissions = d.pop("audits_permissions", UNSET)
        for audits_permissions_item_data in _audits_permissions or []:
            audits_permissions_item = check_role_audits_permissions_item(audits_permissions_item_data)

            audits_permissions.append(audits_permissions_item)

        billing_permissions = []
        _billing_permissions = d.pop("billing_permissions", UNSET)
        for billing_permissions_item_data in _billing_permissions or []:
            billing_permissions_item = check_role_billing_permissions_item(billing_permissions_item_data)

            billing_permissions.append(billing_permissions_item)

        environments_permissions = []
        _environments_permissions = d.pop("environments_permissions", UNSET)
        for environments_permissions_item_data in _environments_permissions or []:
            environments_permissions_item = check_role_environments_permissions_item(environments_permissions_item_data)

            environments_permissions.append(environments_permissions_item)

        form_fields_permissions = []
        _form_fields_permissions = d.pop("form_fields_permissions", UNSET)
        for form_fields_permissions_item_data in _form_fields_permissions or []:
            form_fields_permissions_item = check_role_form_fields_permissions_item(form_fields_permissions_item_data)

            form_fields_permissions.append(form_fields_permissions_item)

        functionalities_permissions = []
        _functionalities_permissions = d.pop("functionalities_permissions", UNSET)
        for functionalities_permissions_item_data in _functionalities_permissions or []:
            functionalities_permissions_item = check_role_functionalities_permissions_item(
                functionalities_permissions_item_data
            )

            functionalities_permissions.append(functionalities_permissions_item)

        groups_permissions = []
        _groups_permissions = d.pop("groups_permissions", UNSET)
        for groups_permissions_item_data in _groups_permissions or []:
            groups_permissions_item = check_role_groups_permissions_item(groups_permissions_item_data)

            groups_permissions.append(groups_permissions_item)

        incident_causes_permissions = []
        _incident_causes_permissions = d.pop("incident_causes_permissions", UNSET)
        for incident_causes_permissions_item_data in _incident_causes_permissions or []:
            incident_causes_permissions_item = check_role_incident_causes_permissions_item(
                incident_causes_permissions_item_data
            )

            incident_causes_permissions.append(incident_causes_permissions_item)

        incident_feedbacks_permissions = []
        _incident_feedbacks_permissions = d.pop("incident_feedbacks_permissions", UNSET)
        for incident_feedbacks_permissions_item_data in _incident_feedbacks_permissions or []:
            incident_feedbacks_permissions_item = check_role_incident_feedbacks_permissions_item(
                incident_feedbacks_permissions_item_data
            )

            incident_feedbacks_permissions.append(incident_feedbacks_permissions_item)

        incident_roles_permissions = []
        _incident_roles_permissions = d.pop("incident_roles_permissions", UNSET)
        for incident_roles_permissions_item_data in _incident_roles_permissions or []:
            incident_roles_permissions_item = check_role_incident_roles_permissions_item(
                incident_roles_permissions_item_data
            )

            incident_roles_permissions.append(incident_roles_permissions_item)

        incident_types_permissions = []
        _incident_types_permissions = d.pop("incident_types_permissions", UNSET)
        for incident_types_permissions_item_data in _incident_types_permissions or []:
            incident_types_permissions_item = check_role_incident_types_permissions_item(
                incident_types_permissions_item_data
            )

            incident_types_permissions.append(incident_types_permissions_item)

        incidents_permissions = []
        _incidents_permissions = d.pop("incidents_permissions", UNSET)
        for incidents_permissions_item_data in _incidents_permissions or []:
            incidents_permissions_item = check_role_incidents_permissions_item(incidents_permissions_item_data)

            incidents_permissions.append(incidents_permissions_item)

        integrations_permissions = []
        _integrations_permissions = d.pop("integrations_permissions", UNSET)
        for integrations_permissions_item_data in _integrations_permissions or []:
            integrations_permissions_item = check_role_integrations_permissions_item(integrations_permissions_item_data)

            integrations_permissions.append(integrations_permissions_item)

        invitations_permissions = []
        _invitations_permissions = d.pop("invitations_permissions", UNSET)
        for invitations_permissions_item_data in _invitations_permissions or []:
            invitations_permissions_item = check_role_invitations_permissions_item(invitations_permissions_item_data)

            invitations_permissions.append(invitations_permissions_item)

        playbooks_permissions = []
        _playbooks_permissions = d.pop("playbooks_permissions", UNSET)
        for playbooks_permissions_item_data in _playbooks_permissions or []:
            playbooks_permissions_item = check_role_playbooks_permissions_item(playbooks_permissions_item_data)

            playbooks_permissions.append(playbooks_permissions_item)

        private_incidents_permissions = []
        _private_incidents_permissions = d.pop("private_incidents_permissions", UNSET)
        for private_incidents_permissions_item_data in _private_incidents_permissions or []:
            private_incidents_permissions_item = check_role_private_incidents_permissions_item(
                private_incidents_permissions_item_data
            )

            private_incidents_permissions.append(private_incidents_permissions_item)

        pulses_permissions = []
        _pulses_permissions = d.pop("pulses_permissions", UNSET)
        for pulses_permissions_item_data in _pulses_permissions or []:
            pulses_permissions_item = check_role_pulses_permissions_item(pulses_permissions_item_data)

            pulses_permissions.append(pulses_permissions_item)

        retrospective_permissions = []
        _retrospective_permissions = d.pop("retrospective_permissions", UNSET)
        for retrospective_permissions_item_data in _retrospective_permissions or []:
            retrospective_permissions_item = check_role_retrospective_permissions_item(
                retrospective_permissions_item_data
            )

            retrospective_permissions.append(retrospective_permissions_item)

        roles_permissions = []
        _roles_permissions = d.pop("roles_permissions", UNSET)
        for roles_permissions_item_data in _roles_permissions or []:
            roles_permissions_item = check_role_roles_permissions_item(roles_permissions_item_data)

            roles_permissions.append(roles_permissions_item)

        secrets_permissions = []
        _secrets_permissions = d.pop("secrets_permissions", UNSET)
        for secrets_permissions_item_data in _secrets_permissions or []:
            secrets_permissions_item = check_role_secrets_permissions_item(secrets_permissions_item_data)

            secrets_permissions.append(secrets_permissions_item)

        services_permissions = []
        _services_permissions = d.pop("services_permissions", UNSET)
        for services_permissions_item_data in _services_permissions or []:
            services_permissions_item = check_role_services_permissions_item(services_permissions_item_data)

            services_permissions.append(services_permissions_item)

        severities_permissions = []
        _severities_permissions = d.pop("severities_permissions", UNSET)
        for severities_permissions_item_data in _severities_permissions or []:
            severities_permissions_item = check_role_severities_permissions_item(severities_permissions_item_data)

            severities_permissions.append(severities_permissions_item)

        status_pages_permissions = []
        _status_pages_permissions = d.pop("status_pages_permissions", UNSET)
        for status_pages_permissions_item_data in _status_pages_permissions or []:
            status_pages_permissions_item = check_role_status_pages_permissions_item(status_pages_permissions_item_data)

            status_pages_permissions.append(status_pages_permissions_item)

        webhooks_permissions = []
        _webhooks_permissions = d.pop("webhooks_permissions", UNSET)
        for webhooks_permissions_item_data in _webhooks_permissions or []:
            webhooks_permissions_item = check_role_webhooks_permissions_item(webhooks_permissions_item_data)

            webhooks_permissions.append(webhooks_permissions_item)

        workflows_permissions = []
        _workflows_permissions = d.pop("workflows_permissions", UNSET)
        for workflows_permissions_item_data in _workflows_permissions or []:
            workflows_permissions_item = check_role_workflows_permissions_item(workflows_permissions_item_data)

            workflows_permissions.append(workflows_permissions_item)

        role = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            incident_permission_set_id=incident_permission_set_id,
            is_deletable=is_deletable,
            is_editable=is_editable,
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

        role.additional_properties = d
        return role

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
