from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.private_agent_attributes_providers_item_capabilities_item import (
        PrivateAgentAttributesProvidersItemCapabilitiesItem,
    )
    from ..models.private_agent_attributes_providers_item_health_type_0 import (
        PrivateAgentAttributesProvidersItemHealthType0,
    )
    from ..models.private_agent_attributes_providers_item_policy_type_0 import (
        PrivateAgentAttributesProvidersItemPolicyType0,
    )


T = TypeVar("T", bound="PrivateAgentAttributesProvidersItem")


@_attrs_define
class PrivateAgentAttributesProvidersItem:
    """
    Attributes:
        id (str):
        type_ (str): Provider adapter type, such as kubernetes, prometheus, loki, tempo, pyroscope, elasticsearch,
            opensearch, postgresql, mysql, mcp, http, kafka, redis, or valkey.
        version (None | str):
        health (None | PrivateAgentAttributesProvidersItemHealthType0): Last reported provider health; may be stale when
            the agent is offline. Invalid or absent fields are omitted.
        policy (None | PrivateAgentAttributesProvidersItemPolicyType0): Reported local policy, not credentials or
            provider connection configuration. Fields are provider-type specific: Kubernetes reports namespace scope; search
            providers report index scope; databases report database/schema scope; HTTP reports method/path/header scope;
            Kafka reports topic and message-read scope; Redis and Valkey report diagnostic limits; and each provider family
            normally reports only its applicable numeric limits. Management responses may preserve legacy cross-family
            fields for backwards compatibility; capability catalog and dispatch use provider-scoped execution metadata.
            Invalid or absent fields are omitted.
        capabilities (list[PrivateAgentAttributesProvidersItemCapabilitiesItem]):
    """

    id: str
    type_: str
    version: None | str
    health: None | PrivateAgentAttributesProvidersItemHealthType0
    policy: None | PrivateAgentAttributesProvidersItemPolicyType0
    capabilities: list[PrivateAgentAttributesProvidersItemCapabilitiesItem]

    def to_dict(self) -> dict[str, Any]:
        from ..models.private_agent_attributes_providers_item_health_type_0 import (
            PrivateAgentAttributesProvidersItemHealthType0,
        )
        from ..models.private_agent_attributes_providers_item_policy_type_0 import (
            PrivateAgentAttributesProvidersItemPolicyType0,
        )

        id = self.id

        type_ = self.type_

        version: None | str
        version = self.version

        health: dict[str, Any] | None
        if isinstance(self.health, PrivateAgentAttributesProvidersItemHealthType0):
            health = self.health.to_dict()
        else:
            health = self.health

        policy: dict[str, Any] | None
        if isinstance(self.policy, PrivateAgentAttributesProvidersItemPolicyType0):
            policy = self.policy.to_dict()
        else:
            policy = self.policy

        capabilities = []
        for capabilities_item_data in self.capabilities:
            capabilities_item = capabilities_item_data.to_dict()
            capabilities.append(capabilities_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
                "version": version,
                "health": health,
                "policy": policy,
                "capabilities": capabilities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.private_agent_attributes_providers_item_capabilities_item import (
            PrivateAgentAttributesProvidersItemCapabilitiesItem,
        )
        from ..models.private_agent_attributes_providers_item_health_type_0 import (
            PrivateAgentAttributesProvidersItemHealthType0,
        )
        from ..models.private_agent_attributes_providers_item_policy_type_0 import (
            PrivateAgentAttributesProvidersItemPolicyType0,
        )

        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        def _parse_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        version = _parse_version(d.pop("version"))

        def _parse_health(data: object) -> None | PrivateAgentAttributesProvidersItemHealthType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                health_type_0 = PrivateAgentAttributesProvidersItemHealthType0.from_dict(data)

                return health_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PrivateAgentAttributesProvidersItemHealthType0, data)

        health = _parse_health(d.pop("health"))

        def _parse_policy(data: object) -> None | PrivateAgentAttributesProvidersItemPolicyType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                policy_type_0 = PrivateAgentAttributesProvidersItemPolicyType0.from_dict(data)

                return policy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PrivateAgentAttributesProvidersItemPolicyType0, data)

        policy = _parse_policy(d.pop("policy"))

        capabilities = []
        _capabilities = d.pop("capabilities")
        for capabilities_item_data in _capabilities:
            capabilities_item = PrivateAgentAttributesProvidersItemCapabilitiesItem.from_dict(capabilities_item_data)

            capabilities.append(capabilities_item)

        private_agent_attributes_providers_item = cls(
            id=id,
            type_=type_,
            version=version,
            health=health,
            policy=policy,
            capabilities=capabilities,
        )

        return private_agent_attributes_providers_item
