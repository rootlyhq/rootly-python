from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_incident_type_data_attributes_fields_item import UpdateIncidentTypeDataAttributesFieldsItem
    from ..models.update_incident_type_data_attributes_slack_aliases_type_0_item import (
        UpdateIncidentTypeDataAttributesSlackAliasesType0Item,
    )
    from ..models.update_incident_type_data_attributes_slack_channels_type_0_item import (
        UpdateIncidentTypeDataAttributesSlackChannelsType0Item,
    )


T = TypeVar("T", bound="UpdateIncidentTypeDataAttributes")


@_attrs_define
class UpdateIncidentTypeDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the incident type
        description (Union[None, Unset, str]): The description of the incident type
        color (Union[None, Unset, str]): The hex color of the incident type
        position (Union[None, Unset, int]): Position of the incident type
        notify_emails (Union[None, Unset, list[str]]): Emails to attach to the incident type
        slack_channels (Union[None, Unset, list['UpdateIncidentTypeDataAttributesSlackChannelsType0Item']]): Slack
            Channels associated with this incident type
        slack_aliases (Union[None, Unset, list['UpdateIncidentTypeDataAttributesSlackAliasesType0Item']]): Slack Aliases
            associated with this incident type
        fields (Union[Unset, list['UpdateIncidentTypeDataAttributesFieldsItem']]): Array of field values for this
            incident type.
    """

    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    color: Union[None, Unset, str] = UNSET
    position: Union[None, Unset, int] = UNSET
    notify_emails: Union[None, Unset, list[str]] = UNSET
    slack_channels: Union[None, Unset, list["UpdateIncidentTypeDataAttributesSlackChannelsType0Item"]] = UNSET
    slack_aliases: Union[None, Unset, list["UpdateIncidentTypeDataAttributesSlackAliasesType0Item"]] = UNSET
    fields: Union[Unset, list["UpdateIncidentTypeDataAttributesFieldsItem"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        notify_emails: Union[None, Unset, list[str]]
        if isinstance(self.notify_emails, Unset):
            notify_emails = UNSET
        elif isinstance(self.notify_emails, list):
            notify_emails = self.notify_emails

        else:
            notify_emails = self.notify_emails

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

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if color is not UNSET:
            field_dict["color"] = color
        if position is not UNSET:
            field_dict["position"] = position
        if notify_emails is not UNSET:
            field_dict["notify_emails"] = notify_emails
        if slack_channels is not UNSET:
            field_dict["slack_channels"] = slack_channels
        if slack_aliases is not UNSET:
            field_dict["slack_aliases"] = slack_aliases
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_incident_type_data_attributes_fields_item import UpdateIncidentTypeDataAttributesFieldsItem
        from ..models.update_incident_type_data_attributes_slack_aliases_type_0_item import (
            UpdateIncidentTypeDataAttributesSlackAliasesType0Item,
        )
        from ..models.update_incident_type_data_attributes_slack_channels_type_0_item import (
            UpdateIncidentTypeDataAttributesSlackChannelsType0Item,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_slack_channels(
            data: object,
        ) -> Union[None, Unset, list["UpdateIncidentTypeDataAttributesSlackChannelsType0Item"]]:
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
                    slack_channels_type_0_item = UpdateIncidentTypeDataAttributesSlackChannelsType0Item.from_dict(
                        slack_channels_type_0_item_data
                    )

                    slack_channels_type_0.append(slack_channels_type_0_item)

                return slack_channels_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["UpdateIncidentTypeDataAttributesSlackChannelsType0Item"]], data)

        slack_channels = _parse_slack_channels(d.pop("slack_channels", UNSET))

        def _parse_slack_aliases(
            data: object,
        ) -> Union[None, Unset, list["UpdateIncidentTypeDataAttributesSlackAliasesType0Item"]]:
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
                    slack_aliases_type_0_item = UpdateIncidentTypeDataAttributesSlackAliasesType0Item.from_dict(
                        slack_aliases_type_0_item_data
                    )

                    slack_aliases_type_0.append(slack_aliases_type_0_item)

                return slack_aliases_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["UpdateIncidentTypeDataAttributesSlackAliasesType0Item"]], data)

        slack_aliases = _parse_slack_aliases(d.pop("slack_aliases", UNSET))

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = UpdateIncidentTypeDataAttributesFieldsItem.from_dict(fields_item_data)

            fields.append(fields_item)

        update_incident_type_data_attributes = cls(
            name=name,
            description=description,
            color=color,
            position=position,
            notify_emails=notify_emails,
            slack_channels=slack_channels,
            slack_aliases=slack_aliases,
            fields=fields,
        )

        return update_incident_type_data_attributes
