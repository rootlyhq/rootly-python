from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MitigateIncidentDataAttributes")


@_attrs_define
class MitigateIncidentDataAttributes:
    """
    Attributes:
        mitigation_message (Union[None, Unset, str]): How was the incident mitigated?
    """

    mitigation_message: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        mitigation_message: None | Unset | str
        if isinstance(self.mitigation_message, Unset):
            mitigation_message = UNSET
        else:
            mitigation_message = self.mitigation_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if mitigation_message is not UNSET:
            field_dict["mitigation_message"] = mitigation_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_mitigation_message(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        mitigation_message = _parse_mitigation_message(d.pop("mitigation_message", UNSET))

        mitigate_incident_data_attributes = cls(
            mitigation_message=mitigation_message,
        )

        return mitigate_incident_data_attributes
