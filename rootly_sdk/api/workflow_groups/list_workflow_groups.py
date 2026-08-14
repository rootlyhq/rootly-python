from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.workflow_group_list import WorkflowGroupList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterexpanded: Unset | bool = UNSET,
    filterposition: Unset | int = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[search]"] = filtersearch

    params["filter[name]"] = filtername

    params["filter[slug]"] = filterslug

    params["filter[kind]"] = filterkind

    params["filter[expanded]"] = filterexpanded

    params["filter[position]"] = filterposition

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/workflow_groups",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WorkflowGroupList | None:
    if response.status_code == 200:
        response_200 = WorkflowGroupList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WorkflowGroupList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterexpanded: Unset | bool = UNSET,
    filterposition: Unset | int = UNSET,
) -> Response[WorkflowGroupList]:
    """List workflow groups

     List workflow groups

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterexpanded (Union[Unset, bool]):
        filterposition (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowGroupList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filtername=filtername,
        filterslug=filterslug,
        filterkind=filterkind,
        filterexpanded=filterexpanded,
        filterposition=filterposition,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterexpanded: Unset | bool = UNSET,
    filterposition: Unset | int = UNSET,
) -> WorkflowGroupList | None:
    """List workflow groups

     List workflow groups

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterexpanded (Union[Unset, bool]):
        filterposition (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowGroupList
    """

    return sync_detailed(
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filtername=filtername,
        filterslug=filterslug,
        filterkind=filterkind,
        filterexpanded=filterexpanded,
        filterposition=filterposition,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterexpanded: Unset | bool = UNSET,
    filterposition: Unset | int = UNSET,
) -> Response[WorkflowGroupList]:
    """List workflow groups

     List workflow groups

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterexpanded (Union[Unset, bool]):
        filterposition (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkflowGroupList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtersearch=filtersearch,
        filtername=filtername,
        filterslug=filterslug,
        filterkind=filterkind,
        filterexpanded=filterexpanded,
        filterposition=filterposition,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    filtersearch: Unset | str = UNSET,
    filtername: Unset | str = UNSET,
    filterslug: Unset | str = UNSET,
    filterkind: Unset | str = UNSET,
    filterexpanded: Unset | bool = UNSET,
    filterposition: Unset | int = UNSET,
) -> WorkflowGroupList | None:
    """List workflow groups

     List workflow groups

    Args:
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        filtersearch (Union[Unset, str]):
        filtername (Union[Unset, str]):
        filterslug (Union[Unset, str]):
        filterkind (Union[Unset, str]):
        filterexpanded (Union[Unset, bool]):
        filterposition (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkflowGroupList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtersearch=filtersearch,
            filtername=filtername,
            filterslug=filterslug,
            filterkind=filterkind,
            filterexpanded=filterexpanded,
            filterposition=filterposition,
        )
    ).parsed
