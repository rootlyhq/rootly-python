from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_form_field_option_data import UpdateFormFieldOptionData


T = TypeVar("T", bound="UpdateFormFieldOption")


@_attrs_define
class UpdateFormFieldOption:
    """
    Attributes:
        data (UpdateFormFieldOptionData):
    """

    data: "UpdateFormFieldOptionData"
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
        from ..models.update_form_field_option_data import UpdateFormFieldOptionData

        d = src_dict.copy()
        data = UpdateFormFieldOptionData.from_dict(d.pop("data"))

        update_form_field_option = cls(
            data=data,
        )

        update_form_field_option.additional_properties = d
        return update_form_field_option

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
