from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorsListErrorsItem")


@_attrs_define
class ErrorsListErrorsItem:
    """
    Attributes:
        title (str):
        status (str):
        code (Union[None, Unset, str]):
        detail (Union[None, Unset, str]):
    """

    title: str
    status: str
    code: None | Unset | str = UNSET
    detail: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        status = self.status

        code: None | Unset | str
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        detail: None | Unset | str
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "status": status,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        status = d.pop("status")

        def _parse_code(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_detail(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        detail = _parse_detail(d.pop("detail", UNSET))

        errors_list_errors_item = cls(
            title=title,
            status=status,
            code=code,
            detail=detail,
        )

        errors_list_errors_item.additional_properties = d
        return errors_list_errors_item

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
