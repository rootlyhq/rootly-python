from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_template_kind import StatusPageTemplateKind, check_status_page_template_kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageTemplate")


@_attrs_define
class StatusPageTemplate:
    """
    Attributes:
        status_page_id (str):
        title (str): Title of the template
        body (str): Description of the event the template will populate
        created_at (str): Date of creation
        updated_at (str): Date of last update
        update_title (Union[None, Unset, str]): Title that will be used for the status page update
        update_status (Union[None, Unset, str]): Status of the event the template will populate
        kind (Union[Unset, StatusPageTemplateKind]): The kind of the status page template
        should_notify_subscribers (Union[None, Unset, bool]): Controls if incident subscribers should be notified
        enabled (Union[None, Unset, bool]): Enable / Disable the status page template
        position (Union[Unset, int]): Position of the workflow task
    """

    status_page_id: str
    title: str
    body: str
    created_at: str
    updated_at: str
    update_title: Union[None, Unset, str] = UNSET
    update_status: Union[None, Unset, str] = UNSET
    kind: Union[Unset, StatusPageTemplateKind] = UNSET
    should_notify_subscribers: Union[None, Unset, bool] = UNSET
    enabled: Union[None, Unset, bool] = UNSET
    position: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status_page_id = self.status_page_id

        title = self.title

        body = self.body

        created_at = self.created_at

        updated_at = self.updated_at

        update_title: Union[None, Unset, str]
        if isinstance(self.update_title, Unset):
            update_title = UNSET
        else:
            update_title = self.update_title

        update_status: Union[None, Unset, str]
        if isinstance(self.update_status, Unset):
            update_status = UNSET
        else:
            update_status = self.update_status

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        should_notify_subscribers: Union[None, Unset, bool]
        if isinstance(self.should_notify_subscribers, Unset):
            should_notify_subscribers = UNSET
        else:
            should_notify_subscribers = self.should_notify_subscribers

        enabled: Union[None, Unset, bool]
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status_page_id": status_page_id,
                "title": title,
                "body": body,
                "created_at": created_at,
                "updated_at": updated_at,
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
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status_page_id = d.pop("status_page_id")

        title = d.pop("title")

        body = d.pop("body")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_update_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        update_title = _parse_update_title(d.pop("update_title", UNSET))

        def _parse_update_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        update_status = _parse_update_status(d.pop("update_status", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, StatusPageTemplateKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_status_page_template_kind(_kind)

        def _parse_should_notify_subscribers(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        should_notify_subscribers = _parse_should_notify_subscribers(d.pop("should_notify_subscribers", UNSET))

        def _parse_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        position = d.pop("position", UNSET)

        status_page_template = cls(
            status_page_id=status_page_id,
            title=title,
            body=body,
            created_at=created_at,
            updated_at=updated_at,
            update_title=update_title,
            update_status=update_status,
            kind=kind,
            should_notify_subscribers=should_notify_subscribers,
            enabled=enabled,
            position=position,
        )

        status_page_template.additional_properties = d
        return status_page_template

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
