from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_event_action import AlertEventAction, check_alert_event_action
from ..models.alert_event_kind import AlertEventKind, check_alert_event_kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertEvent")


@_attrs_define
class AlertEvent:
    """
    Attributes:
        kind (AlertEventKind):
        action (AlertEventAction):
        source (str):
        created_at (str):
        updated_at (str):
        user_id (int | None | Unset): Author of the note.
        details (None | str | Unset): Note message.
    """

    kind: AlertEventKind
    action: AlertEventAction
    source: str
    created_at: str
    updated_at: str
    user_id: int | None | Unset = UNSET
    details: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        action: str = self.action

        source = self.source

        created_at = self.created_at

        updated_at = self.updated_at

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        details: None | str | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        else:
            details = self.details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "action": action,
                "source": source,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = check_alert_event_kind(d.pop("kind"))

        action = check_alert_event_action(d.pop("action"))

        source = d.pop("source")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        alert_event = cls(
            kind=kind,
            action=action,
            source=source,
            created_at=created_at,
            updated_at=updated_at,
            user_id=user_id,
            details=details,
        )

        alert_event.additional_properties = d
        return alert_event

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
