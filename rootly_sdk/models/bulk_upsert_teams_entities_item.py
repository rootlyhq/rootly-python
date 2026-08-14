from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_upsert_teams_entities_item_fields_item import BulkUpsertTeamsEntitiesItemFieldsItem


T = TypeVar("T", bound="BulkUpsertTeamsEntitiesItem")


@_attrs_define
class BulkUpsertTeamsEntitiesItem:
    """
    Attributes:
        external_id (str): External identifier used as the upsert key. Unique per team.
        name (Union[Unset, str]): Required for new records. Optional for updates.
        description (Union[None, Unset, str]):
        public_description (Union[None, Unset, str]):
        color (Union[None, Unset, str]):
        position (Union[None, Unset, int]):
        notify_emails (Union[None, Unset, list[str]]):
        pagerduty_id (Union[None, Unset, str]):
        pagerduty_service_id (Union[None, Unset, str]):
        opsgenie_id (Union[None, Unset, str]):
        victor_ops_id (Union[None, Unset, str]):
        pagertree_id (Union[None, Unset, str]):
        backstage_id (Union[None, Unset, str]):
        cortex_id (Union[None, Unset, str]):
        opslevel_id (Union[None, Unset, str]):
        service_now_ci_sys_id (Union[None, Unset, str]):
        alerts_email_enabled (Union[None, Unset, bool]):
        fields (Union[Unset, list['BulkUpsertTeamsEntitiesItemFieldsItem']]): Catalog property values (merge semantics:
            only mentioned fields written).
    """

    external_id: str
    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    public_description: None | Unset | str = UNSET
    color: None | Unset | str = UNSET
    position: None | Unset | int = UNSET
    notify_emails: None | Unset | list[str] = UNSET
    pagerduty_id: None | Unset | str = UNSET
    pagerduty_service_id: None | Unset | str = UNSET
    opsgenie_id: None | Unset | str = UNSET
    victor_ops_id: None | Unset | str = UNSET
    pagertree_id: None | Unset | str = UNSET
    backstage_id: None | Unset | str = UNSET
    cortex_id: None | Unset | str = UNSET
    opslevel_id: None | Unset | str = UNSET
    service_now_ci_sys_id: None | Unset | str = UNSET
    alerts_email_enabled: None | Unset | bool = UNSET
    fields: Unset | list["BulkUpsertTeamsEntitiesItemFieldsItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        public_description: None | Unset | str
        if isinstance(self.public_description, Unset):
            public_description = UNSET
        else:
            public_description = self.public_description

        color: None | Unset | str
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        position: None | Unset | int
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        notify_emails: None | Unset | list[str]
        if isinstance(self.notify_emails, Unset):
            notify_emails = UNSET
        elif isinstance(self.notify_emails, list):
            notify_emails = self.notify_emails

        else:
            notify_emails = self.notify_emails

        pagerduty_id: None | Unset | str
        if isinstance(self.pagerduty_id, Unset):
            pagerduty_id = UNSET
        else:
            pagerduty_id = self.pagerduty_id

        pagerduty_service_id: None | Unset | str
        if isinstance(self.pagerduty_service_id, Unset):
            pagerduty_service_id = UNSET
        else:
            pagerduty_service_id = self.pagerduty_service_id

        opsgenie_id: None | Unset | str
        if isinstance(self.opsgenie_id, Unset):
            opsgenie_id = UNSET
        else:
            opsgenie_id = self.opsgenie_id

        victor_ops_id: None | Unset | str
        if isinstance(self.victor_ops_id, Unset):
            victor_ops_id = UNSET
        else:
            victor_ops_id = self.victor_ops_id

        pagertree_id: None | Unset | str
        if isinstance(self.pagertree_id, Unset):
            pagertree_id = UNSET
        else:
            pagertree_id = self.pagertree_id

        backstage_id: None | Unset | str
        if isinstance(self.backstage_id, Unset):
            backstage_id = UNSET
        else:
            backstage_id = self.backstage_id

        cortex_id: None | Unset | str
        if isinstance(self.cortex_id, Unset):
            cortex_id = UNSET
        else:
            cortex_id = self.cortex_id

        opslevel_id: None | Unset | str
        if isinstance(self.opslevel_id, Unset):
            opslevel_id = UNSET
        else:
            opslevel_id = self.opslevel_id

        service_now_ci_sys_id: None | Unset | str
        if isinstance(self.service_now_ci_sys_id, Unset):
            service_now_ci_sys_id = UNSET
        else:
            service_now_ci_sys_id = self.service_now_ci_sys_id

        alerts_email_enabled: None | Unset | bool
        if isinstance(self.alerts_email_enabled, Unset):
            alerts_email_enabled = UNSET
        else:
            alerts_email_enabled = self.alerts_email_enabled

        fields: Unset | list[dict[str, Any]] = UNSET
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

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_public_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        public_description = _parse_public_description(d.pop("public_description", UNSET))

        def _parse_color(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_position(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_notify_emails(data: object) -> None | Unset | list[str]:
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
            return cast(None | Unset | list[str], data)

        notify_emails = _parse_notify_emails(d.pop("notify_emails", UNSET))

        def _parse_pagerduty_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        pagerduty_id = _parse_pagerduty_id(d.pop("pagerduty_id", UNSET))

        def _parse_pagerduty_service_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        pagerduty_service_id = _parse_pagerduty_service_id(d.pop("pagerduty_service_id", UNSET))

        def _parse_opsgenie_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        opsgenie_id = _parse_opsgenie_id(d.pop("opsgenie_id", UNSET))

        def _parse_victor_ops_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        victor_ops_id = _parse_victor_ops_id(d.pop("victor_ops_id", UNSET))

        def _parse_pagertree_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        pagertree_id = _parse_pagertree_id(d.pop("pagertree_id", UNSET))

        def _parse_backstage_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        backstage_id = _parse_backstage_id(d.pop("backstage_id", UNSET))

        def _parse_cortex_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        cortex_id = _parse_cortex_id(d.pop("cortex_id", UNSET))

        def _parse_opslevel_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        opslevel_id = _parse_opslevel_id(d.pop("opslevel_id", UNSET))

        def _parse_service_now_ci_sys_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        service_now_ci_sys_id = _parse_service_now_ci_sys_id(d.pop("service_now_ci_sys_id", UNSET))

        def _parse_alerts_email_enabled(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        alerts_email_enabled = _parse_alerts_email_enabled(d.pop("alerts_email_enabled", UNSET))

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = BulkUpsertTeamsEntitiesItemFieldsItem.from_dict(fields_item_data)

            fields.append(fields_item)

        bulk_upsert_teams_entities_item = cls(
            external_id=external_id,
            name=name,
            description=description,
            public_description=public_description,
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
