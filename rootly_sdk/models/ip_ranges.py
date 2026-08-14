from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IpRanges")


@_attrs_define
class IpRanges:
    """
    Attributes:
        integrations_ipv4 (list[str]): IPv4 addresses associated with Rootly integrations.
        integrations_ipv6 (list[str]): IPv6 addresses associated with Rootly integrations.
        webhooks_ipv4 (list[str]): IPv4 addresses associated with Rootly webhooks.
        webhooks_ipv6 (list[str]): IPv6 addresses associated with Rootly webhooks.
    """

    integrations_ipv4: list[str]
    integrations_ipv6: list[str]
    webhooks_ipv4: list[str]
    webhooks_ipv6: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integrations_ipv4 = self.integrations_ipv4

        integrations_ipv6 = self.integrations_ipv6

        webhooks_ipv4 = self.webhooks_ipv4

        webhooks_ipv6 = self.webhooks_ipv6

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "integrations_ipv4": integrations_ipv4,
                "integrations_ipv6": integrations_ipv6,
                "webhooks_ipv4": webhooks_ipv4,
                "webhooks_ipv6": webhooks_ipv6,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        integrations_ipv4 = cast(list[str], d.pop("integrations_ipv4"))

        integrations_ipv6 = cast(list[str], d.pop("integrations_ipv6"))

        webhooks_ipv4 = cast(list[str], d.pop("webhooks_ipv4"))

        webhooks_ipv6 = cast(list[str], d.pop("webhooks_ipv6"))

        ip_ranges = cls(
            integrations_ipv4=integrations_ipv4,
            integrations_ipv6=integrations_ipv6,
            webhooks_ipv4=webhooks_ipv4,
            webhooks_ipv6=webhooks_ipv6,
        )

        ip_ranges.additional_properties = d
        return ip_ranges

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
