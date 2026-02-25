from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_severity_data_attributes_severity import (
    UpdateSeverityDataAttributesSeverity,
    check_update_severity_data_attributes_severity,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_severity_data_attributes_slack_aliases_type_0_item import (
        UpdateSeverityDataAttributesSlackAliasesType0Item,
    )
    from ..models.update_severity_data_attributes_slack_channels_type_0_item import (
        UpdateSeverityDataAttributesSlackChannelsType0Item,
    )


T = TypeVar("T", bound="UpdateSeverityDataAttributes")


@_attrs_define
class UpdateSeverityDataAttributes:
    """
    Attributes:
        name (Union[Unset, str]): The name of the severity
        description (Union[None, Unset, str]): The description of the severity
        severity (Union[Unset, UpdateSeverityDataAttributesSeverity]): The severity of the severity
        color (Union[None, Unset, str]): The hex color of the severity
        position (Union[None, Unset, int]): Position of the severity
        notify_emails (Union[None, Unset, list[str]]): Emails to attach to the severity
        slack_channels (Union[None, Unset, list['UpdateSeverityDataAttributesSlackChannelsType0Item']]): Slack Channels
            associated with this severity
        slack_aliases (Union[None, Unset, list['UpdateSeverityDataAttributesSlackAliasesType0Item']]): Slack Aliases
            associated with this severity
    """

    name: Unset | str = UNSET
    description: None | Unset | str = UNSET
    severity: Unset | UpdateSeverityDataAttributesSeverity = UNSET
    color: None | Unset | str = UNSET
    position: None | Unset | int = UNSET
    notify_emails: None | Unset | list[str] = UNSET
    slack_channels: None | Unset | list["UpdateSeverityDataAttributesSlackChannelsType0Item"] = UNSET
    slack_aliases: None | Unset | list["UpdateSeverityDataAttributesSlackAliasesType0Item"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        severity: Unset | str = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if severity is not UNSET:
            field_dict["severity"] = severity
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_severity_data_attributes_slack_aliases_type_0_item import (
            UpdateSeverityDataAttributesSlackAliasesType0Item,
        )
        from ..models.update_severity_data_attributes_slack_channels_type_0_item import (
            UpdateSeverityDataAttributesSlackChannelsType0Item,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        _severity = d.pop("severity", UNSET)
        severity: Unset | UpdateSeverityDataAttributesSeverity
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = check_update_severity_data_attributes_severity(_severity)

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
        ) -> None | Unset | list["UpdateSeverityDataAttributesSlackChannelsType0Item"]:
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
                    slack_channels_type_0_item = UpdateSeverityDataAttributesSlackChannelsType0Item.from_dict(
                        slack_channels_type_0_item_data
                    )

                    slack_channels_type_0.append(slack_channels_type_0_item)

                return slack_channels_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list["UpdateSeverityDataAttributesSlackChannelsType0Item"], data)

        slack_channels = _parse_slack_channels(d.pop("slack_channels", UNSET))

        def _parse_slack_aliases(
            data: object,
        ) -> None | Unset | list["UpdateSeverityDataAttributesSlackAliasesType0Item"]:
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
                    slack_aliases_type_0_item = UpdateSeverityDataAttributesSlackAliasesType0Item.from_dict(
                        slack_aliases_type_0_item_data
                    )

                    slack_aliases_type_0.append(slack_aliases_type_0_item)

                return slack_aliases_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | list["UpdateSeverityDataAttributesSlackAliasesType0Item"], data)

        slack_aliases = _parse_slack_aliases(d.pop("slack_aliases", UNSET))

        update_severity_data_attributes = cls(
            name=name,
            description=description,
            severity=severity,
            color=color,
            position=position,
            notify_emails=notify_emails,
            slack_channels=slack_channels,
            slack_aliases=slack_aliases,
        )

        return update_severity_data_attributes
