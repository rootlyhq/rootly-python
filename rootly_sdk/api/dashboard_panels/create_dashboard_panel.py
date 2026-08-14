from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dashboard_panel_response import DashboardPanelResponse
from ...models.errors_list import ErrorsList
from ...models.new_dashboard_panel import NewDashboardPanel
from ...types import Response


def _get_kwargs(
    dashboard_id: str,
    *,
    body: NewDashboardPanel,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v1/dashboards/{dashboard_id}/panels",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DashboardPanelResponse | ErrorsList | None:
    if response.status_code == 201:
        response_201 = DashboardPanelResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DashboardPanelResponse | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_id: str,
    *,
    client: AuthenticatedClient,
    body: NewDashboardPanel,
) -> Response[DashboardPanelResponse | ErrorsList]:
    """Creates a dashboard panel

     Creates a new dashboard panel from provided data

    Args:
        dashboard_id (str):
        body (NewDashboardPanel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DashboardPanelResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dashboard_id: str,
    *,
    client: AuthenticatedClient,
    body: NewDashboardPanel,
) -> DashboardPanelResponse | ErrorsList | None:
    """Creates a dashboard panel

     Creates a new dashboard panel from provided data

    Args:
        dashboard_id (str):
        body (NewDashboardPanel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DashboardPanelResponse, ErrorsList]
    """

    return sync_detailed(
        dashboard_id=dashboard_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dashboard_id: str,
    *,
    client: AuthenticatedClient,
    body: NewDashboardPanel,
) -> Response[DashboardPanelResponse | ErrorsList]:
    """Creates a dashboard panel

     Creates a new dashboard panel from provided data

    Args:
        dashboard_id (str):
        body (NewDashboardPanel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DashboardPanelResponse, ErrorsList]]
    """

    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dashboard_id: str,
    *,
    client: AuthenticatedClient,
    body: NewDashboardPanel,
) -> DashboardPanelResponse | ErrorsList | None:
    """Creates a dashboard panel

     Creates a new dashboard panel from provided data

    Args:
        dashboard_id (str):
        body (NewDashboardPanel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DashboardPanelResponse, ErrorsList]
    """

    return (
        await asyncio_detailed(
            dashboard_id=dashboard_id,
            client=client,
            body=body,
        )
    ).parsed
