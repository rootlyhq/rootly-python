from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_role_data_attributes_api_keys_permissions_item import (
    UpdateRoleDataAttributesApiKeysPermissionsItem,
    check_update_role_data_attributes_api_keys_permissions_item,
)
from ..models.update_role_data_attributes_audits_permissions_item import (
    UpdateRoleDataAttributesAuditsPermissionsItem,
    check_update_role_data_attributes_audits_permissions_item,
)
from ..models.update_role_data_attributes_billing_permissions_item import (
    UpdateRoleDataAttributesBillingPermissionsItem,
    check_update_role_data_attributes_billing_permissions_item,
)
from ..models.update_role_data_attributes_environments_permissions_item import (
    UpdateRoleDataAttributesEnvironmentsPermissionsItem,
    check_update_role_data_attributes_environments_permissions_item,
)
from ..models.update_role_data_attributes_form_fields_permissions_item import (
    UpdateRoleDataAttributesFormFieldsPermissionsItem,
    check_update_role_data_attributes_form_fields_permissions_item,
)
from ..models.update_role_data_attributes_functionalities_permissions_item import (
    UpdateRoleDataAttributesFunctionalitiesPermissionsItem,
    check_update_role_data_attributes_functionalities_permissions_item,
)
from ..models.update_role_data_attributes_groups_permissions_item import (
    UpdateRoleDataAttributesGroupsPermissionsItem,
    check_update_role_data_attributes_groups_permissions_item,
)
from ..models.update_role_data_attributes_incident_causes_permissions_item import (
    UpdateRoleDataAttributesIncidentCausesPermissionsItem,
    check_update_role_data_attributes_incident_causes_permissions_item,
)
from ..models.update_role_data_attributes_incident_feedbacks_permissions_item import (
    UpdateRoleDataAttributesIncidentFeedbacksPermissionsItem,
    check_update_role_data_attributes_incident_feedbacks_permissions_item,
)
from ..models.update_role_data_attributes_incident_roles_permissions_item import (
    UpdateRoleDataAttributesIncidentRolesPermissionsItem,
    check_update_role_data_attributes_incident_roles_permissions_item,
)
from ..models.update_role_data_attributes_incident_types_permissions_item import (
    UpdateRoleDataAttributesIncidentTypesPermissionsItem,
    check_update_role_data_attributes_incident_types_permissions_item,
)
from ..models.update_role_data_attributes_incidents_permissions_item import (
    UpdateRoleDataAttributesIncidentsPermissionsItem,
    check_update_role_data_attributes_incidents_permissions_item,
)
from ..models.update_role_data_attributes_integrations_permissions_item import (
    UpdateRoleDataAttributesIntegrationsPermissionsItem,
    check_update_role_data_attributes_integrations_permissions_item,
)
from ..models.update_role_data_attributes_invitations_permissions_item import (
    UpdateRoleDataAttributesInvitationsPermissionsItem,
    check_update_role_data_attributes_invitations_permissions_item,
)
from ..models.update_role_data_attributes_playbooks_permissions_item import (
    UpdateRoleDataAttributesPlaybooksPermissionsItem,
    check_update_role_data_attributes_playbooks_permissions_item,
)
from ..models.update_role_data_attributes_private_incidents_permissions_item import (
    UpdateRoleDataAttributesPrivateIncidentsPermissionsItem,
    check_update_role_data_attributes_private_incidents_permissions_item,
)
from ..models.update_role_data_attributes_retrospective_permissions_item import (
    UpdateRoleDataAttributesRetrospectivePermissionsItem,
    check_update_role_data_attributes_retrospective_permissions_item,
)
from ..models.update_role_data_attributes_roles_permissions_item import (
    UpdateRoleDataAttributesRolesPermissionsItem,
    check_update_role_data_attributes_roles_permissions_item,
)
from ..models.update_role_data_attributes_secrets_permissions_item import (
    UpdateRoleDataAttributesSecretsPermissionsItem,
    check_update_role_data_attributes_secrets_permissions_item,
)
from ..models.update_role_data_attributes_services_permissions_item import (
    UpdateRoleDataAttributesServicesPermissionsItem,
    check_update_role_data_attributes_services_permissions_item,
)
from ..models.update_role_data_attributes_severities_permissions_item import (
    UpdateRoleDataAttributesSeveritiesPermissionsItem,
    check_update_role_data_attributes_severities_permissions_item,
)
from ..models.update_role_data_attributes_status_pages_permissions_item import (
    UpdateRoleDataAttributesStatusPagesPermissionsItem,
    check_update_role_data_attributes_status_pages_permissions_item,
)
from ..models.update_role_data_attributes_webhooks_permissions_item import (
    UpdateRoleDataAttributesWebhooksPermissionsItem,
    check_update_role_data_attributes_webhooks_permissions_item,
)
from ..models.update_role_data_attributes_workflows_permissions_item import (
    UpdateRoleDataAttributesWorkflowsPermissionsItem,
    check_update_role_data_attributes_workflows_permissions_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateRoleDataAttributes")


@_attrs_define
class UpdateRoleDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The role name.
        incident_permission_set_id (Union[None, Unset, str]): Associated incident permissions set.
        is_deletable (Union[Unset, bool]): Whether the role can be deleted.
        is_editable (Union[Unset, bool]): Whether the role can be edited.
        api_keys_permissions (Union[Unset, list[UpdateRoleDataAttributesApiKeysPermissionsItem]]):
        audits_permissions (Union[Unset, list[UpdateRoleDataAttributesAuditsPermissionsItem]]):
        billing_permissions (Union[Unset, list[UpdateRoleDataAttributesBillingPermissionsItem]]):
        environments_permissions (Union[Unset, list[UpdateRoleDataAttributesEnvironmentsPermissionsItem]]):
        form_fields_permissions (Union[Unset, list[UpdateRoleDataAttributesFormFieldsPermissionsItem]]):
        functionalities_permissions (Union[Unset, list[UpdateRoleDataAttributesFunctionalitiesPermissionsItem]]):
        groups_permissions (Union[Unset, list[UpdateRoleDataAttributesGroupsPermissionsItem]]):
        incident_causes_permissions (Union[Unset, list[UpdateRoleDataAttributesIncidentCausesPermissionsItem]]):
        incident_feedbacks_permissions (Union[Unset, list[UpdateRoleDataAttributesIncidentFeedbacksPermissionsItem]]):
        incident_roles_permissions (Union[Unset, list[UpdateRoleDataAttributesIncidentRolesPermissionsItem]]):
        incident_types_permissions (Union[Unset, list[UpdateRoleDataAttributesIncidentTypesPermissionsItem]]):
        incidents_permissions (Union[Unset, list[UpdateRoleDataAttributesIncidentsPermissionsItem]]):
        integrations_permissions (Union[Unset, list[UpdateRoleDataAttributesIntegrationsPermissionsItem]]):
        invitations_permissions (Union[Unset, list[UpdateRoleDataAttributesInvitationsPermissionsItem]]):
        playbooks_permissions (Union[Unset, list[UpdateRoleDataAttributesPlaybooksPermissionsItem]]):
        private_incidents_permissions (Union[Unset, list[UpdateRoleDataAttributesPrivateIncidentsPermissionsItem]]):
        retrospective_permissions (Union[Unset, list[UpdateRoleDataAttributesRetrospectivePermissionsItem]]):
        roles_permissions (Union[Unset, list[UpdateRoleDataAttributesRolesPermissionsItem]]):
        secrets_permissions (Union[Unset, list[UpdateRoleDataAttributesSecretsPermissionsItem]]):
        services_permissions (Union[Unset, list[UpdateRoleDataAttributesServicesPermissionsItem]]):
        severities_permissions (Union[Unset, list[UpdateRoleDataAttributesSeveritiesPermissionsItem]]):
        status_pages_permissions (Union[Unset, list[UpdateRoleDataAttributesStatusPagesPermissionsItem]]):
        webhooks_permissions (Union[Unset, list[UpdateRoleDataAttributesWebhooksPermissionsItem]]):
        workflows_permissions (Union[Unset, list[UpdateRoleDataAttributesWorkflowsPermissionsItem]]):
    """

    name: Unset | str = UNSET
    incident_permission_set_id: None | Unset | str = UNSET
    is_deletable: Unset | bool = UNSET
    is_editable: Unset | bool = UNSET
    api_keys_permissions: Unset | list[UpdateRoleDataAttributesApiKeysPermissionsItem] = UNSET
    audits_permissions: Unset | list[UpdateRoleDataAttributesAuditsPermissionsItem] = UNSET
    billing_permissions: Unset | list[UpdateRoleDataAttributesBillingPermissionsItem] = UNSET
    environments_permissions: Unset | list[UpdateRoleDataAttributesEnvironmentsPermissionsItem] = UNSET
    form_fields_permissions: Unset | list[UpdateRoleDataAttributesFormFieldsPermissionsItem] = UNSET
    functionalities_permissions: Unset | list[UpdateRoleDataAttributesFunctionalitiesPermissionsItem] = UNSET
    groups_permissions: Unset | list[UpdateRoleDataAttributesGroupsPermissionsItem] = UNSET
    incident_causes_permissions: Unset | list[UpdateRoleDataAttributesIncidentCausesPermissionsItem] = UNSET
    incident_feedbacks_permissions: Unset | list[UpdateRoleDataAttributesIncidentFeedbacksPermissionsItem] = UNSET
    incident_roles_permissions: Unset | list[UpdateRoleDataAttributesIncidentRolesPermissionsItem] = UNSET
    incident_types_permissions: Unset | list[UpdateRoleDataAttributesIncidentTypesPermissionsItem] = UNSET
    incidents_permissions: Unset | list[UpdateRoleDataAttributesIncidentsPermissionsItem] = UNSET
    integrations_permissions: Unset | list[UpdateRoleDataAttributesIntegrationsPermissionsItem] = UNSET
    invitations_permissions: Unset | list[UpdateRoleDataAttributesInvitationsPermissionsItem] = UNSET
    playbooks_permissions: Unset | list[UpdateRoleDataAttributesPlaybooksPermissionsItem] = UNSET
    private_incidents_permissions: Unset | list[UpdateRoleDataAttributesPrivateIncidentsPermissionsItem] = UNSET
    retrospective_permissions: Unset | list[UpdateRoleDataAttributesRetrospectivePermissionsItem] = UNSET
    roles_permissions: Unset | list[UpdateRoleDataAttributesRolesPermissionsItem] = UNSET
    secrets_permissions: Unset | list[UpdateRoleDataAttributesSecretsPermissionsItem] = UNSET
    services_permissions: Unset | list[UpdateRoleDataAttributesServicesPermissionsItem] = UNSET
    severities_permissions: Unset | list[UpdateRoleDataAttributesSeveritiesPermissionsItem] = UNSET
    status_pages_permissions: Unset | list[UpdateRoleDataAttributesStatusPagesPermissionsItem] = UNSET
    webhooks_permissions: Unset | list[UpdateRoleDataAttributesWebhooksPermissionsItem] = UNSET
    workflows_permissions: Unset | list[UpdateRoleDataAttributesWorkflowsPermissionsItem] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        incident_permission_set_id: None | Unset | str
        if isinstance(self.incident_permission_set_id, Unset):
            incident_permission_set_id = UNSET
        else:
            incident_permission_set_id = self.incident_permission_set_id

        is_deletable = self.is_deletable

        is_editable = self.is_editable

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

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if incident_permission_set_id is not UNSET:
            field_dict["incident_permission_set_id"] = incident_permission_set_id
        if is_deletable is not UNSET:
            field_dict["is_deletable"] = is_deletable
        if is_editable is not UNSET:
            field_dict["is_editable"] = is_editable
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
        name = d.pop("name", UNSET)

        def _parse_incident_permission_set_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        incident_permission_set_id = _parse_incident_permission_set_id(d.pop("incident_permission_set_id", UNSET))

        is_deletable = d.pop("is_deletable", UNSET)

        is_editable = d.pop("is_editable", UNSET)

        api_keys_permissions = []
        _api_keys_permissions = d.pop("api_keys_permissions", UNSET)
        for api_keys_permissions_item_data in _api_keys_permissions or []:
            api_keys_permissions_item = check_update_role_data_attributes_api_keys_permissions_item(
                api_keys_permissions_item_data
            )

            api_keys_permissions.append(api_keys_permissions_item)

        audits_permissions = []
        _audits_permissions = d.pop("audits_permissions", UNSET)
        for audits_permissions_item_data in _audits_permissions or []:
            audits_permissions_item = check_update_role_data_attributes_audits_permissions_item(
                audits_permissions_item_data
            )

            audits_permissions.append(audits_permissions_item)

        billing_permissions = []
        _billing_permissions = d.pop("billing_permissions", UNSET)
        for billing_permissions_item_data in _billing_permissions or []:
            billing_permissions_item = check_update_role_data_attributes_billing_permissions_item(
                billing_permissions_item_data
            )

            billing_permissions.append(billing_permissions_item)

        environments_permissions = []
        _environments_permissions = d.pop("environments_permissions", UNSET)
        for environments_permissions_item_data in _environments_permissions or []:
            environments_permissions_item = check_update_role_data_attributes_environments_permissions_item(
                environments_permissions_item_data
            )

            environments_permissions.append(environments_permissions_item)

        form_fields_permissions = []
        _form_fields_permissions = d.pop("form_fields_permissions", UNSET)
        for form_fields_permissions_item_data in _form_fields_permissions or []:
            form_fields_permissions_item = check_update_role_data_attributes_form_fields_permissions_item(
                form_fields_permissions_item_data
            )

            form_fields_permissions.append(form_fields_permissions_item)

        functionalities_permissions = []
        _functionalities_permissions = d.pop("functionalities_permissions", UNSET)
        for functionalities_permissions_item_data in _functionalities_permissions or []:
            functionalities_permissions_item = check_update_role_data_attributes_functionalities_permissions_item(
                functionalities_permissions_item_data
            )

            functionalities_permissions.append(functionalities_permissions_item)

        groups_permissions = []
        _groups_permissions = d.pop("groups_permissions", UNSET)
        for groups_permissions_item_data in _groups_permissions or []:
            groups_permissions_item = check_update_role_data_attributes_groups_permissions_item(
                groups_permissions_item_data
            )

            groups_permissions.append(groups_permissions_item)

        incident_causes_permissions = []
        _incident_causes_permissions = d.pop("incident_causes_permissions", UNSET)
        for incident_causes_permissions_item_data in _incident_causes_permissions or []:
            incident_causes_permissions_item = check_update_role_data_attributes_incident_causes_permissions_item(
                incident_causes_permissions_item_data
            )

            incident_causes_permissions.append(incident_causes_permissions_item)

        incident_feedbacks_permissions = []
        _incident_feedbacks_permissions = d.pop("incident_feedbacks_permissions", UNSET)
        for incident_feedbacks_permissions_item_data in _incident_feedbacks_permissions or []:
            incident_feedbacks_permissions_item = check_update_role_data_attributes_incident_feedbacks_permissions_item(
                incident_feedbacks_permissions_item_data
            )

            incident_feedbacks_permissions.append(incident_feedbacks_permissions_item)

        incident_roles_permissions = []
        _incident_roles_permissions = d.pop("incident_roles_permissions", UNSET)
        for incident_roles_permissions_item_data in _incident_roles_permissions or []:
            incident_roles_permissions_item = check_update_role_data_attributes_incident_roles_permissions_item(
                incident_roles_permissions_item_data
            )

            incident_roles_permissions.append(incident_roles_permissions_item)

        incident_types_permissions = []
        _incident_types_permissions = d.pop("incident_types_permissions", UNSET)
        for incident_types_permissions_item_data in _incident_types_permissions or []:
            incident_types_permissions_item = check_update_role_data_attributes_incident_types_permissions_item(
                incident_types_permissions_item_data
            )

            incident_types_permissions.append(incident_types_permissions_item)

        incidents_permissions = []
        _incidents_permissions = d.pop("incidents_permissions", UNSET)
        for incidents_permissions_item_data in _incidents_permissions or []:
            incidents_permissions_item = check_update_role_data_attributes_incidents_permissions_item(
                incidents_permissions_item_data
            )

            incidents_permissions.append(incidents_permissions_item)

        integrations_permissions = []
        _integrations_permissions = d.pop("integrations_permissions", UNSET)
        for integrations_permissions_item_data in _integrations_permissions or []:
            integrations_permissions_item = check_update_role_data_attributes_integrations_permissions_item(
                integrations_permissions_item_data
            )

            integrations_permissions.append(integrations_permissions_item)

        invitations_permissions = []
        _invitations_permissions = d.pop("invitations_permissions", UNSET)
        for invitations_permissions_item_data in _invitations_permissions or []:
            invitations_permissions_item = check_update_role_data_attributes_invitations_permissions_item(
                invitations_permissions_item_data
            )

            invitations_permissions.append(invitations_permissions_item)

        playbooks_permissions = []
        _playbooks_permissions = d.pop("playbooks_permissions", UNSET)
        for playbooks_permissions_item_data in _playbooks_permissions or []:
            playbooks_permissions_item = check_update_role_data_attributes_playbooks_permissions_item(
                playbooks_permissions_item_data
            )

            playbooks_permissions.append(playbooks_permissions_item)

        private_incidents_permissions = []
        _private_incidents_permissions = d.pop("private_incidents_permissions", UNSET)
        for private_incidents_permissions_item_data in _private_incidents_permissions or []:
            private_incidents_permissions_item = check_update_role_data_attributes_private_incidents_permissions_item(
                private_incidents_permissions_item_data
            )

            private_incidents_permissions.append(private_incidents_permissions_item)

        retrospective_permissions = []
        _retrospective_permissions = d.pop("retrospective_permissions", UNSET)
        for retrospective_permissions_item_data in _retrospective_permissions or []:
            retrospective_permissions_item = check_update_role_data_attributes_retrospective_permissions_item(
                retrospective_permissions_item_data
            )

            retrospective_permissions.append(retrospective_permissions_item)

        roles_permissions = []
        _roles_permissions = d.pop("roles_permissions", UNSET)
        for roles_permissions_item_data in _roles_permissions or []:
            roles_permissions_item = check_update_role_data_attributes_roles_permissions_item(
                roles_permissions_item_data
            )

            roles_permissions.append(roles_permissions_item)

        secrets_permissions = []
        _secrets_permissions = d.pop("secrets_permissions", UNSET)
        for secrets_permissions_item_data in _secrets_permissions or []:
            secrets_permissions_item = check_update_role_data_attributes_secrets_permissions_item(
                secrets_permissions_item_data
            )

            secrets_permissions.append(secrets_permissions_item)

        services_permissions = []
        _services_permissions = d.pop("services_permissions", UNSET)
        for services_permissions_item_data in _services_permissions or []:
            services_permissions_item = check_update_role_data_attributes_services_permissions_item(
                services_permissions_item_data
            )

            services_permissions.append(services_permissions_item)

        severities_permissions = []
        _severities_permissions = d.pop("severities_permissions", UNSET)
        for severities_permissions_item_data in _severities_permissions or []:
            severities_permissions_item = check_update_role_data_attributes_severities_permissions_item(
                severities_permissions_item_data
            )

            severities_permissions.append(severities_permissions_item)

        status_pages_permissions = []
        _status_pages_permissions = d.pop("status_pages_permissions", UNSET)
        for status_pages_permissions_item_data in _status_pages_permissions or []:
            status_pages_permissions_item = check_update_role_data_attributes_status_pages_permissions_item(
                status_pages_permissions_item_data
            )

            status_pages_permissions.append(status_pages_permissions_item)

        webhooks_permissions = []
        _webhooks_permissions = d.pop("webhooks_permissions", UNSET)
        for webhooks_permissions_item_data in _webhooks_permissions or []:
            webhooks_permissions_item = check_update_role_data_attributes_webhooks_permissions_item(
                webhooks_permissions_item_data
            )

            webhooks_permissions.append(webhooks_permissions_item)

        workflows_permissions = []
        _workflows_permissions = d.pop("workflows_permissions", UNSET)
        for workflows_permissions_item_data in _workflows_permissions or []:
            workflows_permissions_item = check_update_role_data_attributes_workflows_permissions_item(
                workflows_permissions_item_data
            )

            workflows_permissions.append(workflows_permissions_item)

        update_role_data_attributes = cls(
            name=name,
            incident_permission_set_id=incident_permission_set_id,
            is_deletable=is_deletable,
            is_editable=is_editable,
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
            retrospective_permissions=retrospective_permissions,
            roles_permissions=roles_permissions,
            secrets_permissions=secrets_permissions,
            services_permissions=services_permissions,
            severities_permissions=severities_permissions,
            status_pages_permissions=status_pages_permissions,
            webhooks_permissions=webhooks_permissions,
            workflows_permissions=workflows_permissions,
        )

        return update_role_data_attributes
