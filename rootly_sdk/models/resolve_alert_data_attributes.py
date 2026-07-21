from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResolveAlertDataAttributes")


@_attrs_define
class ResolveAlertDataAttributes:
    """
    Attributes:
        resolution_message (None | str | Unset): How was the alert resolved?
        resolve_related_incidents (bool | None | Unset): Resolve all associated incidents
    """

    resolution_message: None | str | Unset = UNSET
    resolve_related_incidents: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        resolution_message: None | str | Unset
        if isinstance(self.resolution_message, Unset):
            resolution_message = UNSET
        else:
            resolution_message = self.resolution_message

        resolve_related_incidents: bool | None | Unset
        if isinstance(self.resolve_related_incidents, Unset):
            resolve_related_incidents = UNSET
        else:
            resolve_related_incidents = self.resolve_related_incidents

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if resolution_message is not UNSET:
            field_dict["resolution_message"] = resolution_message
        if resolve_related_incidents is not UNSET:
            field_dict["resolve_related_incidents"] = resolve_related_incidents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_resolution_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolution_message = _parse_resolution_message(d.pop("resolution_message", UNSET))

        def _parse_resolve_related_incidents(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        resolve_related_incidents = _parse_resolve_related_incidents(d.pop("resolve_related_incidents", UNSET))

        resolve_alert_data_attributes = cls(
            resolution_message=resolution_message,
            resolve_related_incidents=resolve_related_incidents,
        )

        return resolve_alert_data_attributes
