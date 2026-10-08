from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_upsert_teams_entities_item_schedule_override_policy import (
    BulkUpsertTeamsEntitiesItemScheduleOverridePolicy,
    check_bulk_upsert_teams_entities_item_schedule_override_policy,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_upsert_teams_entities_item_fields_item import BulkUpsertTeamsEntitiesItemFieldsItem


T = TypeVar("T", bound="BulkUpsertTeamsEntitiesItem")


@_attrs_define
class BulkUpsertTeamsEntitiesItem:
    """
    Attributes:
        external_id (str): External identifier used as the upsert key. Unique per team.
        name (str | Unset): Required for new records. Optional for updates.
        description (None | str | Unset):
        public_description (None | str | Unset):
        schedule_override_policy (BulkUpsertTeamsEntitiesItemScheduleOverridePolicy | Unset): Who can create and update
            overrides for schedules owned by this team: `everyone` in the organization, only team `members`, or only team
            `admins`. Users still need override permission from their on-call role. Only available when the team-level
            schedule override policy feature is enabled for the organization. Requests that set it while that feature is
            disabled are rejected.
        color (None | str | Unset):
        position (int | None | Unset):
        notify_emails (list[str] | None | Unset):
        pagerduty_id (None | str | Unset):
        pagerduty_service_id (None | str | Unset):
        opsgenie_id (None | str | Unset):
        victor_ops_id (None | str | Unset):
        pagertree_id (None | str | Unset):
        backstage_id (None | str | Unset):
        cortex_id (None | str | Unset):
        opslevel_id (None | str | Unset):
        service_now_ci_sys_id (None | str | Unset):
        alerts_email_enabled (bool | None | Unset):
        fields (list[BulkUpsertTeamsEntitiesItemFieldsItem] | Unset): Catalog property values (merge semantics: only
            mentioned fields written).
    """

    external_id: str
    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    public_description: None | str | Unset = UNSET
    schedule_override_policy: BulkUpsertTeamsEntitiesItemScheduleOverridePolicy | Unset = UNSET
    color: None | str | Unset = UNSET
    position: int | None | Unset = UNSET
    notify_emails: list[str] | None | Unset = UNSET
    pagerduty_id: None | str | Unset = UNSET
    pagerduty_service_id: None | str | Unset = UNSET
    opsgenie_id: None | str | Unset = UNSET
    victor_ops_id: None | str | Unset = UNSET
    pagertree_id: None | str | Unset = UNSET
    backstage_id: None | str | Unset = UNSET
    cortex_id: None | str | Unset = UNSET
    opslevel_id: None | str | Unset = UNSET
    service_now_ci_sys_id: None | str | Unset = UNSET
    alerts_email_enabled: bool | None | Unset = UNSET
    fields: list[BulkUpsertTeamsEntitiesItemFieldsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        public_description: None | str | Unset
        if isinstance(self.public_description, Unset):
            public_description = UNSET
        else:
            public_description = self.public_description

        schedule_override_policy: str | Unset = UNSET
        if not isinstance(self.schedule_override_policy, Unset):
            schedule_override_policy = self.schedule_override_policy

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        notify_emails: list[str] | None | Unset
        if isinstance(self.notify_emails, Unset):
            notify_emails = UNSET
        elif isinstance(self.notify_emails, list):
            notify_emails = self.notify_emails

        else:
            notify_emails = self.notify_emails

        pagerduty_id: None | str | Unset
        if isinstance(self.pagerduty_id, Unset):
            pagerduty_id = UNSET
        else:
            pagerduty_id = self.pagerduty_id

        pagerduty_service_id: None | str | Unset
        if isinstance(self.pagerduty_service_id, Unset):
            pagerduty_service_id = UNSET
        else:
            pagerduty_service_id = self.pagerduty_service_id

        opsgenie_id: None | str | Unset
        if isinstance(self.opsgenie_id, Unset):
            opsgenie_id = UNSET
        else:
            opsgenie_id = self.opsgenie_id

        victor_ops_id: None | str | Unset
        if isinstance(self.victor_ops_id, Unset):
            victor_ops_id = UNSET
        else:
            victor_ops_id = self.victor_ops_id

        pagertree_id: None | str | Unset
        if isinstance(self.pagertree_id, Unset):
            pagertree_id = UNSET
        else:
            pagertree_id = self.pagertree_id

        backstage_id: None | str | Unset
        if isinstance(self.backstage_id, Unset):
            backstage_id = UNSET
        else:
            backstage_id = self.backstage_id

        cortex_id: None | str | Unset
        if isinstance(self.cortex_id, Unset):
            cortex_id = UNSET
        else:
            cortex_id = self.cortex_id

        opslevel_id: None | str | Unset
        if isinstance(self.opslevel_id, Unset):
            opslevel_id = UNSET
        else:
            opslevel_id = self.opslevel_id

        service_now_ci_sys_id: None | str | Unset
        if isinstance(self.service_now_ci_sys_id, Unset):
            service_now_ci_sys_id = UNSET
        else:
            service_now_ci_sys_id = self.service_now_ci_sys_id

        alerts_email_enabled: bool | None | Unset
        if isinstance(self.alerts_email_enabled, Unset):
            alerts_email_enabled = UNSET
        else:
            alerts_email_enabled = self.alerts_email_enabled

        fields: list[dict[str, Any]] | Unset = UNSET
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
        if schedule_override_policy is not UNSET:
            field_dict["schedule_override_policy"] = schedule_override_policy
        if color is not UNSET:
            field_dict["color"] = color
        if position is not UNSET:
            field_dict["position"] = position
        if notify_emails is not UNSET:
            field_dict["notify_emails"] = notify_emails
        if pagerduty_id is not UNSET:
            field_dict["pagerduty_id"] = pagerduty_id
        if pagerduty_service_id is not UNSET:
            field_dict["pagerduty_service_id"] = pagerduty_service_id
        if opsgenie_id is not UNSET:
            field_dict["opsgenie_id"] = opsgenie_id
        if victor_ops_id is not UNSET:
            field_dict["victor_ops_id"] = victor_ops_id
        if pagertree_id is not UNSET:
            field_dict["pagertree_id"] = pagertree_id
        if backstage_id is not UNSET:
            field_dict["backstage_id"] = backstage_id
        if cortex_id is not UNSET:
            field_dict["cortex_id"] = cortex_id
        if opslevel_id is not UNSET:
            field_dict["opslevel_id"] = opslevel_id
        if service_now_ci_sys_id is not UNSET:
            field_dict["service_now_ci_sys_id"] = service_now_ci_sys_id
        if alerts_email_enabled is not UNSET:
            field_dict["alerts_email_enabled"] = alerts_email_enabled
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_upsert_teams_entities_item_fields_item import BulkUpsertTeamsEntitiesItemFieldsItem

        d = dict(src_dict)
        external_id = d.pop("external_id")

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_public_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_description = _parse_public_description(d.pop("public_description", UNSET))

        _schedule_override_policy = d.pop("schedule_override_policy", UNSET)
        schedule_override_policy: BulkUpsertTeamsEntitiesItemScheduleOverridePolicy | Unset
        if isinstance(_schedule_override_policy, Unset):
            schedule_override_policy = UNSET
        else:
            schedule_override_policy = check_bulk_upsert_teams_entities_item_schedule_override_policy(
                _schedule_override_policy
            )

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

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

        def _parse_pagerduty_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pagerduty_id = _parse_pagerduty_id(d.pop("pagerduty_id", UNSET))

        def _parse_pagerduty_service_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pagerduty_service_id = _parse_pagerduty_service_id(d.pop("pagerduty_service_id", UNSET))

        def _parse_opsgenie_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opsgenie_id = _parse_opsgenie_id(d.pop("opsgenie_id", UNSET))

        def _parse_victor_ops_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        victor_ops_id = _parse_victor_ops_id(d.pop("victor_ops_id", UNSET))

        def _parse_pagertree_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pagertree_id = _parse_pagertree_id(d.pop("pagertree_id", UNSET))

        def _parse_backstage_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backstage_id = _parse_backstage_id(d.pop("backstage_id", UNSET))

        def _parse_cortex_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cortex_id = _parse_cortex_id(d.pop("cortex_id", UNSET))

        def _parse_opslevel_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opslevel_id = _parse_opslevel_id(d.pop("opslevel_id", UNSET))

        def _parse_service_now_ci_sys_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_now_ci_sys_id = _parse_service_now_ci_sys_id(d.pop("service_now_ci_sys_id", UNSET))

        def _parse_alerts_email_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        alerts_email_enabled = _parse_alerts_email_enabled(d.pop("alerts_email_enabled", UNSET))

        _fields = d.pop("fields", UNSET)
        fields: list[BulkUpsertTeamsEntitiesItemFieldsItem] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = BulkUpsertTeamsEntitiesItemFieldsItem.from_dict(fields_item_data)

                fields.append(fields_item)

        bulk_upsert_teams_entities_item = cls(
            external_id=external_id,
            name=name,
            description=description,
            public_description=public_description,
            schedule_override_policy=schedule_override_policy,
            color=color,
            position=position,
            notify_emails=notify_emails,
            pagerduty_id=pagerduty_id,
            pagerduty_service_id=pagerduty_service_id,
            opsgenie_id=opsgenie_id,
            victor_ops_id=victor_ops_id,
            pagertree_id=pagertree_id,
            backstage_id=backstage_id,
            cortex_id=cortex_id,
            opslevel_id=opslevel_id,
            service_now_ci_sys_id=service_now_ci_sys_id,
            alerts_email_enabled=alerts_email_enabled,
            fields=fields,
        )

        bulk_upsert_teams_entities_item.additional_properties = d
        return bulk_upsert_teams_entities_item

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
