from http import HTTPStatus
from typing import Any, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_destroy_environments_response import BulkDestroyEnvironmentsResponse
from ...models.bulk_destroy_environments_type_0 import BulkDestroyEnvironmentsType0
from ...models.bulk_destroy_environments_type_1 import BulkDestroyEnvironmentsType1
from ...models.errors_list import ErrorsList
from ...types import Response


def _get_kwargs(
    *,
    body: Union["BulkDestroyEnvironmentsType0", "BulkDestroyEnvironmentsType1"],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/environments/bulk_delete",
    }

    _kwargs["json"]: dict[str, Any]
    if isinstance(body, BulkDestroyEnvironmentsType0):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BulkDestroyEnvironmentsResponse | ErrorsList | Union["BulkDestroyEnvironmentsResponse", "ErrorsList"] | None:
    if response.status_code == 200:
        response_200 = BulkDestroyEnvironmentsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())

        return response_401

    if response.status_code == 422:

        def _parse_response_422(data: object) -> Union["BulkDestroyEnvironmentsResponse", "ErrorsList"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = ErrorsList.from_dict(data)

                return response_422_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_1 = BulkDestroyEnvironmentsResponse.from_dict(data)

            return response_422_type_1

        response_422 = _parse_response_422(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[BulkDestroyEnvironmentsResponse | ErrorsList | Union["BulkDestroyEnvironmentsResponse", "ErrorsList"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union["BulkDestroyEnvironmentsType0", "BulkDestroyEnvironmentsType1"],
) -> Response[BulkDestroyEnvironmentsResponse | ErrorsList | Union["BulkDestroyEnvironmentsResponse", "ErrorsList"]]:
    """Bulk delete Environments

     Delete environments by external_id list, or prune by managed_by source. Two mutually exclusive
    modes.

    Args:
        body (Union['BulkDestroyEnvironmentsType0', 'BulkDestroyEnvironmentsType1']): Two mutually
            exclusive modes. Pass exactly one of: external_ids (delete specific records) or managed_by
            (prune all managed records not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkDestroyEnvironmentsResponse, ErrorsList, Union['BulkDestroyEnvironmentsResponse', 'ErrorsList']]]
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
    body: Union["BulkDestroyEnvironmentsType0", "BulkDestroyEnvironmentsType1"],
) -> BulkDestroyEnvironmentsResponse | ErrorsList | Union["BulkDestroyEnvironmentsResponse", "ErrorsList"] | None:
    """Bulk delete Environments

     Delete environments by external_id list, or prune by managed_by source. Two mutually exclusive
    modes.

    Args:
        body (Union['BulkDestroyEnvironmentsType0', 'BulkDestroyEnvironmentsType1']): Two mutually
            exclusive modes. Pass exactly one of: external_ids (delete specific records) or managed_by
            (prune all managed records not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkDestroyEnvironmentsResponse, ErrorsList, Union['BulkDestroyEnvironmentsResponse', 'ErrorsList']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union["BulkDestroyEnvironmentsType0", "BulkDestroyEnvironmentsType1"],
) -> Response[BulkDestroyEnvironmentsResponse | ErrorsList | Union["BulkDestroyEnvironmentsResponse", "ErrorsList"]]:
    """Bulk delete Environments

     Delete environments by external_id list, or prune by managed_by source. Two mutually exclusive
    modes.

    Args:
        body (Union['BulkDestroyEnvironmentsType0', 'BulkDestroyEnvironmentsType1']): Two mutually
            exclusive modes. Pass exactly one of: external_ids (delete specific records) or managed_by
            (prune all managed records not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkDestroyEnvironmentsResponse, ErrorsList, Union['BulkDestroyEnvironmentsResponse', 'ErrorsList']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union["BulkDestroyEnvironmentsType0", "BulkDestroyEnvironmentsType1"],
) -> BulkDestroyEnvironmentsResponse | ErrorsList | Union["BulkDestroyEnvironmentsResponse", "ErrorsList"] | None:
    """Bulk delete Environments

     Delete environments by external_id list, or prune by managed_by source. Two mutually exclusive
    modes.

    Args:
        body (Union['BulkDestroyEnvironmentsType0', 'BulkDestroyEnvironmentsType1']): Two mutually
            exclusive modes. Pass exactly one of: external_ids (delete specific records) or managed_by
            (prune all managed records not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkDestroyEnvironmentsResponse, ErrorsList, Union['BulkDestroyEnvironmentsResponse', 'ErrorsList']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
