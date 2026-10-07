from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snooze_alert_data_attributes_actor_type_0 import SnoozeAlertDataAttributesActorType0
    from ..models.snooze_alert_data_attributes_actor_type_1 import SnoozeAlertDataAttributesActorType1
    from ..models.snooze_alert_data_attributes_actor_type_2_type_0 import SnoozeAlertDataAttributesActorType2Type0
    from ..models.snooze_alert_data_attributes_actor_type_2_type_1 import SnoozeAlertDataAttributesActorType2Type1
    from ..models.snooze_alert_data_attributes_actor_type_3_type_0 import SnoozeAlertDataAttributesActorType3Type0
    from ..models.snooze_alert_data_attributes_actor_type_3_type_1 import SnoozeAlertDataAttributesActorType3Type1


T = TypeVar("T", bound="SnoozeAlertDataAttributes")


@_attrs_define
class SnoozeAlertDataAttributes:
    """
    Attributes:
        delay_minutes (int): Number of minutes to snooze the alert for
        actor (SnoozeAlertDataAttributesActorType0 | SnoozeAlertDataAttributesActorType1 |
            SnoozeAlertDataAttributesActorType2Type0 | SnoozeAlertDataAttributesActorType2Type1 |
            SnoozeAlertDataAttributesActorType3Type0 | SnoozeAlertDataAttributesActorType3Type1 | Unset): The user to record
            as performing this action. Only available when actor attribution is enabled for the organization; otherwise it
            is ignored. Only supported with Global and Team API keys; with a Team API key the user must belong to one of the
            key's teams. When omitted or null, the action is attributed to the API key. Otherwise provide either `email` or
            `user_id`, not both.
    """

    delay_minutes: int
    actor: (
        SnoozeAlertDataAttributesActorType0
        | SnoozeAlertDataAttributesActorType1
        | SnoozeAlertDataAttributesActorType2Type0
        | SnoozeAlertDataAttributesActorType2Type1
        | SnoozeAlertDataAttributesActorType3Type0
        | SnoozeAlertDataAttributesActorType3Type1
        | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.snooze_alert_data_attributes_actor_type_0 import SnoozeAlertDataAttributesActorType0
        from ..models.snooze_alert_data_attributes_actor_type_1 import SnoozeAlertDataAttributesActorType1
        from ..models.snooze_alert_data_attributes_actor_type_2_type_0 import SnoozeAlertDataAttributesActorType2Type0
        from ..models.snooze_alert_data_attributes_actor_type_2_type_1 import SnoozeAlertDataAttributesActorType2Type1
        from ..models.snooze_alert_data_attributes_actor_type_3_type_0 import SnoozeAlertDataAttributesActorType3Type0

        delay_minutes = self.delay_minutes

        actor: dict[str, Any] | Unset
        if isinstance(self.actor, Unset):
            actor = UNSET
        elif isinstance(self.actor, SnoozeAlertDataAttributesActorType0):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, SnoozeAlertDataAttributesActorType1):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, SnoozeAlertDataAttributesActorType2Type0):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, SnoozeAlertDataAttributesActorType2Type1):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, SnoozeAlertDataAttributesActorType3Type0):
            actor = self.actor.to_dict()
        else:
            actor = self.actor.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "delay_minutes": delay_minutes,
            }
        )
        if actor is not UNSET:
            field_dict["actor"] = actor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snooze_alert_data_attributes_actor_type_0 import SnoozeAlertDataAttributesActorType0
        from ..models.snooze_alert_data_attributes_actor_type_1 import SnoozeAlertDataAttributesActorType1
        from ..models.snooze_alert_data_attributes_actor_type_2_type_0 import SnoozeAlertDataAttributesActorType2Type0
        from ..models.snooze_alert_data_attributes_actor_type_2_type_1 import SnoozeAlertDataAttributesActorType2Type1
        from ..models.snooze_alert_data_attributes_actor_type_3_type_0 import SnoozeAlertDataAttributesActorType3Type0
        from ..models.snooze_alert_data_attributes_actor_type_3_type_1 import SnoozeAlertDataAttributesActorType3Type1

        d = dict(src_dict)
        delay_minutes = d.pop("delay_minutes")

        def _parse_actor(
            data: object,
        ) -> (
            SnoozeAlertDataAttributesActorType0
            | SnoozeAlertDataAttributesActorType1
            | SnoozeAlertDataAttributesActorType2Type0
            | SnoozeAlertDataAttributesActorType2Type1
            | SnoozeAlertDataAttributesActorType3Type0
            | SnoozeAlertDataAttributesActorType3Type1
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_0 = SnoozeAlertDataAttributesActorType0.from_dict(data)

                return actor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_1 = SnoozeAlertDataAttributesActorType1.from_dict(data)

                return actor_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_2_type_0 = SnoozeAlertDataAttributesActorType2Type0.from_dict(data)

                return actor_type_2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_2_type_1 = SnoozeAlertDataAttributesActorType2Type1.from_dict(data)

                return actor_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_3_type_0 = SnoozeAlertDataAttributesActorType3Type0.from_dict(data)

                return actor_type_3_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            actor_type_3_type_1 = SnoozeAlertDataAttributesActorType3Type1.from_dict(data)

            return actor_type_3_type_1

        actor = _parse_actor(d.pop("actor", UNSET))

        snooze_alert_data_attributes = cls(
            delay_minutes=delay_minutes,
            actor=actor,
        )

        return snooze_alert_data_attributes
