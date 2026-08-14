from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_response import ApiKeyResponse
from ...models.errors_list import ErrorsList
from ...types import Response


def _get_kwargs(
    id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/v1/api_keys/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiKeyResponse, ErrorsList]]:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiKeyResponse, ErrorsList]]:
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
) -> Response[Union[ApiKeyResponse, ErrorsList]]:
    """Revoke an API key

     Revoke an API key. The key is immediately invalidated and can no longer be used for authentication.
    This action cannot be undone.

    For `team` and `organization` keys, the associated service account is also deleted. Any active
    sessions using this key will fail on the next request.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiKeyResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ApiKeyResponse, ErrorsList]]:
    """Revoke an API key

     Revoke an API key. The key is immediately invalidated and can no longer be used for authentication.
    This action cannot be undone.

    For `team` and `organization` keys, the associated service account is also deleted. Any active
    sessions using this key will fail on the next request.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiKeyResponse, ErrorsList]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ApiKeyResponse, ErrorsList]]:
    """Revoke an API key

     Revoke an API key. The key is immediately invalidated and can no longer be used for authentication.
    This action cannot be undone.

    For `team` and `organization` keys, the associated service account is also deleted. Any active
    sessions using this key will fail on the next request.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiKeyResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ApiKeyResponse, ErrorsList]]:
    """Revoke an API key

     Revoke an API key. The key is immediately invalidated and can no longer be used for authentication.
    This action cannot be undone.

    For `team` and `organization` keys, the associated service account is also deleted. Any active
    sessions using this key will fail on the next request.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiKeyResponse, ErrorsList]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
