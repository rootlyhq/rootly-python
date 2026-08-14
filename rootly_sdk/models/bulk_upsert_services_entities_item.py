from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_upsert_services_entities_item_fields_item import BulkUpsertServicesEntitiesItemFieldsItem


T = TypeVar("T", bound="BulkUpsertServicesEntitiesItem")


@_attrs_define
class BulkUpsertServicesEntitiesItem:
    """
    Attributes:
        external_id (str): External identifier used as the upsert key. Unique per team.
        name (Union[Unset, str]): Required for new records. Optional for updates.
        description (Union[None, Unset, str]):
        public_description (Union[None, Unset, str]):
        color (Union[None, Unset, str]):
        position (Union[None, Unset, int]):
        show_uptime (Union[None, Unset, bool]):
        show_uptime_last_days (Union[None, Unset, int]):
        github_repository_name (Union[None, Unset, str]):
        github_repository_branch (Union[None, Unset, str]):
        gitlab_repository_name (Union[None, Unset, str]):
        gitlab_repository_branch (Union[None, Unset, str]):
        kubernetes_deployment_name (Union[None, Unset, str]):
        pagerduty_id (Union[None, Unset, str]):
        opsgenie_id (Union[None, Unset, str]):
        opsgenie_team_id (Union[None, Unset, str]):
        cortex_id (Union[None, Unset, str]):
        opslevel_id (Union[None, Unset, str]):
        backstage_id (Union[None, Unset, str]):
        service_now_ci_sys_id (Union[None, Unset, str]):
        notify_emails (Union[None, Unset, list[str]]):
        alerts_email_enabled (Union[None, Unset, bool]):
        fields (Union[Unset, list['BulkUpsertServicesEntitiesItemFieldsItem']]): Catalog property values (merge
            semantics: only mentioned fields written).
    """

    external_id: str
    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    public_description: Union[None, Unset, str] = UNSET
    color: Union[None, Unset, str] = UNSET
    position: Union[None, Unset, int] = UNSET
    show_uptime: Union[None, Unset, bool] = UNSET
    show_uptime_last_days: Union[None, Unset, int] = UNSET
    github_repository_name: Union[None, Unset, str] = UNSET
    github_repository_branch: Union[None, Unset, str] = UNSET
    gitlab_repository_name: Union[None, Unset, str] = UNSET
    gitlab_repository_branch: Union[None, Unset, str] = UNSET
    kubernetes_deployment_name: Union[None, Unset, str] = UNSET
    pagerduty_id: Union[None, Unset, str] = UNSET
    opsgenie_id: Union[None, Unset, str] = UNSET
    opsgenie_team_id: Union[None, Unset, str] = UNSET
    cortex_id: Union[None, Unset, str] = UNSET
    opslevel_id: Union[None, Unset, str] = UNSET
    backstage_id: Union[None, Unset, str] = UNSET
    service_now_ci_sys_id: Union[None, Unset, str] = UNSET
    notify_emails: Union[None, Unset, list[str]] = UNSET
    alerts_email_enabled: Union[None, Unset, bool] = UNSET
    fields: Union[Unset, list["BulkUpsertServicesEntitiesItemFieldsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        public_description: Union[None, Unset, str]
        if isinstance(self.public_description, Unset):
            public_description = UNSET
        else:
            public_description = self.public_description

        color: Union[None, Unset, str]
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        position: Union[None, Unset, int]
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        show_uptime: Union[None, Unset, bool]
        if isinstance(self.show_uptime, Unset):
            show_uptime = UNSET
        else:
            show_uptime = self.show_uptime

        show_uptime_last_days: Union[None, Unset, int]
        if isinstance(self.show_uptime_last_days, Unset):
            show_uptime_last_days = UNSET
        else:
            show_uptime_last_days = self.show_uptime_last_days

        github_repository_name: Union[None, Unset, str]
        if isinstance(self.github_repository_name, Unset):
            github_repository_name = UNSET
        else:
            github_repository_name = self.github_repository_name

        github_repository_branch: Union[None, Unset, str]
        if isinstance(self.github_repository_branch, Unset):
            github_repository_branch = UNSET
        else:
            github_repository_branch = self.github_repository_branch

        gitlab_repository_name: Union[None, Unset, str]
        if isinstance(self.gitlab_repository_name, Unset):
            gitlab_repository_name = UNSET
        else:
            gitlab_repository_name = self.gitlab_repository_name

        gitlab_repository_branch: Union[None, Unset, str]
        if isinstance(self.gitlab_repository_branch, Unset):
            gitlab_repository_branch = UNSET
        else:
            gitlab_repository_branch = self.gitlab_repository_branch

        kubernetes_deployment_name: Union[None, Unset, str]
        if isinstance(self.kubernetes_deployment_name, Unset):
            kubernetes_deployment_name = UNSET
        else:
            kubernetes_deployment_name = self.kubernetes_deployment_name

        pagerduty_id: Union[None, Unset, str]
        if isinstance(self.pagerduty_id, Unset):
            pagerduty_id = UNSET
        else:
            pagerduty_id = self.pagerduty_id

        opsgenie_id: Union[None, Unset, str]
        if isinstance(self.opsgenie_id, Unset):
            opsgenie_id = UNSET
        else:
            opsgenie_id = self.opsgenie_id

        opsgenie_team_id: Union[None, Unset, str]
        if isinstance(self.opsgenie_team_id, Unset):
            opsgenie_team_id = UNSET
        else:
            opsgenie_team_id = self.opsgenie_team_id

        cortex_id: Union[None, Unset, str]
        if isinstance(self.cortex_id, Unset):
            cortex_id = UNSET
        else:
            cortex_id = self.cortex_id

        opslevel_id: Union[None, Unset, str]
        if isinstance(self.opslevel_id, Unset):
            opslevel_id = UNSET
        else:
            opslevel_id = self.opslevel_id

        backstage_id: Union[None, Unset, str]
        if isinstance(self.backstage_id, Unset):
            backstage_id = UNSET
        else:
            backstage_id = self.backstage_id

        service_now_ci_sys_id: Union[None, Unset, str]
        if isinstance(self.service_now_ci_sys_id, Unset):
            service_now_ci_sys_id = UNSET
        else:
            service_now_ci_sys_id = self.service_now_ci_sys_id

        notify_emails: Union[None, Unset, list[str]]
        if isinstance(self.notify_emails, Unset):
            notify_emails = UNSET
        elif isinstance(self.notify_emails, list):
            notify_emails = self.notify_emails

        else:
            notify_emails = self.notify_emails

        alerts_email_enabled: Union[None, Unset, bool]
        if isinstance(self.alerts_email_enabled, Unset):
            alerts_email_enabled = UNSET
        else:
            alerts_email_enabled = self.alerts_email_enabled

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if public_description is not UNSET:
            field_dict["public_description"] = public_description
        if color is not UNSET:
            field_dict["color"] = color
        if position is not UNSET:
            field_dict["position"] = position
        if show_uptime is not UNSET:
            field_dict["show_uptime"] = show_uptime
        if show_uptime_last_days is not UNSET:
            field_dict["show_uptime_last_days"] = show_uptime_last_days
        if github_repository_name is not UNSET:
            field_dict["github_repository_name"] = github_repository_name
        if github_repository_branch is not UNSET:
            field_dict["github_repository_branch"] = github_repository_branch
        if gitlab_repository_name is not UNSET:
            field_dict["gitlab_repository_name"] = gitlab_repository_name
        if gitlab_repository_branch is not UNSET:
            field_dict["gitlab_repository_branch"] = gitlab_repository_branch
        if kubernetes_deployment_name is not UNSET:
            field_dict["kubernetes_deployment_name"] = kubernetes_deployment_name
        if pagerduty_id is not UNSET:
            field_dict["pagerduty_id"] = pagerduty_id
        if opsgenie_id is not UNSET:
            field_dict["opsgenie_id"] = opsgenie_id
        if opsgenie_team_id is not UNSET:
            field_dict["opsgenie_team_id"] = opsgenie_team_id
        if cortex_id is not UNSET:
            field_dict["cortex_id"] = cortex_id
        if opslevel_id is not UNSET:
            field_dict["opslevel_id"] = opslevel_id
        if backstage_id is not UNSET:
            field_dict["backstage_id"] = backstage_id
        if service_now_ci_sys_id is not UNSET:
            field_dict["service_now_ci_sys_id"] = service_now_ci_sys_id
        if notify_emails is not UNSET:
            field_dict["notify_emails"] = notify_emails
        if alerts_email_enabled is not UNSET:
            field_dict["alerts_email_enabled"] = alerts_email_enabled
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_upsert_services_entities_item_fields_item import BulkUpsertServicesEntitiesItemFieldsItem

        d = dict(src_dict)
        external_id = d.pop("external_id")

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_public_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        public_description = _parse_public_description(d.pop("public_description", UNSET))

        def _parse_color(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_position(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_show_uptime(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        show_uptime = _parse_show_uptime(d.pop("show_uptime", UNSET))

        def _parse_show_uptime_last_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        show_uptime_last_days = _parse_show_uptime_last_days(d.pop("show_uptime_last_days", UNSET))

        def _parse_github_repository_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        github_repository_name = _parse_github_repository_name(d.pop("github_repository_name", UNSET))

        def _parse_github_repository_branch(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        github_repository_branch = _parse_github_repository_branch(d.pop("github_repository_branch", UNSET))

        def _parse_gitlab_repository_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        gitlab_repository_name = _parse_gitlab_repository_name(d.pop("gitlab_repository_name", UNSET))

        def _parse_gitlab_repository_branch(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        gitlab_repository_branch = _parse_gitlab_repository_branch(d.pop("gitlab_repository_branch", UNSET))

        def _parse_kubernetes_deployment_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        kubernetes_deployment_name = _parse_kubernetes_deployment_name(d.pop("kubernetes_deployment_name", UNSET))

        def _parse_pagerduty_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pagerduty_id = _parse_pagerduty_id(d.pop("pagerduty_id", UNSET))

        def _parse_opsgenie_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        opsgenie_id = _parse_opsgenie_id(d.pop("opsgenie_id", UNSET))

        def _parse_opsgenie_team_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        opsgenie_team_id = _parse_opsgenie_team_id(d.pop("opsgenie_team_id", UNSET))

        def _parse_cortex_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cortex_id = _parse_cortex_id(d.pop("cortex_id", UNSET))

        def _parse_opslevel_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        opslevel_id = _parse_opslevel_id(d.pop("opslevel_id", UNSET))

        def _parse_backstage_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backstage_id = _parse_backstage_id(d.pop("backstage_id", UNSET))

        def _parse_service_now_ci_sys_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_now_ci_sys_id = _parse_service_now_ci_sys_id(d.pop("service_now_ci_sys_id", UNSET))

        def _parse_notify_emails(data: object) -> Union[None, Unset, list[str]]:
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
            return cast(Union[None, Unset, list[str]], data)

        notify_emails = _parse_notify_emails(d.pop("notify_emails", UNSET))

        def _parse_alerts_email_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        alerts_email_enabled = _parse_alerts_email_enabled(d.pop("alerts_email_enabled", UNSET))

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = BulkUpsertServicesEntitiesItemFieldsItem.from_dict(fields_item_data)

            fields.append(fields_item)

        bulk_upsert_services_entities_item = cls(
            external_id=external_id,
            name=name,
            description=description,
            public_description=public_description,
            color=color,
            position=position,
            show_uptime=show_uptime,
            show_uptime_last_days=show_uptime_last_days,
            github_repository_name=github_repository_name,
            github_repository_branch=github_repository_branch,
            gitlab_repository_name=gitlab_repository_name,
            gitlab_repository_branch=gitlab_repository_branch,
            kubernetes_deployment_name=kubernetes_deployment_name,
            pagerduty_id=pagerduty_id,
            opsgenie_id=opsgenie_id,
            opsgenie_team_id=opsgenie_team_id,
            cortex_id=cortex_id,
            opslevel_id=opslevel_id,
            backstage_id=backstage_id,
            service_now_ci_sys_id=service_now_ci_sys_id,
            notify_emails=notify_emails,
            alerts_email_enabled=alerts_email_enabled,
            fields=fields,
        )

        bulk_upsert_services_entities_item.additional_properties = d
        return bulk_upsert_services_entities_item

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
