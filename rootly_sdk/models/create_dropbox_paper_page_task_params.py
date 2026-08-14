from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_dropbox_paper_page_task_params_task_type import (
    CreateDropboxPaperPageTaskParamsTaskType,
    check_create_dropbox_paper_page_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_dropbox_paper_page_task_params_namespace import CreateDropboxPaperPageTaskParamsNamespace
    from ..models.create_dropbox_paper_page_task_params_parent_folder import (
        CreateDropboxPaperPageTaskParamsParentFolder,
    )


T = TypeVar("T", bound="CreateDropboxPaperPageTaskParams")


@_attrs_define
class CreateDropboxPaperPageTaskParams:
    """
    Attributes:
        title (str): The page task title
        task_type (Union[Unset, CreateDropboxPaperPageTaskParamsTaskType]):
        post_mortem_template_id (Union[Unset, str]): Retrospective template to use when creating page task, if desired
        mark_post_mortem_as_published (Union[Unset, bool]):  Default: True.
        content (Union[Unset, str]): The page content
        namespace (Union[Unset, CreateDropboxPaperPageTaskParamsNamespace]):
        parent_folder (Union[Unset, CreateDropboxPaperPageTaskParamsParentFolder]):
    """

    title: str
    task_type: Unset | CreateDropboxPaperPageTaskParamsTaskType = UNSET
    post_mortem_template_id: Unset | str = UNSET
    mark_post_mortem_as_published: Unset | bool = True
    content: Unset | str = UNSET
    namespace: Union[Unset, "CreateDropboxPaperPageTaskParamsNamespace"] = UNSET
    parent_folder: Union[Unset, "CreateDropboxPaperPageTaskParamsParentFolder"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        post_mortem_template_id = self.post_mortem_template_id

        mark_post_mortem_as_published = self.mark_post_mortem_as_published

        content = self.content

        namespace: Unset | dict[str, Any] = UNSET
        if not isinstance(self.namespace, Unset):
            namespace = self.namespace.to_dict()

        parent_folder: Unset | dict[str, Any] = UNSET
        if not isinstance(self.parent_folder, Unset):
            parent_folder = self.parent_folder.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if task_type is not UNSET:
            field_dict["task_type"] = task_type
        if post_mortem_template_id is not UNSET:
            field_dict["post_mortem_template_id"] = post_mortem_template_id
        if mark_post_mortem_as_published is not UNSET:
            field_dict["mark_post_mortem_as_published"] = mark_post_mortem_as_published
        if content is not UNSET:
            field_dict["content"] = content
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if parent_folder is not UNSET:
            field_dict["parent_folder"] = parent_folder

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_dropbox_paper_page_task_params_namespace import CreateDropboxPaperPageTaskParamsNamespace
        from ..models.create_dropbox_paper_page_task_params_parent_folder import (
            CreateDropboxPaperPageTaskParamsParentFolder,
        )

        d = dict(src_dict)
        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateDropboxPaperPageTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_dropbox_paper_page_task_params_task_type(_task_type)

        post_mortem_template_id = d.pop("post_mortem_template_id", UNSET)

        mark_post_mortem_as_published = d.pop("mark_post_mortem_as_published", UNSET)

        content = d.pop("content", UNSET)

        _namespace = d.pop("namespace", UNSET)
        namespace: Unset | CreateDropboxPaperPageTaskParamsNamespace
        if isinstance(_namespace, Unset):
            namespace = UNSET
        else:
            namespace = CreateDropboxPaperPageTaskParamsNamespace.from_dict(_namespace)

        _parent_folder = d.pop("parent_folder", UNSET)
        parent_folder: Unset | CreateDropboxPaperPageTaskParamsParentFolder
        if isinstance(_parent_folder, Unset):
            parent_folder = UNSET
        else:
            parent_folder = CreateDropboxPaperPageTaskParamsParentFolder.from_dict(_parent_folder)

        create_dropbox_paper_page_task_params = cls(
            title=title,
            task_type=task_type,
            post_mortem_template_id=post_mortem_template_id,
            mark_post_mortem_as_published=mark_post_mortem_as_published,
            content=content,
            namespace=namespace,
            parent_folder=parent_folder,
        )

        create_dropbox_paper_page_task_params.additional_properties = d
        return create_dropbox_paper_page_task_params

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
