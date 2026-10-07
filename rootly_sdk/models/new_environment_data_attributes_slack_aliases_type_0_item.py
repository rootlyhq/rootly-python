from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="NewEnvironmentDataAttributesSlackAliasesType0Item")


@_attrs_define
class NewEnvironmentDataAttributesSlackAliasesType0Item:
    """
    Attributes:
        id (str): Slack alias ID
        name (str): Slack alias name
    """

    id: str
    name: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        new_environment_data_attributes_slack_aliases_type_0_item = cls(
            id=id,
            name=name,
        )

        return new_environment_data_attributes_slack_aliases_type_0_item
