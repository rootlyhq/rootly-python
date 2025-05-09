from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RestartIncidentDataAttributes")


@_attrs_define
class RestartIncidentDataAttributes:
    """ """

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        restart_incident_data_attributes = cls()

        return restart_incident_data_attributes
