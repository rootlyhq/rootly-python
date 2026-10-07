from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_playbooks_include import ListPlaybooksInclude
from ...models.playbook_list import PlaybookList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: ListPlaybooksInclude | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_include: str | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/playbooks",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PlaybookList | None:
    if response.status_code == 200:
        response_200 = PlaybookList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PlaybookList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: ListPlaybooksInclude | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[PlaybookList]:
    """List playbooks

     List playbooks

    Args:
        include (ListPlaybooksInclude | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlaybookList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: ListPlaybooksInclude | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> PlaybookList | None:
    """List playbooks

     List playbooks

    Args:
        include (ListPlaybooksInclude | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlaybookList
    """

    return sync_detailed(
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: ListPlaybooksInclude | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[PlaybookList]:
    """List playbooks

     List playbooks

    Args:
        include (ListPlaybooksInclude | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlaybookList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: ListPlaybooksInclude | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> PlaybookList | None:
    """List playbooks

     List playbooks

    Args:
        include (ListPlaybooksInclude | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlaybookList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
        )
    ).parsed
