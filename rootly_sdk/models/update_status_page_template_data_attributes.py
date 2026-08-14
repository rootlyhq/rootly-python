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
        update_title (Union[None, Unset, str]): Title that will be used for the status page update
        update_status (Union[Unset, UpdateStatusPageTemplateDataAttributesUpdateStatus]): Status of the event the
            template will populate
        kind (Union[Unset, UpdateStatusPageTemplateDataAttributesKind]): The kind of the status page template
        should_notify_subscribers (Union[None, Unset, bool]): Controls if incident subscribers should be notified
        position (Union[Unset, int]): Position of the workflow task
        enabled (Union[None, Unset, bool]): Enable / Disable the status page template
    """

    title: str
    body: str
    update_title: None | Unset | str = UNSET
    update_status: Unset | UpdateStatusPageTemplateDataAttributesUpdateStatus = UNSET
    kind: Unset | UpdateStatusPageTemplateDataAttributesKind = UNSET
    should_notify_subscribers: None | Unset | bool = UNSET
    position: Unset | int = UNSET
    enabled: None | Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        body = self.body

        update_title: None | Unset | str
        if isinstance(self.update_title, Unset):
            update_title = UNSET
        else:
            update_title = self.update_title

        update_status: Unset | str = UNSET
        if not isinstance(self.update_status, Unset):
            update_status = self.update_status

        kind: Unset | str = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        should_notify_subscribers: None | Unset | bool
        if isinstance(self.should_notify_subscribers, Unset):
            should_notify_subscribers = UNSET
        else:
            should_notify_subscribers = self.should_notify_subscribers

        position = self.position

        enabled: None | Unset | bool
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

        def _parse_update_title(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        update_title = _parse_update_title(d.pop("update_title", UNSET))

        _update_status = d.pop("update_status", UNSET)
        update_status: Unset | UpdateStatusPageTemplateDataAttributesUpdateStatus
        if isinstance(_update_status, Unset):
            update_status = UNSET
        else:
            update_status = check_update_status_page_template_data_attributes_update_status(_update_status)

        _kind = d.pop("kind", UNSET)
        kind: Unset | UpdateStatusPageTemplateDataAttributesKind
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_update_status_page_template_data_attributes_kind(_kind)

        def _parse_should_notify_subscribers(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        should_notify_subscribers = _parse_should_notify_subscribers(d.pop("should_notify_subscribers", UNSET))

        position = d.pop("position", UNSET)

        def _parse_enabled(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

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
