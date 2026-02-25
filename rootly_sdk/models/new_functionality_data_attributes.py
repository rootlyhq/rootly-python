from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.new_functionality_data_attributes_show_uptime_last_days import (
    NewFunctionalityDataAttributesShowUptimeLastDays,
    check_new_functionality_data_attributes_show_uptime_last_days,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_functionality_data_attributes_fields_item import NewFunctionalityDataAttributesFieldsItem
    from ..models.new_functionality_data_attributes_slack_aliases_type_0_item import (
        NewFunctionalityDataAttributesSlackAliasesType0Item,
    )
    from ..models.new_functionality_data_attributes_slack_channels_type_0_item import (
        NewFunctionalityDataAttributesSlackChannelsType0Item,
    )


T = TypeVar("T", bound="NewFunctionalityDataAttributes")


@_attrs_define
class NewFunctionalityDataAttributes:
    """
    Attributes:
        name (str): The name of the functionality
        description (Union[None, Unset, str]): The description of the functionality
        public_description (Union[None, Unset, str]): The public description of the functionality
        notify_emails (Union[None, Unset, list[str]]): Emails to attach to the functionality
        color (Union[None, Unset, str]): The hex color of the functionality
        position (Union[None, Unset, int]): Position of the functionality
        backstage_id (Union[None, Unset, str]): The Backstage entity id associated to this functionality. eg:
            :namespace/:kind/:entity_name
        external_id (Union[None, Unset, str]): The external id associated to this functionality
        pagerduty_id (Union[None, Unset, str]): The PagerDuty service id associated to this functionality
        opsgenie_id (Union[None, Unset, str]): The Opsgenie service id associated to this functionality
        opsgenie_team_id (Union[None, Unset, str]): The Opsgenie team id associated to this functionality
        cortex_id (Union[None, Unset, str]): The Cortex group id associated to this functionality
        service_now_ci_sys_id (Union[None, Unset, str]): The Service Now CI sys id associated to this functionality
        show_uptime (Union[None, Unset, bool]): Show uptime
        show_uptime_last_days (Union[Unset, NewFunctionalityDataAttributesShowUptimeLastDays]): Show uptime over x days
            Default: 60.
        environment_ids (Union[None, Unset, list[str]]): Environments associated with this functionality
        service_ids (Union[None, Unset, list[str]]): Services associated with this functionality
        owner_group_ids (Union[None, Unset, list[str]]): Owner Teams associated with this functionality
        owner_user_ids (Union[None, Unset, list[int]]): Owner Users associated with this functionality
        slack_channels (Union[None, Unset, list['NewFunctionalityDataAttributesSlackChannelsType0Item']]): Slack
            Channels associated with this functionality
        slack_aliases (Union[None, Unset, list['NewFunctionalityDataAttributesSlackAliasesType0Item']]): Slack Aliases
            associated with this functionality
        fields (Union[Unset, list['NewFunctionalityDataAttributesFieldsItem']]): Array of field values for this
            functionality.
    """

    name: str
    description: Union[None, Unset, str] = UNSET
    public_description: Union[None, Unset, str] = UNSET
    notify_emails: Union[None, Unset, list[str]] = UNSET
    color: Union[None, Unset, str] = UNSET
    position: Union[None, Unset, int] = UNSET
    backstage_id: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    pagerduty_id: Union[None, Unset, str] = UNSET
    opsgenie_id: Union[None, Unset, str] = UNSET
    opsgenie_team_id: Union[None, Unset, str] = UNSET
    cortex_id: Union[None, Unset, str] = UNSET
    service_now_ci_sys_id: Union[None, Unset, str] = UNSET
    show_uptime: Union[None, Unset, bool] = UNSET
    show_uptime_last_days: Union[Unset, NewFunctionalityDataAttributesShowUptimeLastDays] = 60
    environment_ids: Union[None, Unset, list[str]] = UNSET
    service_ids: Union[None, Unset, list[str]] = UNSET
    owner_group_ids: Union[None, Unset, list[str]] = UNSET
    owner_user_ids: Union[None, Unset, list[int]] = UNSET
    slack_channels: Union[None, Unset, list["NewFunctionalityDataAttributesSlackChannelsType0Item"]] = UNSET
    slack_aliases: Union[None, Unset, list["NewFunctionalityDataAttributesSlackAliasesType0Item"]] = UNSET
    fields: Union[Unset, list["NewFunctionalityDataAttributesFieldsItem"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        service_now_ci_sys_id: Union[None, Unset, str]
        if isinstance(self.service_now_ci_sys_id, Unset):
            service_now_ci_sys_id = UNSET
        else:
            service_now_ci_sys_id = self.service_now_ci_sys_id

        show_uptime: Union[None, Unset, bool]
        if isinstance(self.show_uptime, Unset):
            show_uptime = UNSET
        else:
            show_uptime = self.show_uptime

        show_uptime_last_days: Union[Unset, int] = UNSET
        if not isinstance(self.show_uptime_last_days, Unset):
            show_uptime_last_days = self.show_uptime_last_days

        environment_ids: Union[None, Unset, list[str]]
        if isinstance(self.environment_ids, Unset):
            environment_ids = UNSET
        elif isinstance(self.environment_ids, list):
            environment_ids = self.environment_ids

        else:
            environment_ids = self.environment_ids

        service_ids: Union[None, Unset, list[str]]
        if isinstance(self.service_ids, Unset):
            service_ids = UNSET
        elif isinstance(self.service_ids, list):
            service_ids = self.service_ids

        else:
            service_ids = self.service_ids

        owner_group_ids: Union[None, Unset, list[str]]
        if isinstance(self.owner_group_ids, Unset):
            owner_group_ids = UNSET
        elif isinstance(self.owner_group_ids, list):
            owner_group_ids = self.owner_group_ids

        else:
            owner_group_ids = self.owner_group_ids

        owner_user_ids: Union[None, Unset, list[int]]
        if isinstance(self.owner_user_ids, Unset):
            owner_user_ids = UNSET
        elif isinstance(self.owner_user_ids, list):
            owner_user_ids = self.owner_user_ids

        else:
            owner_user_ids = self.owner_user_ids

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

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if public_description is not UNSET:
            field_dict["public_description"] = public_description
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
        if opsgenie_id is not UNSET:
            field_dict["opsgenie_id"] = opsgenie_id
        if opsgenie_team_id is not UNSET:
            field_dict["opsgenie_team_id"] = opsgenie_team_id
        if cortex_id is not UNSET:
            field_dict["cortex_id"] = cortex_id
        if service_now_ci_sys_id is not UNSET:
            field_dict["service_now_ci_sys_id"] = service_now_ci_sys_id
        if show_uptime is not UNSET:
            field_dict["show_uptime"] = show_uptime
        if show_uptime_last_days is not UNSET:
            field_dict["show_uptime_last_days"] = show_uptime_last_days
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
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_functionality_data_attributes_fields_item import NewFunctionalityDataAttributesFieldsItem
        from ..models.new_functionality_data_attributes_slack_aliases_type_0_item import (
            NewFunctionalityDataAttributesSlackAliasesType0Item,
        )
        from ..models.new_functionality_data_attributes_slack_channels_type_0_item import (
            NewFunctionalityDataAttributesSlackChannelsType0Item,
        )

        d = dict(src_dict)
        name = d.pop("name")

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

        def _parse_service_now_ci_sys_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service_now_ci_sys_id = _parse_service_now_ci_sys_id(d.pop("service_now_ci_sys_id", UNSET))

        def _parse_show_uptime(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        show_uptime = _parse_show_uptime(d.pop("show_uptime", UNSET))

        _show_uptime_last_days = d.pop("show_uptime_last_days", UNSET)
        show_uptime_last_days: Union[Unset, NewFunctionalityDataAttributesShowUptimeLastDays]
        if isinstance(_show_uptime_last_days, Unset):
            show_uptime_last_days = UNSET
        else:
            show_uptime_last_days = check_new_functionality_data_attributes_show_uptime_last_days(
                _show_uptime_last_days
            )

        def _parse_environment_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                environment_ids_type_0 = cast(list[str], data)

                return environment_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        environment_ids = _parse_environment_ids(d.pop("environment_ids", UNSET))

        def _parse_service_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                service_ids_type_0 = cast(list[str], data)

                return service_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        service_ids = _parse_service_ids(d.pop("service_ids", UNSET))

        def _parse_owner_group_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_group_ids_type_0 = cast(list[str], data)

                return owner_group_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        owner_group_ids = _parse_owner_group_ids(d.pop("owner_group_ids", UNSET))

        def _parse_owner_user_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_ids_type_0 = cast(list[int], data)

                return owner_user_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        owner_user_ids = _parse_owner_user_ids(d.pop("owner_user_ids", UNSET))

        def _parse_slack_channels(
            data: object,
        ) -> Union[None, Unset, list["NewFunctionalityDataAttributesSlackChannelsType0Item"]]:
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
                    slack_channels_type_0_item = NewFunctionalityDataAttributesSlackChannelsType0Item.from_dict(
                        slack_channels_type_0_item_data
                    )

                    slack_channels_type_0.append(slack_channels_type_0_item)

                return slack_channels_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NewFunctionalityDataAttributesSlackChannelsType0Item"]], data)

        slack_channels = _parse_slack_channels(d.pop("slack_channels", UNSET))

        def _parse_slack_aliases(
            data: object,
        ) -> Union[None, Unset, list["NewFunctionalityDataAttributesSlackAliasesType0Item"]]:
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
                    slack_aliases_type_0_item = NewFunctionalityDataAttributesSlackAliasesType0Item.from_dict(
                        slack_aliases_type_0_item_data
                    )

                    slack_aliases_type_0.append(slack_aliases_type_0_item)

                return slack_aliases_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NewFunctionalityDataAttributesSlackAliasesType0Item"]], data)

        slack_aliases = _parse_slack_aliases(d.pop("slack_aliases", UNSET))

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = NewFunctionalityDataAttributesFieldsItem.from_dict(fields_item_data)

            fields.append(fields_item)

        new_functionality_data_attributes = cls(
            name=name,
            description=description,
            public_description=public_description,
            notify_emails=notify_emails,
            color=color,
            position=position,
            backstage_id=backstage_id,
            external_id=external_id,
            pagerduty_id=pagerduty_id,
            opsgenie_id=opsgenie_id,
            opsgenie_team_id=opsgenie_team_id,
            cortex_id=cortex_id,
            service_now_ci_sys_id=service_now_ci_sys_id,
            show_uptime=show_uptime,
            show_uptime_last_days=show_uptime_last_days,
            environment_ids=environment_ids,
            service_ids=service_ids,
            owner_group_ids=owner_group_ids,
            owner_user_ids=owner_user_ids,
            slack_channels=slack_channels,
            slack_aliases=slack_aliases,
            fields=fields,
        )

        return new_functionality_data_attributes
