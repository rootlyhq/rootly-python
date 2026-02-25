from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_list import IncidentList
from ...models.list_incidents_include import ListIncidentsInclude
from ...models.list_incidents_sort import ListIncidentsSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterstatus: Unset | str = UNSET,
    filterprivate: Unset | str = UNSET,
    filteruser_id: Unset | int = UNSET,
    filterseverity: Unset | str = UNSET,
    filterseverity_id: Unset | str = UNSET,
    filterlabels: Unset | str = UNSET,
    filtertypes: Unset | str = UNSET,
    filtertype_ids: Unset | str = UNSET,
    filterenvironments: Unset | str = UNSET,
    filterenvironment_ids: Unset | str = UNSET,
    filterfunctionalities: Unset | str = UNSET,
    filterfunctionality_ids: Unset | str = UNSET,
    filterfunctionality_names: Unset | str = UNSET,
    filterservices: Unset | str = UNSET,
    filterservice_ids: Unset | str = UNSET,
    filterservice_names: Unset | str = UNSET,
    filterteams: Unset | str = UNSET,
    filterteam_ids: Unset | str = UNSET,
    filterteam_names: Unset | str = UNSET,
    filtercause: Unset | str = UNSET,
    filtercause_ids: Unset | str = UNSET,
    filtercustom_field_selected_option_ids: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterupdated_atgt: Unset | str = UNSET,
    filterupdated_atgte: Unset | str = UNSET,
    filterupdated_atlt: Unset | str = UNSET,
    filterupdated_atlte: Unset | str = UNSET,
    filterstarted_atgt: Unset | str = UNSET,
    filterstarted_atgte: Unset | str = UNSET,
    filterstarted_atlt: Unset | str = UNSET,
    filterstarted_atlte: Unset | str = UNSET,
    filterdetected_atgt: Unset | str = UNSET,
    filterdetected_atgte: Unset | str = UNSET,
    filterdetected_atlt: Unset | str = UNSET,
    filterdetected_atlte: Unset | str = UNSET,
    filteracknowledged_atgt: Unset | str = UNSET,
    filteracknowledged_atgte: Unset | str = UNSET,
    filteracknowledged_atlt: Unset | str = UNSET,
    filteracknowledged_atlte: Unset | str = UNSET,
    filtermitigated_atgt: Unset | str = UNSET,
    filtermitigated_atgte: Unset | str = UNSET,
    filtermitigated_atlt: Unset | str = UNSET,
    filtermitigated_atlte: Unset | str = UNSET,
    filterresolved_atgt: Unset | str = UNSET,
    filterresolved_atgte: Unset | str = UNSET,
    filterresolved_atlt: Unset | str = UNSET,
    filterresolved_atlte: Unset | str = UNSET,
    filterclosed_atgt: Unset | str = UNSET,
    filterclosed_atgte: Unset | str = UNSET,
    filterclosed_atlt: Unset | str = UNSET,
    filterclosed_atlte: Unset | str = UNSET,
    filterin_triage_atgt: Unset | str = UNSET,
    filterin_triage_atgte: Unset | str = UNSET,
    filterin_triage_atlt: Unset | str = UNSET,
    filterin_triage_atlte: Unset | str = UNSET,
    sort: Unset | ListIncidentsSort = UNSET,
    include: Unset | ListIncidentsInclude = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[search]"] = filtersearch

    params["filter[kind]"] = filterkind

    params["filter[status]"] = filterstatus

    params["filter[private]"] = filterprivate

    params["filter[user_id]"] = filteruser_id

    params["filter[severity]"] = filterseverity

    params["filter[severity_id]"] = filterseverity_id

    params["filter[labels]"] = filterlabels

    params["filter[types]"] = filtertypes

    params["filter[type_ids]"] = filtertype_ids

    params["filter[environments]"] = filterenvironments

    params["filter[environment_ids]"] = filterenvironment_ids

    params["filter[functionalities]"] = filterfunctionalities

    params["filter[functionality_ids]"] = filterfunctionality_ids

    params["filter[functionality_names]"] = filterfunctionality_names

    params["filter[services]"] = filterservices

    params["filter[service_ids]"] = filterservice_ids

    params["filter[service_names]"] = filterservice_names

    params["filter[teams]"] = filterteams

    params["filter[team_ids]"] = filterteam_ids

    params["filter[team_names]"] = filterteam_names

    params["filter[cause]"] = filtercause

    params["filter[cause_ids]"] = filtercause_ids

    params["filter[custom_field_selected_option_ids]"] = filtercustom_field_selected_option_ids

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[updated_at][gt]"] = filterupdated_atgt

    params["filter[updated_at][gte]"] = filterupdated_atgte

    params["filter[updated_at][lt]"] = filterupdated_atlt

    params["filter[updated_at][lte]"] = filterupdated_atlte

    params["filter[started_at][gt]"] = filterstarted_atgt

    params["filter[started_at][gte]"] = filterstarted_atgte

    params["filter[started_at][lt]"] = filterstarted_atlt

    params["filter[started_at][lte]"] = filterstarted_atlte

    params["filter[detected_at][gt]"] = filterdetected_atgt

    params["filter[detected_at][gte]"] = filterdetected_atgte

    params["filter[detected_at][lt]"] = filterdetected_atlt

    params["filter[detected_at][lte]"] = filterdetected_atlte

    params["filter[acknowledged_at][gt]"] = filteracknowledged_atgt

    params["filter[acknowledged_at][gte]"] = filteracknowledged_atgte

    params["filter[acknowledged_at][lt]"] = filteracknowledged_atlt

    params["filter[acknowledged_at][lte]"] = filteracknowledged_atlte

    params["filter[mitigated_at][gt]"] = filtermitigated_atgt

    params["filter[mitigated_at][gte]"] = filtermitigated_atgte

    params["filter[mitigated_at][lt]"] = filtermitigated_atlt

    params["filter[mitigated_at][lte]"] = filtermitigated_atlte

    params["filter[resolved_at][gt]"] = filterresolved_atgt

    params["filter[resolved_at][gte]"] = filterresolved_atgte

    params["filter[resolved_at][lt]"] = filterresolved_atlt

    params["filter[resolved_at][lte]"] = filterresolved_atlte

    params["filter[closed_at][gt]"] = filterclosed_atgt

    params["filter[closed_at][gte]"] = filterclosed_atgte

    params["filter[closed_at][lt]"] = filterclosed_atlt

    params["filter[closed_at][lte]"] = filterclosed_atlte

    params["filter[in_triage_at][gt]"] = filterin_triage_atgt

    params["filter[in_triage_at][gte]"] = filterin_triage_atgte

    params["filter[in_triage_at][lt]"] = filterin_triage_atlt

    params["filter[in_triage_at][lte]"] = filterin_triage_atlte

    json_sort: Unset | str = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_include: Unset | str = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/incidents",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IncidentList | None:
    if response.status_code == 200:
        response_200 = IncidentList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[IncidentList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterstatus: Unset | str = UNSET,
    filterprivate: Unset | str = UNSET,
    filteruser_id: Unset | int = UNSET,
    filterseverity: Unset | str = UNSET,
    filterseverity_id: Unset | str = UNSET,
    filterlabels: Unset | str = UNSET,
    filtertypes: Unset | str = UNSET,
    filtertype_ids: Unset | str = UNSET,
    filterenvironments: Unset | str = UNSET,
    filterenvironment_ids: Unset | str = UNSET,
    filterfunctionalities: Unset | str = UNSET,
    filterfunctionality_ids: Unset | str = UNSET,
    filterfunctionality_names: Unset | str = UNSET,
    filterservices: Unset | str = UNSET,
    filterservice_ids: Unset | str = UNSET,
    filterservice_names: Unset | str = UNSET,
    filterteams: Unset | str = UNSET,
    filterteam_ids: Unset | str = UNSET,
    filterteam_names: Unset | str = UNSET,
    filtercause: Unset | str = UNSET,
    filtercause_ids: Unset | str = UNSET,
    filtercustom_field_selected_option_ids: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterupdated_atgt: Unset | str = UNSET,
    filterupdated_atgte: Unset | str = UNSET,
    filterupdated_atlt: Unset | str = UNSET,
    filterupdated_atlte: Unset | str = UNSET,
    filterstarted_atgt: Unset | str = UNSET,
    filterstarted_atgte: Unset | str = UNSET,
    filterstarted_atlt: Unset | str = UNSET,
    filterstarted_atlte: Unset | str = UNSET,
    filterdetected_atgt: Unset | str = UNSET,
    filterdetected_atgte: Unset | str = UNSET,
    filterdetected_atlt: Unset | str = UNSET,
    filterdetected_atlte: Unset | str = UNSET,
    filteracknowledged_atgt: Unset | str = UNSET,
    filteracknowledged_atgte: Unset | str = UNSET,
    filteracknowledged_atlt: Unset | str = UNSET,
    filteracknowledged_atlte: Unset | str = UNSET,
    filtermitigated_atgt: Unset | str = UNSET,
    filtermitigated_atgte: Unset | str = UNSET,
    filtermitigated_atlt: Unset | str = UNSET,
    filtermitigated_atlte: Unset | str = UNSET,
    filterresolved_atgt: Unset | str = UNSET,
    filterresolved_atgte: Unset | str = UNSET,
    filterresolved_atlt: Unset | str = UNSET,
    filterresolved_atlte: Unset | str = UNSET,
    filterclosed_atgt: Unset | str = UNSET,
    filterclosed_atgte: Unset | str = UNSET,
    filterclosed_atlt: Unset | str = UNSET,
    filterclosed_atlte: Unset | str = UNSET,
    filterin_triage_atgt: Unset | str = UNSET,
    filterin_triage_atgte: Unset | str = UNSET,
    filterin_triage_atlt: Unset | str = UNSET,
    filterin_triage_atlte: Unset | str = UNSET,
    sort: Unset | ListIncidentsSort = UNSET,
    include: Unset | ListIncidentsInclude = UNSET,
) -> Response[IncidentList]:
    """List incidents

     List incidents

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterstatus (Union[Unset, str]):
        filterprivate (Union[Unset, str]):
        filteruser_id (Union[Unset, int]):
        filterseverity (Union[Unset, str]):
        filterseverity_id (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filtertypes (Union[Unset, str]):
        filtertype_ids (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filterenvironment_ids (Union[Unset, str]):
        filterfunctionalities (Union[Unset, str]):
        filterfunctionality_ids (Union[Unset, str]):
        filterfunctionality_names (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterservice_ids (Union[Unset, str]):
        filterservice_names (Union[Unset, str]):
        filterteams (Union[Unset, str]):
        filterteam_ids (Union[Unset, str]):
        filterteam_names (Union[Unset, str]):
        filtercause (Union[Unset, str]):
        filtercause_ids (Union[Unset, str]):
        filtercustom_field_selected_option_ids (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterupdated_atgt (Union[Unset, str]):
        filterupdated_atgte (Union[Unset, str]):
        filterupdated_atlt (Union[Unset, str]):
        filterupdated_atlte (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterdetected_atgt (Union[Unset, str]):
        filterdetected_atgte (Union[Unset, str]):
        filterdetected_atlt (Union[Unset, str]):
        filterdetected_atlte (Union[Unset, str]):
        filteracknowledged_atgt (Union[Unset, str]):
        filteracknowledged_atgte (Union[Unset, str]):
        filteracknowledged_atlt (Union[Unset, str]):
        filteracknowledged_atlte (Union[Unset, str]):
        filtermitigated_atgt (Union[Unset, str]):
        filtermitigated_atgte (Union[Unset, str]):
        filtermitigated_atlt (Union[Unset, str]):
        filtermitigated_atlte (Union[Unset, str]):
        filterresolved_atgt (Union[Unset, str]):
        filterresolved_atgte (Union[Unset, str]):
        filterresolved_atlt (Union[Unset, str]):
        filterresolved_atlte (Union[Unset, str]):
        filterclosed_atgt (Union[Unset, str]):
        filterclosed_atgte (Union[Unset, str]):
        filterclosed_atlt (Union[Unset, str]):
        filterclosed_atlte (Union[Unset, str]):
        filterin_triage_atgt (Union[Unset, str]):
        filterin_triage_atgte (Union[Unset, str]):
        filterin_triage_atlt (Union[Unset, str]):
        filterin_triage_atlte (Union[Unset, str]):
        sort (Union[Unset, ListIncidentsSort]):
        include (Union[Unset, ListIncidentsInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentList]
    """

    kwargs = _get_kwargs(
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterkind=filterkind,
        filterstatus=filterstatus,
        filterprivate=filterprivate,
        filteruser_id=filteruser_id,
        filterseverity=filterseverity,
        filterseverity_id=filterseverity_id,
        filterlabels=filterlabels,
        filtertypes=filtertypes,
        filtertype_ids=filtertype_ids,
        filterenvironments=filterenvironments,
        filterenvironment_ids=filterenvironment_ids,
        filterfunctionalities=filterfunctionalities,
        filterfunctionality_ids=filterfunctionality_ids,
        filterfunctionality_names=filterfunctionality_names,
        filterservices=filterservices,
        filterservice_ids=filterservice_ids,
        filterservice_names=filterservice_names,
        filterteams=filterteams,
        filterteam_ids=filterteam_ids,
        filterteam_names=filterteam_names,
        filtercause=filtercause,
        filtercause_ids=filtercause_ids,
        filtercustom_field_selected_option_ids=filtercustom_field_selected_option_ids,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterupdated_atgt=filterupdated_atgt,
        filterupdated_atgte=filterupdated_atgte,
        filterupdated_atlt=filterupdated_atlt,
        filterupdated_atlte=filterupdated_atlte,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterdetected_atgt=filterdetected_atgt,
        filterdetected_atgte=filterdetected_atgte,
        filterdetected_atlt=filterdetected_atlt,
        filterdetected_atlte=filterdetected_atlte,
        filteracknowledged_atgt=filteracknowledged_atgt,
        filteracknowledged_atgte=filteracknowledged_atgte,
        filteracknowledged_atlt=filteracknowledged_atlt,
        filteracknowledged_atlte=filteracknowledged_atlte,
        filtermitigated_atgt=filtermitigated_atgt,
        filtermitigated_atgte=filtermitigated_atgte,
        filtermitigated_atlt=filtermitigated_atlt,
        filtermitigated_atlte=filtermitigated_atlte,
        filterresolved_atgt=filterresolved_atgt,
        filterresolved_atgte=filterresolved_atgte,
        filterresolved_atlt=filterresolved_atlt,
        filterresolved_atlte=filterresolved_atlte,
        filterclosed_atgt=filterclosed_atgt,
        filterclosed_atgte=filterclosed_atgte,
        filterclosed_atlt=filterclosed_atlt,
        filterclosed_atlte=filterclosed_atlte,
        filterin_triage_atgt=filterin_triage_atgt,
        filterin_triage_atgte=filterin_triage_atgte,
        filterin_triage_atlt=filterin_triage_atlt,
        filterin_triage_atlte=filterin_triage_atlte,
        sort=sort,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterstatus: Unset | str = UNSET,
    filterprivate: Unset | str = UNSET,
    filteruser_id: Unset | int = UNSET,
    filterseverity: Unset | str = UNSET,
    filterseverity_id: Unset | str = UNSET,
    filterlabels: Unset | str = UNSET,
    filtertypes: Unset | str = UNSET,
    filtertype_ids: Unset | str = UNSET,
    filterenvironments: Unset | str = UNSET,
    filterenvironment_ids: Unset | str = UNSET,
    filterfunctionalities: Unset | str = UNSET,
    filterfunctionality_ids: Unset | str = UNSET,
    filterfunctionality_names: Unset | str = UNSET,
    filterservices: Unset | str = UNSET,
    filterservice_ids: Unset | str = UNSET,
    filterservice_names: Unset | str = UNSET,
    filterteams: Unset | str = UNSET,
    filterteam_ids: Unset | str = UNSET,
    filterteam_names: Unset | str = UNSET,
    filtercause: Unset | str = UNSET,
    filtercause_ids: Unset | str = UNSET,
    filtercustom_field_selected_option_ids: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterupdated_atgt: Unset | str = UNSET,
    filterupdated_atgte: Unset | str = UNSET,
    filterupdated_atlt: Unset | str = UNSET,
    filterupdated_atlte: Unset | str = UNSET,
    filterstarted_atgt: Unset | str = UNSET,
    filterstarted_atgte: Unset | str = UNSET,
    filterstarted_atlt: Unset | str = UNSET,
    filterstarted_atlte: Unset | str = UNSET,
    filterdetected_atgt: Unset | str = UNSET,
    filterdetected_atgte: Unset | str = UNSET,
    filterdetected_atlt: Unset | str = UNSET,
    filterdetected_atlte: Unset | str = UNSET,
    filteracknowledged_atgt: Unset | str = UNSET,
    filteracknowledged_atgte: Unset | str = UNSET,
    filteracknowledged_atlt: Unset | str = UNSET,
    filteracknowledged_atlte: Unset | str = UNSET,
    filtermitigated_atgt: Unset | str = UNSET,
    filtermitigated_atgte: Unset | str = UNSET,
    filtermitigated_atlt: Unset | str = UNSET,
    filtermitigated_atlte: Unset | str = UNSET,
    filterresolved_atgt: Unset | str = UNSET,
    filterresolved_atgte: Unset | str = UNSET,
    filterresolved_atlt: Unset | str = UNSET,
    filterresolved_atlte: Unset | str = UNSET,
    filterclosed_atgt: Unset | str = UNSET,
    filterclosed_atgte: Unset | str = UNSET,
    filterclosed_atlt: Unset | str = UNSET,
    filterclosed_atlte: Unset | str = UNSET,
    filterin_triage_atgt: Unset | str = UNSET,
    filterin_triage_atgte: Unset | str = UNSET,
    filterin_triage_atlt: Unset | str = UNSET,
    filterin_triage_atlte: Unset | str = UNSET,
    sort: Unset | ListIncidentsSort = UNSET,
    include: Unset | ListIncidentsInclude = UNSET,
) -> IncidentList | None:
    """List incidents

     List incidents

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterstatus (Union[Unset, str]):
        filterprivate (Union[Unset, str]):
        filteruser_id (Union[Unset, int]):
        filterseverity (Union[Unset, str]):
        filterseverity_id (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filtertypes (Union[Unset, str]):
        filtertype_ids (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filterenvironment_ids (Union[Unset, str]):
        filterfunctionalities (Union[Unset, str]):
        filterfunctionality_ids (Union[Unset, str]):
        filterfunctionality_names (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterservice_ids (Union[Unset, str]):
        filterservice_names (Union[Unset, str]):
        filterteams (Union[Unset, str]):
        filterteam_ids (Union[Unset, str]):
        filterteam_names (Union[Unset, str]):
        filtercause (Union[Unset, str]):
        filtercause_ids (Union[Unset, str]):
        filtercustom_field_selected_option_ids (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterupdated_atgt (Union[Unset, str]):
        filterupdated_atgte (Union[Unset, str]):
        filterupdated_atlt (Union[Unset, str]):
        filterupdated_atlte (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterdetected_atgt (Union[Unset, str]):
        filterdetected_atgte (Union[Unset, str]):
        filterdetected_atlt (Union[Unset, str]):
        filterdetected_atlte (Union[Unset, str]):
        filteracknowledged_atgt (Union[Unset, str]):
        filteracknowledged_atgte (Union[Unset, str]):
        filteracknowledged_atlt (Union[Unset, str]):
        filteracknowledged_atlte (Union[Unset, str]):
        filtermitigated_atgt (Union[Unset, str]):
        filtermitigated_atgte (Union[Unset, str]):
        filtermitigated_atlt (Union[Unset, str]):
        filtermitigated_atlte (Union[Unset, str]):
        filterresolved_atgt (Union[Unset, str]):
        filterresolved_atgte (Union[Unset, str]):
        filterresolved_atlt (Union[Unset, str]):
        filterresolved_atlte (Union[Unset, str]):
        filterclosed_atgt (Union[Unset, str]):
        filterclosed_atgte (Union[Unset, str]):
        filterclosed_atlt (Union[Unset, str]):
        filterclosed_atlte (Union[Unset, str]):
        filterin_triage_atgt (Union[Unset, str]):
        filterin_triage_atgte (Union[Unset, str]):
        filterin_triage_atlt (Union[Unset, str]):
        filterin_triage_atlte (Union[Unset, str]):
        sort (Union[Unset, ListIncidentsSort]):
        include (Union[Unset, ListIncidentsInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentList
    """

    return sync_detailed(
        client=client,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterkind=filterkind,
        filterstatus=filterstatus,
        filterprivate=filterprivate,
        filteruser_id=filteruser_id,
        filterseverity=filterseverity,
        filterseverity_id=filterseverity_id,
        filterlabels=filterlabels,
        filtertypes=filtertypes,
        filtertype_ids=filtertype_ids,
        filterenvironments=filterenvironments,
        filterenvironment_ids=filterenvironment_ids,
        filterfunctionalities=filterfunctionalities,
        filterfunctionality_ids=filterfunctionality_ids,
        filterfunctionality_names=filterfunctionality_names,
        filterservices=filterservices,
        filterservice_ids=filterservice_ids,
        filterservice_names=filterservice_names,
        filterteams=filterteams,
        filterteam_ids=filterteam_ids,
        filterteam_names=filterteam_names,
        filtercause=filtercause,
        filtercause_ids=filtercause_ids,
        filtercustom_field_selected_option_ids=filtercustom_field_selected_option_ids,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterupdated_atgt=filterupdated_atgt,
        filterupdated_atgte=filterupdated_atgte,
        filterupdated_atlt=filterupdated_atlt,
        filterupdated_atlte=filterupdated_atlte,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterdetected_atgt=filterdetected_atgt,
        filterdetected_atgte=filterdetected_atgte,
        filterdetected_atlt=filterdetected_atlt,
        filterdetected_atlte=filterdetected_atlte,
        filteracknowledged_atgt=filteracknowledged_atgt,
        filteracknowledged_atgte=filteracknowledged_atgte,
        filteracknowledged_atlt=filteracknowledged_atlt,
        filteracknowledged_atlte=filteracknowledged_atlte,
        filtermitigated_atgt=filtermitigated_atgt,
        filtermitigated_atgte=filtermitigated_atgte,
        filtermitigated_atlt=filtermitigated_atlt,
        filtermitigated_atlte=filtermitigated_atlte,
        filterresolved_atgt=filterresolved_atgt,
        filterresolved_atgte=filterresolved_atgte,
        filterresolved_atlt=filterresolved_atlt,
        filterresolved_atlte=filterresolved_atlte,
        filterclosed_atgt=filterclosed_atgt,
        filterclosed_atgte=filterclosed_atgte,
        filterclosed_atlt=filterclosed_atlt,
        filterclosed_atlte=filterclosed_atlte,
        filterin_triage_atgt=filterin_triage_atgt,
        filterin_triage_atgte=filterin_triage_atgte,
        filterin_triage_atlt=filterin_triage_atlt,
        filterin_triage_atlte=filterin_triage_atlte,
        sort=sort,
        include=include,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterstatus: Unset | str = UNSET,
    filterprivate: Unset | str = UNSET,
    filteruser_id: Unset | int = UNSET,
    filterseverity: Unset | str = UNSET,
    filterseverity_id: Unset | str = UNSET,
    filterlabels: Unset | str = UNSET,
    filtertypes: Unset | str = UNSET,
    filtertype_ids: Unset | str = UNSET,
    filterenvironments: Unset | str = UNSET,
    filterenvironment_ids: Unset | str = UNSET,
    filterfunctionalities: Unset | str = UNSET,
    filterfunctionality_ids: Unset | str = UNSET,
    filterfunctionality_names: Unset | str = UNSET,
    filterservices: Unset | str = UNSET,
    filterservice_ids: Unset | str = UNSET,
    filterservice_names: Unset | str = UNSET,
    filterteams: Unset | str = UNSET,
    filterteam_ids: Unset | str = UNSET,
    filterteam_names: Unset | str = UNSET,
    filtercause: Unset | str = UNSET,
    filtercause_ids: Unset | str = UNSET,
    filtercustom_field_selected_option_ids: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterupdated_atgt: Unset | str = UNSET,
    filterupdated_atgte: Unset | str = UNSET,
    filterupdated_atlt: Unset | str = UNSET,
    filterupdated_atlte: Unset | str = UNSET,
    filterstarted_atgt: Unset | str = UNSET,
    filterstarted_atgte: Unset | str = UNSET,
    filterstarted_atlt: Unset | str = UNSET,
    filterstarted_atlte: Unset | str = UNSET,
    filterdetected_atgt: Unset | str = UNSET,
    filterdetected_atgte: Unset | str = UNSET,
    filterdetected_atlt: Unset | str = UNSET,
    filterdetected_atlte: Unset | str = UNSET,
    filteracknowledged_atgt: Unset | str = UNSET,
    filteracknowledged_atgte: Unset | str = UNSET,
    filteracknowledged_atlt: Unset | str = UNSET,
    filteracknowledged_atlte: Unset | str = UNSET,
    filtermitigated_atgt: Unset | str = UNSET,
    filtermitigated_atgte: Unset | str = UNSET,
    filtermitigated_atlt: Unset | str = UNSET,
    filtermitigated_atlte: Unset | str = UNSET,
    filterresolved_atgt: Unset | str = UNSET,
    filterresolved_atgte: Unset | str = UNSET,
    filterresolved_atlt: Unset | str = UNSET,
    filterresolved_atlte: Unset | str = UNSET,
    filterclosed_atgt: Unset | str = UNSET,
    filterclosed_atgte: Unset | str = UNSET,
    filterclosed_atlt: Unset | str = UNSET,
    filterclosed_atlte: Unset | str = UNSET,
    filterin_triage_atgt: Unset | str = UNSET,
    filterin_triage_atgte: Unset | str = UNSET,
    filterin_triage_atlt: Unset | str = UNSET,
    filterin_triage_atlte: Unset | str = UNSET,
    sort: Unset | ListIncidentsSort = UNSET,
    include: Unset | ListIncidentsInclude = UNSET,
) -> Response[IncidentList]:
    """List incidents

     List incidents

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterstatus (Union[Unset, str]):
        filterprivate (Union[Unset, str]):
        filteruser_id (Union[Unset, int]):
        filterseverity (Union[Unset, str]):
        filterseverity_id (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filtertypes (Union[Unset, str]):
        filtertype_ids (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filterenvironment_ids (Union[Unset, str]):
        filterfunctionalities (Union[Unset, str]):
        filterfunctionality_ids (Union[Unset, str]):
        filterfunctionality_names (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterservice_ids (Union[Unset, str]):
        filterservice_names (Union[Unset, str]):
        filterteams (Union[Unset, str]):
        filterteam_ids (Union[Unset, str]):
        filterteam_names (Union[Unset, str]):
        filtercause (Union[Unset, str]):
        filtercause_ids (Union[Unset, str]):
        filtercustom_field_selected_option_ids (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterupdated_atgt (Union[Unset, str]):
        filterupdated_atgte (Union[Unset, str]):
        filterupdated_atlt (Union[Unset, str]):
        filterupdated_atlte (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterdetected_atgt (Union[Unset, str]):
        filterdetected_atgte (Union[Unset, str]):
        filterdetected_atlt (Union[Unset, str]):
        filterdetected_atlte (Union[Unset, str]):
        filteracknowledged_atgt (Union[Unset, str]):
        filteracknowledged_atgte (Union[Unset, str]):
        filteracknowledged_atlt (Union[Unset, str]):
        filteracknowledged_atlte (Union[Unset, str]):
        filtermitigated_atgt (Union[Unset, str]):
        filtermitigated_atgte (Union[Unset, str]):
        filtermitigated_atlt (Union[Unset, str]):
        filtermitigated_atlte (Union[Unset, str]):
        filterresolved_atgt (Union[Unset, str]):
        filterresolved_atgte (Union[Unset, str]):
        filterresolved_atlt (Union[Unset, str]):
        filterresolved_atlte (Union[Unset, str]):
        filterclosed_atgt (Union[Unset, str]):
        filterclosed_atgte (Union[Unset, str]):
        filterclosed_atlt (Union[Unset, str]):
        filterclosed_atlte (Union[Unset, str]):
        filterin_triage_atgt (Union[Unset, str]):
        filterin_triage_atgte (Union[Unset, str]):
        filterin_triage_atlt (Union[Unset, str]):
        filterin_triage_atlte (Union[Unset, str]):
        sort (Union[Unset, ListIncidentsSort]):
        include (Union[Unset, ListIncidentsInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentList]
    """

    kwargs = _get_kwargs(
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filterkind=filterkind,
        filterstatus=filterstatus,
        filterprivate=filterprivate,
        filteruser_id=filteruser_id,
        filterseverity=filterseverity,
        filterseverity_id=filterseverity_id,
        filterlabels=filterlabels,
        filtertypes=filtertypes,
        filtertype_ids=filtertype_ids,
        filterenvironments=filterenvironments,
        filterenvironment_ids=filterenvironment_ids,
        filterfunctionalities=filterfunctionalities,
        filterfunctionality_ids=filterfunctionality_ids,
        filterfunctionality_names=filterfunctionality_names,
        filterservices=filterservices,
        filterservice_ids=filterservice_ids,
        filterservice_names=filterservice_names,
        filterteams=filterteams,
        filterteam_ids=filterteam_ids,
        filterteam_names=filterteam_names,
        filtercause=filtercause,
        filtercause_ids=filtercause_ids,
        filtercustom_field_selected_option_ids=filtercustom_field_selected_option_ids,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filterupdated_atgt=filterupdated_atgt,
        filterupdated_atgte=filterupdated_atgte,
        filterupdated_atlt=filterupdated_atlt,
        filterupdated_atlte=filterupdated_atlte,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterdetected_atgt=filterdetected_atgt,
        filterdetected_atgte=filterdetected_atgte,
        filterdetected_atlt=filterdetected_atlt,
        filterdetected_atlte=filterdetected_atlte,
        filteracknowledged_atgt=filteracknowledged_atgt,
        filteracknowledged_atgte=filteracknowledged_atgte,
        filteracknowledged_atlt=filteracknowledged_atlt,
        filteracknowledged_atlte=filteracknowledged_atlte,
        filtermitigated_atgt=filtermitigated_atgt,
        filtermitigated_atgte=filtermitigated_atgte,
        filtermitigated_atlt=filtermitigated_atlt,
        filtermitigated_atlte=filtermitigated_atlte,
        filterresolved_atgt=filterresolved_atgt,
        filterresolved_atgte=filterresolved_atgte,
        filterresolved_atlt=filterresolved_atlt,
        filterresolved_atlte=filterresolved_atlte,
        filterclosed_atgt=filterclosed_atgt,
        filterclosed_atgte=filterclosed_atgte,
        filterclosed_atlt=filterclosed_atlt,
        filterclosed_atlte=filterclosed_atlte,
        filterin_triage_atgt=filterin_triage_atgt,
        filterin_triage_atgte=filterin_triage_atgte,
        filterin_triage_atlt=filterin_triage_atlt,
        filterin_triage_atlte=filterin_triage_atlte,
        sort=sort,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterstatus: Unset | str = UNSET,
    filterprivate: Unset | str = UNSET,
    filteruser_id: Unset | int = UNSET,
    filterseverity: Unset | str = UNSET,
    filterseverity_id: Unset | str = UNSET,
    filterlabels: Unset | str = UNSET,
    filtertypes: Unset | str = UNSET,
    filtertype_ids: Unset | str = UNSET,
    filterenvironments: Unset | str = UNSET,
    filterenvironment_ids: Unset | str = UNSET,
    filterfunctionalities: Unset | str = UNSET,
    filterfunctionality_ids: Unset | str = UNSET,
    filterfunctionality_names: Unset | str = UNSET,
    filterservices: Unset | str = UNSET,
    filterservice_ids: Unset | str = UNSET,
    filterservice_names: Unset | str = UNSET,
    filterteams: Unset | str = UNSET,
    filterteam_ids: Unset | str = UNSET,
    filterteam_names: Unset | str = UNSET,
    filtercause: Unset | str = UNSET,
    filtercause_ids: Unset | str = UNSET,
    filtercustom_field_selected_option_ids: Unset | str = UNSET,
    filtercreated_atgt: Unset | str = UNSET,
    filtercreated_atgte: Unset | str = UNSET,
    filtercreated_atlt: Unset | str = UNSET,
    filtercreated_atlte: Unset | str = UNSET,
    filterupdated_atgt: Unset | str = UNSET,
    filterupdated_atgte: Unset | str = UNSET,
    filterupdated_atlt: Unset | str = UNSET,
    filterupdated_atlte: Unset | str = UNSET,
    filterstarted_atgt: Unset | str = UNSET,
    filterstarted_atgte: Unset | str = UNSET,
    filterstarted_atlt: Unset | str = UNSET,
    filterstarted_atlte: Unset | str = UNSET,
    filterdetected_atgt: Unset | str = UNSET,
    filterdetected_atgte: Unset | str = UNSET,
    filterdetected_atlt: Unset | str = UNSET,
    filterdetected_atlte: Unset | str = UNSET,
    filteracknowledged_atgt: Unset | str = UNSET,
    filteracknowledged_atgte: Unset | str = UNSET,
    filteracknowledged_atlt: Unset | str = UNSET,
    filteracknowledged_atlte: Unset | str = UNSET,
    filtermitigated_atgt: Unset | str = UNSET,
    filtermitigated_atgte: Unset | str = UNSET,
    filtermitigated_atlt: Unset | str = UNSET,
    filtermitigated_atlte: Unset | str = UNSET,
    filterresolved_atgt: Unset | str = UNSET,
    filterresolved_atgte: Unset | str = UNSET,
    filterresolved_atlt: Unset | str = UNSET,
    filterresolved_atlte: Unset | str = UNSET,
    filterclosed_atgt: Unset | str = UNSET,
    filterclosed_atgte: Unset | str = UNSET,
    filterclosed_atlt: Unset | str = UNSET,
    filterclosed_atlte: Unset | str = UNSET,
    filterin_triage_atgt: Unset | str = UNSET,
    filterin_triage_atgte: Unset | str = UNSET,
    filterin_triage_atlt: Unset | str = UNSET,
    filterin_triage_atlte: Unset | str = UNSET,
    sort: Unset | ListIncidentsSort = UNSET,
    include: Unset | ListIncidentsInclude = UNSET,
) -> IncidentList | None:
    """List incidents

     List incidents

    Args:
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterstatus (Union[Unset, str]):
        filterprivate (Union[Unset, str]):
        filteruser_id (Union[Unset, int]):
        filterseverity (Union[Unset, str]):
        filterseverity_id (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filtertypes (Union[Unset, str]):
        filtertype_ids (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filterenvironment_ids (Union[Unset, str]):
        filterfunctionalities (Union[Unset, str]):
        filterfunctionality_ids (Union[Unset, str]):
        filterfunctionality_names (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterservice_ids (Union[Unset, str]):
        filterservice_names (Union[Unset, str]):
        filterteams (Union[Unset, str]):
        filterteam_ids (Union[Unset, str]):
        filterteam_names (Union[Unset, str]):
        filtercause (Union[Unset, str]):
        filtercause_ids (Union[Unset, str]):
        filtercustom_field_selected_option_ids (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filterupdated_atgt (Union[Unset, str]):
        filterupdated_atgte (Union[Unset, str]):
        filterupdated_atlt (Union[Unset, str]):
        filterupdated_atlte (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterdetected_atgt (Union[Unset, str]):
        filterdetected_atgte (Union[Unset, str]):
        filterdetected_atlt (Union[Unset, str]):
        filterdetected_atlte (Union[Unset, str]):
        filteracknowledged_atgt (Union[Unset, str]):
        filteracknowledged_atgte (Union[Unset, str]):
        filteracknowledged_atlt (Union[Unset, str]):
        filteracknowledged_atlte (Union[Unset, str]):
        filtermitigated_atgt (Union[Unset, str]):
        filtermitigated_atgte (Union[Unset, str]):
        filtermitigated_atlt (Union[Unset, str]):
        filtermitigated_atlte (Union[Unset, str]):
        filterresolved_atgt (Union[Unset, str]):
        filterresolved_atgte (Union[Unset, str]):
        filterresolved_atlt (Union[Unset, str]):
        filterresolved_atlte (Union[Unset, str]):
        filterclosed_atgt (Union[Unset, str]):
        filterclosed_atgte (Union[Unset, str]):
        filterclosed_atlt (Union[Unset, str]):
        filterclosed_atlte (Union[Unset, str]):
        filterin_triage_atgt (Union[Unset, str]):
        filterin_triage_atgte (Union[Unset, str]):
        filterin_triage_atlt (Union[Unset, str]):
        filterin_triage_atlte (Union[Unset, str]):
        sort (Union[Unset, ListIncidentsSort]):
        include (Union[Unset, ListIncidentsInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentList
    """

    return (
        await asyncio_detailed(
            client=client,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtersearch=filtersearch,
            filterkind=filterkind,
            filterstatus=filterstatus,
            filterprivate=filterprivate,
            filteruser_id=filteruser_id,
            filterseverity=filterseverity,
            filterseverity_id=filterseverity_id,
            filterlabels=filterlabels,
            filtertypes=filtertypes,
            filtertype_ids=filtertype_ids,
            filterenvironments=filterenvironments,
            filterenvironment_ids=filterenvironment_ids,
            filterfunctionalities=filterfunctionalities,
            filterfunctionality_ids=filterfunctionality_ids,
            filterfunctionality_names=filterfunctionality_names,
            filterservices=filterservices,
            filterservice_ids=filterservice_ids,
            filterservice_names=filterservice_names,
            filterteams=filterteams,
            filterteam_ids=filterteam_ids,
            filterteam_names=filterteam_names,
            filtercause=filtercause,
            filtercause_ids=filtercause_ids,
            filtercustom_field_selected_option_ids=filtercustom_field_selected_option_ids,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filterupdated_atgt=filterupdated_atgt,
            filterupdated_atgte=filterupdated_atgte,
            filterupdated_atlt=filterupdated_atlt,
            filterupdated_atlte=filterupdated_atlte,
            filterstarted_atgt=filterstarted_atgt,
            filterstarted_atgte=filterstarted_atgte,
            filterstarted_atlt=filterstarted_atlt,
            filterstarted_atlte=filterstarted_atlte,
            filterdetected_atgt=filterdetected_atgt,
            filterdetected_atgte=filterdetected_atgte,
            filterdetected_atlt=filterdetected_atlt,
            filterdetected_atlte=filterdetected_atlte,
            filteracknowledged_atgt=filteracknowledged_atgt,
            filteracknowledged_atgte=filteracknowledged_atgte,
            filteracknowledged_atlt=filteracknowledged_atlt,
            filteracknowledged_atlte=filteracknowledged_atlte,
            filtermitigated_atgt=filtermitigated_atgt,
            filtermitigated_atgte=filtermitigated_atgte,
            filtermitigated_atlt=filtermitigated_atlt,
            filtermitigated_atlte=filtermitigated_atlte,
            filterresolved_atgt=filterresolved_atgt,
            filterresolved_atgte=filterresolved_atgte,
            filterresolved_atlt=filterresolved_atlt,
            filterresolved_atlte=filterresolved_atlte,
            filterclosed_atgt=filterclosed_atgt,
            filterclosed_atgte=filterclosed_atgte,
            filterclosed_atlt=filterclosed_atlt,
            filterclosed_atlte=filterclosed_atlte,
            filterin_triage_atgt=filterin_triage_atgt,
            filterin_triage_atgte=filterin_triage_atgte,
            filterin_triage_atlt=filterin_triage_atlt,
            filterin_triage_atlte=filterin_triage_atlte,
            sort=sort,
            include=include,
        )
    ).parsed
