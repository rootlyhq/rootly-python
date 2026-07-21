from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulk_upsert_functionalities import BulkUpsertFunctionalities
from ...models.bulk_upsert_functionalities_error import BulkUpsertFunctionalitiesError
from ...models.bulk_upsert_functionalities_response import BulkUpsertFunctionalitiesResponse
from ...models.errors_list import ErrorsList
from typing import cast



def _get_kwargs(
    *,
    body: BulkUpsertFunctionalities,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/functionalities/bulk_upsert",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/vnd.api+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BulkUpsertFunctionalitiesError | ErrorsList | BulkUpsertFunctionalitiesResponse | ErrorsList | None:
    if response.status_code == 200:
        response_200 = BulkUpsertFunctionalitiesResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ErrorsList.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        def _parse_response_422(data: object) -> BulkUpsertFunctionalitiesError | ErrorsList:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = ErrorsList.from_dict(data)



                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_1 = BulkUpsertFunctionalitiesError.from_dict(data)



            return response_422_type_1

        response_422 = _parse_response_422(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BulkUpsertFunctionalitiesError | ErrorsList | BulkUpsertFunctionalitiesResponse | ErrorsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkUpsertFunctionalities,

) -> Response[BulkUpsertFunctionalitiesError | ErrorsList | BulkUpsertFunctionalitiesResponse | ErrorsList]:
    """ Bulk upsert Functionalities

     Create or update multiple functionalities by external_id. Only attributes present in the payload are
    written (managed-fields semantics). Transactional: all succeed or all fail. Requires an API key with
    both create and update capability across the resource scope (team/org-scoped); record-scoped
    principals cannot use this endpoint (they receive 404), which also prevents the create-vs-update
    branch from leaking whether an external_id exists.

    Args:
        body (BulkUpsertFunctionalities):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkUpsertFunctionalitiesError | ErrorsList | BulkUpsertFunctionalitiesResponse | ErrorsList]
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
    body: BulkUpsertFunctionalities,

) -> BulkUpsertFunctionalitiesError | ErrorsList | BulkUpsertFunctionalitiesResponse | ErrorsList | None:
    """ Bulk upsert Functionalities

     Create or update multiple functionalities by external_id. Only attributes present in the payload are
    written (managed-fields semantics). Transactional: all succeed or all fail. Requires an API key with
    both create and update capability across the resource scope (team/org-scoped); record-scoped
    principals cannot use this endpoint (they receive 404), which also prevents the create-vs-update
    branch from leaking whether an external_id exists.

    Args:
        body (BulkUpsertFunctionalities):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkUpsertFunctionalitiesError | ErrorsList | BulkUpsertFunctionalitiesResponse | ErrorsList
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkUpsertFunctionalities,

) -> Response[BulkUpsertFunctionalitiesError | ErrorsList | BulkUpsertFunctionalitiesResponse | ErrorsList]:
    """ Bulk upsert Functionalities

     Create or update multiple functionalities by external_id. Only attributes present in the payload are
    written (managed-fields semantics). Transactional: all succeed or all fail. Requires an API key with
    both create and update capability across the resource scope (team/org-scoped); record-scoped
    principals cannot use this endpoint (they receive 404), which also prevents the create-vs-update
    branch from leaking whether an external_id exists.

    Args:
        body (BulkUpsertFunctionalities):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkUpsertFunctionalitiesError | ErrorsList | BulkUpsertFunctionalitiesResponse | ErrorsList]
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
    body: BulkUpsertFunctionalities,

) -> BulkUpsertFunctionalitiesError | ErrorsList | BulkUpsertFunctionalitiesResponse | ErrorsList | None:
    """ Bulk upsert Functionalities

     Create or update multiple functionalities by external_id. Only attributes present in the payload are
    written (managed-fields semantics). Transactional: all succeed or all fail. Requires an API key with
    both create and update capability across the resource scope (team/org-scoped); record-scoped
    principals cannot use this endpoint (they receive 404), which also prevents the create-vs-update
    branch from leaking whether an external_id exists.

    Args:
        body (BulkUpsertFunctionalities):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkUpsertFunctionalitiesError | ErrorsList | BulkUpsertFunctionalitiesResponse | ErrorsList
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
