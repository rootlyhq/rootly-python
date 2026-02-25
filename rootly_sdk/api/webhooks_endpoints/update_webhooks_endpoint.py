from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.update_webhooks_endpoint import UpdateWebhooksEndpoint
from ...models.webhooks_endpoint_response import WebhooksEndpointResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateWebhooksEndpoint,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v1/webhooks/endpoints/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | WebhooksEndpointResponse | None:
    if response.status_code == 200:
        response_200 = WebhooksEndpointResponse.from_dict(response.json())

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
) -> Response[ErrorsList | WebhooksEndpointResponse]:
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
    body: UpdateWebhooksEndpoint,
) -> Response[ErrorsList | WebhooksEndpointResponse]:
    """Update a webhook endpoint

     Update a specific webhook endpoint by id

    Args:
        id (str):
        body (UpdateWebhooksEndpoint):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, WebhooksEndpointResponse]]
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
    body: UpdateWebhooksEndpoint,
) -> ErrorsList | WebhooksEndpointResponse | None:
    """Update a webhook endpoint

     Update a specific webhook endpoint by id

    Args:
        id (str):
        body (UpdateWebhooksEndpoint):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, WebhooksEndpointResponse]
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
    body: UpdateWebhooksEndpoint,
) -> Response[ErrorsList | WebhooksEndpointResponse]:
    """Update a webhook endpoint

     Update a specific webhook endpoint by id

    Args:
        id (str):
        body (UpdateWebhooksEndpoint):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorsList, WebhooksEndpointResponse]]
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
    body: UpdateWebhooksEndpoint,
) -> ErrorsList | WebhooksEndpointResponse | None:
    """Update a webhook endpoint

     Update a specific webhook endpoint by id

    Args:
        id (str):
        body (UpdateWebhooksEndpoint):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorsList, WebhooksEndpointResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
