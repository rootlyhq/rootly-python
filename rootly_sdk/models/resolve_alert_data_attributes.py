from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resolve_alert_data_attributes_actor_type_0 import ResolveAlertDataAttributesActorType0
    from ..models.resolve_alert_data_attributes_actor_type_1 import ResolveAlertDataAttributesActorType1
    from ..models.resolve_alert_data_attributes_actor_type_2_type_0 import ResolveAlertDataAttributesActorType2Type0
    from ..models.resolve_alert_data_attributes_actor_type_2_type_1 import ResolveAlertDataAttributesActorType2Type1
    from ..models.resolve_alert_data_attributes_actor_type_3_type_0 import ResolveAlertDataAttributesActorType3Type0
    from ..models.resolve_alert_data_attributes_actor_type_3_type_1 import ResolveAlertDataAttributesActorType3Type1


T = TypeVar("T", bound="ResolveAlertDataAttributes")


@_attrs_define
class ResolveAlertDataAttributes:
    """
    Attributes:
        resolution_message (None | str | Unset): How was the alert resolved?
        resolve_related_incidents (bool | None | Unset): Resolve all associated incidents
        actor (ResolveAlertDataAttributesActorType0 | ResolveAlertDataAttributesActorType1 |
            ResolveAlertDataAttributesActorType2Type0 | ResolveAlertDataAttributesActorType2Type1 |
            ResolveAlertDataAttributesActorType3Type0 | ResolveAlertDataAttributesActorType3Type1 | Unset): The user to
            record as performing this action. Only available when actor attribution is enabled for the organization;
            otherwise it is ignored. Only supported with Global and Team API keys; with a Team API key the user must belong
            to one of the key's teams. When omitted or null, the action is attributed to the API key. Otherwise provide
            either `email` or `user_id`, not both.
    """

    resolution_message: None | str | Unset = UNSET
    resolve_related_incidents: bool | None | Unset = UNSET
    actor: (
        ResolveAlertDataAttributesActorType0
        | ResolveAlertDataAttributesActorType1
        | ResolveAlertDataAttributesActorType2Type0
        | ResolveAlertDataAttributesActorType2Type1
        | ResolveAlertDataAttributesActorType3Type0
        | ResolveAlertDataAttributesActorType3Type1
        | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.resolve_alert_data_attributes_actor_type_0 import ResolveAlertDataAttributesActorType0
        from ..models.resolve_alert_data_attributes_actor_type_1 import ResolveAlertDataAttributesActorType1
        from ..models.resolve_alert_data_attributes_actor_type_2_type_0 import ResolveAlertDataAttributesActorType2Type0
        from ..models.resolve_alert_data_attributes_actor_type_2_type_1 import ResolveAlertDataAttributesActorType2Type1
        from ..models.resolve_alert_data_attributes_actor_type_3_type_0 import ResolveAlertDataAttributesActorType3Type0

        resolution_message: None | str | Unset
        if isinstance(self.resolution_message, Unset):
            resolution_message = UNSET
        else:
            resolution_message = self.resolution_message

        resolve_related_incidents: bool | None | Unset
        if isinstance(self.resolve_related_incidents, Unset):
            resolve_related_incidents = UNSET
        else:
            resolve_related_incidents = self.resolve_related_incidents

        actor: dict[str, Any] | Unset
        if isinstance(self.actor, Unset):
            actor = UNSET
        elif isinstance(self.actor, ResolveAlertDataAttributesActorType0):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, ResolveAlertDataAttributesActorType1):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, ResolveAlertDataAttributesActorType2Type0):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, ResolveAlertDataAttributesActorType2Type1):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, ResolveAlertDataAttributesActorType3Type0):
            actor = self.actor.to_dict()
        else:
            actor = self.actor.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if resolution_message is not UNSET:
            field_dict["resolution_message"] = resolution_message
        if resolve_related_incidents is not UNSET:
            field_dict["resolve_related_incidents"] = resolve_related_incidents
        if actor is not UNSET:
            field_dict["actor"] = actor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resolve_alert_data_attributes_actor_type_0 import ResolveAlertDataAttributesActorType0
        from ..models.resolve_alert_data_attributes_actor_type_1 import ResolveAlertDataAttributesActorType1
        from ..models.resolve_alert_data_attributes_actor_type_2_type_0 import ResolveAlertDataAttributesActorType2Type0
        from ..models.resolve_alert_data_attributes_actor_type_2_type_1 import ResolveAlertDataAttributesActorType2Type1
        from ..models.resolve_alert_data_attributes_actor_type_3_type_0 import ResolveAlertDataAttributesActorType3Type0
        from ..models.resolve_alert_data_attributes_actor_type_3_type_1 import ResolveAlertDataAttributesActorType3Type1

        d = dict(src_dict)

        def _parse_resolution_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolution_message = _parse_resolution_message(d.pop("resolution_message", UNSET))

        def _parse_resolve_related_incidents(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        resolve_related_incidents = _parse_resolve_related_incidents(d.pop("resolve_related_incidents", UNSET))

        def _parse_actor(
            data: object,
        ) -> (
            ResolveAlertDataAttributesActorType0
            | ResolveAlertDataAttributesActorType1
            | ResolveAlertDataAttributesActorType2Type0
            | ResolveAlertDataAttributesActorType2Type1
            | ResolveAlertDataAttributesActorType3Type0
            | ResolveAlertDataAttributesActorType3Type1
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_0 = ResolveAlertDataAttributesActorType0.from_dict(data)

                return actor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_1 = ResolveAlertDataAttributesActorType1.from_dict(data)

                return actor_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_2_type_0 = ResolveAlertDataAttributesActorType2Type0.from_dict(data)

                return actor_type_2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_2_type_1 = ResolveAlertDataAttributesActorType2Type1.from_dict(data)

                return actor_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_3_type_0 = ResolveAlertDataAttributesActorType3Type0.from_dict(data)

                return actor_type_3_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            actor_type_3_type_1 = ResolveAlertDataAttributesActorType3Type1.from_dict(data)

            return actor_type_3_type_1

        actor = _parse_actor(d.pop("actor", UNSET))

        resolve_alert_data_attributes = cls(
            resolution_message=resolution_message,
            resolve_related_incidents=resolve_related_incidents,
            actor=actor,
        )

        return resolve_alert_data_attributes
