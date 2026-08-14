from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Secret")


@_attrs_define
class Secret:
    """
    Attributes:
        name (str): The name of the secret
        created_at (str): Date of creation
        updated_at (str): Date of last update
        secret (Union[Unset, str]): The redacted secret
        hashicorp_vault_mount (Union[Unset, str]): The HashiCorp Vault secret mount path
        hashicorp_vault_path (Union[None, Unset, str]): The HashiCorp Vault secret path
        hashicorp_vault_version (Union[Unset, int]): The HashiCorp Vault secret version
    """

    name: str
    created_at: str
    updated_at: str
    secret: Unset | str = UNSET
    hashicorp_vault_mount: Unset | str = UNSET
    hashicorp_vault_path: None | Unset | str = UNSET
    hashicorp_vault_version: Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        secret = self.secret

        hashicorp_vault_mount = self.hashicorp_vault_mount

        hashicorp_vault_path: None | Unset | str
        if isinstance(self.hashicorp_vault_path, Unset):
            hashicorp_vault_path = UNSET
        else:
            hashicorp_vault_path = self.hashicorp_vault_path

        hashicorp_vault_version = self.hashicorp_vault_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if secret is not UNSET:
            field_dict["secret"] = secret
        if hashicorp_vault_mount is not UNSET:
            field_dict["hashicorp_vault_mount"] = hashicorp_vault_mount
        if hashicorp_vault_path is not UNSET:
            field_dict["hashicorp_vault_path"] = hashicorp_vault_path
        if hashicorp_vault_version is not UNSET:
            field_dict["hashicorp_vault_version"] = hashicorp_vault_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        secret = d.pop("secret", UNSET)

        hashicorp_vault_mount = d.pop("hashicorp_vault_mount", UNSET)

        def _parse_hashicorp_vault_path(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        hashicorp_vault_path = _parse_hashicorp_vault_path(d.pop("hashicorp_vault_path", UNSET))

        hashicorp_vault_version = d.pop("hashicorp_vault_version", UNSET)

        secret = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            secret=secret,
            hashicorp_vault_mount=hashicorp_vault_mount,
            hashicorp_vault_path=hashicorp_vault_path,
            hashicorp_vault_version=hashicorp_vault_version,
        )

        secret.additional_properties = d
        return secret

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
