from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_sub_status_list import IncidentSubStatusList
from ...models.list_incident_sub_statuses_include import (
    ListIncidentSubStatusesInclude,
)
from ...models.list_incident_sub_statuses_sort import ListIncidentSubStatusesSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    incident_id: str,
    *,
    include: Unset | ListIncidentSubStatusesInclude = UNSET,
    sort: Unset | ListIncidentSubStatusesSort = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersub_status_id: Unset | str = UNSET,
    filterassigned_atgt: Unset | str = UNSET,
    filterassigned_atgte: Unset | str = UNSET,
    filterassigned_atlt: Unset | str = UNSET,
    filterassigned_atlte: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Unset | str = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    json_sort: Unset | str = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[sub_status_id]"] = filtersub_status_id

    params["filter[assigned_at][gt]"] = filterassigned_atgt

    params["filter[assigned_at][gte]"] = filterassigned_atgte

    params["filter[assigned_at][lt]"] = filterassigned_atlt

    params["filter[assigned_at][lte]"] = filterassigned_atlte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/incidents/{incident_id}/sub_statuses",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IncidentSubStatusList | None:
    if response.status_code == 200:
        response_200 = IncidentSubStatusList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IncidentSubStatusList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | ListIncidentSubStatusesInclude = UNSET,
    sort: Unset | ListIncidentSubStatusesSort = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersub_status_id: Unset | str = UNSET,
    filterassigned_atgt: Unset | str = UNSET,
    filterassigned_atgte: Unset | str = UNSET,
    filterassigned_atlt: Unset | str = UNSET,
    filterassigned_atlte: Unset | str = UNSET,
) -> Response[IncidentSubStatusList]:
    """List incident_sub_statuses

     List incident_sub_statuses

    Args:
        incident_id (str):
        include (Union[Unset, ListIncidentSubStatusesInclude]):
        sort (Union[Unset, ListIncidentSubStatusesSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersub_status_id (Union[Unset, str]):
        filterassigned_atgt (Union[Unset, str]):
        filterassigned_atgte (Union[Unset, str]):
        filterassigned_atlt (Union[Unset, str]):
        filterassigned_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentSubStatusList]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersub_status_id=filtersub_status_id,
        filterassigned_atgt=filterassigned_atgt,
        filterassigned_atgte=filterassigned_atgte,
        filterassigned_atlt=filterassigned_atlt,
        filterassigned_atlte=filterassigned_atlte,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | ListIncidentSubStatusesInclude = UNSET,
    sort: Unset | ListIncidentSubStatusesSort = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersub_status_id: Unset | str = UNSET,
    filterassigned_atgt: Unset | str = UNSET,
    filterassigned_atgte: Unset | str = UNSET,
    filterassigned_atlt: Unset | str = UNSET,
    filterassigned_atlte: Unset | str = UNSET,
) -> IncidentSubStatusList | None:
    """List incident_sub_statuses

     List incident_sub_statuses

    Args:
        incident_id (str):
        include (Union[Unset, ListIncidentSubStatusesInclude]):
        sort (Union[Unset, ListIncidentSubStatusesSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersub_status_id (Union[Unset, str]):
        filterassigned_atgt (Union[Unset, str]):
        filterassigned_atgte (Union[Unset, str]):
        filterassigned_atlt (Union[Unset, str]):
        filterassigned_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentSubStatusList
    """

    return sync_detailed(
        incident_id=incident_id,
        client=client,
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersub_status_id=filtersub_status_id,
        filterassigned_atgt=filterassigned_atgt,
        filterassigned_atgte=filterassigned_atgte,
        filterassigned_atlt=filterassigned_atlt,
        filterassigned_atlte=filterassigned_atlte,
    ).parsed


async def asyncio_detailed(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | ListIncidentSubStatusesInclude = UNSET,
    sort: Unset | ListIncidentSubStatusesSort = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersub_status_id: Unset | str = UNSET,
    filterassigned_atgt: Unset | str = UNSET,
    filterassigned_atgte: Unset | str = UNSET,
    filterassigned_atlt: Unset | str = UNSET,
    filterassigned_atlte: Unset | str = UNSET,
) -> Response[IncidentSubStatusList]:
    """List incident_sub_statuses

     List incident_sub_statuses

    Args:
        incident_id (str):
        include (Union[Unset, ListIncidentSubStatusesInclude]):
        sort (Union[Unset, ListIncidentSubStatusesSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersub_status_id (Union[Unset, str]):
        filterassigned_atgt (Union[Unset, str]):
        filterassigned_atgte (Union[Unset, str]):
        filterassigned_atlt (Union[Unset, str]):
        filterassigned_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentSubStatusList]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersub_status_id=filtersub_status_id,
        filterassigned_atgt=filterassigned_atgt,
        filterassigned_atgte=filterassigned_atgte,
        filterassigned_atlt=filterassigned_atlt,
        filterassigned_atlte=filterassigned_atlte,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | ListIncidentSubStatusesInclude = UNSET,
    sort: Unset | ListIncidentSubStatusesSort = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersub_status_id: Unset | str = UNSET,
    filterassigned_atgt: Unset | str = UNSET,
    filterassigned_atgte: Unset | str = UNSET,
    filterassigned_atlt: Unset | str = UNSET,
    filterassigned_atlte: Unset | str = UNSET,
) -> IncidentSubStatusList | None:
    """List incident_sub_statuses

     List incident_sub_statuses

    Args:
        incident_id (str):
        include (Union[Unset, ListIncidentSubStatusesInclude]):
        sort (Union[Unset, ListIncidentSubStatusesSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersub_status_id (Union[Unset, str]):
        filterassigned_atgt (Union[Unset, str]):
        filterassigned_atgte (Union[Unset, str]):
        filterassigned_atlt (Union[Unset, str]):
        filterassigned_atlte (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentSubStatusList
    """

    return (
        await asyncio_detailed(
            incident_id=incident_id,
            client=client,
            include=include,
            sort=sort,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtersub_status_id=filtersub_status_id,
            filterassigned_atgt=filterassigned_atgt,
            filterassigned_atgte=filterassigned_atgte,
            filterassigned_atlt=filterassigned_atlt,
            filterassigned_atlte=filterassigned_atlte,
        )
    ).parsed
