from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSecretDataAttributes")


@_attrs_define
class UpdateSecretDataAttributes:
    """
    Attributes:
        name (str): The name of the secret
        secret (Union[Unset, str]): The secret
        hashicorp_vault_mount (Union[None, Unset, str]): The HashiCorp Vault secret mount path Default: 'secret'.
        hashicorp_vault_path (Union[None, Unset, str]): The HashiCorp Vault secret path
        hashicorp_vault_version (Union[None, Unset, int]): The HashiCorp Vault secret version Default: 0.
    """

    name: str
    secret: Unset | str = UNSET
    hashicorp_vault_mount: None | Unset | str = "secret"
    hashicorp_vault_path: None | Unset | str = UNSET
    hashicorp_vault_version: None | Unset | int = 0

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        secret = self.secret

        hashicorp_vault_mount: None | Unset | str
        if isinstance(self.hashicorp_vault_mount, Unset):
            hashicorp_vault_mount = UNSET
        else:
            hashicorp_vault_mount = self.hashicorp_vault_mount

        hashicorp_vault_path: None | Unset | str
        if isinstance(self.hashicorp_vault_path, Unset):
            hashicorp_vault_path = UNSET
        else:
            hashicorp_vault_path = self.hashicorp_vault_path

        hashicorp_vault_version: None | Unset | int
        if isinstance(self.hashicorp_vault_version, Unset):
            hashicorp_vault_version = UNSET
        else:
            hashicorp_vault_version = self.hashicorp_vault_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
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

        secret = d.pop("secret", UNSET)

        def _parse_hashicorp_vault_mount(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        hashicorp_vault_mount = _parse_hashicorp_vault_mount(d.pop("hashicorp_vault_mount", UNSET))

        def _parse_hashicorp_vault_path(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        hashicorp_vault_path = _parse_hashicorp_vault_path(d.pop("hashicorp_vault_path", UNSET))

        def _parse_hashicorp_vault_version(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        hashicorp_vault_version = _parse_hashicorp_vault_version(d.pop("hashicorp_vault_version", UNSET))

        update_secret_data_attributes = cls(
            name=name,
            secret=secret,
            hashicorp_vault_mount=hashicorp_vault_mount,
            hashicorp_vault_path=hashicorp_vault_path,
            hashicorp_vault_version=hashicorp_vault_version,
        )

        return update_secret_data_attributes
