from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.publish_incident_task_params_selected_component_statuses_additional_property import (
    PublishIncidentTaskParamsSelectedComponentStatusesAdditionalProperty,
    check_publish_incident_task_params_selected_component_statuses_additional_property,
)

T = TypeVar("T", bound="PublishIncidentTaskParamsSelectedComponentStatuses")


@_attrs_define
class PublishIncidentTaskParamsSelectedComponentStatuses:
    """Impact status to publish for each selected component key. Keys must match selected_component_keys entries."""

    additional_properties: dict[str, PublishIncidentTaskParamsSelectedComponentStatusesAdditionalProperty] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        publish_incident_task_params_selected_component_statuses = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = check_publish_incident_task_params_selected_component_statuses_additional_property(
                prop_dict
            )

            additional_properties[prop_name] = additional_property

        publish_incident_task_params_selected_component_statuses.additional_properties = additional_properties
        return publish_incident_task_params_selected_component_statuses

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> PublishIncidentTaskParamsSelectedComponentStatusesAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: PublishIncidentTaskParamsSelectedComponentStatusesAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
