from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewStatusPageAnnouncementDataAttributes")


@_attrs_define
class NewStatusPageAnnouncementDataAttributes:
    """
    Attributes:
        title (str): Title of the announcement
        body (str): Body of the announcement
        notify_subscribers (Union[Unset, bool]): Controls if status page subscribers should be notified. Defaults to
            true
    """

    title: str
    body: str
    notify_subscribers: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        body = self.body

        notify_subscribers = self.notify_subscribers

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "title": title,
                "body": body,
            }
        )
        if notify_subscribers is not UNSET:
            field_dict["notify_subscribers"] = notify_subscribers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        body = d.pop("body")

        notify_subscribers = d.pop("notify_subscribers", UNSET)

        new_status_page_announcement_data_attributes = cls(
            title=title,
            body=body,
            notify_subscribers=notify_subscribers,
        )

        return new_status_page_announcement_data_attributes
