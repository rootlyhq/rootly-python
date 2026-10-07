from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acknowledge_alert_data_attributes_actor_type_0 import AcknowledgeAlertDataAttributesActorType0
    from ..models.acknowledge_alert_data_attributes_actor_type_1 import AcknowledgeAlertDataAttributesActorType1
    from ..models.acknowledge_alert_data_attributes_actor_type_2_type_0 import (
        AcknowledgeAlertDataAttributesActorType2Type0,
    )
    from ..models.acknowledge_alert_data_attributes_actor_type_2_type_1 import (
        AcknowledgeAlertDataAttributesActorType2Type1,
    )
    from ..models.acknowledge_alert_data_attributes_actor_type_3_type_0 import (
        AcknowledgeAlertDataAttributesActorType3Type0,
    )
    from ..models.acknowledge_alert_data_attributes_actor_type_3_type_1 import (
        AcknowledgeAlertDataAttributesActorType3Type1,
    )


T = TypeVar("T", bound="AcknowledgeAlertDataAttributes")


@_attrs_define
class AcknowledgeAlertDataAttributes:
    """
    Attributes:
        actor (AcknowledgeAlertDataAttributesActorType0 | AcknowledgeAlertDataAttributesActorType1 |
            AcknowledgeAlertDataAttributesActorType2Type0 | AcknowledgeAlertDataAttributesActorType2Type1 |
            AcknowledgeAlertDataAttributesActorType3Type0 | AcknowledgeAlertDataAttributesActorType3Type1 | Unset): The user
            to record as performing this action. Only available when actor attribution is enabled for the organization;
            otherwise it is ignored. Only supported with Global and Team API keys; with a Team API key the user must belong
            to one of the key's teams. When omitted or null, the action is attributed to the API key. Otherwise provide
            either `email` or `user_id`, not both.
    """

    actor: (
        AcknowledgeAlertDataAttributesActorType0
        | AcknowledgeAlertDataAttributesActorType1
        | AcknowledgeAlertDataAttributesActorType2Type0
        | AcknowledgeAlertDataAttributesActorType2Type1
        | AcknowledgeAlertDataAttributesActorType3Type0
        | AcknowledgeAlertDataAttributesActorType3Type1
        | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.acknowledge_alert_data_attributes_actor_type_0 import AcknowledgeAlertDataAttributesActorType0
        from ..models.acknowledge_alert_data_attributes_actor_type_1 import AcknowledgeAlertDataAttributesActorType1
        from ..models.acknowledge_alert_data_attributes_actor_type_2_type_0 import (
            AcknowledgeAlertDataAttributesActorType2Type0,
        )
        from ..models.acknowledge_alert_data_attributes_actor_type_2_type_1 import (
            AcknowledgeAlertDataAttributesActorType2Type1,
        )
        from ..models.acknowledge_alert_data_attributes_actor_type_3_type_0 import (
            AcknowledgeAlertDataAttributesActorType3Type0,
        )

        actor: dict[str, Any] | Unset
        if isinstance(self.actor, Unset):
            actor = UNSET
        elif isinstance(self.actor, AcknowledgeAlertDataAttributesActorType0):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, AcknowledgeAlertDataAttributesActorType1):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, AcknowledgeAlertDataAttributesActorType2Type0):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, AcknowledgeAlertDataAttributesActorType2Type1):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, AcknowledgeAlertDataAttributesActorType3Type0):
            actor = self.actor.to_dict()
        else:
            actor = self.actor.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if actor is not UNSET:
            field_dict["actor"] = actor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acknowledge_alert_data_attributes_actor_type_0 import AcknowledgeAlertDataAttributesActorType0
        from ..models.acknowledge_alert_data_attributes_actor_type_1 import AcknowledgeAlertDataAttributesActorType1
        from ..models.acknowledge_alert_data_attributes_actor_type_2_type_0 import (
            AcknowledgeAlertDataAttributesActorType2Type0,
        )
        from ..models.acknowledge_alert_data_attributes_actor_type_2_type_1 import (
            AcknowledgeAlertDataAttributesActorType2Type1,
        )
        from ..models.acknowledge_alert_data_attributes_actor_type_3_type_0 import (
            AcknowledgeAlertDataAttributesActorType3Type0,
        )
        from ..models.acknowledge_alert_data_attributes_actor_type_3_type_1 import (
            AcknowledgeAlertDataAttributesActorType3Type1,
        )

        d = dict(src_dict)

        def _parse_actor(
            data: object,
        ) -> (
            AcknowledgeAlertDataAttributesActorType0
            | AcknowledgeAlertDataAttributesActorType1
            | AcknowledgeAlertDataAttributesActorType2Type0
            | AcknowledgeAlertDataAttributesActorType2Type1
            | AcknowledgeAlertDataAttributesActorType3Type0
            | AcknowledgeAlertDataAttributesActorType3Type1
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_0 = AcknowledgeAlertDataAttributesActorType0.from_dict(data)

                return actor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_1 = AcknowledgeAlertDataAttributesActorType1.from_dict(data)

                return actor_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_2_type_0 = AcknowledgeAlertDataAttributesActorType2Type0.from_dict(data)

                return actor_type_2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_2_type_1 = AcknowledgeAlertDataAttributesActorType2Type1.from_dict(data)

                return actor_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_3_type_0 = AcknowledgeAlertDataAttributesActorType3Type0.from_dict(data)

                return actor_type_3_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            actor_type_3_type_1 = AcknowledgeAlertDataAttributesActorType3Type1.from_dict(data)

            return actor_type_3_type_1

        actor = _parse_actor(d.pop("actor", UNSET))

        acknowledge_alert_data_attributes = cls(
            actor=actor,
        )

        return acknowledge_alert_data_attributes
