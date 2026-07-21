from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.start_session_request import StartSessionRequest
from ...models.start_session_response import StartSessionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: StartSessionRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/meeting_recordings/start_session",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | StartSessionResponse | None:
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | StartSessionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: StartSessionRequest | Unset = UNSET,

) -> Response[Any | StartSessionResponse]:
    """ Start a recording session

     Start a new desktop recording session. The server creates a recording record and returns a stream
    token the desktop client uses to send audio. No provider-specific configuration is needed from the
    client.

    Args:
        body (StartSessionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StartSessionResponse]
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
    body: StartSessionRequest | Unset = UNSET,

) -> Any | StartSessionResponse | None:
    """ Start a recording session

     Start a new desktop recording session. The server creates a recording record and returns a stream
    token the desktop client uses to send audio. No provider-specific configuration is needed from the
    client.

    Args:
        body (StartSessionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StartSessionResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: StartSessionRequest | Unset = UNSET,

) -> Response[Any | StartSessionResponse]:
    """ Start a recording session

     Start a new desktop recording session. The server creates a recording record and returns a stream
    token the desktop client uses to send audio. No provider-specific configuration is needed from the
    client.

    Args:
        body (StartSessionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | StartSessionResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: StartSessionRequest | Unset = UNSET,

) -> Any | StartSessionResponse | None:
    """ Start a recording session

     Start a new desktop recording session. The server creates a recording record and returns a stream
    token the desktop client uses to send audio. No provider-specific configuration is needed from the
    client.

    Args:
        body (StartSessionRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | StartSessionResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
