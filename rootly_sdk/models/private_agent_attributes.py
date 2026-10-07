from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.private_agent_attributes_deployment_mode import (
    PrivateAgentAttributesDeploymentMode,
    check_private_agent_attributes_deployment_mode,
)
from ..models.private_agent_attributes_status import PrivateAgentAttributesStatus, check_private_agent_attributes_status

if TYPE_CHECKING:
    from ..models.private_agent_attributes_providers_item import PrivateAgentAttributesProvidersItem


T = TypeVar("T", bound="PrivateAgentAttributes")


@_attrs_define
class PrivateAgentAttributes:
    """
    Attributes:
        name (str):
        description (None | str): Non-sensitive routing metadata. Do not include secrets or personal data.
        enabled (bool): For active agents, whether Rootly may advertise tools and assign new work.
        status (PrivateAgentAttributesStatus):
        online (bool): Active agent seen within two minutes; does not imply all providers are healthy.
        deployment_mode (PrivateAgentAttributesDeploymentMode):
        agent_version (str):
        last_seen_at (datetime.datetime | None):
        schema_digest (None | str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        providers (list[PrivateAgentAttributesProvidersItem]):
    """

    name: str
    description: None | str
    enabled: bool
    status: PrivateAgentAttributesStatus
    online: bool
    deployment_mode: PrivateAgentAttributesDeploymentMode
    agent_version: str
    last_seen_at: datetime.datetime | None
    schema_digest: None | str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    providers: list[PrivateAgentAttributesProvidersItem]

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str
        description = self.description

        enabled = self.enabled

        status: str = self.status

        online = self.online

        deployment_mode: str = self.deployment_mode

        agent_version = self.agent_version

        last_seen_at: None | str
        if isinstance(self.last_seen_at, datetime.datetime):
            last_seen_at = self.last_seen_at.isoformat()
        else:
            last_seen_at = self.last_seen_at

        schema_digest: None | str
        schema_digest = self.schema_digest

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        providers = []
        for providers_item_data in self.providers:
            providers_item = providers_item_data.to_dict()
            providers.append(providers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "description": description,
                "enabled": enabled,
                "status": status,
                "online": online,
                "deployment_mode": deployment_mode,
                "agent_version": agent_version,
                "last_seen_at": last_seen_at,
                "schema_digest": schema_digest,
                "created_at": created_at,
                "updated_at": updated_at,
                "providers": providers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.private_agent_attributes_providers_item import PrivateAgentAttributesProvidersItem

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        enabled = d.pop("enabled")

        status = check_private_agent_attributes_status(d.pop("status"))

        online = d.pop("online")

        deployment_mode = check_private_agent_attributes_deployment_mode(d.pop("deployment_mode"))

        agent_version = d.pop("agent_version")

        def _parse_last_seen_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_seen_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_seen_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_seen_at = _parse_last_seen_at(d.pop("last_seen_at"))

        def _parse_schema_digest(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        schema_digest = _parse_schema_digest(d.pop("schema_digest"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        providers = []
        _providers = d.pop("providers")
        for providers_item_data in _providers:
            providers_item = PrivateAgentAttributesProvidersItem.from_dict(providers_item_data)

            providers.append(providers_item)

        private_agent_attributes = cls(
            name=name,
            description=description,
            enabled=enabled,
            status=status,
            online=online,
            deployment_mode=deployment_mode,
            agent_version=agent_version,
            last_seen_at=last_seen_at,
            schema_digest=schema_digest,
            created_at=created_at,
            updated_at=updated_at,
            providers=providers,
        )

        return private_agent_attributes
