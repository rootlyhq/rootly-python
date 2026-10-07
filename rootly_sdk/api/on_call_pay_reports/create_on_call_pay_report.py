from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.errors_list import ErrorsList
from ...models.new_on_call_pay_report import NewOnCallPayReport
from ...models.on_call_pay_report_response import OnCallPayReportResponse
from ...types import Response


def _get_kwargs(
    *,
    body: NewOnCallPayReport,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/on_call_pay_reports",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorsList | OnCallPayReportResponse | None:
    if response.status_code == 201:
        response_201 = OnCallPayReportResponse.from_dict(response.json())

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
) -> Response[ErrorsList | OnCallPayReportResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NewOnCallPayReport,
) -> Response[ErrorsList | OnCallPayReportResponse]:
    """Creates an On-Call Pay Report

     Generates a new on-call pay report for the given date range. The report is generated asynchronously.

    Args:
        body (NewOnCallPayReport):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | OnCallPayReportResponse]
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
    body: NewOnCallPayReport,
) -> ErrorsList | OnCallPayReportResponse | None:
    """Creates an On-Call Pay Report

     Generates a new on-call pay report for the given date range. The report is generated asynchronously.

    Args:
        body (NewOnCallPayReport):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | OnCallPayReportResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewOnCallPayReport,
) -> Response[ErrorsList | OnCallPayReportResponse]:
    """Creates an On-Call Pay Report

     Generates a new on-call pay report for the given date range. The report is generated asynchronously.

    Args:
        body (NewOnCallPayReport):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorsList | OnCallPayReportResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NewOnCallPayReport,
) -> ErrorsList | OnCallPayReportResponse | None:
    """Creates an On-Call Pay Report

     Generates a new on-call pay report for the given date range. The report is generated asynchronously.

    Args:
        body (NewOnCallPayReport):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorsList | OnCallPayReportResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
