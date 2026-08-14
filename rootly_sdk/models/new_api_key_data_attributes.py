import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.new_api_key_data_attributes_kind import (
    NewApiKeyDataAttributesKind,
    check_new_api_key_data_attributes_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewApiKeyDataAttributes")


@_attrs_define
class NewApiKeyDataAttributes:
    """
    Attributes:
        name (str): The name of the API key
        kind (NewApiKeyDataAttributesKind): The kind of the API key
        expires_at (datetime.datetime): The expiration date of the API key (ISO 8601)
        description (Union[None, Unset, str]): A description of the API key
        group_id (Union[None, Unset, str]): The group (team) ID. Required when kind is 'team'.
        role_id (Union[None, Unset, str]): The role ID for organization API keys
        on_call_role_id (Union[None, Unset, str]): The on-call role ID for organization API keys
    """

    name: str
    kind: NewApiKeyDataAttributesKind
    expires_at: datetime.datetime
    description: Union[None, Unset, str] = UNSET
    group_id: Union[None, Unset, str] = UNSET
    role_id: Union[None, Unset, str] = UNSET
    on_call_role_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind: str = self.kind

        expires_at = self.expires_at.isoformat()

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        group_id: Union[None, Unset, str]
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        role_id: Union[None, Unset, str]
        if isinstance(self.role_id, Unset):
            role_id = UNSET
        else:
            role_id = self.role_id

        on_call_role_id: Union[None, Unset, str]
        if isinstance(self.on_call_role_id, Unset):
            on_call_role_id = UNSET
        else:
            on_call_role_id = self.on_call_role_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "kind": kind,
                "expires_at": expires_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
        if on_call_role_id is not UNSET:
            field_dict["on_call_role_id"] = on_call_role_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        kind = check_new_api_key_data_attributes_kind(d.pop("kind"))

        expires_at = isoparse(d.pop("expires_at"))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_group_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        group_id = _parse_group_id(d.pop("group_id", UNSET))

        def _parse_role_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        role_id = _parse_role_id(d.pop("role_id", UNSET))

        def _parse_on_call_role_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        on_call_role_id = _parse_on_call_role_id(d.pop("on_call_role_id", UNSET))

        new_api_key_data_attributes = cls(
            name=name,
            kind=kind,
            expires_at=expires_at,
            description=description,
            group_id=group_id,
            role_id=role_id,
            on_call_role_id=on_call_role_id,
        )

        return new_api_key_data_attributes
