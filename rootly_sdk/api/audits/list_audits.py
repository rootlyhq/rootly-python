from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audits_list import AuditsList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filteruser_id: str | Unset = UNSET,
    filterapi_key_id: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filteritem_type: str | Unset = UNSET,
    filteruser_ideq: str | Unset = UNSET,
    filteruser_idnot_eq: str | Unset = UNSET,
    filteruser_idin: str | Unset = UNSET,
    filteruser_idnot_in: str | Unset = UNSET,
    filterapi_key_ideq: str | Unset = UNSET,
    filterapi_key_idnot_eq: str | Unset = UNSET,
    filterapi_key_idin: str | Unset = UNSET,
    filterapi_key_idnot_in: str | Unset = UNSET,
    filtersourceeq: str | Unset = UNSET,
    filtersourcenot_eq: str | Unset = UNSET,
    filtersourcein: str | Unset = UNSET,
    filtersourcenot_in: str | Unset = UNSET,
    filteritem_typeeq: str | Unset = UNSET,
    filteritem_typenot_eq: str | Unset = UNSET,
    filteritem_typein: str | Unset = UNSET,
    filteritem_typenot_in: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include"] = include

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[user_id]"] = filteruser_id

    params["filter[api_key_id]"] = filterapi_key_id

    params["filter[source]"] = filtersource

    params["filter[item_type]"] = filteritem_type

    params["filter[user_id][eq]"] = filteruser_ideq

    params["filter[user_id][not_eq]"] = filteruser_idnot_eq

    params["filter[user_id][in]"] = filteruser_idin

    params["filter[user_id][not_in]"] = filteruser_idnot_in

    params["filter[api_key_id][eq]"] = filterapi_key_ideq

    params["filter[api_key_id][not_eq]"] = filterapi_key_idnot_eq

    params["filter[api_key_id][in]"] = filterapi_key_idin

    params["filter[api_key_id][not_in]"] = filterapi_key_idnot_in

    params["filter[source][eq]"] = filtersourceeq

    params["filter[source][not_eq]"] = filtersourcenot_eq

    params["filter[source][in]"] = filtersourcein

    params["filter[source][not_in]"] = filtersourcenot_in

    params["filter[item_type][eq]"] = filteritem_typeeq

    params["filter[item_type][not_eq]"] = filteritem_typenot_eq

    params["filter[item_type][in]"] = filteritem_typein

    params["filter[item_type][not_in]"] = filteritem_typenot_in

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/audits",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AuditsList | None:
    if response.status_code == 200:
        response_200 = AuditsList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AuditsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filteruser_id: str | Unset = UNSET,
    filterapi_key_id: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filteritem_type: str | Unset = UNSET,
    filteruser_ideq: str | Unset = UNSET,
    filteruser_idnot_eq: str | Unset = UNSET,
    filteruser_idin: str | Unset = UNSET,
    filteruser_idnot_in: str | Unset = UNSET,
    filterapi_key_ideq: str | Unset = UNSET,
    filterapi_key_idnot_eq: str | Unset = UNSET,
    filterapi_key_idin: str | Unset = UNSET,
    filterapi_key_idnot_in: str | Unset = UNSET,
    filtersourceeq: str | Unset = UNSET,
    filtersourcenot_eq: str | Unset = UNSET,
    filtersourcein: str | Unset = UNSET,
    filtersourcenot_in: str | Unset = UNSET,
    filteritem_typeeq: str | Unset = UNSET,
    filteritem_typenot_eq: str | Unset = UNSET,
    filteritem_typein: str | Unset = UNSET,
    filteritem_typenot_in: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[AuditsList]:
    """List audits

     List audits

    Args:
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filteruser_id (str | Unset):
        filterapi_key_id (str | Unset):
        filtersource (str | Unset):
        filteritem_type (str | Unset):
        filteruser_ideq (str | Unset):
        filteruser_idnot_eq (str | Unset):
        filteruser_idin (str | Unset):
        filteruser_idnot_in (str | Unset):
        filterapi_key_ideq (str | Unset):
        filterapi_key_idnot_eq (str | Unset):
        filterapi_key_idin (str | Unset):
        filterapi_key_idnot_in (str | Unset):
        filtersourceeq (str | Unset):
        filtersourcenot_eq (str | Unset):
        filtersourcein (str | Unset):
        filtersourcenot_in (str | Unset):
        filteritem_typeeq (str | Unset):
        filteritem_typenot_eq (str | Unset):
        filteritem_typein (str | Unset):
        filteritem_typenot_in (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditsList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filteruser_id=filteruser_id,
        filterapi_key_id=filterapi_key_id,
        filtersource=filtersource,
        filteritem_type=filteritem_type,
        filteruser_ideq=filteruser_ideq,
        filteruser_idnot_eq=filteruser_idnot_eq,
        filteruser_idin=filteruser_idin,
        filteruser_idnot_in=filteruser_idnot_in,
        filterapi_key_ideq=filterapi_key_ideq,
        filterapi_key_idnot_eq=filterapi_key_idnot_eq,
        filterapi_key_idin=filterapi_key_idin,
        filterapi_key_idnot_in=filterapi_key_idnot_in,
        filtersourceeq=filtersourceeq,
        filtersourcenot_eq=filtersourcenot_eq,
        filtersourcein=filtersourcein,
        filtersourcenot_in=filtersourcenot_in,
        filteritem_typeeq=filteritem_typeeq,
        filteritem_typenot_eq=filteritem_typenot_eq,
        filteritem_typein=filteritem_typein,
        filteritem_typenot_in=filteritem_typenot_in,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filteruser_id: str | Unset = UNSET,
    filterapi_key_id: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filteritem_type: str | Unset = UNSET,
    filteruser_ideq: str | Unset = UNSET,
    filteruser_idnot_eq: str | Unset = UNSET,
    filteruser_idin: str | Unset = UNSET,
    filteruser_idnot_in: str | Unset = UNSET,
    filterapi_key_ideq: str | Unset = UNSET,
    filterapi_key_idnot_eq: str | Unset = UNSET,
    filterapi_key_idin: str | Unset = UNSET,
    filterapi_key_idnot_in: str | Unset = UNSET,
    filtersourceeq: str | Unset = UNSET,
    filtersourcenot_eq: str | Unset = UNSET,
    filtersourcein: str | Unset = UNSET,
    filtersourcenot_in: str | Unset = UNSET,
    filteritem_typeeq: str | Unset = UNSET,
    filteritem_typenot_eq: str | Unset = UNSET,
    filteritem_typein: str | Unset = UNSET,
    filteritem_typenot_in: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> AuditsList | None:
    """List audits

     List audits

    Args:
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filteruser_id (str | Unset):
        filterapi_key_id (str | Unset):
        filtersource (str | Unset):
        filteritem_type (str | Unset):
        filteruser_ideq (str | Unset):
        filteruser_idnot_eq (str | Unset):
        filteruser_idin (str | Unset):
        filteruser_idnot_in (str | Unset):
        filterapi_key_ideq (str | Unset):
        filterapi_key_idnot_eq (str | Unset):
        filterapi_key_idin (str | Unset):
        filterapi_key_idnot_in (str | Unset):
        filtersourceeq (str | Unset):
        filtersourcenot_eq (str | Unset):
        filtersourcein (str | Unset):
        filtersourcenot_in (str | Unset):
        filteritem_typeeq (str | Unset):
        filteritem_typenot_eq (str | Unset):
        filteritem_typein (str | Unset):
        filteritem_typenot_in (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditsList
    """

    return sync_detailed(
        client=client,
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filteruser_id=filteruser_id,
        filterapi_key_id=filterapi_key_id,
        filtersource=filtersource,
        filteritem_type=filteritem_type,
        filteruser_ideq=filteruser_ideq,
        filteruser_idnot_eq=filteruser_idnot_eq,
        filteruser_idin=filteruser_idin,
        filteruser_idnot_in=filteruser_idnot_in,
        filterapi_key_ideq=filterapi_key_ideq,
        filterapi_key_idnot_eq=filterapi_key_idnot_eq,
        filterapi_key_idin=filterapi_key_idin,
        filterapi_key_idnot_in=filterapi_key_idnot_in,
        filtersourceeq=filtersourceeq,
        filtersourcenot_eq=filtersourcenot_eq,
        filtersourcein=filtersourcein,
        filtersourcenot_in=filtersourcenot_in,
        filteritem_typeeq=filteritem_typeeq,
        filteritem_typenot_eq=filteritem_typenot_eq,
        filteritem_typein=filteritem_typein,
        filteritem_typenot_in=filteritem_typenot_in,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filteruser_id: str | Unset = UNSET,
    filterapi_key_id: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filteritem_type: str | Unset = UNSET,
    filteruser_ideq: str | Unset = UNSET,
    filteruser_idnot_eq: str | Unset = UNSET,
    filteruser_idin: str | Unset = UNSET,
    filteruser_idnot_in: str | Unset = UNSET,
    filterapi_key_ideq: str | Unset = UNSET,
    filterapi_key_idnot_eq: str | Unset = UNSET,
    filterapi_key_idin: str | Unset = UNSET,
    filterapi_key_idnot_in: str | Unset = UNSET,
    filtersourceeq: str | Unset = UNSET,
    filtersourcenot_eq: str | Unset = UNSET,
    filtersourcein: str | Unset = UNSET,
    filtersourcenot_in: str | Unset = UNSET,
    filteritem_typeeq: str | Unset = UNSET,
    filteritem_typenot_eq: str | Unset = UNSET,
    filteritem_typein: str | Unset = UNSET,
    filteritem_typenot_in: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[AuditsList]:
    """List audits

     List audits

    Args:
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filteruser_id (str | Unset):
        filterapi_key_id (str | Unset):
        filtersource (str | Unset):
        filteritem_type (str | Unset):
        filteruser_ideq (str | Unset):
        filteruser_idnot_eq (str | Unset):
        filteruser_idin (str | Unset):
        filteruser_idnot_in (str | Unset):
        filterapi_key_ideq (str | Unset):
        filterapi_key_idnot_eq (str | Unset):
        filterapi_key_idin (str | Unset):
        filterapi_key_idnot_in (str | Unset):
        filtersourceeq (str | Unset):
        filtersourcenot_eq (str | Unset):
        filtersourcein (str | Unset):
        filtersourcenot_in (str | Unset):
        filteritem_typeeq (str | Unset):
        filteritem_typenot_eq (str | Unset):
        filteritem_typein (str | Unset):
        filteritem_typenot_in (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditsList]
    """

    kwargs = _get_kwargs(
        include=include,
        pagenumber=pagenumber,
        pagesize=pagesize,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filteruser_id=filteruser_id,
        filterapi_key_id=filterapi_key_id,
        filtersource=filtersource,
        filteritem_type=filteritem_type,
        filteruser_ideq=filteruser_ideq,
        filteruser_idnot_eq=filteruser_idnot_eq,
        filteruser_idin=filteruser_idin,
        filteruser_idnot_in=filteruser_idnot_in,
        filterapi_key_ideq=filterapi_key_ideq,
        filterapi_key_idnot_eq=filterapi_key_idnot_eq,
        filterapi_key_idin=filterapi_key_idin,
        filterapi_key_idnot_in=filterapi_key_idnot_in,
        filtersourceeq=filtersourceeq,
        filtersourcenot_eq=filtersourcenot_eq,
        filtersourcein=filtersourcein,
        filtersourcenot_in=filtersourcenot_in,
        filteritem_typeeq=filteritem_typeeq,
        filteritem_typenot_eq=filteritem_typenot_eq,
        filteritem_typein=filteritem_typein,
        filteritem_typenot_in=filteritem_typenot_in,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filteruser_id: str | Unset = UNSET,
    filterapi_key_id: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filteritem_type: str | Unset = UNSET,
    filteruser_ideq: str | Unset = UNSET,
    filteruser_idnot_eq: str | Unset = UNSET,
    filteruser_idin: str | Unset = UNSET,
    filteruser_idnot_in: str | Unset = UNSET,
    filterapi_key_ideq: str | Unset = UNSET,
    filterapi_key_idnot_eq: str | Unset = UNSET,
    filterapi_key_idin: str | Unset = UNSET,
    filterapi_key_idnot_in: str | Unset = UNSET,
    filtersourceeq: str | Unset = UNSET,
    filtersourcenot_eq: str | Unset = UNSET,
    filtersourcein: str | Unset = UNSET,
    filtersourcenot_in: str | Unset = UNSET,
    filteritem_typeeq: str | Unset = UNSET,
    filteritem_typenot_eq: str | Unset = UNSET,
    filteritem_typein: str | Unset = UNSET,
    filteritem_typenot_in: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> AuditsList | None:
    """List audits

     List audits

    Args:
        include (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filteruser_id (str | Unset):
        filterapi_key_id (str | Unset):
        filtersource (str | Unset):
        filteritem_type (str | Unset):
        filteruser_ideq (str | Unset):
        filteruser_idnot_eq (str | Unset):
        filteruser_idin (str | Unset):
        filteruser_idnot_in (str | Unset):
        filterapi_key_ideq (str | Unset):
        filterapi_key_idnot_eq (str | Unset):
        filterapi_key_idin (str | Unset):
        filterapi_key_idnot_in (str | Unset):
        filtersourceeq (str | Unset):
        filtersourcenot_eq (str | Unset):
        filtersourcein (str | Unset):
        filtersourcenot_in (str | Unset):
        filteritem_typeeq (str | Unset):
        filteritem_typenot_eq (str | Unset):
        filteritem_typein (str | Unset):
        filteritem_typenot_in (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditsList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            pagenumber=pagenumber,
            pagesize=pagesize,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filteruser_id=filteruser_id,
            filterapi_key_id=filterapi_key_id,
            filtersource=filtersource,
            filteritem_type=filteritem_type,
            filteruser_ideq=filteruser_ideq,
            filteruser_idnot_eq=filteruser_idnot_eq,
            filteruser_idin=filteruser_idin,
            filteruser_idnot_in=filteruser_idnot_in,
            filterapi_key_ideq=filterapi_key_ideq,
            filterapi_key_idnot_eq=filterapi_key_idnot_eq,
            filterapi_key_idin=filterapi_key_idin,
            filterapi_key_idnot_in=filterapi_key_idnot_in,
            filtersourceeq=filtersourceeq,
            filtersourcenot_eq=filtersourcenot_eq,
            filtersourcein=filtersourcein,
            filtersourcenot_in=filtersourcenot_in,
            filteritem_typeeq=filteritem_typeeq,
            filteritem_typenot_eq=filteritem_typenot_eq,
            filteritem_typein=filteritem_typein,
            filteritem_typenot_in=filteritem_typenot_in,
            sort=sort,
        )
    ).parsed
