from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.severity_severity import SeveritySeverity, check_severity_severity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.severity_slack_aliases_type_0_item import SeveritySlackAliasesType0Item
    from ..models.severity_slack_channels_type_0_item import SeveritySlackChannelsType0Item


T = TypeVar("T", bound="Severity")


@_attrs_define
class Severity:
    """
    Attributes:
        name (str): The name of the severity
        created_at (str): Date of creation
        updated_at (str): Date of last update
        slug (str | Unset): The slug of the severity
        description (None | str | Unset): The description of the severity
        severity (SeveritySeverity | Unset): The severity of the severity
        color (None | str | Unset): The hex color of the severity
        position (int | None | Unset): Position of the severity
        notify_emails (list[str] | None | Unset): Emails to attach to the severity
        slack_channels (list[SeveritySlackChannelsType0Item] | None | Unset): Slack Channels associated with this
            severity
        slack_aliases (list[SeveritySlackAliasesType0Item] | None | Unset): Slack Aliases associated with this severity
    """

    name: str
    created_at: str
    updated_at: str
    slug: str | Unset = UNSET
    description: None | str | Unset = UNSET
    severity: SeveritySeverity | Unset = UNSET
    color: None | str | Unset = UNSET
    position: int | None | Unset = UNSET
    notify_emails: list[str] | None | Unset = UNSET
    slack_channels: list[SeveritySlackChannelsType0Item] | None | Unset = UNSET
    slack_aliases: list[SeveritySlackAliasesType0Item] | None | Unset = UNSET
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

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity

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

        notify_emails: list[str] | None | Unset
        if isinstance(self.notify_emails, Unset):
            notify_emails = UNSET
        elif isinstance(self.notify_emails, list):
            notify_emails = self.notify_emails

        else:
            notify_emails = self.notify_emails

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
        from ..models.severity_slack_aliases_type_0_item import SeveritySlackAliasesType0Item
        from ..models.severity_slack_channels_type_0_item import SeveritySlackChannelsType0Item

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

        _severity = d.pop("severity", UNSET)
        severity: SeveritySeverity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = check_severity_severity(_severity)

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

        def _parse_slack_channels(data: object) -> list[SeveritySlackChannelsType0Item] | None | Unset:
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
                    slack_channels_type_0_item = SeveritySlackChannelsType0Item.from_dict(
                        slack_channels_type_0_item_data
                    )

                    slack_channels_type_0.append(slack_channels_type_0_item)

                return slack_channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SeveritySlackChannelsType0Item] | None | Unset, data)

        slack_channels = _parse_slack_channels(d.pop("slack_channels", UNSET))

        def _parse_slack_aliases(data: object) -> list[SeveritySlackAliasesType0Item] | None | Unset:
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
                    slack_aliases_type_0_item = SeveritySlackAliasesType0Item.from_dict(slack_aliases_type_0_item_data)

                    slack_aliases_type_0.append(slack_aliases_type_0_item)

                return slack_aliases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SeveritySlackAliasesType0Item] | None | Unset, data)

        slack_aliases = _parse_slack_aliases(d.pop("slack_aliases", UNSET))

        severity = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            description=description,
            severity=severity,
            color=color,
            position=position,
            notify_emails=notify_emails,
            slack_channels=slack_channels,
            slack_aliases=slack_aliases,
        )

        severity.additional_properties = d
        return severity

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
