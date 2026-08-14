from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResolveIncidentDataAttributes")


@_attrs_define
class ResolveIncidentDataAttributes:
    """
    Attributes:
        resolution_message (Union[None, Unset, str]): How was the incident resolved?
    """

    resolution_message: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        resolution_message: None | Unset | str
        if isinstance(self.resolution_message, Unset):
            resolution_message = UNSET
        else:
            resolution_message = self.resolution_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if resolution_message is not UNSET:
            field_dict["resolution_message"] = resolution_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_resolution_message(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        resolution_message = _parse_resolution_message(d.pop("resolution_message", UNSET))

        resolve_incident_data_attributes = cls(
            resolution_message=resolution_message,
        )

        return resolve_incident_data_attributes
