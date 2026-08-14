from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_incident_type_data_attributes_properties_item import NewIncidentTypeDataAttributesPropertiesItem
    from ..models.new_incident_type_data_attributes_slack_aliases_type_0_item import (
        NewIncidentTypeDataAttributesSlackAliasesType0Item,
    )
    from ..models.new_incident_type_data_attributes_slack_channels_type_0_item import (
        NewIncidentTypeDataAttributesSlackChannelsType0Item,
    )


T = TypeVar("T", bound="NewIncidentTypeDataAttributes")


@_attrs_define
class NewIncidentTypeDataAttributes:
    """
    Attributes:
        name (str): The name of the incident type
        slug (Union[None, Unset, str]): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        description (Union[None, Unset, str]): The description of the incident type
        public_description (Union[None, Unset, str]): The status page description of the incident type
        color (Union[None, Unset, str]): The hex color of the incident type
        position (Union[None, Unset, int]): Position of the incident type
        notify_emails (Union[None, Unset, list[str]]): Emails to attach to the incident type
        slack_channels (Union[None, Unset, list['NewIncidentTypeDataAttributesSlackChannelsType0Item']]): Slack Channels
            associated with this incident type
        slack_aliases (Union[None, Unset, list['NewIncidentTypeDataAttributesSlackAliasesType0Item']]): Slack Aliases
            associated with this incident type
        properties (Union[Unset, list['NewIncidentTypeDataAttributesPropertiesItem']]): Array of property values for
            this incident type.
    """

    name: str
    slug: None | Unset | str = UNSET
    description: None | Unset | str = UNSET
    public_description: None | Unset | str = UNSET
    color: None | Unset | str = UNSET
    position: None | Unset | int = UNSET
    notify_emails: None | Unset | list[str] = UNSET
    slack_channels: None | Unset | list["NewIncidentTypeDataAttributesSlackChannelsType0Item"] = UNSET
    slack_aliases: None | Unset | list["NewIncidentTypeDataAttributesSlackAliasesType0Item"] = UNSET
    properties: Unset | list["NewIncidentTypeDataAttributesPropertiesItem"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug: None | Unset | str
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

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

        slack_channels: None | Unset | list[dict[str, Any]]
        if isinstance(self.slack_channels, Unset):
            slack_channels = UNSET
        elif isinstance(self.slack_channels, list):
            slack_channels = []
            for slack_channels_type_0_item_data in self.slack_channels:
                slack_channels_type_0_item = slack_channels_type_0_item_data.to_dict()
                slack_channels.append(slack_channels_type_0_item)

        else:
            slack_channels = self.slack_channels

        slack_aliases: None | Unset | list[dict[str, Any]]
        if isinstance(self.slack_aliases, Unset):
            slack_aliases = UNSET
        elif isinstance(self.slack_aliases, list):
            slack_aliases = []
            for slack_aliases_type_0_item_data in self.slack_aliases:
                slack_aliases_type_0_item = slack_aliases_type_0_item_data.to_dict()
                slack_aliases.append(slack_aliases_type_0_item)

        else:
            slack_aliases = self.slack_aliases

        properties: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
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
        if slack_channels is not UNSET:
            field_dict["slack_channels"] = slack_channels
        if slack_aliases is not UNSET:
            field_dict["slack_aliases"] = slack_aliases
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_incident_type_data_attributes_properties_item import (
            NewIncidentTypeDataAttributesPropertiesItem,
        )
        from ..models.new_incident_type_data_attributes_slack_aliases_type_0_item import (
            NewIncidentTypeDataAttributesSlackAliasesType0Item,
        )
        from ..models.new_incident_type_data_attributes_slack_channels_type_0_item import (
            NewIncidentTypeDataAttributesSlackChannelsType0Item,
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_slug(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        slug = _parse_slug(d.pop("slug", UNSET))

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

        def _parse_slack_channels(
            data: object,
        ) -> None | Unset | list["NewIncidentTypeDataAttributesSlackChannelsType0Item"]:
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
                    slack_channels_type_0_item = NewIncidentTypeDataAttributesSlackChannelsType0Item.from_dict(
                        slack_channels_type_0_item_data
                    )

                    slack_channels_type_0.append(slack_channels_type_0_item)

                return slack_channels_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list["NewIncidentTypeDataAttributesSlackChannelsType0Item"], data)

        slack_channels = _parse_slack_channels(d.pop("slack_channels", UNSET))

        def _parse_slack_aliases(
            data: object,
        ) -> None | Unset | list["NewIncidentTypeDataAttributesSlackAliasesType0Item"]:
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
                    slack_aliases_type_0_item = NewIncidentTypeDataAttributesSlackAliasesType0Item.from_dict(
                        slack_aliases_type_0_item_data
                    )

                    slack_aliases_type_0.append(slack_aliases_type_0_item)

                return slack_aliases_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list["NewIncidentTypeDataAttributesSlackAliasesType0Item"], data)

        slack_aliases = _parse_slack_aliases(d.pop("slack_aliases", UNSET))

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = NewIncidentTypeDataAttributesPropertiesItem.from_dict(properties_item_data)

            properties.append(properties_item)

        new_incident_type_data_attributes = cls(
            name=name,
            slug=slug,
            description=description,
            public_description=public_description,
            color=color,
            position=position,
            notify_emails=notify_emails,
            slack_channels=slack_channels,
            slack_aliases=slack_aliases,
            properties=properties,
        )

        return new_incident_type_data_attributes
