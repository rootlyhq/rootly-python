from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CancelIncidentDataAttributes")


@_attrs_define
class CancelIncidentDataAttributes:
    """
    Attributes:
        cancellation_message (Union[None, Unset, str]): Why was the incident cancelled?
    """

    cancellation_message: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        cancellation_message: None | Unset | str
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

        def _parse_cancellation_message(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        cancellation_message = _parse_cancellation_message(d.pop("cancellation_message", UNSET))

        cancel_incident_data_attributes = cls(
            cancellation_message=cancellation_message,
        )

        return cancel_incident_data_attributes
