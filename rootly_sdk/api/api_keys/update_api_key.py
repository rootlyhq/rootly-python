from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_response import ApiKeyResponse
from ...models.errors_list import ErrorsList
from ...models.update_api_key import UpdateApiKey
from ...types import Response


def _get_kwargs(
    id: UUID,
    *,
    body: UpdateApiKey,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/api_keys/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
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
    body: UpdateApiKey,
) -> Response[ApiKeyResponse | ErrorsList]:
    """Update an API key

     Update an API key's mutable attributes: `name`, `description`, and `expires_at`.

    The key's `kind`, `role_id`, `on_call_role_id`, and token cannot be changed after creation. To issue
    a new token, use the rotate endpoint. To change the role or kind, revoke the key and create a new
    one.

    The new `expires_at` must be in the future and within 5 years.

    Args:
        id (UUID):
        body (UpdateApiKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyResponse | ErrorsList]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateApiKey,
) -> ApiKeyResponse | ErrorsList | None:
    """Update an API key

     Update an API key's mutable attributes: `name`, `description`, and `expires_at`.

    The key's `kind`, `role_id`, `on_call_role_id`, and token cannot be changed after creation. To issue
    a new token, use the rotate endpoint. To change the role or kind, revoke the key and create a new
    one.

    The new `expires_at` must be in the future and within 5 years.

    Args:
        id (UUID):
        body (UpdateApiKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyResponse | ErrorsList
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateApiKey,
) -> Response[ApiKeyResponse | ErrorsList]:
    """Update an API key

     Update an API key's mutable attributes: `name`, `description`, and `expires_at`.

    The key's `kind`, `role_id`, `on_call_role_id`, and token cannot be changed after creation. To issue
    a new token, use the rotate endpoint. To change the role or kind, revoke the key and create a new
    one.

    The new `expires_at` must be in the future and within 5 years.

    Args:
        id (UUID):
        body (UpdateApiKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyResponse | ErrorsList]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateApiKey,
) -> ApiKeyResponse | ErrorsList | None:
    """Update an API key

     Update an API key's mutable attributes: `name`, `description`, and `expires_at`.

    The key's `kind`, `role_id`, `on_call_role_id`, and token cannot be changed after creation. To issue
    a new token, use the rotate endpoint. To change the role or kind, revoke the key and create a new
    one.

    The new `expires_at` must be in the future and within 5 years.

    Args:
        id (UUID):
        body (UpdateApiKey):

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
            body=body,
        )
    ).parsed
