from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.escalate_alert_data_attributes_actor_type_0 import EscalateAlertDataAttributesActorType0
    from ..models.escalate_alert_data_attributes_actor_type_1 import EscalateAlertDataAttributesActorType1
    from ..models.escalate_alert_data_attributes_actor_type_2_type_0 import EscalateAlertDataAttributesActorType2Type0
    from ..models.escalate_alert_data_attributes_actor_type_2_type_1 import EscalateAlertDataAttributesActorType2Type1
    from ..models.escalate_alert_data_attributes_actor_type_3_type_0 import EscalateAlertDataAttributesActorType3Type0
    from ..models.escalate_alert_data_attributes_actor_type_3_type_1 import EscalateAlertDataAttributesActorType3Type1


T = TypeVar("T", bound="EscalateAlertDataAttributes")


@_attrs_define
class EscalateAlertDataAttributes:
    """
    Attributes:
        escalation_policy_id (str | Unset): The ID of the escalation policy to escalate to. If omitted, uses the alert's
            current escalation policy from metadata. Required for resolved alerts whose metadata may have been cleared.
        escalation_policy_level (int | Unset): The escalation policy level to escalate to. If omitted, defaults to the
            next level (same EP) or level 1 (different EP).
        actor (EscalateAlertDataAttributesActorType0 | EscalateAlertDataAttributesActorType1 |
            EscalateAlertDataAttributesActorType2Type0 | EscalateAlertDataAttributesActorType2Type1 |
            EscalateAlertDataAttributesActorType3Type0 | EscalateAlertDataAttributesActorType3Type1 | Unset): The user to
            record as performing this action. Only available when actor attribution is enabled for the organization;
            otherwise it is ignored. Only supported with Global and Team API keys; with a Team API key the user must belong
            to one of the key's teams. When omitted or null, the action is attributed to the API key. Otherwise provide
            either `email` or `user_id`, not both.
    """

    escalation_policy_id: str | Unset = UNSET
    escalation_policy_level: int | Unset = UNSET
    actor: (
        EscalateAlertDataAttributesActorType0
        | EscalateAlertDataAttributesActorType1
        | EscalateAlertDataAttributesActorType2Type0
        | EscalateAlertDataAttributesActorType2Type1
        | EscalateAlertDataAttributesActorType3Type0
        | EscalateAlertDataAttributesActorType3Type1
        | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.escalate_alert_data_attributes_actor_type_0 import EscalateAlertDataAttributesActorType0
        from ..models.escalate_alert_data_attributes_actor_type_1 import EscalateAlertDataAttributesActorType1
        from ..models.escalate_alert_data_attributes_actor_type_2_type_0 import (
            EscalateAlertDataAttributesActorType2Type0,
        )
        from ..models.escalate_alert_data_attributes_actor_type_2_type_1 import (
            EscalateAlertDataAttributesActorType2Type1,
        )
        from ..models.escalate_alert_data_attributes_actor_type_3_type_0 import (
            EscalateAlertDataAttributesActorType3Type0,
        )

        escalation_policy_id = self.escalation_policy_id

        escalation_policy_level = self.escalation_policy_level

        actor: dict[str, Any] | Unset
        if isinstance(self.actor, Unset):
            actor = UNSET
        elif isinstance(self.actor, EscalateAlertDataAttributesActorType0):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, EscalateAlertDataAttributesActorType1):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, EscalateAlertDataAttributesActorType2Type0):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, EscalateAlertDataAttributesActorType2Type1):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, EscalateAlertDataAttributesActorType3Type0):
            actor = self.actor.to_dict()
        else:
            actor = self.actor.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if escalation_policy_id is not UNSET:
            field_dict["escalation_policy_id"] = escalation_policy_id
        if escalation_policy_level is not UNSET:
            field_dict["escalation_policy_level"] = escalation_policy_level
        if actor is not UNSET:
            field_dict["actor"] = actor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.escalate_alert_data_attributes_actor_type_0 import EscalateAlertDataAttributesActorType0
        from ..models.escalate_alert_data_attributes_actor_type_1 import EscalateAlertDataAttributesActorType1
        from ..models.escalate_alert_data_attributes_actor_type_2_type_0 import (
            EscalateAlertDataAttributesActorType2Type0,
        )
        from ..models.escalate_alert_data_attributes_actor_type_2_type_1 import (
            EscalateAlertDataAttributesActorType2Type1,
        )
        from ..models.escalate_alert_data_attributes_actor_type_3_type_0 import (
            EscalateAlertDataAttributesActorType3Type0,
        )
        from ..models.escalate_alert_data_attributes_actor_type_3_type_1 import (
            EscalateAlertDataAttributesActorType3Type1,
        )

        d = dict(src_dict)
        escalation_policy_id = d.pop("escalation_policy_id", UNSET)

        escalation_policy_level = d.pop("escalation_policy_level", UNSET)

        def _parse_actor(
            data: object,
        ) -> (
            EscalateAlertDataAttributesActorType0
            | EscalateAlertDataAttributesActorType1
            | EscalateAlertDataAttributesActorType2Type0
            | EscalateAlertDataAttributesActorType2Type1
            | EscalateAlertDataAttributesActorType3Type0
            | EscalateAlertDataAttributesActorType3Type1
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_0 = EscalateAlertDataAttributesActorType0.from_dict(data)

                return actor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_1 = EscalateAlertDataAttributesActorType1.from_dict(data)

                return actor_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_2_type_0 = EscalateAlertDataAttributesActorType2Type0.from_dict(data)

                return actor_type_2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_2_type_1 = EscalateAlertDataAttributesActorType2Type1.from_dict(data)

                return actor_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_3_type_0 = EscalateAlertDataAttributesActorType3Type0.from_dict(data)

                return actor_type_3_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            actor_type_3_type_1 = EscalateAlertDataAttributesActorType3Type1.from_dict(data)

            return actor_type_3_type_1

        actor = _parse_actor(d.pop("actor", UNSET))

        escalate_alert_data_attributes = cls(
            escalation_policy_id=escalation_policy_id,
            escalation_policy_level=escalation_policy_level,
            actor=actor,
        )

        return escalate_alert_data_attributes
