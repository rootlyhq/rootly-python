from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_alert_broadcast_channel_type_0 import TeamAlertBroadcastChannelType0
    from ..models.team_fields_type_0_item import TeamFieldsType0Item
    from ..models.team_incident_broadcast_channel_type_0 import TeamIncidentBroadcastChannelType0
    from ..models.team_slack_aliases_type_0_item import TeamSlackAliasesType0Item
    from ..models.team_slack_channels_type_0_item import TeamSlackChannelsType0Item


T = TypeVar("T", bound="Team")


@_attrs_define
class Team:
    """
    Attributes:
        name (str): The name of the team
        created_at (str): Date of creation
        updated_at (str): Date of last update
        slug (Union[Unset, str]):
        description (Union[None, Unset, str]): The description of the team
        notify_emails (Union[None, Unset, list[str]]): Emails to attach to the team
        color (Union[None, Unset, str]): The hex color of the team
        position (Union[None, Unset, int]): Position of the team
        backstage_id (Union[None, Unset, str]): The Backstage entity id associated to this team. eg:
            :namespace/:kind/:entity_name
        external_id (Union[None, Unset, str]): The external id associated to this team
        pagerduty_id (Union[None, Unset, str]): The PagerDuty group id associated to this team
        pagerduty_service_id (Union[None, Unset, str]): The PagerDuty service id associated to this team
        opsgenie_id (Union[None, Unset, str]): The Opsgenie group id associated to this team
        victor_ops_id (Union[None, Unset, str]): The VictorOps group id associated to this team
        pagertree_id (Union[None, Unset, str]): The PagerTree group id associated to this team
        cortex_id (Union[None, Unset, str]): The Cortex group id associated to this team
        service_now_ci_sys_id (Union[None, Unset, str]): The Service Now CI sys id associated to this team
        user_ids (Union[None, Unset, list[int]]): The user ids of the members of this team.
        admin_ids (Union[None, Unset, list[int]]): The user ids of the admins of this team. These users must also be
            present in user_ids attribute.
        alerts_email_enabled (Union[None, Unset, bool]): Enable alerts through email
        alerts_email_address (Union[None, Unset, str]): Email generated to send alerts to
        alert_urgency_id (Union[None, Unset, str]): The alert urgency id of the team
        slack_channels (Union[None, Unset, list['TeamSlackChannelsType0Item']]): Slack Channels associated with this
            team
        slack_aliases (Union[None, Unset, list['TeamSlackAliasesType0Item']]): Slack Aliases associated with this team
        alert_broadcast_enabled (Union[None, Unset, bool]): Enable alerts to be broadcasted to a specific channel
        alert_broadcast_channel (Union['TeamAlertBroadcastChannelType0', None, Unset]): Slack channel to broadcast
            alerts to
        incident_broadcast_enabled (Union[None, Unset, bool]): Enable incidents to be broadcasted to a specific channel
        incident_broadcast_channel (Union['TeamIncidentBroadcastChannelType0', None, Unset]): Slack channel to broadcast
            incidents to
        auto_add_members_when_attached (Union[None, Unset, bool]): Auto add members to incident channel when team is
            attached
        fields (Union[None, Unset, list['TeamFieldsType0Item']]): Array of field values for this team.
    """

    name: str
    created_at: str
    updated_at: str
    slug: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    notify_emails: Union[None, Unset, list[str]] = UNSET
    color: Union[None, Unset, str] = UNSET
    position: Union[None, Unset, int] = UNSET
    backstage_id: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    pagerduty_id: Union[None, Unset, str] = UNSET
    pagerduty_service_id: Union[None, Unset, str] = UNSET
    opsgenie_id: Union[None, Unset, str] = UNSET
    victor_ops_id: Union[None, Unset, str] = UNSET
    pagertree_id: Union[None, Unset, str] = UNSET
    cortex_id: Union[None, Unset, str] = UNSET
    service_now_ci_sys_id: Union[None, Unset, str] = UNSET
    user_ids: Union[None, Unset, list[int]] = UNSET
    admin_ids: Union[None, Unset, list[int]] = UNSET
    alerts_email_enabled: Union[None, Unset, bool] = UNSET
    alerts_email_address: Union[None, Unset, str] = UNSET
    alert_urgency_id: Union[None, Unset, str] = UNSET
    slack_channels: Union[None, Unset, list["TeamSlackChannelsType0Item"]] = UNSET
    slack_aliases: Union[None, Unset, list["TeamSlackAliasesType0Item"]] = UNSET
    alert_broadcast_enabled: Union[None, Unset, bool] = UNSET
    alert_broadcast_channel: Union["TeamAlertBroadcastChannelType0", None, Unset] = UNSET
    incident_broadcast_enabled: Union[None, Unset, bool] = UNSET
    incident_broadcast_channel: Union["TeamIncidentBroadcastChannelType0", None, Unset] = UNSET
    auto_add_members_when_attached: Union[None, Unset, bool] = UNSET
    fields: Union[None, Unset, list["TeamFieldsType0Item"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.team_alert_broadcast_channel_type_0 import TeamAlertBroadcastChannelType0
        from ..models.team_incident_broadcast_channel_type_0 import TeamIncidentBroadcastChannelType0

        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        notify_emails: Union[None, Unset, list[str]]
        if isinstance(self.notify_emails, Unset):
            notify_emails = UNSET
        elif isinstance(self.notify_emails, list):
            notify_emails = self.notify_emails

        else:
            notify_emails = self.notify_emails

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

        backstage_id: Union[None, Unset, str]
        if isinstance(self.backstage_id, Unset):
            backstage_id = UNSET
        else:
            backstage_id = self.backstage_id

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        pagerduty_id: Union[None, Unset, str]
        if isinstance(self.pagerduty_id, Unset):
            pagerduty_id = UNSET
        else:
            pagerduty_id = self.pagerduty_id

        pagerduty_service_id: Union[None, Unset, str]
        if isinstance(self.pagerduty_service_id, Unset):
            pagerduty_service_id = UNSET
        else:
            pagerduty_service_id = self.pagerduty_service_id

        opsgenie_id: Union[None, Unset, str]
        if isinstance(self.opsgenie_id, Unset):
            opsgenie_id = UNSET
        else:
            opsgenie_id = self.opsgenie_id

        victor_ops_id: Union[None, Unset, str]
        if isinstance(self.victor_ops_id, Unset):
            victor_ops_id = UNSET
        else:
            victor_ops_id = self.victor_ops_id

        pagertree_id: Union[None, Unset, str]
        if isinstance(self.pagertree_id, Unset):
            pagertree_id = UNSET
        else:
            pagertree_id = self.pagertree_id

        cortex_id: Union[None, Unset, str]
        if isinstance(self.cortex_id, Unset):
            cortex_id = UNSET
        else:
            cortex_id = self.cortex_id

        service_now_ci_sys_id: Union[None, Unset, str]
        if isinstance(self.service_now_ci_sys_id, Unset):
            service_now_ci_sys_id = UNSET
        else:
            service_now_ci_sys_id = self.service_now_ci_sys_id

        user_ids: Union[None, Unset, list[int]]
        if isinstance(self.user_ids, Unset):
            user_ids = UNSET
        elif isinstance(self.user_ids, list):
            user_ids = self.user_ids

        else:
            user_ids = self.user_ids

        admin_ids: Union[None, Unset, list[int]]
        if isinstance(self.admin_ids, Unset):
            admin_ids = UNSET
        elif isinstance(self.admin_ids, list):
            admin_ids = self.admin_ids

        else:
            admin_ids = self.admin_ids

        alerts_email_enabled: Union[None, Unset, bool]
        if isinstance(self.alerts_email_enabled, Unset):
            alerts_email_enabled = UNSET
        else:
            alerts_email_enabled = self.alerts_email_enabled

        alerts_email_address: Union[None, Unset, str]
        if isinstance(self.alerts_email_address, Unset):
            alerts_email_address = UNSET
        else:
            alerts_email_address = self.alerts_email_address

        alert_urgency_id: Union[None, Unset, str]
        if isinstance(self.alert_urgency_id, Unset):
            alert_urgency_id = UNSET
        else:
            alert_urgency_id = self.alert_urgency_id

        slack_channels: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.slack_channels, Unset):
            slack_channels = UNSET
        elif isinstance(self.slack_channels, list):
            slack_channels = []
            for slack_channels_type_0_item_data in self.slack_channels:
                slack_channels_type_0_item = slack_channels_type_0_item_data.to_dict()
                slack_channels.append(slack_channels_type_0_item)

        else:
            slack_channels = self.slack_channels

        slack_aliases: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.slack_aliases, Unset):
            slack_aliases = UNSET
        elif isinstance(self.slack_aliases, list):
            slack_aliases = []
            for slack_aliases_type_0_item_data in self.slack_aliases:
                slack_aliases_type_0_item = slack_aliases_type_0_item_data.to_dict()
                slack_aliases.append(slack_aliases_type_0_item)

        else:
            slack_aliases = self.slack_aliases

        alert_broadcast_enabled: Union[None, Unset, bool]
        if isinstance(self.alert_broadcast_enabled, Unset):
            alert_broadcast_enabled = UNSET
        else:
            alert_broadcast_enabled = self.alert_broadcast_enabled

        alert_broadcast_channel: Union[None, Unset, dict[str, Any]]
        if isinstance(self.alert_broadcast_channel, Unset):
            alert_broadcast_channel = UNSET
        elif isinstance(self.alert_broadcast_channel, TeamAlertBroadcastChannelType0):
            alert_broadcast_channel = self.alert_broadcast_channel.to_dict()
        else:
            alert_broadcast_channel = self.alert_broadcast_channel

        incident_broadcast_enabled: Union[None, Unset, bool]
        if isinstance(self.incident_broadcast_enabled, Unset):
            incident_broadcast_enabled = UNSET
        else:
            incident_broadcast_enabled = self.incident_broadcast_enabled

        incident_broadcast_channel: Union[None, Unset, dict[str, Any]]
        if isinstance(self.incident_broadcast_channel, Unset):
            incident_broadcast_channel = UNSET
        elif isinstance(self.incident_broadcast_channel, TeamIncidentBroadcastChannelType0):
            incident_broadcast_channel = self.incident_broadcast_channel.to_dict()
        else:
            incident_broadcast_channel = self.incident_broadcast_channel

        auto_add_members_when_attached: Union[None, Unset, bool]
        if isinstance(self.auto_add_members_when_attached, Unset):
            auto_add_members_when_attached = UNSET
        else:
            auto_add_members_when_attached = self.auto_add_members_when_attached

        fields: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = []
            for fields_type_0_item_data in self.fields:
                fields_type_0_item = fields_type_0_item_data.to_dict()
                fields.append(fields_type_0_item)

        else:
            fields = self.fields

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
        if alerts_email_address is not UNSET:
            field_dict["alerts_email_address"] = alerts_email_address
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
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_alert_broadcast_channel_type_0 import TeamAlertBroadcastChannelType0
        from ..models.team_fields_type_0_item import TeamFieldsType0Item
        from ..models.team_incident_broadcast_channel_type_0 import TeamIncidentBroadcastChannelType0
        from ..models.team_slack_aliases_type_0_item import TeamSlackAliasesType0Item
        from ..models.team_slack_channels_type_0_item import TeamSlackChannelsType0Item

        d = dict(src_dict)
        name = d.pop("name")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_backstage_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backstage_id = _parse_backstage_id(d.pop("backstage_id", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_pagerduty_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pagerduty_id = _parse_pagerduty_id(d.pop("pagerduty_id", UNSET))

        def _parse_pagerduty_service_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pagerduty_service_id = _parse_pagerduty_service_id(d.pop("pagerduty_service_id", UNSET))

        def _parse_opsgenie_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        opsgenie_id = _parse_opsgenie_id(d.pop("opsgenie_id", UNSET))

        def _parse_victor_ops_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        victor_ops_id = _parse_victor_ops_id(d.pop("victor_ops_id", UNSET))

        def _parse_pagertree_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pagertree_id = _parse_pagertree_id(d.pop("pagertree_id", UNSET))

        def _parse_cortex_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cortex_id = _parse_cortex_id(d.pop("cortex_id", UNSET))

        def _parse_service_now_ci_sys_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_now_ci_sys_id = _parse_service_now_ci_sys_id(d.pop("service_now_ci_sys_id", UNSET))

        def _parse_user_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_ids_type_0 = cast(list[int], data)

                return user_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        user_ids = _parse_user_ids(d.pop("user_ids", UNSET))

        def _parse_admin_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                admin_ids_type_0 = cast(list[int], data)

                return admin_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        admin_ids = _parse_admin_ids(d.pop("admin_ids", UNSET))

        def _parse_alerts_email_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        alerts_email_enabled = _parse_alerts_email_enabled(d.pop("alerts_email_enabled", UNSET))

        def _parse_alerts_email_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alerts_email_address = _parse_alerts_email_address(d.pop("alerts_email_address", UNSET))

        def _parse_alert_urgency_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alert_urgency_id = _parse_alert_urgency_id(d.pop("alert_urgency_id", UNSET))

        def _parse_slack_channels(data: object) -> Union[None, Unset, list["TeamSlackChannelsType0Item"]]:
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
                    slack_channels_type_0_item = TeamSlackChannelsType0Item.from_dict(slack_channels_type_0_item_data)

                    slack_channels_type_0.append(slack_channels_type_0_item)

                return slack_channels_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["TeamSlackChannelsType0Item"]], data)

        slack_channels = _parse_slack_channels(d.pop("slack_channels", UNSET))

        def _parse_slack_aliases(data: object) -> Union[None, Unset, list["TeamSlackAliasesType0Item"]]:
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
                    slack_aliases_type_0_item = TeamSlackAliasesType0Item.from_dict(slack_aliases_type_0_item_data)

                    slack_aliases_type_0.append(slack_aliases_type_0_item)

                return slack_aliases_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["TeamSlackAliasesType0Item"]], data)

        slack_aliases = _parse_slack_aliases(d.pop("slack_aliases", UNSET))

        def _parse_alert_broadcast_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        alert_broadcast_enabled = _parse_alert_broadcast_enabled(d.pop("alert_broadcast_enabled", UNSET))

        def _parse_alert_broadcast_channel(data: object) -> Union["TeamAlertBroadcastChannelType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                alert_broadcast_channel_type_0 = TeamAlertBroadcastChannelType0.from_dict(data)

                return alert_broadcast_channel_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TeamAlertBroadcastChannelType0", None, Unset], data)

        alert_broadcast_channel = _parse_alert_broadcast_channel(d.pop("alert_broadcast_channel", UNSET))

        def _parse_incident_broadcast_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        incident_broadcast_enabled = _parse_incident_broadcast_enabled(d.pop("incident_broadcast_enabled", UNSET))

        def _parse_incident_broadcast_channel(data: object) -> Union["TeamIncidentBroadcastChannelType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                incident_broadcast_channel_type_0 = TeamIncidentBroadcastChannelType0.from_dict(data)

                return incident_broadcast_channel_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TeamIncidentBroadcastChannelType0", None, Unset], data)

        incident_broadcast_channel = _parse_incident_broadcast_channel(d.pop("incident_broadcast_channel", UNSET))

        def _parse_auto_add_members_when_attached(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        auto_add_members_when_attached = _parse_auto_add_members_when_attached(
            d.pop("auto_add_members_when_attached", UNSET)
        )

        def _parse_fields(data: object) -> Union[None, Unset, list["TeamFieldsType0Item"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_0 = []
                _fields_type_0 = data
                for fields_type_0_item_data in _fields_type_0:
                    fields_type_0_item = TeamFieldsType0Item.from_dict(fields_type_0_item_data)

                    fields_type_0.append(fields_type_0_item)

                return fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["TeamFieldsType0Item"]], data)

        fields = _parse_fields(d.pop("fields", UNSET))

        team = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
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
            alerts_email_address=alerts_email_address,
            alert_urgency_id=alert_urgency_id,
            slack_channels=slack_channels,
            slack_aliases=slack_aliases,
            alert_broadcast_enabled=alert_broadcast_enabled,
            alert_broadcast_channel=alert_broadcast_channel,
            incident_broadcast_enabled=incident_broadcast_enabled,
            incident_broadcast_channel=incident_broadcast_channel,
            auto_add_members_when_attached=auto_add_members_when_attached,
            fields=fields,
        )

        team.additional_properties = d
        return team

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
