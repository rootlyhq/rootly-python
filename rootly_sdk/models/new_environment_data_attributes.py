from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_environment_data_attributes_properties_item import NewEnvironmentDataAttributesPropertiesItem
    from ..models.new_environment_data_attributes_slack_aliases_type_0_item import (
        NewEnvironmentDataAttributesSlackAliasesType0Item,
    )
    from ..models.new_environment_data_attributes_slack_channels_type_0_item import (
        NewEnvironmentDataAttributesSlackChannelsType0Item,
    )


T = TypeVar("T", bound="NewEnvironmentDataAttributes")


@_attrs_define
class NewEnvironmentDataAttributes:
    """
    Attributes:
        name (str): The name of the environment
        slug (Union[None, Unset, str]): Deprecated. `slug` is derived from `name`; any submitted value is ignored. This
            property will be removed from the request schema in a future version.
        description (Union[None, Unset, str]): The description of the environment
        public_description (Union[None, Unset, str]): The status page description of the environment
        color (Union[None, Unset, str]): The hex color of the environment
        position (Union[None, Unset, int]): Position of the environment
        external_id (Union[None, Unset, str]): The external id associated to this environment
        notify_emails (Union[None, Unset, list[str]]): Emails to attach to the environment
        slack_channels (Union[None, Unset, list['NewEnvironmentDataAttributesSlackChannelsType0Item']]): Slack Channels
            associated with this environment
        slack_aliases (Union[None, Unset, list['NewEnvironmentDataAttributesSlackAliasesType0Item']]): Slack Aliases
            associated with this environment
        properties (Union[Unset, list['NewEnvironmentDataAttributesPropertiesItem']]): Array of property values for this
            environment.
    """

    name: str
    slug: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    public_description: Union[None, Unset, str] = UNSET
    color: Union[None, Unset, str] = UNSET
    position: Union[None, Unset, int] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    notify_emails: Union[None, Unset, list[str]] = UNSET
    slack_channels: Union[None, Unset, list["NewEnvironmentDataAttributesSlackChannelsType0Item"]] = UNSET
    slack_aliases: Union[None, Unset, list["NewEnvironmentDataAttributesSlackAliasesType0Item"]] = UNSET
    properties: Union[Unset, list["NewEnvironmentDataAttributesPropertiesItem"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        slug: Union[None, Unset, str]
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

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

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

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

        properties: Union[Unset, list[dict[str, Any]]] = UNSET
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
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
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
        from ..models.new_environment_data_attributes_properties_item import NewEnvironmentDataAttributesPropertiesItem
        from ..models.new_environment_data_attributes_slack_aliases_type_0_item import (
            NewEnvironmentDataAttributesSlackAliasesType0Item,
        )
        from ..models.new_environment_data_attributes_slack_channels_type_0_item import (
            NewEnvironmentDataAttributesSlackChannelsType0Item,
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_slug(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        slug = _parse_slug(d.pop("slug", UNSET))

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

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

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
        ) -> Union[None, Unset, list["NewEnvironmentDataAttributesSlackChannelsType0Item"]]:
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
                    slack_channels_type_0_item = NewEnvironmentDataAttributesSlackChannelsType0Item.from_dict(
                        slack_channels_type_0_item_data
                    )

                    slack_channels_type_0.append(slack_channels_type_0_item)

                return slack_channels_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NewEnvironmentDataAttributesSlackChannelsType0Item"]], data)

        slack_channels = _parse_slack_channels(d.pop("slack_channels", UNSET))

        def _parse_slack_aliases(
            data: object,
        ) -> Union[None, Unset, list["NewEnvironmentDataAttributesSlackAliasesType0Item"]]:
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
                    slack_aliases_type_0_item = NewEnvironmentDataAttributesSlackAliasesType0Item.from_dict(
                        slack_aliases_type_0_item_data
                    )

                    slack_aliases_type_0.append(slack_aliases_type_0_item)

                return slack_aliases_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["NewEnvironmentDataAttributesSlackAliasesType0Item"]], data)

        slack_aliases = _parse_slack_aliases(d.pop("slack_aliases", UNSET))

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = NewEnvironmentDataAttributesPropertiesItem.from_dict(properties_item_data)

            properties.append(properties_item)

        new_environment_data_attributes = cls(
            name=name,
            slug=slug,
            description=description,
            public_description=public_description,
            color=color,
            position=position,
            external_id=external_id,
            notify_emails=notify_emails,
            slack_channels=slack_channels,
            slack_aliases=slack_aliases,
            properties=properties,
        )

        return new_environment_data_attributes
