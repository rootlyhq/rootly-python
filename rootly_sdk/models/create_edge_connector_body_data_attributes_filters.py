from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEdgeConnectorBodyDataAttributesFilters")


@_attrs_define
class CreateEdgeConnectorBodyDataAttributesFilters:
    """Event filters. OR within dimension, AND across dimensions.

    Attributes:
        group_ids (list[str] | Unset): Filter by group UUIDs
        service_ids (list[str] | Unset): Filter by service UUIDs
        environment_ids (list[str] | Unset): Filter by environment UUIDs
        functionality_ids (list[str] | Unset): Filter by functionality UUIDs
    """

    group_ids: list[str] | Unset = UNSET
    service_ids: list[str] | Unset = UNSET
    environment_ids: list[str] | Unset = UNSET
    functionality_ids: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_ids: list[str] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        service_ids: list[str] | Unset = UNSET
        if not isinstance(self.service_ids, Unset):
            service_ids = self.service_ids

        environment_ids: list[str] | Unset = UNSET
        if not isinstance(self.environment_ids, Unset):
            environment_ids = self.environment_ids

        functionality_ids: list[str] | Unset = UNSET
        if not isinstance(self.functionality_ids, Unset):
            functionality_ids = self.functionality_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if environment_ids is not UNSET:
            field_dict["environment_ids"] = environment_ids
        if functionality_ids is not UNSET:
            field_dict["functionality_ids"] = functionality_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_ids = cast(list[str], d.pop("group_ids", UNSET))

        service_ids = cast(list[str], d.pop("service_ids", UNSET))

        environment_ids = cast(list[str], d.pop("environment_ids", UNSET))

        functionality_ids = cast(list[str], d.pop("functionality_ids", UNSET))

        create_edge_connector_body_data_attributes_filters = cls(
            group_ids=group_ids,
            service_ids=service_ids,
            environment_ids=environment_ids,
            functionality_ids=functionality_ids,
        )

        return create_edge_connector_body_data_attributes_filters
