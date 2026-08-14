from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.api_key_kind import ApiKeyKind, check_api_key_kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKeyWithTokenResponseDataAttributes")


@_attrs_define
class ApiKeyWithTokenResponseDataAttributes:
    """
    Attributes:
        name (str): The name of the API key
        kind (ApiKeyKind): The kind of the API key
        created_at (str): Date of creation
        updated_at (str): Date of last update
        token (str): The API key token (only shown once)
        description (Union[None, Unset, str]): A description of the API key
        role_id (Union[None, Unset, str]): The role ID
        on_call_role_id (Union[None, Unset, str]): The on-call role ID
        expires_at (Union[None, Unset, str]): Expiration date
        last_used_at (Union[None, Unset, str]): Date of last use
        grace_period_ends_at (Union[None, Unset, str]): Grace period end date
    """

    name: str
    kind: ApiKeyKind
    created_at: str
    updated_at: str
    token: str
    description: Union[None, Unset, str] = UNSET
    role_id: Union[None, Unset, str] = UNSET
    on_call_role_id: Union[None, Unset, str] = UNSET
    expires_at: Union[None, Unset, str] = UNSET
    last_used_at: Union[None, Unset, str] = UNSET
    grace_period_ends_at: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind: str = self.kind

        created_at = self.created_at

        updated_at = self.updated_at

        token = self.token

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

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

        expires_at: Union[None, Unset, str]
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = self.expires_at

        last_used_at: Union[None, Unset, str]
        if isinstance(self.last_used_at, Unset):
            last_used_at = UNSET
        else:
            last_used_at = self.last_used_at

        grace_period_ends_at: Union[None, Unset, str]
        if isinstance(self.grace_period_ends_at, Unset):
            grace_period_ends_at = UNSET
        else:
            grace_period_ends_at = self.grace_period_ends_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "kind": kind,
                "created_at": created_at,
                "updated_at": updated_at,
                "token": token,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if role_id is not UNSET:
            field_dict["role_id"] = role_id
        if on_call_role_id is not UNSET:
            field_dict["on_call_role_id"] = on_call_role_id
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if grace_period_ends_at is not UNSET:
            field_dict["grace_period_ends_at"] = grace_period_ends_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        kind = check_api_key_kind(d.pop("kind"))

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        token = d.pop("token")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_expires_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_last_used_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at", UNSET))

        def _parse_grace_period_ends_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        grace_period_ends_at = _parse_grace_period_ends_at(d.pop("grace_period_ends_at", UNSET))

        api_key_with_token_response_data_attributes = cls(
            name=name,
            kind=kind,
            created_at=created_at,
            updated_at=updated_at,
            token=token,
            description=description,
            role_id=role_id,
            on_call_role_id=on_call_role_id,
            expires_at=expires_at,
            last_used_at=last_used_at,
            grace_period_ends_at=grace_period_ends_at,
        )

        api_key_with_token_response_data_attributes.additional_properties = d
        return api_key_with_token_response_data_attributes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
