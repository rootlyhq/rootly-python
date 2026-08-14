from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DuplicateIncidentDataAttributes")


@_attrs_define
class DuplicateIncidentDataAttributes:
    """
    Attributes:
        duplicate_incident_id (Union[Unset, str]):
        auto_cancel_incident (Union[None, Unset, bool]):  Default: True.
        reason_for_cancellation (Union[None, Unset, str]): Why was the incident cancelled?
    """

    duplicate_incident_id: Unset | str = UNSET
    auto_cancel_incident: None | Unset | bool = True
    reason_for_cancellation: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        duplicate_incident_id = self.duplicate_incident_id

        auto_cancel_incident: None | Unset | bool
        if isinstance(self.auto_cancel_incident, Unset):
            auto_cancel_incident = UNSET
        else:
            auto_cancel_incident = self.auto_cancel_incident

        reason_for_cancellation: None | Unset | str
        if isinstance(self.reason_for_cancellation, Unset):
            reason_for_cancellation = UNSET
        else:
            reason_for_cancellation = self.reason_for_cancellation

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if duplicate_incident_id is not UNSET:
            field_dict["duplicate_incident_id"] = duplicate_incident_id
        if auto_cancel_incident is not UNSET:
            field_dict["auto_cancel_incident"] = auto_cancel_incident
        if reason_for_cancellation is not UNSET:
            field_dict["reason_for_cancellation"] = reason_for_cancellation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duplicate_incident_id = d.pop("duplicate_incident_id", UNSET)

        def _parse_auto_cancel_incident(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        auto_cancel_incident = _parse_auto_cancel_incident(d.pop("auto_cancel_incident", UNSET))

        def _parse_reason_for_cancellation(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        reason_for_cancellation = _parse_reason_for_cancellation(d.pop("reason_for_cancellation", UNSET))

        duplicate_incident_data_attributes = cls(
            duplicate_incident_id=duplicate_incident_id,
            auto_cancel_incident=auto_cancel_incident,
            reason_for_cancellation=reason_for_cancellation,
        )

        return duplicate_incident_data_attributes
