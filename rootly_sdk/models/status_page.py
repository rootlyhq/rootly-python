from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_page_authentication_method import (
    StatusPageAuthenticationMethod,
    check_status_page_authentication_method,
)
from ..models.status_page_saml_name_identifier_format import (
    StatusPageSamlNameIdentifierFormat,
    check_status_page_saml_name_identifier_format,
)
from ..models.status_page_show_uptime_last_days import (
    StatusPageShowUptimeLastDays,
    check_status_page_show_uptime_last_days,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPage")


@_attrs_define
class StatusPage:
    """
    Attributes:
        title (str): The title of the status page
        created_at (str): Date of creation
        updated_at (str): Date of last update
        slug (Union[Unset, str]): The slug of the status page
        public_title (Union[None, Unset, str]): The public title of the status page
        description (Union[None, Unset, str]): The description of the status page
        public_description (Union[None, Unset, str]): The public description of the status page
        header_color (Union[None, Unset, str]): The color of the header. Eg. "#0061F2"
        footer_color (Union[None, Unset, str]): The color of the footer. Eg. "#1F2F41"
        allow_search_engine_index (Union[None, Unset, bool]): Allow search engines to include your public status page in
            search results
        show_uptime (Union[None, Unset, bool]): Show uptime
        show_uptime_last_days (Union[Unset, StatusPageShowUptimeLastDays]): Show uptime over x days
        success_message (Union[None, Unset, str]): Message showing when all components are operational
        failure_message (Union[None, Unset, str]): Message showing when at least one component is not operational
        authentication_method (Union[Unset, StatusPageAuthenticationMethod]): Authentication method Default: 'none'.
        authentication_enabled (Union[None, Unset, bool]): Enable authentication (deprecated - use authentication_method
            instead) Default: False.
        authentication_password (Union[None, Unset, str]): Authentication password
        saml_idp_sso_service_url (Union[None, Unset, str]): SAML IdP SSO service URL
        saml_idp_slo_service_url (Union[None, Unset, str]): SAML IdP SLO service URL
        saml_idp_cert (Union[None, Unset, str]): SAML IdP certificate
        saml_idp_cert_fingerprint (Union[None, Unset, str]): SAML IdP certificate fingerprint
        saml_name_identifier_format (Union[Unset, StatusPageSamlNameIdentifierFormat]): SAML name identifier format
        website_url (Union[None, Unset, str]): Website URL
        website_privacy_url (Union[None, Unset, str]): Website Privacy URL
        website_support_url (Union[None, Unset, str]): Website Support URL
        ga_tracking_id (Union[None, Unset, str]): Google Analytics tracking ID
        time_zone (Union[None, Unset, str]): A valid IANA time zone name. Default: 'Etc/UTC'.
        public (Union[None, Unset, bool]): Make the status page accessible to the public
        service_ids (Union[Unset, list[str]]): Services attached to the status page
        functionality_ids (Union[Unset, list[str]]): Functionalities attached to the status page
        external_domain_names (Union[Unset, list[str]]): External domain names attached to the status page
        enabled (Union[None, Unset, bool]): Enabled / Disable the status page
    """

    title: str
    created_at: str
    updated_at: str
    slug: Unset | str = UNSET
    public_title: None | Unset | str = UNSET
    description: None | Unset | str = UNSET
    public_description: None | Unset | str = UNSET
    header_color: None | Unset | str = UNSET
    footer_color: None | Unset | str = UNSET
    allow_search_engine_index: None | Unset | bool = UNSET
    show_uptime: None | Unset | bool = UNSET
    show_uptime_last_days: Unset | StatusPageShowUptimeLastDays = UNSET
    success_message: None | Unset | str = UNSET
    failure_message: None | Unset | str = UNSET
    authentication_method: Unset | StatusPageAuthenticationMethod = "none"
    authentication_enabled: None | Unset | bool = False
    authentication_password: None | Unset | str = UNSET
    saml_idp_sso_service_url: None | Unset | str = UNSET
    saml_idp_slo_service_url: None | Unset | str = UNSET
    saml_idp_cert: None | Unset | str = UNSET
    saml_idp_cert_fingerprint: None | Unset | str = UNSET
    saml_name_identifier_format: Unset | StatusPageSamlNameIdentifierFormat = UNSET
    website_url: None | Unset | str = UNSET
    website_privacy_url: None | Unset | str = UNSET
    website_support_url: None | Unset | str = UNSET
    ga_tracking_id: None | Unset | str = UNSET
    time_zone: None | Unset | str = "Etc/UTC"
    public: None | Unset | bool = UNSET
    service_ids: Unset | list[str] = UNSET
    functionality_ids: Unset | list[str] = UNSET
    external_domain_names: Unset | list[str] = UNSET
    enabled: None | Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        created_at = self.created_at

        updated_at = self.updated_at

        slug = self.slug

        public_title: None | Unset | str
        if isinstance(self.public_title, Unset):
            public_title = UNSET
        else:
            public_title = self.public_title

        description: None | Unset | str
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        public_description: None | Unset | str
        if isinstance(self.public_description, Unset):
            public_description = UNSET
        else:
            public_description = self.public_description

        header_color: None | Unset | str
        if isinstance(self.header_color, Unset):
            header_color = UNSET
        else:
            header_color = self.header_color

        footer_color: None | Unset | str
        if isinstance(self.footer_color, Unset):
            footer_color = UNSET
        else:
            footer_color = self.footer_color

        allow_search_engine_index: None | Unset | bool
        if isinstance(self.allow_search_engine_index, Unset):
            allow_search_engine_index = UNSET
        else:
            allow_search_engine_index = self.allow_search_engine_index

        show_uptime: None | Unset | bool
        if isinstance(self.show_uptime, Unset):
            show_uptime = UNSET
        else:
            show_uptime = self.show_uptime

        show_uptime_last_days: Unset | int = UNSET
        if not isinstance(self.show_uptime_last_days, Unset):
            show_uptime_last_days = self.show_uptime_last_days

        success_message: None | Unset | str
        if isinstance(self.success_message, Unset):
            success_message = UNSET
        else:
            success_message = self.success_message

        failure_message: None | Unset | str
        if isinstance(self.failure_message, Unset):
            failure_message = UNSET
        else:
            failure_message = self.failure_message

        authentication_method: Unset | str = UNSET
        if not isinstance(self.authentication_method, Unset):
            authentication_method = self.authentication_method

        authentication_enabled: None | Unset | bool
        if isinstance(self.authentication_enabled, Unset):
            authentication_enabled = UNSET
        else:
            authentication_enabled = self.authentication_enabled

        authentication_password: None | Unset | str
        if isinstance(self.authentication_password, Unset):
            authentication_password = UNSET
        else:
            authentication_password = self.authentication_password

        saml_idp_sso_service_url: None | Unset | str
        if isinstance(self.saml_idp_sso_service_url, Unset):
            saml_idp_sso_service_url = UNSET
        else:
            saml_idp_sso_service_url = self.saml_idp_sso_service_url

        saml_idp_slo_service_url: None | Unset | str
        if isinstance(self.saml_idp_slo_service_url, Unset):
            saml_idp_slo_service_url = UNSET
        else:
            saml_idp_slo_service_url = self.saml_idp_slo_service_url

        saml_idp_cert: None | Unset | str
        if isinstance(self.saml_idp_cert, Unset):
            saml_idp_cert = UNSET
        else:
            saml_idp_cert = self.saml_idp_cert

        saml_idp_cert_fingerprint: None | Unset | str
        if isinstance(self.saml_idp_cert_fingerprint, Unset):
            saml_idp_cert_fingerprint = UNSET
        else:
            saml_idp_cert_fingerprint = self.saml_idp_cert_fingerprint

        saml_name_identifier_format: Unset | str = UNSET
        if not isinstance(self.saml_name_identifier_format, Unset):
            saml_name_identifier_format = self.saml_name_identifier_format

        website_url: None | Unset | str
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        website_privacy_url: None | Unset | str
        if isinstance(self.website_privacy_url, Unset):
            website_privacy_url = UNSET
        else:
            website_privacy_url = self.website_privacy_url

        website_support_url: None | Unset | str
        if isinstance(self.website_support_url, Unset):
            website_support_url = UNSET
        else:
            website_support_url = self.website_support_url

        ga_tracking_id: None | Unset | str
        if isinstance(self.ga_tracking_id, Unset):
            ga_tracking_id = UNSET
        else:
            ga_tracking_id = self.ga_tracking_id

        time_zone: None | Unset | str
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        public: None | Unset | bool
        if isinstance(self.public, Unset):
            public = UNSET
        else:
            public = self.public

        service_ids: Unset | list[str] = UNSET
        if not isinstance(self.service_ids, Unset):
            service_ids = self.service_ids

        functionality_ids: Unset | list[str] = UNSET
        if not isinstance(self.functionality_ids, Unset):
            functionality_ids = self.functionality_ids

        external_domain_names: Unset | list[str] = UNSET
        if not isinstance(self.external_domain_names, Unset):
            external_domain_names = self.external_domain_names

        enabled: None | Unset | bool
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if slug is not UNSET:
            field_dict["slug"] = slug
        if public_title is not UNSET:
            field_dict["public_title"] = public_title
        if description is not UNSET:
            field_dict["description"] = description
        if public_description is not UNSET:
            field_dict["public_description"] = public_description
        if header_color is not UNSET:
            field_dict["header_color"] = header_color
        if footer_color is not UNSET:
            field_dict["footer_color"] = footer_color
        if allow_search_engine_index is not UNSET:
            field_dict["allow_search_engine_index"] = allow_search_engine_index
        if show_uptime is not UNSET:
            field_dict["show_uptime"] = show_uptime
        if show_uptime_last_days is not UNSET:
            field_dict["show_uptime_last_days"] = show_uptime_last_days
        if success_message is not UNSET:
            field_dict["success_message"] = success_message
        if failure_message is not UNSET:
            field_dict["failure_message"] = failure_message
        if authentication_method is not UNSET:
            field_dict["authentication_method"] = authentication_method
        if authentication_enabled is not UNSET:
            field_dict["authentication_enabled"] = authentication_enabled
        if authentication_password is not UNSET:
            field_dict["authentication_password"] = authentication_password
        if saml_idp_sso_service_url is not UNSET:
            field_dict["saml_idp_sso_service_url"] = saml_idp_sso_service_url
        if saml_idp_slo_service_url is not UNSET:
            field_dict["saml_idp_slo_service_url"] = saml_idp_slo_service_url
        if saml_idp_cert is not UNSET:
            field_dict["saml_idp_cert"] = saml_idp_cert
        if saml_idp_cert_fingerprint is not UNSET:
            field_dict["saml_idp_cert_fingerprint"] = saml_idp_cert_fingerprint
        if saml_name_identifier_format is not UNSET:
            field_dict["saml_name_identifier_format"] = saml_name_identifier_format
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if website_privacy_url is not UNSET:
            field_dict["website_privacy_url"] = website_privacy_url
        if website_support_url is not UNSET:
            field_dict["website_support_url"] = website_support_url
        if ga_tracking_id is not UNSET:
            field_dict["ga_tracking_id"] = ga_tracking_id
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if public is not UNSET:
            field_dict["public"] = public
        if service_ids is not UNSET:
            field_dict["service_ids"] = service_ids
        if functionality_ids is not UNSET:
            field_dict["functionality_ids"] = functionality_ids
        if external_domain_names is not UNSET:
            field_dict["external_domain_names"] = external_domain_names
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        slug = d.pop("slug", UNSET)

        def _parse_public_title(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        public_title = _parse_public_title(d.pop("public_title", UNSET))

        def _parse_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_public_description(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        public_description = _parse_public_description(d.pop("public_description", UNSET))

        def _parse_header_color(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        header_color = _parse_header_color(d.pop("header_color", UNSET))

        def _parse_footer_color(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        footer_color = _parse_footer_color(d.pop("footer_color", UNSET))

        def _parse_allow_search_engine_index(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        allow_search_engine_index = _parse_allow_search_engine_index(d.pop("allow_search_engine_index", UNSET))

        def _parse_show_uptime(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        show_uptime = _parse_show_uptime(d.pop("show_uptime", UNSET))

        _show_uptime_last_days = d.pop("show_uptime_last_days", UNSET)
        show_uptime_last_days: Unset | StatusPageShowUptimeLastDays
        if isinstance(_show_uptime_last_days, Unset):
            show_uptime_last_days = UNSET
        else:
            show_uptime_last_days = check_status_page_show_uptime_last_days(_show_uptime_last_days)

        def _parse_success_message(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        success_message = _parse_success_message(d.pop("success_message", UNSET))

        def _parse_failure_message(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        failure_message = _parse_failure_message(d.pop("failure_message", UNSET))

        _authentication_method = d.pop("authentication_method", UNSET)
        authentication_method: Unset | StatusPageAuthenticationMethod
        if isinstance(_authentication_method, Unset):
            authentication_method = UNSET
        else:
            authentication_method = check_status_page_authentication_method(_authentication_method)

        def _parse_authentication_enabled(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        authentication_enabled = _parse_authentication_enabled(d.pop("authentication_enabled", UNSET))

        def _parse_authentication_password(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        authentication_password = _parse_authentication_password(d.pop("authentication_password", UNSET))

        def _parse_saml_idp_sso_service_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        saml_idp_sso_service_url = _parse_saml_idp_sso_service_url(d.pop("saml_idp_sso_service_url", UNSET))

        def _parse_saml_idp_slo_service_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        saml_idp_slo_service_url = _parse_saml_idp_slo_service_url(d.pop("saml_idp_slo_service_url", UNSET))

        def _parse_saml_idp_cert(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        saml_idp_cert = _parse_saml_idp_cert(d.pop("saml_idp_cert", UNSET))

        def _parse_saml_idp_cert_fingerprint(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        saml_idp_cert_fingerprint = _parse_saml_idp_cert_fingerprint(d.pop("saml_idp_cert_fingerprint", UNSET))

        _saml_name_identifier_format = d.pop("saml_name_identifier_format", UNSET)
        saml_name_identifier_format: Unset | StatusPageSamlNameIdentifierFormat
        if isinstance(_saml_name_identifier_format, Unset):
            saml_name_identifier_format = UNSET
        else:
            saml_name_identifier_format = check_status_page_saml_name_identifier_format(_saml_name_identifier_format)

        def _parse_website_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        website_url = _parse_website_url(d.pop("website_url", UNSET))

        def _parse_website_privacy_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        website_privacy_url = _parse_website_privacy_url(d.pop("website_privacy_url", UNSET))

        def _parse_website_support_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        website_support_url = _parse_website_support_url(d.pop("website_support_url", UNSET))

        def _parse_ga_tracking_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        ga_tracking_id = _parse_ga_tracking_id(d.pop("ga_tracking_id", UNSET))

        def _parse_time_zone(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        time_zone = _parse_time_zone(d.pop("time_zone", UNSET))

        def _parse_public(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        public = _parse_public(d.pop("public", UNSET))

        service_ids = cast(list[str], d.pop("service_ids", UNSET))

        functionality_ids = cast(list[str], d.pop("functionality_ids", UNSET))

        external_domain_names = cast(list[str], d.pop("external_domain_names", UNSET))

        def _parse_enabled(data: object) -> None | Unset | bool:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | bool, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        status_page = cls(
            title=title,
            created_at=created_at,
            updated_at=updated_at,
            slug=slug,
            public_title=public_title,
            description=description,
            public_description=public_description,
            header_color=header_color,
            footer_color=footer_color,
            allow_search_engine_index=allow_search_engine_index,
            show_uptime=show_uptime,
            show_uptime_last_days=show_uptime_last_days,
            success_message=success_message,
            failure_message=failure_message,
            authentication_method=authentication_method,
            authentication_enabled=authentication_enabled,
            authentication_password=authentication_password,
            saml_idp_sso_service_url=saml_idp_sso_service_url,
            saml_idp_slo_service_url=saml_idp_slo_service_url,
            saml_idp_cert=saml_idp_cert,
            saml_idp_cert_fingerprint=saml_idp_cert_fingerprint,
            saml_name_identifier_format=saml_name_identifier_format,
            website_url=website_url,
            website_privacy_url=website_privacy_url,
            website_support_url=website_support_url,
            ga_tracking_id=ga_tracking_id,
            time_zone=time_zone,
            public=public,
            service_ids=service_ids,
            functionality_ids=functionality_ids,
            external_domain_names=external_domain_names,
            enabled=enabled,
        )

        status_page.additional_properties = d
        return status_page

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
