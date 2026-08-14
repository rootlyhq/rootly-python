from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_edge_connector_action_body import UpdateEdgeConnectorActionBody
from ...types import Response


def _get_kwargs(
    edge_connector_id: str,
    id: UUID | str,
    *,
    body: UpdateEdgeConnectorActionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/v1/edge_connectors/{edge_connector_id}/actions/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    edge_connector_id: str,
    id: UUID | str,
    *,
    client: AuthenticatedClient,
    body: UpdateEdgeConnectorActionBody,
) -> Response[Any]:
    """Update edge connector action

    Args:
        edge_connector_id (str):
        id (Union[UUID, str]):
        body (UpdateEdgeConnectorActionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        edge_connector_id=edge_connector_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    edge_connector_id: str,
    id: UUID | str,
    *,
    client: AuthenticatedClient,
    body: UpdateEdgeConnectorActionBody,
) -> Response[Any]:
    """Update edge connector action

    Args:
        edge_connector_id (str):
        id (Union[UUID, str]):
        body (UpdateEdgeConnectorActionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        edge_connector_id=edge_connector_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
