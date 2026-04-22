from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.functionality_properties_type_0_item import FunctionalityPropertiesType0Item
    from ..models.functionality_slack_aliases_type_0_item import FunctionalitySlackAliasesType0Item
    from ..models.functionality_slack_channels_type_0_item import FunctionalitySlackChannelsType0Item


T = TypeVar("T", bound="Functionality")


@_attrs_define
class Functionality:
    """
    Attributes:
        name (str): The name of the functionality
        created_at (str): Date of creation
        updated_at (str): Date of last update
        slug (str | Unset): The slug of the functionality
        description (None | str | Unset): The description of the functionality
        public_description (None | str | Unset): The public description of the functionality
        notify_emails (list[str] | None | Unset): Emails attached to the functionality
        color (None | str | Unset): The hex color of the functionality
        backstage_id (None | str | Unset): The Backstage entity id associated to this functionality. eg:
            :namespace/:kind/:entity_name
        external_id (None | str | Unset): The external id associated to this functionality
        pagerduty_id (None | str | Unset): The PagerDuty service id associated to this functionality
        opsgenie_id (None | str | Unset): The Opsgenie service id associated to this functionality
        opsgenie_team_id (None | str | Unset): The Opsgenie team id associated to this functionality
        cortex_id (None | str | Unset): The Cortex group id associated to this functionality
        service_now_ci_sys_id (None | str | Unset): The Service Now CI sys id associated to this functionality
        position (int | None | Unset): Position of the functionality
        environment_ids (list[str] | None | Unset): Environments associated with this functionality
        service_ids (list[str] | None | Unset): Services associated with this functionality
        owner_group_ids (list[str] | None | Unset): Owner Teams associated with this functionality
        owner_user_ids (list[int] | None | Unset): Owner Users associated with this functionality
        slack_channels (list[FunctionalitySlackChannelsType0Item] | None | Unset): Slack Channels associated with this
            functionality
        slack_aliases (list[FunctionalitySlackAliasesType0Item] | None | Unset): Slack Aliases associated with this
            functionality
        properties (list[FunctionalityPropertiesType0Item] | None | Unset): Array of property values for this
            functionality.
    """

    name: str
    created_at: str
    updated_at: str
    slug: str | Unset = UNSET
    description: None | str | Unset = UNSET
    public_description: None | str | Unset = UNSET
    notify_emails: list[str] | None | Unset = UNSET
    color: None | str | Unset = UNSET
    backstage_id: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    pagerduty_id: None | str | Unset = UNSET
    opsgenie_id: None | str | Unset = UNSET
    opsgenie_team_id: None | str | Unset = UNSET
    cortex_id: None | str | Unset = UNSET
    service_now_ci_sys_id: None | str | Unset = UNSET
    position: int | None | Unset = UNSET
    environment_ids: list[str] | None | Unset = UNSET
    service_ids: list[str] | None | Unset = UNSET
    owner_group_ids: list[str] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    slack_channels: list[FunctionalitySlackChannelsType0Item] | None | Unset = UNSET
    slack_aliases: list[FunctionalitySlackAliasesType0Item] | None | Unset = UNSET
    properties: list[FunctionalityPropertiesType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

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

        notify_emails: list[str] | None | Unset
        if isinstance(self.notify_emails, Unset):
            notify_emails = UNSET
        elif isinstance(self.notify_emails, list):
            notify_emails = self.notify_emails

        else:
            notify_emails = self.notify_emails

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        backstage_id: None | str | Unset
        if isinstance(self.backstage_id, Unset):
            backstage_id = UNSET
        else:
            backstage_id = self.backstage_id

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        pagerduty_id: None | str | Unset
        if isinstance(self.pagerduty_id, Unset):
            pagerduty_id = UNSET
        else:
            pagerduty_id = self.pagerduty_id

        opsgenie_id: None | str | Unset
        if isinstance(self.opsgenie_id, Unset):
            opsgenie_id = UNSET
        else:
            opsgenie_id = self.opsgenie_id

        opsgenie_team_id: None | str | Unset
        if isinstance(self.opsgenie_team_id, Unset):
            opsgenie_team_id = UNSET
        else:
            opsgenie_team_id = self.opsgenie_team_id

        cortex_id: None | str | Unset
        if isinstance(self.cortex_id, Unset):
            cortex_id = UNSET
        else:
            cortex_id = self.cortex_id

        service_now_ci_sys_id: None | str | Unset
        if isinstance(self.service_now_ci_sys_id, Unset):
            service_now_ci_sys_id = UNSET
        else:
            service_now_ci_sys_id = self.service_now_ci_sys_id

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        environment_ids: list[str] | None | Unset
        if isinstance(self.environment_ids, Unset):
            environment_ids = UNSET
        elif isinstance(self.environment_ids, list):
            environment_ids = self.environment_ids

        else:
            environment_ids = self.environment_ids

        service_ids: list[str] | None | Unset
        if isinstance(self.service_ids, Unset):
            service_ids = UNSET
        elif isinstance(self.service_ids, list):
            service_ids = self.service_ids

        else:
            service_ids = self.service_ids

        owner_group_ids: list[str] | None | Unset
        if isinstance(self.owner_group_ids, Unset):
            owner_group_ids = UNSET
        elif isinstance(self.owner_group_ids, list):
            owner_group_ids = self.owner_group_ids

        else:
            owner_group_ids = self.owner_group_ids

        owner_user_ids: list[int] | None | Unset
        if isinstance(self.owner_user_ids, Unset):
            owner_user_ids = UNSET
        elif isinstance(self.owner_user_ids, list):
            owner_user_ids = self.owner_user_ids

        else:
            owner_user_ids = self.owner_user_ids

        slack_channels: list[dict[str, Any]] | None | Unset
        if isinstance(self.slack_channels, Unset):
            slack_channels = UNSET
        elif isinstance(self.slack_channels, list):
            slack_channels = []
            for slack_channels_type_0_item_data in self.slack_channels:
                slack_channels_type_0_item = slack_channels_type_0_item_data.to_dict()
                slack_channels.append(slack_channels_type_0_item)

        else:
            slack_channels = self.slack_channels

        slack_aliases: list[dict[str, Any]] | None | Unset
        if isinstance(self.slack_aliases, Unset):
            slack_aliases = UNSET
        elif isinstance(self.slack_aliases, list):
            slack_aliases = []
            for slack_aliases_type_0_item_data in self.slack_aliases:
                slack_aliases_type_0_item = slack_aliases_type_0_item_data.to_dict()
                slack_aliases.append(slack_aliases_type_0_item)

        else:
            slack_aliases = self.slack_aliases

        properties: list[dict[str, Any]] | None | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif isinstance(self.properties, list):
            properties = []
            for properties_type_0_item_data in self.properties:
                properties_type_0_item = properties_type_0_item_data.to_dict()
                properties.append(properties_type_0_item)

        else:
            properties = self.properties

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
        if description is not UNSET:
            field_dict["description"] = description
        if public_description is not UNSET:
            field_dict["public_description"] = public_description
        if notify_emails is not UNSET:
            field_dict["notify_emails"] = notify_emails
        if color is not UNSET:
            field_dict["color"] = color
        if backstage_id is not UNSET:
            field_dict["backstage_id"] = backstage_id
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if pagerduty_id is not UNSET:
            field_dict["pagerduty_id"] = pagerduty_id
        if opsgenie_id is not UNSET:
            field_dict["opsgenie_id"] = opsgenie_id
        if opsgenie_team_id is not UNSET:
            field_dict["opsgenie_team_id"] = opsgenie_team_id
        if cortex_id is not UNSET:
            field_dict["cortex_id"] = cortex_id
        if service_now_ci_sys_id is not UNSET:
            field_dict["service_now_ci_sys_id"] = service_now_ci_sys_id
        if position is not UNSET:
            field_dict["position"] = position
        if environment_ids is not UNSET:
            field_dict["environment_ids"] = environment_ids
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if owner_group_ids is not UNSET:
            field_dict["owner_group_ids"] = owner_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids
        if slack_channels is not UNSET:
            field_dict["slack_channels"] = slack_channels
        if slack_aliases is not UNSET:
            field_dict["slack_aliases"] = slack_aliases
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.functionality_properties_type_0_item import FunctionalityPropertiesType0Item
        from ..models.functionality_slack_aliases_type_0_item import FunctionalitySlackAliasesType0Item
        from ..models.functionality_slack_channels_type_0_item import FunctionalitySlackChannelsType0Item

        d = dict(src_dict)
        name = d.pop("name")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

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

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_backstage_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backstage_id = _parse_backstage_id(d.pop("backstage_id", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_pagerduty_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pagerduty_id = _parse_pagerduty_id(d.pop("pagerduty_id", UNSET))

        def _parse_opsgenie_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opsgenie_id = _parse_opsgenie_id(d.pop("opsgenie_id", UNSET))

        def _parse_opsgenie_team_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opsgenie_team_id = _parse_opsgenie_team_id(d.pop("opsgenie_team_id", UNSET))

        def _parse_cortex_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cortex_id = _parse_cortex_id(d.pop("cortex_id", UNSET))

        def _parse_service_now_ci_sys_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_now_ci_sys_id = _parse_service_now_ci_sys_id(d.pop("service_now_ci_sys_id", UNSET))

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_environment_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                environment_ids_type_0 = cast(list[str], data)

                return environment_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        environment_ids = _parse_environment_ids(d.pop("environment_ids", UNSET))

        def _parse_service_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                service_ids_type_0 = cast(list[str], data)

                return service_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        service_ids = _parse_service_ids(d.pop("service_ids", UNSET))

        def _parse_owner_group_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_group_ids_type_0 = cast(list[str], data)

                return owner_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        owner_group_ids = _parse_owner_group_ids(d.pop("owner_group_ids", UNSET))

        def _parse_owner_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_ids_type_0 = cast(list[int], data)

                return owner_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_ids = _parse_owner_user_ids(d.pop("owner_user_ids", UNSET))

        def _parse_slack_channels(data: object) -> list[FunctionalitySlackChannelsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                slack_channels_type_0 = []
                _slack_channels_type_0 = data
                for slack_channels_type_0_item_data in _slack_channels_type_0:
                    slack_channels_type_0_item = FunctionalitySlackChannelsType0Item.from_dict(
                        slack_channels_type_0_item_data
                    )

                    slack_channels_type_0.append(slack_channels_type_0_item)

                return slack_channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FunctionalitySlackChannelsType0Item] | None | Unset, data)

        slack_channels = _parse_slack_channels(d.pop("slack_channels", UNSET))

        def _parse_slack_aliases(data: object) -> list[FunctionalitySlackAliasesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                slack_aliases_type_0 = []
                _slack_aliases_type_0 = data
                for slack_aliases_type_0_item_data in _slack_aliases_type_0:
                    slack_aliases_type_0_item = FunctionalitySlackAliasesType0Item.from_dict(
                        slack_aliases_type_0_item_data
                    )

                    slack_aliases_type_0.append(slack_aliases_type_0_item)

                return slack_aliases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FunctionalitySlackAliasesType0Item] | None | Unset, data)

        slack_aliases = _parse_slack_aliases(d.pop("slack_aliases", UNSET))

        def _parse_properties(data: object) -> list[FunctionalityPropertiesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                properties_type_0 = []
                _properties_type_0 = data
                for properties_type_0_item_data in _properties_type_0:
                    properties_type_0_item = FunctionalityPropertiesType0Item.from_dict(properties_type_0_item_data)

                    properties_type_0.append(properties_type_0_item)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FunctionalityPropertiesType0Item] | None | Unset, data)

        properties = _parse_properties(d.pop("properties", UNSET))

        functionality = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            description=description,
            public_description=public_description,
            notify_emails=notify_emails,
            color=color,
            backstage_id=backstage_id,
            external_id=external_id,
            pagerduty_id=pagerduty_id,
            opsgenie_id=opsgenie_id,
            opsgenie_team_id=opsgenie_team_id,
            cortex_id=cortex_id,
            service_now_ci_sys_id=service_now_ci_sys_id,
            position=position,
            environment_ids=environment_ids,
            service_ids=service_ids,
            owner_group_ids=owner_group_ids,
            owner_user_ids=owner_user_ids,
            slack_channels=slack_channels,
            slack_aliases=slack_aliases,
            properties=properties,
        )

        functionality.additional_properties = d
        return functionality

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
