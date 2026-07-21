from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_retrospective_process_groups_include import (
    ListRetrospectiveProcessGroupsInclude,
)
from ...models.list_retrospective_process_groups_sort import (
    ListRetrospectiveProcessGroupsSort,
)
from ...models.retrospective_process_group_list import RetrospectiveProcessGroupList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    retrospective_process_id: str,
    *,
    include: ListRetrospectiveProcessGroupsInclude | Unset = UNSET,
    sort: ListRetrospectiveProcessGroupsSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersub_status_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include: str | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[sub_status_id]"] = filtersub_status_id

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/retrospective_processes/{retrospective_process_id}/groups".format(
            retrospective_process_id=quote(str(retrospective_process_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RetrospectiveProcessGroupList | None:
    if response.status_code == 200:
        response_200 = RetrospectiveProcessGroupList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrospectiveProcessGroupList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    retrospective_process_id: str,
    *,
    client: AuthenticatedClient,
    include: ListRetrospectiveProcessGroupsInclude | Unset = UNSET,
    sort: ListRetrospectiveProcessGroupsSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersub_status_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> Response[RetrospectiveProcessGroupList]:
    """List Retrospective Process Groups

     List Retrospective Process Groups

    Args:
        retrospective_process_id (str):
        include (ListRetrospectiveProcessGroupsInclude | Unset):
        sort (ListRetrospectiveProcessGroupsSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersub_status_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrospectiveProcessGroupList]
    """

    kwargs = _get_kwargs(
        retrospective_process_id=retrospective_process_id,
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersub_status_id=filtersub_status_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    retrospective_process_id: str,
    *,
    client: AuthenticatedClient,
    include: ListRetrospectiveProcessGroupsInclude | Unset = UNSET,
    sort: ListRetrospectiveProcessGroupsSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersub_status_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> RetrospectiveProcessGroupList | None:
    """List Retrospective Process Groups

     List Retrospective Process Groups

    Args:
        retrospective_process_id (str):
        include (ListRetrospectiveProcessGroupsInclude | Unset):
        sort (ListRetrospectiveProcessGroupsSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersub_status_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrospectiveProcessGroupList
    """

    return sync_detailed(
        retrospective_process_id=retrospective_process_id,
        client=client,
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersub_status_id=filtersub_status_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
    ).parsed


async def asyncio_detailed(
    retrospective_process_id: str,
    *,
    client: AuthenticatedClient,
    include: ListRetrospectiveProcessGroupsInclude | Unset = UNSET,
    sort: ListRetrospectiveProcessGroupsSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersub_status_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> Response[RetrospectiveProcessGroupList]:
    """List Retrospective Process Groups

     List Retrospective Process Groups

    Args:
        retrospective_process_id (str):
        include (ListRetrospectiveProcessGroupsInclude | Unset):
        sort (ListRetrospectiveProcessGroupsSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersub_status_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrospectiveProcessGroupList]
    """

    kwargs = _get_kwargs(
        retrospective_process_id=retrospective_process_id,
        include=include,
        sort=sort,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersub_status_id=filtersub_status_id,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    retrospective_process_id: str,
    *,
    client: AuthenticatedClient,
    include: ListRetrospectiveProcessGroupsInclude | Unset = UNSET,
    sort: ListRetrospectiveProcessGroupsSort | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtersub_status_id: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
) -> RetrospectiveProcessGroupList | None:
    """List Retrospective Process Groups

     List Retrospective Process Groups

    Args:
        retrospective_process_id (str):
        include (ListRetrospectiveProcessGroupsInclude | Unset):
        sort (ListRetrospectiveProcessGroupsSort | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtersub_status_id (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrospectiveProcessGroupList
    """

    return (
        await asyncio_detailed(
            retrospective_process_id=retrospective_process_id,
            client=client,
            include=include,
            sort=sort,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtersub_status_id=filtersub_status_id,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
        )
    ).parsed
