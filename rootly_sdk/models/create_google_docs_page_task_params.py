from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_google_docs_page_task_params_task_type import (
    CreateGoogleDocsPageTaskParamsTaskType,
    check_create_google_docs_page_task_params_task_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_google_docs_page_task_params_drive import CreateGoogleDocsPageTaskParamsDrive
    from ..models.create_google_docs_page_task_params_parent_folder import CreateGoogleDocsPageTaskParamsParentFolder


T = TypeVar("T", bound="CreateGoogleDocsPageTaskParams")


@_attrs_define
class CreateGoogleDocsPageTaskParams:
    """
    Attributes:
        title (str): The page title
        task_type (Union[Unset, CreateGoogleDocsPageTaskParamsTaskType]):
        post_mortem_template_id (Union[Unset, str]): Retrospective template to use when creating page, if desired
        mark_post_mortem_as_published (Union[Unset, bool]):  Default: True.
        drive (Union[Unset, CreateGoogleDocsPageTaskParamsDrive]):
        parent_folder (Union[Unset, CreateGoogleDocsPageTaskParamsParentFolder]):
        content (Union[Unset, str]): The page content
        template_id (Union[Unset, str]): The Google Doc file ID to use as a template
        permissions (Union[Unset, str]): Page permissions JSON
        include_overview (Union[Unset, bool]):  Default: True.
        include_timeline (Union[Unset, bool]):  Default: True.
        include_follow_ups (Union[Unset, bool]):  Default: True.
    """

    title: str
    task_type: Unset | CreateGoogleDocsPageTaskParamsTaskType = UNSET
    post_mortem_template_id: Unset | str = UNSET
    mark_post_mortem_as_published: Unset | bool = True
    drive: Union[Unset, "CreateGoogleDocsPageTaskParamsDrive"] = UNSET
    parent_folder: Union[Unset, "CreateGoogleDocsPageTaskParamsParentFolder"] = UNSET
    content: Unset | str = UNSET
    template_id: Unset | str = UNSET
    permissions: Unset | str = UNSET
    include_overview: Unset | bool = True
    include_timeline: Unset | bool = True
    include_follow_ups: Unset | bool = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        task_type: Unset | str = UNSET
        if not isinstance(self.task_type, Unset):
            task_type = self.task_type

        post_mortem_template_id = self.post_mortem_template_id

        mark_post_mortem_as_published = self.mark_post_mortem_as_published

        drive: Unset | dict[str, Any] = UNSET
        if not isinstance(self.drive, Unset):
            drive = self.drive.to_dict()

        parent_folder: Unset | dict[str, Any] = UNSET
        if not isinstance(self.parent_folder, Unset):
            parent_folder = self.parent_folder.to_dict()

        content = self.content

        template_id = self.template_id

        permissions = self.permissions

        include_overview = self.include_overview

        include_timeline = self.include_timeline

        include_follow_ups = self.include_follow_ups

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
        if drive is not UNSET:
            field_dict["drive"] = drive
        if parent_folder is not UNSET:
            field_dict["parent_folder"] = parent_folder
        if content is not UNSET:
            field_dict["content"] = content
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if include_overview is not UNSET:
            field_dict["include_overview"] = include_overview
        if include_timeline is not UNSET:
            field_dict["include_timeline"] = include_timeline
        if include_follow_ups is not UNSET:
            field_dict["include_follow_ups"] = include_follow_ups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_google_docs_page_task_params_drive import CreateGoogleDocsPageTaskParamsDrive
        from ..models.create_google_docs_page_task_params_parent_folder import (
            CreateGoogleDocsPageTaskParamsParentFolder,
        )

        d = dict(src_dict)
        title = d.pop("title")

        _task_type = d.pop("task_type", UNSET)
        task_type: Unset | CreateGoogleDocsPageTaskParamsTaskType
        if isinstance(_task_type, Unset):
            task_type = UNSET
        else:
            task_type = check_create_google_docs_page_task_params_task_type(_task_type)

        post_mortem_template_id = d.pop("post_mortem_template_id", UNSET)

        mark_post_mortem_as_published = d.pop("mark_post_mortem_as_published", UNSET)

        _drive = d.pop("drive", UNSET)
        drive: Unset | CreateGoogleDocsPageTaskParamsDrive
        if isinstance(_drive, Unset):
            drive = UNSET
        else:
            drive = CreateGoogleDocsPageTaskParamsDrive.from_dict(_drive)

        _parent_folder = d.pop("parent_folder", UNSET)
        parent_folder: Unset | CreateGoogleDocsPageTaskParamsParentFolder
        if isinstance(_parent_folder, Unset):
            parent_folder = UNSET
        else:
            parent_folder = CreateGoogleDocsPageTaskParamsParentFolder.from_dict(_parent_folder)

        content = d.pop("content", UNSET)

        template_id = d.pop("template_id", UNSET)

        permissions = d.pop("permissions", UNSET)

        include_overview = d.pop("include_overview", UNSET)

        include_timeline = d.pop("include_timeline", UNSET)

        include_follow_ups = d.pop("include_follow_ups", UNSET)

        create_google_docs_page_task_params = cls(
            title=title,
            task_type=task_type,
            post_mortem_template_id=post_mortem_template_id,
            mark_post_mortem_as_published=mark_post_mortem_as_published,
            drive=drive,
            parent_folder=parent_folder,
            content=content,
            template_id=template_id,
            permissions=permissions,
            include_overview=include_overview,
            include_timeline=include_timeline,
            include_follow_ups=include_follow_ups,
        )

        create_google_docs_page_task_params.additional_properties = d
        return create_google_docs_page_task_params

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
