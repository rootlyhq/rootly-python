from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_permission_set_boolean_list import IncidentPermissionSetBooleanList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    incident_permission_set_id: str,
    *,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[kind]"] = filterkind

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/incident_permission_sets/{incident_permission_set_id}/booleans".format(
            incident_permission_set_id=quote(str(incident_permission_set_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IncidentPermissionSetBooleanList | None:
    if response.status_code == 200:
        response_200 = IncidentPermissionSetBooleanList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IncidentPermissionSetBooleanList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    incident_permission_set_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[IncidentPermissionSetBooleanList]:
    """List incident_permission_set_booleans

     List incident_permission_set_booleans

    Args:
        incident_permission_set_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterkind (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentPermissionSetBooleanList]
    """

    kwargs = _get_kwargs(
        incident_permission_set_id=incident_permission_set_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterkind=filterkind,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_permission_set_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> IncidentPermissionSetBooleanList | None:
    """List incident_permission_set_booleans

     List incident_permission_set_booleans

    Args:
        incident_permission_set_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterkind (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentPermissionSetBooleanList
    """

    return sync_detailed(
        incident_permission_set_id=incident_permission_set_id,
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterkind=filterkind,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    incident_permission_set_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[IncidentPermissionSetBooleanList]:
    """List incident_permission_set_booleans

     List incident_permission_set_booleans

    Args:
        incident_permission_set_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterkind (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentPermissionSetBooleanList]
    """

    kwargs = _get_kwargs(
        incident_permission_set_id=incident_permission_set_id,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filterkind=filterkind,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_permission_set_id: str,
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filterkind: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> IncidentPermissionSetBooleanList | None:
    """List incident_permission_set_booleans

     List incident_permission_set_booleans

    Args:
        incident_permission_set_id (str):
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filterkind (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentPermissionSetBooleanList
    """

    return (
        await asyncio_detailed(
            incident_permission_set_id=incident_permission_set_id,
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filterkind=filterkind,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            sort=sort,
        )
    ).parsed
