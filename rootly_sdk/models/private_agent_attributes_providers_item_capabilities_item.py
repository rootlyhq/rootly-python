from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateAgentAttributesProvidersItemCapabilitiesItem")


@_attrs_define
class PrivateAgentAttributesProvidersItemCapabilitiesItem:
    """
    Attributes:
        name (str):
        version (str):
        description (str | Unset):
        sensitivity (str | Unset):
    """

    name: str
    version: str
    description: str | Unset = UNSET
    sensitivity: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        version = self.version

        description = self.description

        sensitivity = self.sensitivity

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "version": version,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if sensitivity is not UNSET:
            field_dict["sensitivity"] = sensitivity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        version = d.pop("version")

        description = d.pop("description", UNSET)

        sensitivity = d.pop("sensitivity", UNSET)

        private_agent_attributes_providers_item_capabilities_item = cls(
            name=name,
            version=version,
            description=description,
            sensitivity=sensitivity,
        )

        return private_agent_attributes_providers_item_capabilities_item
