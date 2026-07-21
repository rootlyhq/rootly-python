from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_response import ApiKeyResponse
from ...models.errors_list import ErrorsList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    include: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include"] = include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/api_keys/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiKeyResponse | ErrorsList | None:
    if response.status_code == 200:
        response_200 = ApiKeyResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorsList.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiKeyResponse | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
) -> Response[ApiKeyResponse | ErrorsList]:
    """Retrieves an API key

     Retrieves a specific API key by its UUID. Returns key metadata including name, kind, expiration,
    last usage timestamp, and the grace period status — the secret token is never included.

    Args:
        id (UUID):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyResponse | ErrorsList]
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
    id: UUID,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
) -> ApiKeyResponse | ErrorsList | None:
    """Retrieves an API key

     Retrieves a specific API key by its UUID. Returns key metadata including name, kind, expiration,
    last usage timestamp, and the grace period status — the secret token is never included.

    Args:
        id (UUID):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyResponse | ErrorsList
    """

    return sync_detailed(
        id=id,
        client=client,
        include=include,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
) -> Response[ApiKeyResponse | ErrorsList]:
    """Retrieves an API key

     Retrieves a specific API key by its UUID. Returns key metadata including name, kind, expiration,
    last usage timestamp, and the grace period status — the secret token is never included.

    Args:
        id (UUID):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyResponse | ErrorsList]
    """

    kwargs = _get_kwargs(
        id=id,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
) -> ApiKeyResponse | ErrorsList | None:
    """Retrieves an API key

     Retrieves a specific API key by its UUID. Returns key metadata including name, kind, expiration,
    last usage timestamp, and the grace period status — the secret token is never included.

    Args:
        id (UUID):
        include (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyResponse | ErrorsList
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include=include,
        )
    ).parsed
