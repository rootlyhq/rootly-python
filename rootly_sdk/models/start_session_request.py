from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.start_session_request_platform import StartSessionRequestPlatform, check_start_session_request_platform
from ..types import UNSET, Unset

T = TypeVar("T", bound="StartSessionRequest")


@_attrs_define
class StartSessionRequest:
    """
    Attributes:
        platform (Union[Unset, StartSessionRequestPlatform]): Meeting platform
        title (Union[None, Unset, str]): Human-readable label for the recording session
    """

    platform: Unset | StartSessionRequestPlatform = UNSET
    title: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform: Unset | str = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform

        title: None | Unset | str
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform is not UNSET:
            field_dict["platform"] = platform
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _platform = d.pop("platform", UNSET)
        platform: Unset | StartSessionRequestPlatform
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = check_start_session_request_platform(_platform)

        def _parse_title(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        title = _parse_title(d.pop("title", UNSET))

        start_session_request = cls(
            platform=platform,
            title=title,
        )

        start_session_request.additional_properties = d
        return start_session_request

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
