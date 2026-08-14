from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_alert_route_response_200 import DeleteAlertRouteResponse200
from ...models.errors_list import ErrorsList
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/v1/alert_routes/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteAlertRouteResponse200 | ErrorsList | None:
    if response.status_code == 200:
        response_200 = DeleteAlertRouteResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorsList.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ErrorsList.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteAlertRouteResponse200 | ErrorsList]:
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
) -> Response[DeleteAlertRouteResponse200 | ErrorsList]:
    """Delete an alert route

     Delete a specific alert route by id. **Note: This endpoint requires access to Advanced Alert
    Routing. If you're unsure whether you have access to this feature, please contact Rootly customer
    support.**

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteAlertRouteResponse200, ErrorsList]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> DeleteAlertRouteResponse200 | ErrorsList | None:
    """Delete an alert route

     Delete a specific alert route by id. **Note: This endpoint requires access to Advanced Alert
    Routing. If you're unsure whether you have access to this feature, please contact Rootly customer
    support.**

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteAlertRouteResponse200, ErrorsList]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteAlertRouteResponse200 | ErrorsList]:
    """Delete an alert route

     Delete a specific alert route by id. **Note: This endpoint requires access to Advanced Alert
    Routing. If you're unsure whether you have access to this feature, please contact Rootly customer
    support.**

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteAlertRouteResponse200, ErrorsList]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> DeleteAlertRouteResponse200 | ErrorsList | None:
    """Delete an alert route

     Delete a specific alert route by id. **Note: This endpoint requires access to Advanced Alert
    Routing. If you're unsure whether you have access to this feature, please contact Rootly customer
    support.**

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteAlertRouteResponse200, ErrorsList]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
