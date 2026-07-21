from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_with_token_response import ApiKeyWithTokenResponse
from ...models.errors_list import ErrorsList
from ...models.rotate_api_key import RotateApiKey
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: RotateApiKey | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/api_keys/{id}/rotate".format(
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiKeyWithTokenResponse | ErrorsList | None:
    if response.status_code == 200:
        response_200 = ApiKeyWithTokenResponse.from_dict(response.json())

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
) -> Response[ApiKeyWithTokenResponse | ErrorsList]:
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
    body: RotateApiKey | Unset = UNSET,
) -> Response[ApiKeyWithTokenResponse | ErrorsList]:
    """Rotate an API key

     Rotate an API key's token. Issues a new secret token and returns it — **the new token is only shown
    once**, so store it securely.

    **Self-only:** You can only rotate the API key that was used to authenticate this request.
    Attempting to rotate a different key returns `403 Forbidden`.

    **Grace period:** When enabled for your organization, the previous token remains valid after
    rotation, giving you time to deploy the new token without downtime. Pass `grace_period_minutes`
    (integer, 0–1440, default 30) to control how long the old token stays valid. Set to 0 to immediately
    invalidate the old token. The `grace_period_ends_at` field in the response confirms the exact time
    the old token will stop working.

    **Expiration:** Optionally provide a new `expires_at` date (ISO 8601, up to 5 years). Defaults to 90
    days from now if omitted. Dates in the past are rejected.

    **Typical rotation workflow:**
    1. Call this endpoint to get a new token (optionally with a custom `grace_period_minutes`).
    2. Deploy the new token to your systems.
    3. The old token continues working for `grace_period_minutes` (if grace period is enabled).
    4. After the grace period, the old token is automatically invalidated.

    Args:
        id (str):
        body (RotateApiKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyWithTokenResponse | ErrorsList]
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
    id: str,
    *,
    client: AuthenticatedClient,
    body: RotateApiKey | Unset = UNSET,
) -> ApiKeyWithTokenResponse | ErrorsList | None:
    """Rotate an API key

     Rotate an API key's token. Issues a new secret token and returns it — **the new token is only shown
    once**, so store it securely.

    **Self-only:** You can only rotate the API key that was used to authenticate this request.
    Attempting to rotate a different key returns `403 Forbidden`.

    **Grace period:** When enabled for your organization, the previous token remains valid after
    rotation, giving you time to deploy the new token without downtime. Pass `grace_period_minutes`
    (integer, 0–1440, default 30) to control how long the old token stays valid. Set to 0 to immediately
    invalidate the old token. The `grace_period_ends_at` field in the response confirms the exact time
    the old token will stop working.

    **Expiration:** Optionally provide a new `expires_at` date (ISO 8601, up to 5 years). Defaults to 90
    days from now if omitted. Dates in the past are rejected.

    **Typical rotation workflow:**
    1. Call this endpoint to get a new token (optionally with a custom `grace_period_minutes`).
    2. Deploy the new token to your systems.
    3. The old token continues working for `grace_period_minutes` (if grace period is enabled).
    4. After the grace period, the old token is automatically invalidated.

    Args:
        id (str):
        body (RotateApiKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyWithTokenResponse | ErrorsList
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: RotateApiKey | Unset = UNSET,
) -> Response[ApiKeyWithTokenResponse | ErrorsList]:
    """Rotate an API key

     Rotate an API key's token. Issues a new secret token and returns it — **the new token is only shown
    once**, so store it securely.

    **Self-only:** You can only rotate the API key that was used to authenticate this request.
    Attempting to rotate a different key returns `403 Forbidden`.

    **Grace period:** When enabled for your organization, the previous token remains valid after
    rotation, giving you time to deploy the new token without downtime. Pass `grace_period_minutes`
    (integer, 0–1440, default 30) to control how long the old token stays valid. Set to 0 to immediately
    invalidate the old token. The `grace_period_ends_at` field in the response confirms the exact time
    the old token will stop working.

    **Expiration:** Optionally provide a new `expires_at` date (ISO 8601, up to 5 years). Defaults to 90
    days from now if omitted. Dates in the past are rejected.

    **Typical rotation workflow:**
    1. Call this endpoint to get a new token (optionally with a custom `grace_period_minutes`).
    2. Deploy the new token to your systems.
    3. The old token continues working for `grace_period_minutes` (if grace period is enabled).
    4. After the grace period, the old token is automatically invalidated.

    Args:
        id (str):
        body (RotateApiKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyWithTokenResponse | ErrorsList]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: RotateApiKey | Unset = UNSET,
) -> ApiKeyWithTokenResponse | ErrorsList | None:
    """Rotate an API key

     Rotate an API key's token. Issues a new secret token and returns it — **the new token is only shown
    once**, so store it securely.

    **Self-only:** You can only rotate the API key that was used to authenticate this request.
    Attempting to rotate a different key returns `403 Forbidden`.

    **Grace period:** When enabled for your organization, the previous token remains valid after
    rotation, giving you time to deploy the new token without downtime. Pass `grace_period_minutes`
    (integer, 0–1440, default 30) to control how long the old token stays valid. Set to 0 to immediately
    invalidate the old token. The `grace_period_ends_at` field in the response confirms the exact time
    the old token will stop working.

    **Expiration:** Optionally provide a new `expires_at` date (ISO 8601, up to 5 years). Defaults to 90
    days from now if omitted. Dates in the past are rejected.

    **Typical rotation workflow:**
    1. Call this endpoint to get a new token (optionally with a custom `grace_period_minutes`).
    2. Deploy the new token to your systems.
    3. The old token continues working for `grace_period_minutes` (if grace period is enabled).
    4. After the grace period, the old token is automatically invalidated.

    Args:
        id (str):
        body (RotateApiKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyWithTokenResponse | ErrorsList
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
