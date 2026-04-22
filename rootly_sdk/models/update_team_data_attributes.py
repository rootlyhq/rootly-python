from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_team_data_attributes_alert_broadcast_channel_type_0 import (
        UpdateTeamDataAttributesAlertBroadcastChannelType0,
    )
    from ..models.update_team_data_attributes_incident_broadcast_channel_type_0 import (
        UpdateTeamDataAttributesIncidentBroadcastChannelType0,
    )
    from ..models.update_team_data_attributes_properties_item import UpdateTeamDataAttributesPropertiesItem
    from ..models.update_team_data_attributes_slack_aliases_type_0_item import (
        UpdateTeamDataAttributesSlackAliasesType0Item,
    )
    from ..models.update_team_data_attributes_slack_channels_type_0_item import (
        UpdateTeamDataAttributesSlackChannelsType0Item,
    )


T = TypeVar("T", bound="UpdateTeamDataAttributes")


@_attrs_define
class UpdateTeamDataAttributes:
    """
    Attributes:
        name (str | Unset): The name of the team
        description (None | str | Unset): The description of the team
        notify_emails (list[str] | None | Unset): Emails to attach to the team
        color (None | str | Unset): The hex color of the team
        position (int | None | Unset): Position of the team
        backstage_id (None | str | Unset): The Backstage entity id associated to this team. eg:
            :namespace/:kind/:entity_name
        external_id (None | str | Unset): The external id associated to this team
        pagerduty_id (None | str | Unset): The PagerDuty group id associated to this team
        pagerduty_service_id (None | str | Unset): The PagerDuty service id associated to this team
        opsgenie_id (None | str | Unset): The Opsgenie group id associated to this team
        victor_ops_id (None | str | Unset): The VictorOps group id associated to this team
        pagertree_id (None | str | Unset): The PagerTree group id associated to this team
        cortex_id (None | str | Unset): The Cortex group id associated to this team
        service_now_ci_sys_id (None | str | Unset): The Service Now CI sys id associated to this team
        user_ids (list[int] | None | Unset): The user ids of the members of this team.
        admin_ids (list[int] | None | Unset): The user ids of the admins of this team. These users must also be present
            in user_ids attribute.
        alerts_email_enabled (bool | None | Unset): Enable alerts through email
        alert_urgency_id (None | str | Unset): The alert urgency id of the team
        slack_channels (list[UpdateTeamDataAttributesSlackChannelsType0Item] | None | Unset): Slack Channels associated
            with this team
        slack_aliases (list[UpdateTeamDataAttributesSlackAliasesType0Item] | None | Unset): Slack Aliases associated
            with this team
        alert_broadcast_enabled (bool | None | Unset): Enable alerts to be broadcasted to a specific channel
        alert_broadcast_channel (None | Unset | UpdateTeamDataAttributesAlertBroadcastChannelType0): Slack channel to
            broadcast alerts to
        incident_broadcast_enabled (bool | None | Unset): Enable incidents to be broadcasted to a specific channel
        incident_broadcast_channel (None | Unset | UpdateTeamDataAttributesIncidentBroadcastChannelType0): Slack channel
            to broadcast incidents to
        auto_add_members_when_attached (bool | None | Unset): Auto add members to incident channel when team is attached
        properties (list[UpdateTeamDataAttributesPropertiesItem] | Unset): Array of property values for this team.
    """

    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    notify_emails: list[str] | None | Unset = UNSET
    color: None | str | Unset = UNSET
    position: int | None | Unset = UNSET
    backstage_id: None | str | Unset = UNSET
    external_id: None | str | Unset = UNSET
    pagerduty_id: None | str | Unset = UNSET
    pagerduty_service_id: None | str | Unset = UNSET
    opsgenie_id: None | str | Unset = UNSET
    victor_ops_id: None | str | Unset = UNSET
    pagertree_id: None | str | Unset = UNSET
    cortex_id: None | str | Unset = UNSET
    service_now_ci_sys_id: None | str | Unset = UNSET
    user_ids: list[int] | None | Unset = UNSET
    admin_ids: list[int] | None | Unset = UNSET
    alerts_email_enabled: bool | None | Unset = UNSET
    alert_urgency_id: None | str | Unset = UNSET
    slack_channels: list[UpdateTeamDataAttributesSlackChannelsType0Item] | None | Unset = UNSET
    slack_aliases: list[UpdateTeamDataAttributesSlackAliasesType0Item] | None | Unset = UNSET
    alert_broadcast_enabled: bool | None | Unset = UNSET
    alert_broadcast_channel: None | Unset | UpdateTeamDataAttributesAlertBroadcastChannelType0 = UNSET
    incident_broadcast_enabled: bool | None | Unset = UNSET
    incident_broadcast_channel: None | Unset | UpdateTeamDataAttributesIncidentBroadcastChannelType0 = UNSET
    auto_add_members_when_attached: bool | None | Unset = UNSET
    properties: list[UpdateTeamDataAttributesPropertiesItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_team_data_attributes_alert_broadcast_channel_type_0 import (
            UpdateTeamDataAttributesAlertBroadcastChannelType0,
        )
        from ..models.update_team_data_attributes_incident_broadcast_channel_type_0 import (
            UpdateTeamDataAttributesIncidentBroadcastChannelType0,
        )

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        position: int | None | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

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

        user_ids: list[int] | None | Unset
        if isinstance(self.user_ids, Unset):
            user_ids = UNSET
        elif isinstance(self.user_ids, list):
            user_ids = self.user_ids

        else:
            user_ids = self.user_ids

        admin_ids: list[int] | None | Unset
        if isinstance(self.admin_ids, Unset):
            admin_ids = UNSET
        elif isinstance(self.admin_ids, list):
            admin_ids = self.admin_ids

        else:
            admin_ids = self.admin_ids

        alerts_email_enabled: bool | None | Unset
        if isinstance(self.alerts_email_enabled, Unset):
            alerts_email_enabled = UNSET
        else:
            alerts_email_enabled = self.alerts_email_enabled

        alert_urgency_id: None | str | Unset
        if isinstance(self.alert_urgency_id, Unset):
            alert_urgency_id = UNSET
        else:
            alert_urgency_id = self.alert_urgency_id

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

        alert_broadcast_enabled: bool | None | Unset
        if isinstance(self.alert_broadcast_enabled, Unset):
            alert_broadcast_enabled = UNSET
        else:
            alert_broadcast_enabled = self.alert_broadcast_enabled

        alert_broadcast_channel: dict[str, Any] | None | Unset
        if isinstance(self.alert_broadcast_channel, Unset):
            alert_broadcast_channel = UNSET
        elif isinstance(self.alert_broadcast_channel, UpdateTeamDataAttributesAlertBroadcastChannelType0):
            alert_broadcast_channel = self.alert_broadcast_channel.to_dict()
        else:
            alert_broadcast_channel = self.alert_broadcast_channel

        incident_broadcast_enabled: bool | None | Unset
        if isinstance(self.incident_broadcast_enabled, Unset):
            incident_broadcast_enabled = UNSET
        else:
            incident_broadcast_enabled = self.incident_broadcast_enabled

        incident_broadcast_channel: dict[str, Any] | None | Unset
        if isinstance(self.incident_broadcast_channel, Unset):
            incident_broadcast_channel = UNSET
        elif isinstance(self.incident_broadcast_channel, UpdateTeamDataAttributesIncidentBroadcastChannelType0):
            incident_broadcast_channel = self.incident_broadcast_channel.to_dict()
        else:
            incident_broadcast_channel = self.incident_broadcast_channel

        auto_add_members_when_attached: bool | None | Unset
        if isinstance(self.auto_add_members_when_attached, Unset):
            auto_add_members_when_attached = UNSET
        else:
            auto_add_members_when_attached = self.auto_add_members_when_attached

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if notify_emails is not UNSET:
            field_dict["notify_emails"] = notify_emails
        if color is not UNSET:
            field_dict["color"] = color
        if position is not UNSET:
            field_dict["position"] = position
        if backstage_id is not UNSET:
            field_dict["backstage_id"] = backstage_id
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
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
        if cortex_id is not UNSET:
            field_dict["cortex_id"] = cortex_id
        if service_now_ci_sys_id is not UNSET:
            field_dict["service_now_ci_sys_id"] = service_now_ci_sys_id
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids
        if admin_ids is not UNSET:
            field_dict["admin_ids"] = admin_ids
        if alerts_email_enabled is not UNSET:
            field_dict["alerts_email_enabled"] = alerts_email_enabled
        if alert_urgency_id is not UNSET:
            field_dict["alert_urgency_id"] = alert_urgency_id
        if slack_channels is not UNSET:
            field_dict["slack_channels"] = slack_channels
        if slack_aliases is not UNSET:
            field_dict["slack_aliases"] = slack_aliases
        if alert_broadcast_enabled is not UNSET:
            field_dict["alert_broadcast_enabled"] = alert_broadcast_enabled
        if alert_broadcast_channel is not UNSET:
            field_dict["alert_broadcast_channel"] = alert_broadcast_channel
        if incident_broadcast_enabled is not UNSET:
            field_dict["incident_broadcast_enabled"] = incident_broadcast_enabled
        if incident_broadcast_channel is not UNSET:
            field_dict["incident_broadcast_channel"] = incident_broadcast_channel
        if auto_add_members_when_attached is not UNSET:
            field_dict["auto_add_members_when_attached"] = auto_add_members_when_attached
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_team_data_attributes_alert_broadcast_channel_type_0 import (
            UpdateTeamDataAttributesAlertBroadcastChannelType0,
        )
        from ..models.update_team_data_attributes_incident_broadcast_channel_type_0 import (
            UpdateTeamDataAttributesIncidentBroadcastChannelType0,
        )
        from ..models.update_team_data_attributes_properties_item import UpdateTeamDataAttributesPropertiesItem
        from ..models.update_team_data_attributes_slack_aliases_type_0_item import (
            UpdateTeamDataAttributesSlackAliasesType0Item,
        )
        from ..models.update_team_data_attributes_slack_channels_type_0_item import (
            UpdateTeamDataAttributesSlackChannelsType0Item,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_position(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

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

        def _parse_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_ids_type_0 = cast(list[int], data)

                return user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        user_ids = _parse_user_ids(d.pop("user_ids", UNSET))

        def _parse_admin_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                admin_ids_type_0 = cast(list[int], data)

                return admin_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        admin_ids = _parse_admin_ids(d.pop("admin_ids", UNSET))

        def _parse_alerts_email_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        alerts_email_enabled = _parse_alerts_email_enabled(d.pop("alerts_email_enabled", UNSET))

        def _parse_alert_urgency_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alert_urgency_id = _parse_alert_urgency_id(d.pop("alert_urgency_id", UNSET))

        def _parse_slack_channels(data: object) -> list[UpdateTeamDataAttributesSlackChannelsType0Item] | None | Unset:
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
                    slack_channels_type_0_item = UpdateTeamDataAttributesSlackChannelsType0Item.from_dict(
                        slack_channels_type_0_item_data
                    )

                    slack_channels_type_0.append(slack_channels_type_0_item)

                return slack_channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UpdateTeamDataAttributesSlackChannelsType0Item] | None | Unset, data)

        slack_channels = _parse_slack_channels(d.pop("slack_channels", UNSET))

        def _parse_slack_aliases(data: object) -> list[UpdateTeamDataAttributesSlackAliasesType0Item] | None | Unset:
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
                    slack_aliases_type_0_item = UpdateTeamDataAttributesSlackAliasesType0Item.from_dict(
                        slack_aliases_type_0_item_data
                    )

                    slack_aliases_type_0.append(slack_aliases_type_0_item)

                return slack_aliases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UpdateTeamDataAttributesSlackAliasesType0Item] | None | Unset, data)

        slack_aliases = _parse_slack_aliases(d.pop("slack_aliases", UNSET))

        def _parse_alert_broadcast_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        alert_broadcast_enabled = _parse_alert_broadcast_enabled(d.pop("alert_broadcast_enabled", UNSET))

        def _parse_alert_broadcast_channel(
            data: object,
        ) -> None | Unset | UpdateTeamDataAttributesAlertBroadcastChannelType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                alert_broadcast_channel_type_0 = UpdateTeamDataAttributesAlertBroadcastChannelType0.from_dict(data)

                return alert_broadcast_channel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateTeamDataAttributesAlertBroadcastChannelType0, data)

        alert_broadcast_channel = _parse_alert_broadcast_channel(d.pop("alert_broadcast_channel", UNSET))

        def _parse_incident_broadcast_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        incident_broadcast_enabled = _parse_incident_broadcast_enabled(d.pop("incident_broadcast_enabled", UNSET))

        def _parse_incident_broadcast_channel(
            data: object,
        ) -> None | Unset | UpdateTeamDataAttributesIncidentBroadcastChannelType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                incident_broadcast_channel_type_0 = UpdateTeamDataAttributesIncidentBroadcastChannelType0.from_dict(
                    data
                )

                return incident_broadcast_channel_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateTeamDataAttributesIncidentBroadcastChannelType0, data)

        incident_broadcast_channel = _parse_incident_broadcast_channel(d.pop("incident_broadcast_channel", UNSET))

        def _parse_auto_add_members_when_attached(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_add_members_when_attached = _parse_auto_add_members_when_attached(
            d.pop("auto_add_members_when_attached", UNSET)
        )

        _properties = d.pop("properties", UNSET)
        properties: list[UpdateTeamDataAttributesPropertiesItem] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = UpdateTeamDataAttributesPropertiesItem.from_dict(properties_item_data)

                properties.append(properties_item)

        update_team_data_attributes = cls(
            name=name,
            description=description,
            notify_emails=notify_emails,
            color=color,
            position=position,
            backstage_id=backstage_id,
            external_id=external_id,
            pagerduty_id=pagerduty_id,
            pagerduty_service_id=pagerduty_service_id,
            opsgenie_id=opsgenie_id,
            victor_ops_id=victor_ops_id,
            pagertree_id=pagertree_id,
            cortex_id=cortex_id,
            service_now_ci_sys_id=service_now_ci_sys_id,
            user_ids=user_ids,
            admin_ids=admin_ids,
            alerts_email_enabled=alerts_email_enabled,
            alert_urgency_id=alert_urgency_id,
            slack_channels=slack_channels,
            slack_aliases=slack_aliases,
            alert_broadcast_enabled=alert_broadcast_enabled,
            alert_broadcast_channel=alert_broadcast_channel,
            incident_broadcast_enabled=incident_broadcast_enabled,
            incident_broadcast_channel=incident_broadcast_channel,
            auto_add_members_when_attached=auto_add_members_when_attached,
            properties=properties,
        )

        return update_team_data_attributes
