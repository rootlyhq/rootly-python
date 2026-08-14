from http import HTTPStatus
from typing import Any, Optional, Union

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
    include: Union[Unset, ListRetrospectiveProcessGroupsInclude] = UNSET,
    sort: Union[Unset, ListRetrospectiveProcessGroupsSort] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersub_status_id: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Union[Unset, str] = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    json_sort: Union[Unset, str] = UNSET
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
        "url": f"/v1/retrospective_processes/{retrospective_process_id}/groups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RetrospectiveProcessGroupList]:
    if response.status_code == 200:
        response_200 = RetrospectiveProcessGroupList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
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
    include: Union[Unset, ListRetrospectiveProcessGroupsInclude] = UNSET,
    sort: Union[Unset, ListRetrospectiveProcessGroupsSort] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersub_status_id: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
) -> Response[RetrospectiveProcessGroupList]:
    """List Retrospective Process Groups

     List Retrospective Process Groups

    Args:
        retrospective_process_id (str):
        include (Union[Unset, ListRetrospectiveProcessGroupsInclude]):
        sort (Union[Unset, ListRetrospectiveProcessGroupsSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersub_status_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

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
    include: Union[Unset, ListRetrospectiveProcessGroupsInclude] = UNSET,
    sort: Union[Unset, ListRetrospectiveProcessGroupsSort] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersub_status_id: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
) -> Optional[RetrospectiveProcessGroupList]:
    """List Retrospective Process Groups

     List Retrospective Process Groups

    Args:
        retrospective_process_id (str):
        include (Union[Unset, ListRetrospectiveProcessGroupsInclude]):
        sort (Union[Unset, ListRetrospectiveProcessGroupsSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersub_status_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

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
    include: Union[Unset, ListRetrospectiveProcessGroupsInclude] = UNSET,
    sort: Union[Unset, ListRetrospectiveProcessGroupsSort] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersub_status_id: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
) -> Response[RetrospectiveProcessGroupList]:
    """List Retrospective Process Groups

     List Retrospective Process Groups

    Args:
        retrospective_process_id (str):
        include (Union[Unset, ListRetrospectiveProcessGroupsInclude]):
        sort (Union[Unset, ListRetrospectiveProcessGroupsSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersub_status_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

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
    include: Union[Unset, ListRetrospectiveProcessGroupsInclude] = UNSET,
    sort: Union[Unset, ListRetrospectiveProcessGroupsSort] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
    filtersub_status_id: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
) -> Optional[RetrospectiveProcessGroupList]:
    """List Retrospective Process Groups

     List Retrospective Process Groups

    Args:
        retrospective_process_id (str):
        include (Union[Unset, ListRetrospectiveProcessGroupsInclude]):
        sort (Union[Unset, ListRetrospectiveProcessGroupsSort]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersub_status_id (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):

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
