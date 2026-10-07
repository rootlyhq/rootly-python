from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_destroy_services_response import BulkDestroyServicesResponse
from ...models.bulk_destroy_services_type_0 import BulkDestroyServicesType0
from ...models.bulk_destroy_services_type_1 import BulkDestroyServicesType1
from ...models.errors_list import ErrorsList
from ...types import Response


def _get_kwargs(
    *,
    body: BulkDestroyServicesType0 | BulkDestroyServicesType1,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/services/bulk_delete",
    }

    if isinstance(body, BulkDestroyServicesType0):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BulkDestroyServicesResponse | BulkDestroyServicesResponse | ErrorsList | ErrorsList | None:
    if response.status_code == 200:
        response_200 = BulkDestroyServicesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if response.status_code == 422:

        def _parse_response_422(data: object) -> BulkDestroyServicesResponse | ErrorsList:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = ErrorsList.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_1 = BulkDestroyServicesResponse.from_dict(data)

            return response_422_type_1

        response_422 = _parse_response_422(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BulkDestroyServicesResponse | BulkDestroyServicesResponse | ErrorsList | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkDestroyServicesType0 | BulkDestroyServicesType1,
) -> Response[BulkDestroyServicesResponse | BulkDestroyServicesResponse | ErrorsList | ErrorsList]:
    """Bulk delete Services

     Delete services by external_id list, or prune by managed_by source. Two mutually exclusive modes.

    Args:
        body (BulkDestroyServicesType0 | BulkDestroyServicesType1): Two mutually exclusive modes.
            Pass exactly one of: external_ids (delete specific records) or managed_by (prune all
            managed records not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkDestroyServicesResponse | BulkDestroyServicesResponse | ErrorsList | ErrorsList]
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
    body: BulkDestroyServicesType0 | BulkDestroyServicesType1,
) -> BulkDestroyServicesResponse | BulkDestroyServicesResponse | ErrorsList | ErrorsList | None:
    """Bulk delete Services

     Delete services by external_id list, or prune by managed_by source. Two mutually exclusive modes.

    Args:
        body (BulkDestroyServicesType0 | BulkDestroyServicesType1): Two mutually exclusive modes.
            Pass exactly one of: external_ids (delete specific records) or managed_by (prune all
            managed records not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkDestroyServicesResponse | BulkDestroyServicesResponse | ErrorsList | ErrorsList
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkDestroyServicesType0 | BulkDestroyServicesType1,
) -> Response[BulkDestroyServicesResponse | BulkDestroyServicesResponse | ErrorsList | ErrorsList]:
    """Bulk delete Services

     Delete services by external_id list, or prune by managed_by source. Two mutually exclusive modes.

    Args:
        body (BulkDestroyServicesType0 | BulkDestroyServicesType1): Two mutually exclusive modes.
            Pass exactly one of: external_ids (delete specific records) or managed_by (prune all
            managed records not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkDestroyServicesResponse | BulkDestroyServicesResponse | ErrorsList | ErrorsList]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BulkDestroyServicesType0 | BulkDestroyServicesType1,
) -> BulkDestroyServicesResponse | BulkDestroyServicesResponse | ErrorsList | ErrorsList | None:
    """Bulk delete Services

     Delete services by external_id list, or prune by managed_by source. Two mutually exclusive modes.

    Args:
        body (BulkDestroyServicesType0 | BulkDestroyServicesType1): Two mutually exclusive modes.
            Pass exactly one of: external_ids (delete specific records) or managed_by (prune all
            managed records not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkDestroyServicesResponse | BulkDestroyServicesResponse | ErrorsList | ErrorsList
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
