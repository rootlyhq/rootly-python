from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AttachAlertDataAttributes")


@_attrs_define
class AttachAlertDataAttributes:
    """
    Attributes:
        alert_ids (Union[None, list[str]]): Alert Id to attach to the incident
    """

    alert_ids: None | list[str]

    def to_dict(self) -> dict[str, Any]:
        alert_ids: None | list[str]
        if isinstance(self.alert_ids, list):
            alert_ids = self.alert_ids

        else:
            alert_ids = self.alert_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "alert_ids": alert_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_alert_ids(data: object) -> None | list[str]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alert_ids_type_0 = cast(list[str], data)

                return alert_ids_type_0
            except:  # noqa: E722
                pass
            return cast(None | list[str], data)

        alert_ids = _parse_alert_ids(d.pop("alert_ids"))

        attach_alert_data_attributes = cls(
            alert_ids=alert_ids,
        )

        return attach_alert_data_attributes
