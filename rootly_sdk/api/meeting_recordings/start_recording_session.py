from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.start_session_request import StartSessionRequest
from ...models.start_session_response import StartSessionResponse
from ...types import Response


def _get_kwargs(
    *,
    body: StartSessionRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/meeting_recordings/start_session",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, StartSessionResponse]]:
    if response.status_code == 201:
        response_201 = StartSessionResponse.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, StartSessionResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: StartSessionRequest,
) -> Response[Union[Any, StartSessionResponse]]:
    """Start a recording session

     Start a new desktop recording session. The server creates a recording record and returns a stream
    token the desktop client uses to send audio. No provider-specific configuration is needed from the
    client.

    Args:
        body (StartSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StartSessionResponse]]
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
    body: StartSessionRequest,
) -> Optional[Union[Any, StartSessionResponse]]:
    """Start a recording session

     Start a new desktop recording session. The server creates a recording record and returns a stream
    token the desktop client uses to send audio. No provider-specific configuration is needed from the
    client.

    Args:
        body (StartSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StartSessionResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: StartSessionRequest,
) -> Response[Union[Any, StartSessionResponse]]:
    """Start a recording session

     Start a new desktop recording session. The server creates a recording record and returns a stream
    token the desktop client uses to send audio. No provider-specific configuration is needed from the
    client.

    Args:
        body (StartSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StartSessionResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: StartSessionRequest,
) -> Optional[Union[Any, StartSessionResponse]]:
    """Start a recording session

     Start a new desktop recording session. The server creates a recording record and returns a stream
    token the desktop client uses to send audio. No provider-specific configuration is needed from the
    client.

    Args:
        body (StartSessionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StartSessionResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
