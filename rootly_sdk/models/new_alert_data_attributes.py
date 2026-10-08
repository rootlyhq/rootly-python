from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.new_alert_data_attributes_noise import NewAlertDataAttributesNoise, check_new_alert_data_attributes_noise
from ..models.new_alert_data_attributes_notification_target_type import (
    NewAlertDataAttributesNotificationTargetType,
    check_new_alert_data_attributes_notification_target_type,
)
from ..models.new_alert_data_attributes_status import (
    NewAlertDataAttributesStatus,
    check_new_alert_data_attributes_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_alert_data_attributes_actor_type_0 import NewAlertDataAttributesActorType0
    from ..models.new_alert_data_attributes_actor_type_1 import NewAlertDataAttributesActorType1
    from ..models.new_alert_data_attributes_actor_type_2_type_0 import NewAlertDataAttributesActorType2Type0
    from ..models.new_alert_data_attributes_actor_type_2_type_1 import NewAlertDataAttributesActorType2Type1
    from ..models.new_alert_data_attributes_actor_type_3_type_0 import NewAlertDataAttributesActorType3Type0
    from ..models.new_alert_data_attributes_actor_type_3_type_1 import NewAlertDataAttributesActorType3Type1
    from ..models.new_alert_data_attributes_alert_field_values_attributes_item_type_0 import (
        NewAlertDataAttributesAlertFieldValuesAttributesItemType0,
    )
    from ..models.new_alert_data_attributes_data_type_0 import NewAlertDataAttributesDataType0
    from ..models.new_alert_data_attributes_labels_item_type_0 import NewAlertDataAttributesLabelsItemType0
    from ..models.new_alert_data_attributes_notification_targets_type_0_item import (
        NewAlertDataAttributesNotificationTargetsType0Item,
    )


T = TypeVar("T", bound="NewAlertDataAttributes")


@_attrs_define
class NewAlertDataAttributes:
    """
    Attributes:
        summary (str): The summary of the alert
        actor (NewAlertDataAttributesActorType0 | NewAlertDataAttributesActorType1 |
            NewAlertDataAttributesActorType2Type0 | NewAlertDataAttributesActorType2Type1 |
            NewAlertDataAttributesActorType3Type0 | NewAlertDataAttributesActorType3Type1 | Unset): The user to record as
            performing this action. Only available when actor attribution is enabled for the organization; otherwise it is
            ignored. Only supported with Global and Team API keys; with a Team API key the user must belong to one of the
            key's teams. When omitted or null, the action is attributed to the API key. Otherwise provide either `email` or
            `user_id`, not both.
        noise (NewAlertDataAttributesNoise | Unset): Whether the alert is marked as noise
        source (str | Unset): Deprecated. Accepted for backwards compatibility; new clients should omit. Defaults to
            `api`.
        status (NewAlertDataAttributesStatus | Unset): Only available for organizations with Rootly On-Call enabled. Can
            be one of open, triggered.
        description (None | str | Unset): The description of the alert
        service_ids (list[str] | None | Unset): The Service IDs to attach to the alert. If your organization has On-Call
            enabled and your notification target is a Service. This field will be automatically set for you.
        group_ids (list[str] | None | Unset): The Group IDs to attach to the alert. If your organization has On-Call
            enabled and your notification target is a Group. This field will be automatically set for you.
        functionality_ids (list[str] | None | Unset): The Functionality IDs to attach to the alert
        environment_ids (list[str] | None | Unset): The Environment IDs to attach to the alert
        started_at (datetime.datetime | None | Unset): Alert start datetime
        ended_at (datetime.datetime | None | Unset): Alert end datetime
        external_id (None | str | Unset): External ID
        external_url (None | str | Unset): External Url
        alert_urgency_id (None | str | Unset): The ID of the alert urgency
        notification_target_type (NewAlertDataAttributesNotificationTargetType | Unset): Only available for
            organizations with Rootly On-Call enabled. Can be one of Group, Service, EscalationPolicy, Functionality, User.
            Please contact support if you encounter issues using `Functionality` as a notification target type.
        notification_target_id (None | str | Unset): Only available for organizations with Rootly On-Call enabled. The
            _identifier_ of the notification target object.
        notification_targets (list[NewAlertDataAttributesNotificationTargetsType0Item] | None | Unset): Only available
            for organizations with Rootly On-Call enabled. Page multiple destinations (any combination of Group, Service,
            EscalationPolicy, Functionality, or User) in a single request. `Functionality` targets require the
            `enable_paging_functionalities` feature; a request that includes one while it is disabled is rejected. Applies
            to alert creation only. When provided, this takes precedence over the singular `notification_target_type` /
            `notification_target_id` fields.
        labels (list[NewAlertDataAttributesLabelsItemType0 | None] | Unset):
        data (NewAlertDataAttributesDataType0 | None | Unset): Additional data
        deduplication_key (None | str | Unset): Alerts sharing the same deduplication key are treated as a single alert.
        alert_field_values_attributes (list[NewAlertDataAttributesAlertFieldValuesAttributesItemType0 | None] | Unset):
            Custom alert field values to create with the alert
    """

    summary: str
    actor: (
        NewAlertDataAttributesActorType0
        | NewAlertDataAttributesActorType1
        | NewAlertDataAttributesActorType2Type0
        | NewAlertDataAttributesActorType2Type1
        | NewAlertDataAttributesActorType3Type0
        | NewAlertDataAttributesActorType3Type1
        | Unset
    ) = UNSET
    noise: NewAlertDataAttributesNoise | Unset = UNSET
    source: str | Unset = UNSET
    status: NewAlertDataAttributesStatus | Unset = UNSET
    description: None | str | Unset = UNSET
    service_ids: list[str] | None | Unset = UNSET
    group_ids: list[str] | None | Unset = UNSET
    functionality_ids: list[str] | None | Unset = UNSET
    environment_ids: list[str] | None | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    ended_at: datetime.datetime | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    external_url: None | str | Unset = UNSET
    alert_urgency_id: None | str | Unset = UNSET
    notification_target_type: NewAlertDataAttributesNotificationTargetType | Unset = UNSET
    notification_target_id: None | str | Unset = UNSET
    notification_targets: list[NewAlertDataAttributesNotificationTargetsType0Item] | None | Unset = UNSET
    labels: list[NewAlertDataAttributesLabelsItemType0 | None] | Unset = UNSET
    data: NewAlertDataAttributesDataType0 | None | Unset = UNSET
    deduplication_key: None | str | Unset = UNSET
    alert_field_values_attributes: list[NewAlertDataAttributesAlertFieldValuesAttributesItemType0 | None] | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.new_alert_data_attributes_actor_type_0 import NewAlertDataAttributesActorType0
        from ..models.new_alert_data_attributes_actor_type_1 import NewAlertDataAttributesActorType1
        from ..models.new_alert_data_attributes_actor_type_2_type_0 import NewAlertDataAttributesActorType2Type0
        from ..models.new_alert_data_attributes_actor_type_2_type_1 import NewAlertDataAttributesActorType2Type1
        from ..models.new_alert_data_attributes_actor_type_3_type_0 import NewAlertDataAttributesActorType3Type0
        from ..models.new_alert_data_attributes_alert_field_values_attributes_item_type_0 import (
            NewAlertDataAttributesAlertFieldValuesAttributesItemType0,
        )
        from ..models.new_alert_data_attributes_data_type_0 import NewAlertDataAttributesDataType0
        from ..models.new_alert_data_attributes_labels_item_type_0 import NewAlertDataAttributesLabelsItemType0

        summary = self.summary

        actor: dict[str, Any] | Unset
        if isinstance(self.actor, Unset):
            actor = UNSET
        elif isinstance(self.actor, NewAlertDataAttributesActorType0):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, NewAlertDataAttributesActorType1):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, NewAlertDataAttributesActorType2Type0):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, NewAlertDataAttributesActorType2Type1):
            actor = self.actor.to_dict()
        elif isinstance(self.actor, NewAlertDataAttributesActorType3Type0):
            actor = self.actor.to_dict()
        else:
            actor = self.actor.to_dict()

        noise: str | Unset = UNSET
        if not isinstance(self.noise, Unset):
            noise = self.noise

        source = self.source

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        service_ids: list[str] | None | Unset
        if isinstance(self.service_ids, Unset):
            service_ids = UNSET
        elif isinstance(self.service_ids, list):
            service_ids = self.service_ids

        else:
            service_ids = self.service_ids

        group_ids: list[str] | None | Unset
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        functionality_ids: list[str] | None | Unset
        if isinstance(self.functionality_ids, Unset):
            functionality_ids = UNSET
        elif isinstance(self.functionality_ids, list):
            functionality_ids = self.functionality_ids

        else:
            functionality_ids = self.functionality_ids

        environment_ids: list[str] | None | Unset
        if isinstance(self.environment_ids, Unset):
            environment_ids = UNSET
        elif isinstance(self.environment_ids, list):
            environment_ids = self.environment_ids

        else:
            environment_ids = self.environment_ids

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        ended_at: None | str | Unset
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        external_url: None | str | Unset
        if isinstance(self.external_url, Unset):
            external_url = UNSET
        else:
            external_url = self.external_url

        alert_urgency_id: None | str | Unset
        if isinstance(self.alert_urgency_id, Unset):
            alert_urgency_id = UNSET
        else:
            alert_urgency_id = self.alert_urgency_id

        notification_target_type: str | Unset = UNSET
        if not isinstance(self.notification_target_type, Unset):
            notification_target_type = self.notification_target_type

        notification_target_id: None | str | Unset
        if isinstance(self.notification_target_id, Unset):
            notification_target_id = UNSET
        else:
            notification_target_id = self.notification_target_id

        notification_targets: list[dict[str, Any]] | None | Unset
        if isinstance(self.notification_targets, Unset):
            notification_targets = UNSET
        elif isinstance(self.notification_targets, list):
            notification_targets = []
            for notification_targets_type_0_item_data in self.notification_targets:
                notification_targets_type_0_item = notification_targets_type_0_item_data.to_dict()
                notification_targets.append(notification_targets_type_0_item)

        else:
            notification_targets = self.notification_targets

        labels: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item: dict[str, Any] | None
                if isinstance(labels_item_data, NewAlertDataAttributesLabelsItemType0):
                    labels_item = labels_item_data.to_dict()
                else:
                    labels_item = labels_item_data
                labels.append(labels_item)

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, NewAlertDataAttributesDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        deduplication_key: None | str | Unset
        if isinstance(self.deduplication_key, Unset):
            deduplication_key = UNSET
        else:
            deduplication_key = self.deduplication_key

        alert_field_values_attributes: list[dict[str, Any] | None] | Unset = UNSET
        if not isinstance(self.alert_field_values_attributes, Unset):
            alert_field_values_attributes = []
            for alert_field_values_attributes_item_data in self.alert_field_values_attributes:
                alert_field_values_attributes_item: dict[str, Any] | None
                if isinstance(
                    alert_field_values_attributes_item_data, NewAlertDataAttributesAlertFieldValuesAttributesItemType0
                ):
                    alert_field_values_attributes_item = alert_field_values_attributes_item_data.to_dict()
                else:
                    alert_field_values_attributes_item = alert_field_values_attributes_item_data
                alert_field_values_attributes.append(alert_field_values_attributes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "summary": summary,
            }
        )
        if actor is not UNSET:
            field_dict["actor"] = actor
        if noise is not UNSET:
            field_dict["noise"] = noise
        if source is not UNSET:
            field_dict["source"] = source
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if functionality_ids is not UNSET:
            field_dict["functionality_ids"] = functionality_ids
        if environment_ids is not UNSET:
            field_dict["environment_ids"] = environment_ids
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if alert_urgency_id is not UNSET:
            field_dict["alert_urgency_id"] = alert_urgency_id
        if notification_target_type is not UNSET:
            field_dict["notification_target_type"] = notification_target_type
        if notification_target_id is not UNSET:
            field_dict["notification_target_id"] = notification_target_id
        if notification_targets is not UNSET:
            field_dict["notification_targets"] = notification_targets
        if labels is not UNSET:
            field_dict["labels"] = labels
        if data is not UNSET:
            field_dict["data"] = data
        if deduplication_key is not UNSET:
            field_dict["deduplication_key"] = deduplication_key
        if alert_field_values_attributes is not UNSET:
            field_dict["alert_field_values_attributes"] = alert_field_values_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_alert_data_attributes_actor_type_0 import NewAlertDataAttributesActorType0
        from ..models.new_alert_data_attributes_actor_type_1 import NewAlertDataAttributesActorType1
        from ..models.new_alert_data_attributes_actor_type_2_type_0 import NewAlertDataAttributesActorType2Type0
        from ..models.new_alert_data_attributes_actor_type_2_type_1 import NewAlertDataAttributesActorType2Type1
        from ..models.new_alert_data_attributes_actor_type_3_type_0 import NewAlertDataAttributesActorType3Type0
        from ..models.new_alert_data_attributes_actor_type_3_type_1 import NewAlertDataAttributesActorType3Type1
        from ..models.new_alert_data_attributes_alert_field_values_attributes_item_type_0 import (
            NewAlertDataAttributesAlertFieldValuesAttributesItemType0,
        )
        from ..models.new_alert_data_attributes_data_type_0 import NewAlertDataAttributesDataType0
        from ..models.new_alert_data_attributes_labels_item_type_0 import NewAlertDataAttributesLabelsItemType0
        from ..models.new_alert_data_attributes_notification_targets_type_0_item import (
            NewAlertDataAttributesNotificationTargetsType0Item,
        )

        d = dict(src_dict)
        summary = d.pop("summary")

        def _parse_actor(
            data: object,
        ) -> (
            NewAlertDataAttributesActorType0
            | NewAlertDataAttributesActorType1
            | NewAlertDataAttributesActorType2Type0
            | NewAlertDataAttributesActorType2Type1
            | NewAlertDataAttributesActorType3Type0
            | NewAlertDataAttributesActorType3Type1
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_0 = NewAlertDataAttributesActorType0.from_dict(data)

                return actor_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_1 = NewAlertDataAttributesActorType1.from_dict(data)

                return actor_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_2_type_0 = NewAlertDataAttributesActorType2Type0.from_dict(data)

                return actor_type_2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_2_type_1 = NewAlertDataAttributesActorType2Type1.from_dict(data)

                return actor_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_3_type_0 = NewAlertDataAttributesActorType3Type0.from_dict(data)

                return actor_type_3_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            actor_type_3_type_1 = NewAlertDataAttributesActorType3Type1.from_dict(data)

            return actor_type_3_type_1

        actor = _parse_actor(d.pop("actor", UNSET))

        _noise = d.pop("noise", UNSET)
        noise: NewAlertDataAttributesNoise | Unset
        if isinstance(_noise, Unset):
            noise = UNSET
        else:
            noise = check_new_alert_data_attributes_noise(_noise)

        source = d.pop("source", UNSET)

        _status = d.pop("status", UNSET)
        status: NewAlertDataAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_new_alert_data_attributes_status(_status)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_service_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                service_ids_type_0 = cast(list[str], data)

                return service_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        service_ids = _parse_service_ids(d.pop("service_ids", UNSET))

        def _parse_group_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = cast(list[str], data)

                return group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        group_ids = _parse_group_ids(d.pop("group_ids", UNSET))

        def _parse_functionality_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                functionality_ids_type_0 = cast(list[str], data)

                return functionality_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        functionality_ids = _parse_functionality_ids(d.pop("functionality_ids", UNSET))

        def _parse_environment_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                environment_ids_type_0 = cast(list[str], data)

                return environment_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        environment_ids = _parse_environment_ids(d.pop("environment_ids", UNSET))

        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))

        def _parse_ended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = datetime.datetime.fromisoformat(data)

                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ended_at = _parse_ended_at(d.pop("ended_at", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_external_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_url = _parse_external_url(d.pop("external_url", UNSET))

        def _parse_alert_urgency_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alert_urgency_id = _parse_alert_urgency_id(d.pop("alert_urgency_id", UNSET))

        _notification_target_type = d.pop("notification_target_type", UNSET)
        notification_target_type: NewAlertDataAttributesNotificationTargetType | Unset
        if isinstance(_notification_target_type, Unset):
            notification_target_type = UNSET
        else:
            notification_target_type = check_new_alert_data_attributes_notification_target_type(
                _notification_target_type
            )

        def _parse_notification_target_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notification_target_id = _parse_notification_target_id(d.pop("notification_target_id", UNSET))

        def _parse_notification_targets(
            data: object,
        ) -> list[NewAlertDataAttributesNotificationTargetsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                notification_targets_type_0 = []
                _notification_targets_type_0 = data
                for notification_targets_type_0_item_data in _notification_targets_type_0:
                    notification_targets_type_0_item = NewAlertDataAttributesNotificationTargetsType0Item.from_dict(
                        notification_targets_type_0_item_data
                    )

                    notification_targets_type_0.append(notification_targets_type_0_item)

                return notification_targets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NewAlertDataAttributesNotificationTargetsType0Item] | None | Unset, data)

        notification_targets = _parse_notification_targets(d.pop("notification_targets", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: list[NewAlertDataAttributesLabelsItemType0 | None] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:

                def _parse_labels_item(data: object) -> NewAlertDataAttributesLabelsItemType0 | None:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        labels_item_type_0 = NewAlertDataAttributesLabelsItemType0.from_dict(data)

                        return labels_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(NewAlertDataAttributesLabelsItemType0 | None, data)

                labels_item = _parse_labels_item(labels_item_data)

                labels.append(labels_item)

        def _parse_data(data: object) -> NewAlertDataAttributesDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = NewAlertDataAttributesDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewAlertDataAttributesDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        def _parse_deduplication_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deduplication_key = _parse_deduplication_key(d.pop("deduplication_key", UNSET))

        _alert_field_values_attributes = d.pop("alert_field_values_attributes", UNSET)
        alert_field_values_attributes: (
            list[NewAlertDataAttributesAlertFieldValuesAttributesItemType0 | None] | Unset
        ) = UNSET
        if _alert_field_values_attributes is not UNSET:
            alert_field_values_attributes = []
            for alert_field_values_attributes_item_data in _alert_field_values_attributes:

                def _parse_alert_field_values_attributes_item(
                    data: object,
                ) -> NewAlertDataAttributesAlertFieldValuesAttributesItemType0 | None:
                    if data is None:
                        return data
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        alert_field_values_attributes_item_type_0 = (
                            NewAlertDataAttributesAlertFieldValuesAttributesItemType0.from_dict(data)
                        )

                        return alert_field_values_attributes_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(NewAlertDataAttributesAlertFieldValuesAttributesItemType0 | None, data)

                alert_field_values_attributes_item = _parse_alert_field_values_attributes_item(
                    alert_field_values_attributes_item_data
                )

                alert_field_values_attributes.append(alert_field_values_attributes_item)

        new_alert_data_attributes = cls(
            summary=summary,
            actor=actor,
            noise=noise,
            source=source,
            status=status,
            description=description,
            service_ids=service_ids,
            group_ids=group_ids,
            functionality_ids=functionality_ids,
            environment_ids=environment_ids,
            started_at=started_at,
            ended_at=ended_at,
            external_id=external_id,
            external_url=external_url,
            alert_urgency_id=alert_urgency_id,
            notification_target_type=notification_target_type,
            notification_target_id=notification_target_id,
            notification_targets=notification_targets,
            labels=labels,
            data=data,
            deduplication_key=deduplication_key,
            alert_field_values_attributes=alert_field_values_attributes,
        )

        return new_alert_data_attributes
