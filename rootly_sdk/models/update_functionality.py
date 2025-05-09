from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_functionality_data import UpdateFunctionalityData


T = TypeVar("T", bound="UpdateFunctionality")


@_attrs_define
class UpdateFunctionality:
    """
    Attributes:
        data (UpdateFunctionalityData):
    """

    data: "UpdateFunctionalityData"
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
        from ..models.update_functionality_data import UpdateFunctionalityData

        d = src_dict.copy()
        data = UpdateFunctionalityData.from_dict(d.pop("data"))

        update_functionality = cls(
            data=data,
        )

        update_functionality.additional_properties = d
        return update_functionality

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
