from __future__ import annotations

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
        secret (str | Unset): The secret
        hashicorp_vault_mount (None | str | Unset): The HashiCorp Vault secret mount path Default: 'secret'.
        hashicorp_vault_path (None | str | Unset): The HashiCorp Vault secret path
        hashicorp_vault_version (int | None | Unset): The HashiCorp Vault secret version Default: 0.
        owner_group_ids (list[str] | None | Unset): IDs of the teams whose members can see and pick this secret; their
            team admins can manage it. Empty means only users with the org Secrets permission can. Ignored unless team
            scoping is enabled for the organization.
    """

    name: str
    secret: str | Unset = UNSET
    hashicorp_vault_mount: None | str | Unset = "secret"
    hashicorp_vault_path: None | str | Unset = UNSET
    hashicorp_vault_version: int | None | Unset = 0
    owner_group_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        secret = self.secret

        hashicorp_vault_mount: None | str | Unset
        if isinstance(self.hashicorp_vault_mount, Unset):
            hashicorp_vault_mount = UNSET
        else:
            hashicorp_vault_mount = self.hashicorp_vault_mount

        hashicorp_vault_path: None | str | Unset
        if isinstance(self.hashicorp_vault_path, Unset):
            hashicorp_vault_path = UNSET
        else:
            hashicorp_vault_path = self.hashicorp_vault_path

        hashicorp_vault_version: int | None | Unset
        if isinstance(self.hashicorp_vault_version, Unset):
            hashicorp_vault_version = UNSET
        else:
            hashicorp_vault_version = self.hashicorp_vault_version

        owner_group_ids: list[str] | None | Unset
        if isinstance(self.owner_group_ids, Unset):
            owner_group_ids = UNSET
        elif isinstance(self.owner_group_ids, list):
            owner_group_ids = self.owner_group_ids

        else:
            owner_group_ids = self.owner_group_ids

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
        if owner_group_ids is not UNSET:
            field_dict["owner_group_ids"] = owner_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        secret = d.pop("secret", UNSET)

        def _parse_hashicorp_vault_mount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hashicorp_vault_mount = _parse_hashicorp_vault_mount(d.pop("hashicorp_vault_mount", UNSET))

        def _parse_hashicorp_vault_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hashicorp_vault_path = _parse_hashicorp_vault_path(d.pop("hashicorp_vault_path", UNSET))

        def _parse_hashicorp_vault_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hashicorp_vault_version = _parse_hashicorp_vault_version(d.pop("hashicorp_vault_version", UNSET))

        def _parse_owner_group_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_group_ids_type_0 = cast(list[str], data)

                return owner_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        owner_group_ids = _parse_owner_group_ids(d.pop("owner_group_ids", UNSET))

        update_secret_data_attributes = cls(
            name=name,
            secret=secret,
            hashicorp_vault_mount=hashicorp_vault_mount,
            hashicorp_vault_path=hashicorp_vault_path,
            hashicorp_vault_version=hashicorp_vault_version,
            owner_group_ids=owner_group_ids,
        )

        return update_secret_data_attributes
