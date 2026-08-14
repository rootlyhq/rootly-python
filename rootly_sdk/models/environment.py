from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.environment_managed_by import EnvironmentManagedBy, check_environment_managed_by
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_properties_type_0_item import EnvironmentPropertiesType0Item
    from ..models.environment_slack_aliases_type_0_item import EnvironmentSlackAliasesType0Item
    from ..models.environment_slack_channels_type_0_item import EnvironmentSlackChannelsType0Item


T = TypeVar("T", bound="Environment")


@_attrs_define
class Environment:
    """
    Attributes:
        name (str): The name of the environment
        created_at (str): Date of creation
        updated_at (str): Date of last update
        slug (Union[Unset, str]): The slug of the environment
        managed_by (Union[Unset, EnvironmentManagedBy]): How this environment is managed (provenance): web, api,
            terraform, etc. Read-only.
        external_id (Union[None, Unset, str]): The external id associated to this environment
        description (Union[None, Unset, str]): The description of the environment
        public_description (Union[None, Unset, str]): The status page description of the environment
        notify_emails (Union[None, Unset, list[str]]): Emails attached to the environment
        color (Union[None, Unset, str]): The hex color of the environment
        position (Union[None, Unset, int]): Position of the environment
        slack_channels (Union[None, Unset, list['EnvironmentSlackChannelsType0Item']]): Slack Channels associated with
            this environment
        slack_aliases (Union[None, Unset, list['EnvironmentSlackAliasesType0Item']]): Slack Aliases associated with this
            environment
        properties (Union[None, Unset, list['EnvironmentPropertiesType0Item']]): Array of property values for this
            environment.
    """

    name: str
    created_at: str
    updated_at: str
    slug: Unset | str = UNSET
    managed_by: Unset | EnvironmentManagedBy = UNSET
    external_id: None | Unset | str = UNSET
    description: None | Unset | str = UNSET
    public_description: None | Unset | str = UNSET
    notify_emails: None | Unset | list[str] = UNSET
    color: None | Unset | str = UNSET
    position: None | Unset | int = UNSET
    slack_channels: None | Unset | list["EnvironmentSlackChannelsType0Item"] = UNSET
    slack_aliases: None | Unset | list["EnvironmentSlackAliasesType0Item"] = UNSET
    properties: None | Unset | list["EnvironmentPropertiesType0Item"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        managed_by: Unset | str = UNSET
        if not isinstance(self.managed_by, Unset):
            managed_by = self.managed_by

        external_id: None | Unset | str
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

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

        notify_emails: None | Unset | list[str]
        if isinstance(self.notify_emails, Unset):
            notify_emails = UNSET
        elif isinstance(self.notify_emails, list):
            notify_emails = self.notify_emails

        else:
            notify_emails = self.notify_emails

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

        properties: None | Unset | list[dict[str, Any]]
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
        if managed_by is not UNSET:
            field_dict["managed_by"] = managed_by
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
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
        if slack_channels is not UNSET:
            field_dict["slack_channels"] = slack_channels
        if slack_aliases is not UNSET:
            field_dict["slack_aliases"] = slack_aliases
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_properties_type_0_item import EnvironmentPropertiesType0Item
        from ..models.environment_slack_aliases_type_0_item import EnvironmentSlackAliasesType0Item
        from ..models.environment_slack_channels_type_0_item import EnvironmentSlackChannelsType0Item

        d = dict(src_dict)
        name = d.pop("name")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        _managed_by = d.pop("managed_by", UNSET)
        managed_by: Unset | EnvironmentManagedBy
        if isinstance(_managed_by, Unset):
            managed_by = UNSET
        else:
            managed_by = check_environment_managed_by(_managed_by)

        def _parse_external_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

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

        def _parse_slack_channels(data: object) -> None | Unset | list["EnvironmentSlackChannelsType0Item"]:
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
                    slack_channels_type_0_item = EnvironmentSlackChannelsType0Item.from_dict(
                        slack_channels_type_0_item_data
                    )

                    slack_channels_type_0.append(slack_channels_type_0_item)

                return slack_channels_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list["EnvironmentSlackChannelsType0Item"], data)

        slack_channels = _parse_slack_channels(d.pop("slack_channels", UNSET))

        def _parse_slack_aliases(data: object) -> None | Unset | list["EnvironmentSlackAliasesType0Item"]:
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
                    slack_aliases_type_0_item = EnvironmentSlackAliasesType0Item.from_dict(
                        slack_aliases_type_0_item_data
                    )

                    slack_aliases_type_0.append(slack_aliases_type_0_item)

                return slack_aliases_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list["EnvironmentSlackAliasesType0Item"], data)

        slack_aliases = _parse_slack_aliases(d.pop("slack_aliases", UNSET))

        def _parse_properties(data: object) -> None | Unset | list["EnvironmentPropertiesType0Item"]:
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
                    properties_type_0_item = EnvironmentPropertiesType0Item.from_dict(properties_type_0_item_data)

                    properties_type_0.append(properties_type_0_item)

                return properties_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list["EnvironmentPropertiesType0Item"], data)

        properties = _parse_properties(d.pop("properties", UNSET))

        environment = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            managed_by=managed_by,
            external_id=external_id,
            description=description,
            public_description=public_description,
            notify_emails=notify_emails,
            color=color,
            position=position,
            slack_channels=slack_channels,
            slack_aliases=slack_aliases,
            properties=properties,
        )

        environment.additional_properties = d
        return environment

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
