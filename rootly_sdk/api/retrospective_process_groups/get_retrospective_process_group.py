from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_retrospective_process_group_include import (
    GetRetrospectiveProcessGroupInclude,
)
from ...models.retrospective_process_group_response import RetrospectiveProcessGroupResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    include: Unset | GetRetrospectiveProcessGroupInclude = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Unset | str = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/retrospective_process_groups/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RetrospectiveProcessGroupResponse | None:
    if response.status_code == 200:
        response_200 = RetrospectiveProcessGroupResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RetrospectiveProcessGroupResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | GetRetrospectiveProcessGroupInclude = UNSET,
) -> Response[RetrospectiveProcessGroupResponse]:
    """Retrieves a Retrospective Process Group

     Retrieves a specific Retrospective Process Group by id

    Args:
        id (str):
        include (Union[Unset, GetRetrospectiveProcessGroupInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrospectiveProcessGroupResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | GetRetrospectiveProcessGroupInclude = UNSET,
) -> RetrospectiveProcessGroupResponse | None:
    """Retrieves a Retrospective Process Group

     Retrieves a specific Retrospective Process Group by id

    Args:
        id (str):
        include (Union[Unset, GetRetrospectiveProcessGroupInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrospectiveProcessGroupResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        include=include,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | GetRetrospectiveProcessGroupInclude = UNSET,
) -> Response[RetrospectiveProcessGroupResponse]:
    """Retrieves a Retrospective Process Group

     Retrieves a specific Retrospective Process Group by id

    Args:
        id (str):
        include (Union[Unset, GetRetrospectiveProcessGroupInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RetrospectiveProcessGroupResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    include: Unset | GetRetrospectiveProcessGroupInclude = UNSET,
) -> RetrospectiveProcessGroupResponse | None:
    """Retrieves a Retrospective Process Group

     Retrieves a specific Retrospective Process Group by id

    Args:
        id (str):
        include (Union[Unset, GetRetrospectiveProcessGroupInclude]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RetrospectiveProcessGroupResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include=include,
        )
    ).parsed
