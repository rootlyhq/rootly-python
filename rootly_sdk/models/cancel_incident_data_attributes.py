from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="CancelIncidentDataAttributes")


@_attrs_define
class CancelIncidentDataAttributes:
    """
    Attributes:
        cancellation_message (None | str | Unset): Why was the incident cancelled?
    """

    cancellation_message: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cancellation_message: None | str | Unset
        if isinstance(self.cancellation_message, Unset):
            cancellation_message = UNSET
        else:
            cancellation_message = self.cancellation_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cancellation_message is not UNSET:
            field_dict["cancellation_message"] = cancellation_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_cancellation_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancellation_message = _parse_cancellation_message(d.pop("cancellation_message", UNSET))

        cancel_incident_data_attributes = cls(
            cancellation_message=cancellation_message,
        )

        return cancel_incident_data_attributes
