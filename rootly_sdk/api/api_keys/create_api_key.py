from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_key_with_token_response import ApiKeyWithTokenResponse
from ...models.errors_list import ErrorsList
from ...models.new_api_key import NewApiKey
from ...types import Response


def _get_kwargs(
    *,
    body: NewApiKey,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/api_keys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiKeyWithTokenResponse | ErrorsList | None:
    if response.status_code == 201:
        response_201 = ApiKeyWithTokenResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422

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
    *,
    client: AuthenticatedClient,
    body: NewApiKey,
) -> Response[ApiKeyWithTokenResponse | ErrorsList]:
    """Creates an API key

     Creates a new API key and returns it with the plaintext token. **The token is only returned once** —
    store it securely, as it cannot be retrieved again.

    **Kinds and required fields:**
    - `personal` — created for the authenticated user. No additional fields required.
    - `team` — scoped to a team (group). Requires `group_id`. A service account is automatically created
    with permissions derived from group membership.
    - `organization` — organization-wide access. Requires owner or admin role. Optionally set `role_id`
    and `on_call_role_id` to control the service account's permissions.

    **Expiration:** All keys require an `expires_at` date set in the future (maximum 5 years). Names
    must be unique within their kind and scope.

    Args:
        body (NewApiKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyWithTokenResponse | ErrorsList]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: NewApiKey,
) -> ApiKeyWithTokenResponse | ErrorsList | None:
    """Creates an API key

     Creates a new API key and returns it with the plaintext token. **The token is only returned once** —
    store it securely, as it cannot be retrieved again.

    **Kinds and required fields:**
    - `personal` — created for the authenticated user. No additional fields required.
    - `team` — scoped to a team (group). Requires `group_id`. A service account is automatically created
    with permissions derived from group membership.
    - `organization` — organization-wide access. Requires owner or admin role. Optionally set `role_id`
    and `on_call_role_id` to control the service account's permissions.

    **Expiration:** All keys require an `expires_at` date set in the future (maximum 5 years). Names
    must be unique within their kind and scope.

    Args:
        body (NewApiKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyWithTokenResponse | ErrorsList
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewApiKey,
) -> Response[ApiKeyWithTokenResponse | ErrorsList]:
    """Creates an API key

     Creates a new API key and returns it with the plaintext token. **The token is only returned once** —
    store it securely, as it cannot be retrieved again.

    **Kinds and required fields:**
    - `personal` — created for the authenticated user. No additional fields required.
    - `team` — scoped to a team (group). Requires `group_id`. A service account is automatically created
    with permissions derived from group membership.
    - `organization` — organization-wide access. Requires owner or admin role. Optionally set `role_id`
    and `on_call_role_id` to control the service account's permissions.

    **Expiration:** All keys require an `expires_at` date set in the future (maximum 5 years). Names
    must be unique within their kind and scope.

    Args:
        body (NewApiKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiKeyWithTokenResponse | ErrorsList]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NewApiKey,
) -> ApiKeyWithTokenResponse | ErrorsList | None:
    """Creates an API key

     Creates a new API key and returns it with the plaintext token. **The token is only returned once** —
    store it securely, as it cannot be retrieved again.

    **Kinds and required fields:**
    - `personal` — created for the authenticated user. No additional fields required.
    - `team` — scoped to a team (group). Requires `group_id`. A service account is automatically created
    with permissions derived from group membership.
    - `organization` — organization-wide access. Requires owner or admin role. Optionally set `role_id`
    and `on_call_role_id` to control the service account's permissions.

    **Expiration:** All keys require an `expires_at` date set in the future (maximum 5 years). Names
    must be unique within their kind and scope.

    Args:
        body (NewApiKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiKeyWithTokenResponse | ErrorsList
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
