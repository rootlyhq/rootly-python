from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.links import Links
    from ..models.playbook_task_list_data_item import PlaybookTaskListDataItem


T = TypeVar("T", bound="PlaybookTaskList")


@_attrs_define
class PlaybookTaskList:
    """
    Attributes:
        data (list['PlaybookTaskListDataItem']):
        links (Links):
    """

    data: list["PlaybookTaskListDataItem"]
    links: "Links"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.links import Links
        from ..models.playbook_task_list_data_item import PlaybookTaskListDataItem

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = PlaybookTaskListDataItem.from_dict(data_item_data)

            data.append(data_item)

        links = Links.from_dict(d.pop("links"))

        playbook_task_list = cls(
            data=data,
            links=links,
        )

        playbook_task_list.additional_properties = d
        return playbook_task_list

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
