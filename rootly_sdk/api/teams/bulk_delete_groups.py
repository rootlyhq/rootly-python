from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulk_destroy_teams_response import BulkDestroyTeamsResponse
from ...models.bulk_destroy_teams_type_0 import BulkDestroyTeamsType0
from ...models.bulk_destroy_teams_type_1 import BulkDestroyTeamsType1
from ...models.errors_list import ErrorsList
from typing import cast



def _get_kwargs(
    *,
    body: BulkDestroyTeamsType0 | BulkDestroyTeamsType1,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/teams/bulk_delete",
    }

    
    if isinstance(body, BulkDestroyTeamsType0):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()



    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BulkDestroyTeamsResponse | BulkDestroyTeamsResponse | ErrorsList | ErrorsList | None:
    if response.status_code == 200:
        response_200 = BulkDestroyTeamsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        def _parse_response_422(data: object) -> BulkDestroyTeamsResponse | ErrorsList:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = ErrorsList.from_dict(data)



                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_1 = BulkDestroyTeamsResponse.from_dict(data)



            return response_422_type_1

        response_422 = _parse_response_422(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BulkDestroyTeamsResponse | BulkDestroyTeamsResponse | ErrorsList | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkDestroyTeamsType0 | BulkDestroyTeamsType1,

) -> Response[BulkDestroyTeamsResponse | BulkDestroyTeamsResponse | ErrorsList | ErrorsList]:
    """ Bulk delete Teams

     Delete teams by external_id list, or prune by managed_by source. Two mutually exclusive modes.

    Args:
        body (BulkDestroyTeamsType0 | BulkDestroyTeamsType1): Two mutually exclusive modes. Pass
            exactly one of: external_ids (delete specific records) or managed_by (prune all managed
            records not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkDestroyTeamsResponse | BulkDestroyTeamsResponse | ErrorsList | ErrorsList]
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
    body: BulkDestroyTeamsType0 | BulkDestroyTeamsType1,

) -> BulkDestroyTeamsResponse | BulkDestroyTeamsResponse | ErrorsList | ErrorsList | None:
    """ Bulk delete Teams

     Delete teams by external_id list, or prune by managed_by source. Two mutually exclusive modes.

    Args:
        body (BulkDestroyTeamsType0 | BulkDestroyTeamsType1): Two mutually exclusive modes. Pass
            exactly one of: external_ids (delete specific records) or managed_by (prune all managed
            records not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkDestroyTeamsResponse | BulkDestroyTeamsResponse | ErrorsList | ErrorsList
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkDestroyTeamsType0 | BulkDestroyTeamsType1,

) -> Response[BulkDestroyTeamsResponse | BulkDestroyTeamsResponse | ErrorsList | ErrorsList]:
    """ Bulk delete Teams

     Delete teams by external_id list, or prune by managed_by source. Two mutually exclusive modes.

    Args:
        body (BulkDestroyTeamsType0 | BulkDestroyTeamsType1): Two mutually exclusive modes. Pass
            exactly one of: external_ids (delete specific records) or managed_by (prune all managed
            records not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkDestroyTeamsResponse | BulkDestroyTeamsResponse | ErrorsList | ErrorsList]
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
    body: BulkDestroyTeamsType0 | BulkDestroyTeamsType1,

) -> BulkDestroyTeamsResponse | BulkDestroyTeamsResponse | ErrorsList | ErrorsList | None:
    """ Bulk delete Teams

     Delete teams by external_id list, or prune by managed_by source. Two mutually exclusive modes.

    Args:
        body (BulkDestroyTeamsType0 | BulkDestroyTeamsType1): Two mutually exclusive modes. Pass
            exactly one of: external_ids (delete specific records) or managed_by (prune all managed
            records not in keep set).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkDestroyTeamsResponse | BulkDestroyTeamsResponse | ErrorsList | ErrorsList
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
