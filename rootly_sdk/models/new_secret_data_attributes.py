from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_secret_data_attributes_kind import NewSecretDataAttributesKind, check_new_secret_data_attributes_kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewSecretDataAttributes")


@_attrs_define
class NewSecretDataAttributes:
    """
    Attributes:
        name (str): The name of the secret
        secret (str): The secret
        kind (NewSecretDataAttributesKind | Unset): The kind of the secret
        hashicorp_vault_mount (None | str | Unset): The HashiCorp Vault secret mount path Default: 'secret'.
        hashicorp_vault_path (None | str | Unset): The HashiCorp Vault secret path
        hashicorp_vault_version (None | str | Unset): The HashiCorp Vault secret version Default: '0'.
        owner_group_ids (list[str] | None | Unset): IDs of the teams whose members can see and pick this secret; their
            team admins can manage it. Empty means only users with the org Secrets permission can. Ignored unless team
            scoping is enabled for the organization.
    """

    name: str
    secret: str
    kind: NewSecretDataAttributesKind | Unset = UNSET
    hashicorp_vault_mount: None | str | Unset = "secret"
    hashicorp_vault_path: None | str | Unset = UNSET
    hashicorp_vault_version: None | str | Unset = "0"
    owner_group_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        secret = self.secret

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

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

        hashicorp_vault_version: None | str | Unset
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
                "secret": secret,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
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

        secret = d.pop("secret")

        _kind = d.pop("kind", UNSET)
        kind: NewSecretDataAttributesKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_new_secret_data_attributes_kind(_kind)

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

        def _parse_hashicorp_vault_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

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

        new_secret_data_attributes = cls(
            name=name,
            secret=secret,
            kind=kind,
            hashicorp_vault_mount=hashicorp_vault_mount,
            hashicorp_vault_path=hashicorp_vault_path,
            hashicorp_vault_version=hashicorp_vault_version,
            owner_group_ids=owner_group_ids,
        )

        return new_secret_data_attributes
