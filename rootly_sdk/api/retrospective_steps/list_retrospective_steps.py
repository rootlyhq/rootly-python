from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrospective_step_list import RetrospectiveStepList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    retrospective_process_id: str,
    *,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    sort: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/retrospective_processes/{retrospective_process_id}/retrospective_steps",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RetrospectiveStepList | None:
    if response.status_code == 200:
        response_200 = RetrospectiveStepList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrospectiveStepList]:
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
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    sort: Unset | str = UNSET,
) -> Response[RetrospectiveStepList]:
    """List retrospective steps

     List retrospective steps

    Args:
        retrospective_process_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrospectiveStepList]
    """

    kwargs = _get_kwargs(
        retrospective_process_id=retrospective_process_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    retrospective_process_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    sort: Unset | str = UNSET,
) -> RetrospectiveStepList | None:
    """List retrospective steps

     List retrospective steps

    Args:
        retrospective_process_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrospectiveStepList
    """

    return sync_detailed(
        retrospective_process_id=retrospective_process_id,
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    retrospective_process_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    sort: Unset | str = UNSET,
) -> Response[RetrospectiveStepList]:
    """List retrospective steps

     List retrospective steps

    Args:
        retrospective_process_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrospectiveStepList]
    """

    kwargs = _get_kwargs(
        retrospective_process_id=retrospective_process_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    retrospective_process_id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | str = UNSET,
    pagenumber: Unset | int = UNSET,
    pagesize: Unset | int = UNSET,
    sort: Unset | str = UNSET,
) -> RetrospectiveStepList | None:
    """List retrospective steps

     List retrospective steps

    Args:
        retrospective_process_id (str):
        include (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):
        sort (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrospectiveStepList
    """

    return (
        await asyncio_detailed(
            retrospective_process_id=retrospective_process_id,
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            sort=sort,
        )
    ).parsed
