from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_route_response import AlertRouteResponse
from ...models.errors_list import ErrorsList
from ...models.patch_alert_route import PatchAlertRoute
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: PatchAlertRoute,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/v1/alert_routes/{id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AlertRouteResponse | ErrorsList | None:
    if response.status_code == 200:
        response_200 = AlertRouteResponse.from_dict(response.json())

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
) -> Response[AlertRouteResponse | ErrorsList]:
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
    body: PatchAlertRoute,
) -> Response[AlertRouteResponse | ErrorsList]:
    """Update an alert route

     Updates an alert route. **Note: This endpoint requires access to Advanced Alert Routing. If you're
    unsure whether you have access to this feature, please contact Rootly customer support.**

    Args:
        id (str):
        body (PatchAlertRoute):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertRouteResponse, ErrorsList]]
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
    body: PatchAlertRoute,
) -> AlertRouteResponse | ErrorsList | None:
    """Update an alert route

     Updates an alert route. **Note: This endpoint requires access to Advanced Alert Routing. If you're
    unsure whether you have access to this feature, please contact Rootly customer support.**

    Args:
        id (str):
        body (PatchAlertRoute):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertRouteResponse, ErrorsList]
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
    body: PatchAlertRoute,
) -> Response[AlertRouteResponse | ErrorsList]:
    """Update an alert route

     Updates an alert route. **Note: This endpoint requires access to Advanced Alert Routing. If you're
    unsure whether you have access to this feature, please contact Rootly customer support.**

    Args:
        id (str):
        body (PatchAlertRoute):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlertRouteResponse, ErrorsList]]
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
    body: PatchAlertRoute,
) -> AlertRouteResponse | ErrorsList | None:
    """Update an alert route

     Updates an alert route. **Note: This endpoint requires access to Advanced Alert Routing. If you're
    unsure whether you have access to this feature, please contact Rootly customer support.**

    Args:
        id (str):
        body (PatchAlertRoute):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlertRouteResponse, ErrorsList]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
