from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alerts_source_sourceable_attributes_type_0_notification_target_type import (
    AlertsSourceSourceableAttributesType0NotificationTargetType,
    check_alerts_source_sourceable_attributes_type_0_notification_target_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alerts_source_sourceable_attributes_type_0_field_mappings_attributes_item import (
        AlertsSourceSourceableAttributesType0FieldMappingsAttributesItem,
    )


T = TypeVar("T", bound="AlertsSourceSourceableAttributesType0")


@_attrs_define
class AlertsSourceSourceableAttributesType0:
    """Provide additional attributes for the underlying source. `auto_resolve`, `resolve_state` and
    `field_mappings_attributes` apply to generic_webhook sources; `accept_threaded_emails`, `notification_target_type`
    and `notification_target_id` apply to email sources.

        Attributes:
            id (UUID | Unset): Unique ID of the underlying source. Read-only; it is resolved from the alert source itself on
                update.
            auto_resolve (bool | Unset): Set this to true to auto-resolve alerts based on field_mappings_attributes
                conditions
            resolve_state (None | str | Unset): This value is matched with the value extracted from alerts payload using
                JSON path in field_mappings_attributes
            accept_threaded_emails (bool | Unset): Set this to false to reject threaded emails
            notification_target_type (AlertsSourceSourceableAttributesType0NotificationTargetType | Unset): Email sources
                only. The type of the notification target every alert from this source pages directly; While it points to an
                active, pageable target, Alert Routes are not evaluated. Only used when the `email-alert-source-notification-
                target` feature flag is on for the team.
            notification_target_id (None | str | Unset): Email sources only. The ID of the notification target. Set to null
                to clear it; this also clears `notification_target_type`. Only used when the `email-alert-source-notification-
                target` feature flag is on for the team.
            field_mappings_attributes (list[AlertsSourceSourceableAttributesType0FieldMappingsAttributesItem] | Unset):
                Specify rules to auto resolve alerts
    """

    id: UUID | Unset = UNSET
    auto_resolve: bool | Unset = UNSET
    resolve_state: None | str | Unset = UNSET
    accept_threaded_emails: bool | Unset = UNSET
    notification_target_type: AlertsSourceSourceableAttributesType0NotificationTargetType | Unset = UNSET
    notification_target_id: None | str | Unset = UNSET
    field_mappings_attributes: list[AlertsSourceSourceableAttributesType0FieldMappingsAttributesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        auto_resolve = self.auto_resolve

        resolve_state: None | str | Unset
        if isinstance(self.resolve_state, Unset):
            resolve_state = UNSET
        else:
            resolve_state = self.resolve_state

        accept_threaded_emails = self.accept_threaded_emails

        notification_target_type: str | Unset = UNSET
        if not isinstance(self.notification_target_type, Unset):
            notification_target_type = self.notification_target_type

        notification_target_id: None | str | Unset
        if isinstance(self.notification_target_id, Unset):
            notification_target_id = UNSET
        else:
            notification_target_id = self.notification_target_id

        field_mappings_attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.field_mappings_attributes, Unset):
            field_mappings_attributes = []
            for field_mappings_attributes_item_data in self.field_mappings_attributes:
                field_mappings_attributes_item = field_mappings_attributes_item_data.to_dict()
                field_mappings_attributes.append(field_mappings_attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if auto_resolve is not UNSET:
            field_dict["auto_resolve"] = auto_resolve
        if resolve_state is not UNSET:
            field_dict["resolve_state"] = resolve_state
        if accept_threaded_emails is not UNSET:
            field_dict["accept_threaded_emails"] = accept_threaded_emails
        if notification_target_type is not UNSET:
            field_dict["notification_target_type"] = notification_target_type
        if notification_target_id is not UNSET:
            field_dict["notification_target_id"] = notification_target_id
        if field_mappings_attributes is not UNSET:
            field_dict["field_mappings_attributes"] = field_mappings_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alerts_source_sourceable_attributes_type_0_field_mappings_attributes_item import (
            AlertsSourceSourceableAttributesType0FieldMappingsAttributesItem,
        )

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        auto_resolve = d.pop("auto_resolve", UNSET)

        def _parse_resolve_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resolve_state = _parse_resolve_state(d.pop("resolve_state", UNSET))

        accept_threaded_emails = d.pop("accept_threaded_emails", UNSET)

        _notification_target_type = d.pop("notification_target_type", UNSET)
        notification_target_type: AlertsSourceSourceableAttributesType0NotificationTargetType | Unset
        if isinstance(_notification_target_type, Unset):
            notification_target_type = UNSET
        else:
            notification_target_type = check_alerts_source_sourceable_attributes_type_0_notification_target_type(
                _notification_target_type
            )

        def _parse_notification_target_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notification_target_id = _parse_notification_target_id(d.pop("notification_target_id", UNSET))

        _field_mappings_attributes = d.pop("field_mappings_attributes", UNSET)
        field_mappings_attributes: list[AlertsSourceSourceableAttributesType0FieldMappingsAttributesItem] | Unset = (
            UNSET
        )
        if _field_mappings_attributes is not UNSET:
            field_mappings_attributes = []
            for field_mappings_attributes_item_data in _field_mappings_attributes:
                field_mappings_attributes_item = (
                    AlertsSourceSourceableAttributesType0FieldMappingsAttributesItem.from_dict(
                        field_mappings_attributes_item_data
                    )
                )

                field_mappings_attributes.append(field_mappings_attributes_item)

        alerts_source_sourceable_attributes_type_0 = cls(
            id=id,
            auto_resolve=auto_resolve,
            resolve_state=resolve_state,
            accept_threaded_emails=accept_threaded_emails,
            notification_target_type=notification_target_type,
            notification_target_id=notification_target_id,
            field_mappings_attributes=field_mappings_attributes,
        )

        alerts_source_sourceable_attributes_type_0.additional_properties = d
        return alerts_source_sourceable_attributes_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
