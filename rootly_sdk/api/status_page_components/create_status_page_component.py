from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.new_status_page_component import NewStatusPageComponent
from ...models.status_page_component_response import StatusPageComponentResponse
from ...types import Response


def _get_kwargs(
    status_page_id: str,
    *,
    body: NewStatusPageComponent,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/status-pages/{status_page_id}/components".format(
            status_page_id=quote(str(status_page_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | StatusPageComponentResponse | None:
    if response.status_code == 201:
        response_201 = StatusPageComponentResponse.from_dict(response.json())

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
) -> Response[ErrorsList | StatusPageComponentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    status_page_id: str,
    *,
    client: AuthenticatedClient,
    body: NewStatusPageComponent,
) -> Response[ErrorsList | StatusPageComponentResponse]:
    """Creates a status page component

     Creates a new status page component from provided data

    Args:
        status_page_id (str):
        body (NewStatusPageComponent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | StatusPageComponentResponse]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    status_page_id: str,
    *,
    client: AuthenticatedClient,
    body: NewStatusPageComponent,
) -> ErrorsList | StatusPageComponentResponse | None:
    """Creates a status page component

     Creates a new status page component from provided data

    Args:
        status_page_id (str):
        body (NewStatusPageComponent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | StatusPageComponentResponse
    """

    return sync_detailed(
        status_page_id=status_page_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    status_page_id: str,
    *,
    client: AuthenticatedClient,
    body: NewStatusPageComponent,
) -> Response[ErrorsList | StatusPageComponentResponse]:
    """Creates a status page component

     Creates a new status page component from provided data

    Args:
        status_page_id (str):
        body (NewStatusPageComponent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | StatusPageComponentResponse]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    status_page_id: str,
    *,
    client: AuthenticatedClient,
    body: NewStatusPageComponent,
) -> ErrorsList | StatusPageComponentResponse | None:
    """Creates a status page component

     Creates a new status page component from provided data

    Args:
        status_page_id (str):
        body (NewStatusPageComponent):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | StatusPageComponentResponse
    """

    return (
        await asyncio_detailed(
            status_page_id=status_page_id,
            client=client,
            body=body,
        )
    ).parsed
