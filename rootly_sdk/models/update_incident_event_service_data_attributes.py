from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_incident_event_service_data_attributes_status import (
    check_update_incident_event_service_data_attributes_status,
)
from ..models.update_incident_event_service_data_attributes_status import UpdateIncidentEventServiceDataAttributesStatus
from typing import cast


T = TypeVar("T", bound="UpdateIncidentEventServiceDataAttributes")


@_attrs_define
class UpdateIncidentEventServiceDataAttributes:
    """
    Attributes:
        status (UpdateIncidentEventServiceDataAttributesStatus): The status of the affected service
    """

    status: UpdateIncidentEventServiceDataAttributesStatus

    def to_dict(self) -> dict[str, Any]:
        status: str = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = check_update_incident_event_service_data_attributes_status(d.pop("status"))

        update_incident_event_service_data_attributes = cls(
            status=status,
        )

        return update_incident_event_service_data_attributes
