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
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterprivate: str | Unset = UNSET,
    filteruser_id: int | Unset = UNSET,
    filterseverity: str | Unset = UNSET,
    filterseverity_id: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filtertypes: str | Unset = UNSET,
    filtertype_ids: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterenvironment_ids: str | Unset = UNSET,
    filterfunctionalities: str | Unset = UNSET,
    filterfunctionality_ids: str | Unset = UNSET,
    filterfunctionality_names: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filterservice_names: str | Unset = UNSET,
    filterteams: str | Unset = UNSET,
    filterteam_ids: str | Unset = UNSET,
    filterteam_names: str | Unset = UNSET,
    filtercause: str | Unset = UNSET,
    filtercause_ids: str | Unset = UNSET,
    filtercustom_field_selected_option_ids: str | Unset = UNSET,
    filterslack_channel_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterupdated_atgt: str | Unset = UNSET,
    filterupdated_atgte: str | Unset = UNSET,
    filterupdated_atlt: str | Unset = UNSET,
    filterupdated_atlte: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterdetected_atgt: str | Unset = UNSET,
    filterdetected_atgte: str | Unset = UNSET,
    filterdetected_atlt: str | Unset = UNSET,
    filterdetected_atlte: str | Unset = UNSET,
    filteracknowledged_atgt: str | Unset = UNSET,
    filteracknowledged_atgte: str | Unset = UNSET,
    filteracknowledged_atlt: str | Unset = UNSET,
    filteracknowledged_atlte: str | Unset = UNSET,
    filtermitigated_atgt: str | Unset = UNSET,
    filtermitigated_atgte: str | Unset = UNSET,
    filtermitigated_atlt: str | Unset = UNSET,
    filtermitigated_atlte: str | Unset = UNSET,
    filterresolved_atgt: str | Unset = UNSET,
    filterresolved_atgte: str | Unset = UNSET,
    filterresolved_atlt: str | Unset = UNSET,
    filterresolved_atlte: str | Unset = UNSET,
    filterclosed_atgt: str | Unset = UNSET,
    filterclosed_atgte: str | Unset = UNSET,
    filterclosed_atlt: str | Unset = UNSET,
    filterclosed_atlte: str | Unset = UNSET,
    filterin_triage_atgt: str | Unset = UNSET,
    filterin_triage_atgte: str | Unset = UNSET,
    filterin_triage_atlt: str | Unset = UNSET,
    filterin_triage_atlte: str | Unset = UNSET,
    sort: ListIncidentsSort | Unset = UNSET,
    include: ListIncidentsInclude | Unset = UNSET,
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

    params["filter[slack_channel_id]"] = filterslack_channel_id

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

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_include: str | Unset = UNSET
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
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterprivate: str | Unset = UNSET,
    filteruser_id: int | Unset = UNSET,
    filterseverity: str | Unset = UNSET,
    filterseverity_id: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filtertypes: str | Unset = UNSET,
    filtertype_ids: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterenvironment_ids: str | Unset = UNSET,
    filterfunctionalities: str | Unset = UNSET,
    filterfunctionality_ids: str | Unset = UNSET,
    filterfunctionality_names: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filterservice_names: str | Unset = UNSET,
    filterteams: str | Unset = UNSET,
    filterteam_ids: str | Unset = UNSET,
    filterteam_names: str | Unset = UNSET,
    filtercause: str | Unset = UNSET,
    filtercause_ids: str | Unset = UNSET,
    filtercustom_field_selected_option_ids: str | Unset = UNSET,
    filterslack_channel_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterupdated_atgt: str | Unset = UNSET,
    filterupdated_atgte: str | Unset = UNSET,
    filterupdated_atlt: str | Unset = UNSET,
    filterupdated_atlte: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterdetected_atgt: str | Unset = UNSET,
    filterdetected_atgte: str | Unset = UNSET,
    filterdetected_atlt: str | Unset = UNSET,
    filterdetected_atlte: str | Unset = UNSET,
    filteracknowledged_atgt: str | Unset = UNSET,
    filteracknowledged_atgte: str | Unset = UNSET,
    filteracknowledged_atlt: str | Unset = UNSET,
    filteracknowledged_atlte: str | Unset = UNSET,
    filtermitigated_atgt: str | Unset = UNSET,
    filtermitigated_atgte: str | Unset = UNSET,
    filtermitigated_atlt: str | Unset = UNSET,
    filtermitigated_atlte: str | Unset = UNSET,
    filterresolved_atgt: str | Unset = UNSET,
    filterresolved_atgte: str | Unset = UNSET,
    filterresolved_atlt: str | Unset = UNSET,
    filterresolved_atlte: str | Unset = UNSET,
    filterclosed_atgt: str | Unset = UNSET,
    filterclosed_atgte: str | Unset = UNSET,
    filterclosed_atlt: str | Unset = UNSET,
    filterclosed_atlte: str | Unset = UNSET,
    filterin_triage_atgt: str | Unset = UNSET,
    filterin_triage_atgte: str | Unset = UNSET,
    filterin_triage_atlt: str | Unset = UNSET,
    filterin_triage_atlte: str | Unset = UNSET,
    sort: ListIncidentsSort | Unset = UNSET,
    include: ListIncidentsInclude | Unset = UNSET,
) -> Response[IncidentList]:
    """List incidents

     List incidents

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterkind (str | Unset):
        filterstatus (str | Unset):
        filterprivate (str | Unset):
        filteruser_id (int | Unset):
        filterseverity (str | Unset):
        filterseverity_id (str | Unset):
        filterlabels (str | Unset):
        filtertypes (str | Unset):
        filtertype_ids (str | Unset):
        filterenvironments (str | Unset):
        filterenvironment_ids (str | Unset):
        filterfunctionalities (str | Unset):
        filterfunctionality_ids (str | Unset):
        filterfunctionality_names (str | Unset):
        filterservices (str | Unset):
        filterservice_ids (str | Unset):
        filterservice_names (str | Unset):
        filterteams (str | Unset):
        filterteam_ids (str | Unset):
        filterteam_names (str | Unset):
        filtercause (str | Unset):
        filtercause_ids (str | Unset):
        filtercustom_field_selected_option_ids (str | Unset):
        filterslack_channel_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterupdated_atgt (str | Unset):
        filterupdated_atgte (str | Unset):
        filterupdated_atlt (str | Unset):
        filterupdated_atlte (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterdetected_atgt (str | Unset):
        filterdetected_atgte (str | Unset):
        filterdetected_atlt (str | Unset):
        filterdetected_atlte (str | Unset):
        filteracknowledged_atgt (str | Unset):
        filteracknowledged_atgte (str | Unset):
        filteracknowledged_atlt (str | Unset):
        filteracknowledged_atlte (str | Unset):
        filtermitigated_atgt (str | Unset):
        filtermitigated_atgte (str | Unset):
        filtermitigated_atlt (str | Unset):
        filtermitigated_atlte (str | Unset):
        filterresolved_atgt (str | Unset):
        filterresolved_atgte (str | Unset):
        filterresolved_atlt (str | Unset):
        filterresolved_atlte (str | Unset):
        filterclosed_atgt (str | Unset):
        filterclosed_atgte (str | Unset):
        filterclosed_atlt (str | Unset):
        filterclosed_atlte (str | Unset):
        filterin_triage_atgt (str | Unset):
        filterin_triage_atgte (str | Unset):
        filterin_triage_atlt (str | Unset):
        filterin_triage_atlte (str | Unset):
        sort (ListIncidentsSort | Unset):
        include (ListIncidentsInclude | Unset):

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
        filterslack_channel_id=filterslack_channel_id,
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
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterprivate: str | Unset = UNSET,
    filteruser_id: int | Unset = UNSET,
    filterseverity: str | Unset = UNSET,
    filterseverity_id: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filtertypes: str | Unset = UNSET,
    filtertype_ids: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterenvironment_ids: str | Unset = UNSET,
    filterfunctionalities: str | Unset = UNSET,
    filterfunctionality_ids: str | Unset = UNSET,
    filterfunctionality_names: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filterservice_names: str | Unset = UNSET,
    filterteams: str | Unset = UNSET,
    filterteam_ids: str | Unset = UNSET,
    filterteam_names: str | Unset = UNSET,
    filtercause: str | Unset = UNSET,
    filtercause_ids: str | Unset = UNSET,
    filtercustom_field_selected_option_ids: str | Unset = UNSET,
    filterslack_channel_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterupdated_atgt: str | Unset = UNSET,
    filterupdated_atgte: str | Unset = UNSET,
    filterupdated_atlt: str | Unset = UNSET,
    filterupdated_atlte: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterdetected_atgt: str | Unset = UNSET,
    filterdetected_atgte: str | Unset = UNSET,
    filterdetected_atlt: str | Unset = UNSET,
    filterdetected_atlte: str | Unset = UNSET,
    filteracknowledged_atgt: str | Unset = UNSET,
    filteracknowledged_atgte: str | Unset = UNSET,
    filteracknowledged_atlt: str | Unset = UNSET,
    filteracknowledged_atlte: str | Unset = UNSET,
    filtermitigated_atgt: str | Unset = UNSET,
    filtermitigated_atgte: str | Unset = UNSET,
    filtermitigated_atlt: str | Unset = UNSET,
    filtermitigated_atlte: str | Unset = UNSET,
    filterresolved_atgt: str | Unset = UNSET,
    filterresolved_atgte: str | Unset = UNSET,
    filterresolved_atlt: str | Unset = UNSET,
    filterresolved_atlte: str | Unset = UNSET,
    filterclosed_atgt: str | Unset = UNSET,
    filterclosed_atgte: str | Unset = UNSET,
    filterclosed_atlt: str | Unset = UNSET,
    filterclosed_atlte: str | Unset = UNSET,
    filterin_triage_atgt: str | Unset = UNSET,
    filterin_triage_atgte: str | Unset = UNSET,
    filterin_triage_atlt: str | Unset = UNSET,
    filterin_triage_atlte: str | Unset = UNSET,
    sort: ListIncidentsSort | Unset = UNSET,
    include: ListIncidentsInclude | Unset = UNSET,
) -> IncidentList | None:
    """List incidents

     List incidents

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterkind (str | Unset):
        filterstatus (str | Unset):
        filterprivate (str | Unset):
        filteruser_id (int | Unset):
        filterseverity (str | Unset):
        filterseverity_id (str | Unset):
        filterlabels (str | Unset):
        filtertypes (str | Unset):
        filtertype_ids (str | Unset):
        filterenvironments (str | Unset):
        filterenvironment_ids (str | Unset):
        filterfunctionalities (str | Unset):
        filterfunctionality_ids (str | Unset):
        filterfunctionality_names (str | Unset):
        filterservices (str | Unset):
        filterservice_ids (str | Unset):
        filterservice_names (str | Unset):
        filterteams (str | Unset):
        filterteam_ids (str | Unset):
        filterteam_names (str | Unset):
        filtercause (str | Unset):
        filtercause_ids (str | Unset):
        filtercustom_field_selected_option_ids (str | Unset):
        filterslack_channel_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterupdated_atgt (str | Unset):
        filterupdated_atgte (str | Unset):
        filterupdated_atlt (str | Unset):
        filterupdated_atlte (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterdetected_atgt (str | Unset):
        filterdetected_atgte (str | Unset):
        filterdetected_atlt (str | Unset):
        filterdetected_atlte (str | Unset):
        filteracknowledged_atgt (str | Unset):
        filteracknowledged_atgte (str | Unset):
        filteracknowledged_atlt (str | Unset):
        filteracknowledged_atlte (str | Unset):
        filtermitigated_atgt (str | Unset):
        filtermitigated_atgte (str | Unset):
        filtermitigated_atlt (str | Unset):
        filtermitigated_atlte (str | Unset):
        filterresolved_atgt (str | Unset):
        filterresolved_atgte (str | Unset):
        filterresolved_atlt (str | Unset):
        filterresolved_atlte (str | Unset):
        filterclosed_atgt (str | Unset):
        filterclosed_atgte (str | Unset):
        filterclosed_atlt (str | Unset):
        filterclosed_atlte (str | Unset):
        filterin_triage_atgt (str | Unset):
        filterin_triage_atgte (str | Unset):
        filterin_triage_atlt (str | Unset):
        filterin_triage_atlte (str | Unset):
        sort (ListIncidentsSort | Unset):
        include (ListIncidentsInclude | Unset):

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
        filterslack_channel_id=filterslack_channel_id,
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
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterprivate: str | Unset = UNSET,
    filteruser_id: int | Unset = UNSET,
    filterseverity: str | Unset = UNSET,
    filterseverity_id: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filtertypes: str | Unset = UNSET,
    filtertype_ids: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterenvironment_ids: str | Unset = UNSET,
    filterfunctionalities: str | Unset = UNSET,
    filterfunctionality_ids: str | Unset = UNSET,
    filterfunctionality_names: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filterservice_names: str | Unset = UNSET,
    filterteams: str | Unset = UNSET,
    filterteam_ids: str | Unset = UNSET,
    filterteam_names: str | Unset = UNSET,
    filtercause: str | Unset = UNSET,
    filtercause_ids: str | Unset = UNSET,
    filtercustom_field_selected_option_ids: str | Unset = UNSET,
    filterslack_channel_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterupdated_atgt: str | Unset = UNSET,
    filterupdated_atgte: str | Unset = UNSET,
    filterupdated_atlt: str | Unset = UNSET,
    filterupdated_atlte: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterdetected_atgt: str | Unset = UNSET,
    filterdetected_atgte: str | Unset = UNSET,
    filterdetected_atlt: str | Unset = UNSET,
    filterdetected_atlte: str | Unset = UNSET,
    filteracknowledged_atgt: str | Unset = UNSET,
    filteracknowledged_atgte: str | Unset = UNSET,
    filteracknowledged_atlt: str | Unset = UNSET,
    filteracknowledged_atlte: str | Unset = UNSET,
    filtermitigated_atgt: str | Unset = UNSET,
    filtermitigated_atgte: str | Unset = UNSET,
    filtermitigated_atlt: str | Unset = UNSET,
    filtermitigated_atlte: str | Unset = UNSET,
    filterresolved_atgt: str | Unset = UNSET,
    filterresolved_atgte: str | Unset = UNSET,
    filterresolved_atlt: str | Unset = UNSET,
    filterresolved_atlte: str | Unset = UNSET,
    filterclosed_atgt: str | Unset = UNSET,
    filterclosed_atgte: str | Unset = UNSET,
    filterclosed_atlt: str | Unset = UNSET,
    filterclosed_atlte: str | Unset = UNSET,
    filterin_triage_atgt: str | Unset = UNSET,
    filterin_triage_atgte: str | Unset = UNSET,
    filterin_triage_atlt: str | Unset = UNSET,
    filterin_triage_atlte: str | Unset = UNSET,
    sort: ListIncidentsSort | Unset = UNSET,
    include: ListIncidentsInclude | Unset = UNSET,
) -> Response[IncidentList]:
    """List incidents

     List incidents

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterkind (str | Unset):
        filterstatus (str | Unset):
        filterprivate (str | Unset):
        filteruser_id (int | Unset):
        filterseverity (str | Unset):
        filterseverity_id (str | Unset):
        filterlabels (str | Unset):
        filtertypes (str | Unset):
        filtertype_ids (str | Unset):
        filterenvironments (str | Unset):
        filterenvironment_ids (str | Unset):
        filterfunctionalities (str | Unset):
        filterfunctionality_ids (str | Unset):
        filterfunctionality_names (str | Unset):
        filterservices (str | Unset):
        filterservice_ids (str | Unset):
        filterservice_names (str | Unset):
        filterteams (str | Unset):
        filterteam_ids (str | Unset):
        filterteam_names (str | Unset):
        filtercause (str | Unset):
        filtercause_ids (str | Unset):
        filtercustom_field_selected_option_ids (str | Unset):
        filterslack_channel_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterupdated_atgt (str | Unset):
        filterupdated_atgte (str | Unset):
        filterupdated_atlt (str | Unset):
        filterupdated_atlte (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterdetected_atgt (str | Unset):
        filterdetected_atgte (str | Unset):
        filterdetected_atlt (str | Unset):
        filterdetected_atlte (str | Unset):
        filteracknowledged_atgt (str | Unset):
        filteracknowledged_atgte (str | Unset):
        filteracknowledged_atlt (str | Unset):
        filteracknowledged_atlte (str | Unset):
        filtermitigated_atgt (str | Unset):
        filtermitigated_atgte (str | Unset):
        filtermitigated_atlt (str | Unset):
        filtermitigated_atlte (str | Unset):
        filterresolved_atgt (str | Unset):
        filterresolved_atgte (str | Unset):
        filterresolved_atlt (str | Unset):
        filterresolved_atlte (str | Unset):
        filterclosed_atgt (str | Unset):
        filterclosed_atgte (str | Unset):
        filterclosed_atlt (str | Unset):
        filterclosed_atlte (str | Unset):
        filterin_triage_atgt (str | Unset):
        filterin_triage_atgte (str | Unset):
        filterin_triage_atlt (str | Unset):
        filterin_triage_atlte (str | Unset):
        sort (ListIncidentsSort | Unset):
        include (ListIncidentsInclude | Unset):

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
        filterslack_channel_id=filterslack_channel_id,
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
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersearch: str | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filterstatus: str | Unset = UNSET,
    filterprivate: str | Unset = UNSET,
    filteruser_id: int | Unset = UNSET,
    filterseverity: str | Unset = UNSET,
    filterseverity_id: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filtertypes: str | Unset = UNSET,
    filtertype_ids: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterenvironment_ids: str | Unset = UNSET,
    filterfunctionalities: str | Unset = UNSET,
    filterfunctionality_ids: str | Unset = UNSET,
    filterfunctionality_names: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterservice_ids: str | Unset = UNSET,
    filterservice_names: str | Unset = UNSET,
    filterteams: str | Unset = UNSET,
    filterteam_ids: str | Unset = UNSET,
    filterteam_names: str | Unset = UNSET,
    filtercause: str | Unset = UNSET,
    filtercause_ids: str | Unset = UNSET,
    filtercustom_field_selected_option_ids: str | Unset = UNSET,
    filterslack_channel_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filterupdated_atgt: str | Unset = UNSET,
    filterupdated_atgte: str | Unset = UNSET,
    filterupdated_atlt: str | Unset = UNSET,
    filterupdated_atlte: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterdetected_atgt: str | Unset = UNSET,
    filterdetected_atgte: str | Unset = UNSET,
    filterdetected_atlt: str | Unset = UNSET,
    filterdetected_atlte: str | Unset = UNSET,
    filteracknowledged_atgt: str | Unset = UNSET,
    filteracknowledged_atgte: str | Unset = UNSET,
    filteracknowledged_atlt: str | Unset = UNSET,
    filteracknowledged_atlte: str | Unset = UNSET,
    filtermitigated_atgt: str | Unset = UNSET,
    filtermitigated_atgte: str | Unset = UNSET,
    filtermitigated_atlt: str | Unset = UNSET,
    filtermitigated_atlte: str | Unset = UNSET,
    filterresolved_atgt: str | Unset = UNSET,
    filterresolved_atgte: str | Unset = UNSET,
    filterresolved_atlt: str | Unset = UNSET,
    filterresolved_atlte: str | Unset = UNSET,
    filterclosed_atgt: str | Unset = UNSET,
    filterclosed_atgte: str | Unset = UNSET,
    filterclosed_atlt: str | Unset = UNSET,
    filterclosed_atlte: str | Unset = UNSET,
    filterin_triage_atgt: str | Unset = UNSET,
    filterin_triage_atgte: str | Unset = UNSET,
    filterin_triage_atlt: str | Unset = UNSET,
    filterin_triage_atlte: str | Unset = UNSET,
    sort: ListIncidentsSort | Unset = UNSET,
    include: ListIncidentsInclude | Unset = UNSET,
) -> IncidentList | None:
    """List incidents

     List incidents

    Args:
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersearch (str | Unset):
        filterkind (str | Unset):
        filterstatus (str | Unset):
        filterprivate (str | Unset):
        filteruser_id (int | Unset):
        filterseverity (str | Unset):
        filterseverity_id (str | Unset):
        filterlabels (str | Unset):
        filtertypes (str | Unset):
        filtertype_ids (str | Unset):
        filterenvironments (str | Unset):
        filterenvironment_ids (str | Unset):
        filterfunctionalities (str | Unset):
        filterfunctionality_ids (str | Unset):
        filterfunctionality_names (str | Unset):
        filterservices (str | Unset):
        filterservice_ids (str | Unset):
        filterservice_names (str | Unset):
        filterteams (str | Unset):
        filterteam_ids (str | Unset):
        filterteam_names (str | Unset):
        filtercause (str | Unset):
        filtercause_ids (str | Unset):
        filtercustom_field_selected_option_ids (str | Unset):
        filterslack_channel_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filterupdated_atgt (str | Unset):
        filterupdated_atgte (str | Unset):
        filterupdated_atlt (str | Unset):
        filterupdated_atlte (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterdetected_atgt (str | Unset):
        filterdetected_atgte (str | Unset):
        filterdetected_atlt (str | Unset):
        filterdetected_atlte (str | Unset):
        filteracknowledged_atgt (str | Unset):
        filteracknowledged_atgte (str | Unset):
        filteracknowledged_atlt (str | Unset):
        filteracknowledged_atlte (str | Unset):
        filtermitigated_atgt (str | Unset):
        filtermitigated_atgte (str | Unset):
        filtermitigated_atlt (str | Unset):
        filtermitigated_atlte (str | Unset):
        filterresolved_atgt (str | Unset):
        filterresolved_atgte (str | Unset):
        filterresolved_atlt (str | Unset):
        filterresolved_atlte (str | Unset):
        filterclosed_atgt (str | Unset):
        filterclosed_atgte (str | Unset):
        filterclosed_atlt (str | Unset):
        filterclosed_atlte (str | Unset):
        filterin_triage_atgt (str | Unset):
        filterin_triage_atgte (str | Unset):
        filterin_triage_atlt (str | Unset):
        filterin_triage_atlte (str | Unset):
        sort (ListIncidentsSort | Unset):
        include (ListIncidentsInclude | Unset):

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
            filterslack_channel_id=filterslack_channel_id,
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
