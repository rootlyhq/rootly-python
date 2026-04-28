from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.update_status_page_template_data_attributes_kind import (
    UpdateStatusPageTemplateDataAttributesKind,
    check_update_status_page_template_data_attributes_kind,
)
from ..models.update_status_page_template_data_attributes_update_status import (
    UpdateStatusPageTemplateDataAttributesUpdateStatus,
    check_update_status_page_template_data_attributes_update_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateStatusPageTemplateDataAttributes")


@_attrs_define
class UpdateStatusPageTemplateDataAttributes:
    """
    Attributes:
        title (str): Title of the template
        body (str): Description of the event the template will populate
        update_title (None | str | Unset): Title that will be used for the status page update
        update_status (UpdateStatusPageTemplateDataAttributesUpdateStatus | Unset): Status of the event the template
            will populate
        kind (UpdateStatusPageTemplateDataAttributesKind | Unset): The kind of the status page template
        should_notify_subscribers (bool | None | Unset): Controls if incident subscribers should be notified
        position (int | Unset): Position of the workflow task
        enabled (bool | None | Unset): Enable / Disable the status page template
    """

    title: str
    body: str
    update_title: None | str | Unset = UNSET
    update_status: UpdateStatusPageTemplateDataAttributesUpdateStatus | Unset = UNSET
    kind: UpdateStatusPageTemplateDataAttributesKind | Unset = UNSET
    should_notify_subscribers: bool | None | Unset = UNSET
    position: int | Unset = UNSET
    enabled: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        body = self.body

        update_title: None | str | Unset
        if isinstance(self.update_title, Unset):
            update_title = UNSET
        else:
            update_title = self.update_title

        update_status: str | Unset = UNSET
        if not isinstance(self.update_status, Unset):
            update_status = self.update_status

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        should_notify_subscribers: bool | None | Unset
        if isinstance(self.should_notify_subscribers, Unset):
            should_notify_subscribers = UNSET
        else:
            should_notify_subscribers = self.should_notify_subscribers

        position = self.position

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "title": title,
                "body": body,
            }
        )
        if update_title is not UNSET:
            field_dict["update_title"] = update_title
        if update_status is not UNSET:
            field_dict["update_status"] = update_status
        if kind is not UNSET:
            field_dict["kind"] = kind
        if should_notify_subscribers is not UNSET:
            field_dict["should_notify_subscribers"] = should_notify_subscribers
        if position is not UNSET:
            field_dict["position"] = position
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        body = d.pop("body")

        def _parse_update_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        update_title = _parse_update_title(d.pop("update_title", UNSET))

        _update_status = d.pop("update_status", UNSET)
        update_status: UpdateStatusPageTemplateDataAttributesUpdateStatus | Unset
        if isinstance(_update_status, Unset):
            update_status = UNSET
        else:
            update_status = check_update_status_page_template_data_attributes_update_status(_update_status)

        _kind = d.pop("kind", UNSET)
        kind: UpdateStatusPageTemplateDataAttributesKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_update_status_page_template_data_attributes_kind(_kind)

        def _parse_should_notify_subscribers(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        should_notify_subscribers = _parse_should_notify_subscribers(d.pop("should_notify_subscribers", UNSET))

        position = d.pop("position", UNSET)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        update_status_page_template_data_attributes = cls(
            title=title,
            body=body,
            update_title=update_title,
            update_status=update_status,
            kind=kind,
            should_notify_subscribers=should_notify_subscribers,
            position=position,
            enabled=enabled,
        )

        return update_status_page_template_data_attributes
