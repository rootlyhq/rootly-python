from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sub_status_response_data import SubStatusResponseData


T = TypeVar("T", bound="SubStatusResponse")


@_attrs_define
class SubStatusResponse:
    """
    Attributes:
        data (SubStatusResponseData):
    """

    data: "SubStatusResponseData"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.sub_status_response_data import SubStatusResponseData

        d = src_dict.copy()
        data = SubStatusResponseData.from_dict(d.pop("data"))

        sub_status_response = cls(
            data=data,
        )

        sub_status_response.additional_properties = d
        return sub_status_response

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
