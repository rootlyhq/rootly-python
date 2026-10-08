from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pulse_list import PulseList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filterrefs: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterended_atgt: str | Unset = UNSET,
    filterended_atgte: str | Unset = UNSET,
    filterended_atlt: str | Unset = UNSET,
    filterended_atlte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filtersourceeq: str | Unset = UNSET,
    filtersourcenot_eq: str | Unset = UNSET,
    filtersourcein: str | Unset = UNSET,
    filtersourcenot_in: str | Unset = UNSET,
    filterserviceseq: str | Unset = UNSET,
    filterservicesnot_eq: str | Unset = UNSET,
    filterservicesin: str | Unset = UNSET,
    filterservicesnot_in: str | Unset = UNSET,
    filterenvironmentseq: str | Unset = UNSET,
    filterenvironmentsnot_eq: str | Unset = UNSET,
    filterenvironmentsin: str | Unset = UNSET,
    filterenvironmentsnot_in: str | Unset = UNSET,
    filterlabelseq: str | Unset = UNSET,
    filterlabelsnot_eq: str | Unset = UNSET,
    filterlabelsin: str | Unset = UNSET,
    filterlabelsnot_in: str | Unset = UNSET,
    filterrefseq: str | Unset = UNSET,
    filterrefsnot_eq: str | Unset = UNSET,
    filterrefsin: str | Unset = UNSET,
    filterrefsnot_in: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include"] = include

    params["filter[source]"] = filtersource

    params["filter[services]"] = filterservices

    params["filter[environments]"] = filterenvironments

    params["filter[labels]"] = filterlabels

    params["filter[refs]"] = filterrefs

    params["filter[started_at][gt]"] = filterstarted_atgt

    params["filter[started_at][gte]"] = filterstarted_atgte

    params["filter[started_at][lt]"] = filterstarted_atlt

    params["filter[started_at][lte]"] = filterstarted_atlte

    params["filter[ended_at][gt]"] = filterended_atgt

    params["filter[ended_at][gte]"] = filterended_atgte

    params["filter[ended_at][lt]"] = filterended_atlt

    params["filter[ended_at][lte]"] = filterended_atlte

    params["filter[created_at][gt]"] = filtercreated_atgt

    params["filter[created_at][gte]"] = filtercreated_atgte

    params["filter[created_at][lt]"] = filtercreated_atlt

    params["filter[created_at][lte]"] = filtercreated_atlte

    params["filter[source][eq]"] = filtersourceeq

    params["filter[source][not_eq]"] = filtersourcenot_eq

    params["filter[source][in]"] = filtersourcein

    params["filter[source][not_in]"] = filtersourcenot_in

    params["filter[services][eq]"] = filterserviceseq

    params["filter[services][not_eq]"] = filterservicesnot_eq

    params["filter[services][in]"] = filterservicesin

    params["filter[services][not_in]"] = filterservicesnot_in

    params["filter[environments][eq]"] = filterenvironmentseq

    params["filter[environments][not_eq]"] = filterenvironmentsnot_eq

    params["filter[environments][in]"] = filterenvironmentsin

    params["filter[environments][not_in]"] = filterenvironmentsnot_in

    params["filter[labels][eq]"] = filterlabelseq

    params["filter[labels][not_eq]"] = filterlabelsnot_eq

    params["filter[labels][in]"] = filterlabelsin

    params["filter[labels][not_in]"] = filterlabelsnot_in

    params["filter[refs][eq]"] = filterrefseq

    params["filter[refs][not_eq]"] = filterrefsnot_eq

    params["filter[refs][in]"] = filterrefsin

    params["filter[refs][not_in]"] = filterrefsnot_in

    params["page[number]"] = pagenumber

    params["page[size]"] = pagesize

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/pulses",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PulseList | None:
    if response.status_code == 200:
        response_200 = PulseList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PulseList]:
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
    filtersource: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filterrefs: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterended_atgt: str | Unset = UNSET,
    filterended_atgte: str | Unset = UNSET,
    filterended_atlt: str | Unset = UNSET,
    filterended_atlte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filtersourceeq: str | Unset = UNSET,
    filtersourcenot_eq: str | Unset = UNSET,
    filtersourcein: str | Unset = UNSET,
    filtersourcenot_in: str | Unset = UNSET,
    filterserviceseq: str | Unset = UNSET,
    filterservicesnot_eq: str | Unset = UNSET,
    filterservicesin: str | Unset = UNSET,
    filterservicesnot_in: str | Unset = UNSET,
    filterenvironmentseq: str | Unset = UNSET,
    filterenvironmentsnot_eq: str | Unset = UNSET,
    filterenvironmentsin: str | Unset = UNSET,
    filterenvironmentsnot_in: str | Unset = UNSET,
    filterlabelseq: str | Unset = UNSET,
    filterlabelsnot_eq: str | Unset = UNSET,
    filterlabelsin: str | Unset = UNSET,
    filterlabelsnot_in: str | Unset = UNSET,
    filterrefseq: str | Unset = UNSET,
    filterrefsnot_eq: str | Unset = UNSET,
    filterrefsin: str | Unset = UNSET,
    filterrefsnot_in: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[PulseList]:
    """List pulses

     List pulses

    Args:
        include (str | Unset):
        filtersource (str | Unset):
        filterservices (str | Unset):
        filterenvironments (str | Unset):
        filterlabels (str | Unset):
        filterrefs (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterended_atgt (str | Unset):
        filterended_atgte (str | Unset):
        filterended_atlt (str | Unset):
        filterended_atlte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filtersourceeq (str | Unset):
        filtersourcenot_eq (str | Unset):
        filtersourcein (str | Unset):
        filtersourcenot_in (str | Unset):
        filterserviceseq (str | Unset):
        filterservicesnot_eq (str | Unset):
        filterservicesin (str | Unset):
        filterservicesnot_in (str | Unset):
        filterenvironmentseq (str | Unset):
        filterenvironmentsnot_eq (str | Unset):
        filterenvironmentsin (str | Unset):
        filterenvironmentsnot_in (str | Unset):
        filterlabelseq (str | Unset):
        filterlabelsnot_eq (str | Unset):
        filterlabelsin (str | Unset):
        filterlabelsnot_in (str | Unset):
        filterrefseq (str | Unset):
        filterrefsnot_eq (str | Unset):
        filterrefsin (str | Unset):
        filterrefsnot_in (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PulseList]
    """

    kwargs = _get_kwargs(
        include=include,
        filtersource=filtersource,
        filterservices=filterservices,
        filterenvironments=filterenvironments,
        filterlabels=filterlabels,
        filterrefs=filterrefs,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterended_atgt=filterended_atgt,
        filterended_atgte=filterended_atgte,
        filterended_atlt=filterended_atlt,
        filterended_atlte=filterended_atlte,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filtersourceeq=filtersourceeq,
        filtersourcenot_eq=filtersourcenot_eq,
        filtersourcein=filtersourcein,
        filtersourcenot_in=filtersourcenot_in,
        filterserviceseq=filterserviceseq,
        filterservicesnot_eq=filterservicesnot_eq,
        filterservicesin=filterservicesin,
        filterservicesnot_in=filterservicesnot_in,
        filterenvironmentseq=filterenvironmentseq,
        filterenvironmentsnot_eq=filterenvironmentsnot_eq,
        filterenvironmentsin=filterenvironmentsin,
        filterenvironmentsnot_in=filterenvironmentsnot_in,
        filterlabelseq=filterlabelseq,
        filterlabelsnot_eq=filterlabelsnot_eq,
        filterlabelsin=filterlabelsin,
        filterlabelsnot_in=filterlabelsnot_in,
        filterrefseq=filterrefseq,
        filterrefsnot_eq=filterrefsnot_eq,
        filterrefsin=filterrefsin,
        filterrefsnot_in=filterrefsnot_in,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filterrefs: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterended_atgt: str | Unset = UNSET,
    filterended_atgte: str | Unset = UNSET,
    filterended_atlt: str | Unset = UNSET,
    filterended_atlte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filtersourceeq: str | Unset = UNSET,
    filtersourcenot_eq: str | Unset = UNSET,
    filtersourcein: str | Unset = UNSET,
    filtersourcenot_in: str | Unset = UNSET,
    filterserviceseq: str | Unset = UNSET,
    filterservicesnot_eq: str | Unset = UNSET,
    filterservicesin: str | Unset = UNSET,
    filterservicesnot_in: str | Unset = UNSET,
    filterenvironmentseq: str | Unset = UNSET,
    filterenvironmentsnot_eq: str | Unset = UNSET,
    filterenvironmentsin: str | Unset = UNSET,
    filterenvironmentsnot_in: str | Unset = UNSET,
    filterlabelseq: str | Unset = UNSET,
    filterlabelsnot_eq: str | Unset = UNSET,
    filterlabelsin: str | Unset = UNSET,
    filterlabelsnot_in: str | Unset = UNSET,
    filterrefseq: str | Unset = UNSET,
    filterrefsnot_eq: str | Unset = UNSET,
    filterrefsin: str | Unset = UNSET,
    filterrefsnot_in: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> PulseList | None:
    """List pulses

     List pulses

    Args:
        include (str | Unset):
        filtersource (str | Unset):
        filterservices (str | Unset):
        filterenvironments (str | Unset):
        filterlabels (str | Unset):
        filterrefs (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterended_atgt (str | Unset):
        filterended_atgte (str | Unset):
        filterended_atlt (str | Unset):
        filterended_atlte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filtersourceeq (str | Unset):
        filtersourcenot_eq (str | Unset):
        filtersourcein (str | Unset):
        filtersourcenot_in (str | Unset):
        filterserviceseq (str | Unset):
        filterservicesnot_eq (str | Unset):
        filterservicesin (str | Unset):
        filterservicesnot_in (str | Unset):
        filterenvironmentseq (str | Unset):
        filterenvironmentsnot_eq (str | Unset):
        filterenvironmentsin (str | Unset):
        filterenvironmentsnot_in (str | Unset):
        filterlabelseq (str | Unset):
        filterlabelsnot_eq (str | Unset):
        filterlabelsin (str | Unset):
        filterlabelsnot_in (str | Unset):
        filterrefseq (str | Unset):
        filterrefsnot_eq (str | Unset):
        filterrefsin (str | Unset):
        filterrefsnot_in (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PulseList
    """

    return sync_detailed(
        client=client,
        include=include,
        filtersource=filtersource,
        filterservices=filterservices,
        filterenvironments=filterenvironments,
        filterlabels=filterlabels,
        filterrefs=filterrefs,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterended_atgt=filterended_atgt,
        filterended_atgte=filterended_atgte,
        filterended_atlt=filterended_atlt,
        filterended_atlte=filterended_atlte,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filtersourceeq=filtersourceeq,
        filtersourcenot_eq=filtersourcenot_eq,
        filtersourcein=filtersourcein,
        filtersourcenot_in=filtersourcenot_in,
        filterserviceseq=filterserviceseq,
        filterservicesnot_eq=filterservicesnot_eq,
        filterservicesin=filterservicesin,
        filterservicesnot_in=filterservicesnot_in,
        filterenvironmentseq=filterenvironmentseq,
        filterenvironmentsnot_eq=filterenvironmentsnot_eq,
        filterenvironmentsin=filterenvironmentsin,
        filterenvironmentsnot_in=filterenvironmentsnot_in,
        filterlabelseq=filterlabelseq,
        filterlabelsnot_eq=filterlabelsnot_eq,
        filterlabelsin=filterlabelsin,
        filterlabelsnot_in=filterlabelsnot_in,
        filterrefseq=filterrefseq,
        filterrefsnot_eq=filterrefsnot_eq,
        filterrefsin=filterrefsin,
        filterrefsnot_in=filterrefsnot_in,
        pagenumber=pagenumber,
        pagesize=pagesize,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filterrefs: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterended_atgt: str | Unset = UNSET,
    filterended_atgte: str | Unset = UNSET,
    filterended_atlt: str | Unset = UNSET,
    filterended_atlte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filtersourceeq: str | Unset = UNSET,
    filtersourcenot_eq: str | Unset = UNSET,
    filtersourcein: str | Unset = UNSET,
    filtersourcenot_in: str | Unset = UNSET,
    filterserviceseq: str | Unset = UNSET,
    filterservicesnot_eq: str | Unset = UNSET,
    filterservicesin: str | Unset = UNSET,
    filterservicesnot_in: str | Unset = UNSET,
    filterenvironmentseq: str | Unset = UNSET,
    filterenvironmentsnot_eq: str | Unset = UNSET,
    filterenvironmentsin: str | Unset = UNSET,
    filterenvironmentsnot_in: str | Unset = UNSET,
    filterlabelseq: str | Unset = UNSET,
    filterlabelsnot_eq: str | Unset = UNSET,
    filterlabelsin: str | Unset = UNSET,
    filterlabelsnot_in: str | Unset = UNSET,
    filterrefseq: str | Unset = UNSET,
    filterrefsnot_eq: str | Unset = UNSET,
    filterrefsin: str | Unset = UNSET,
    filterrefsnot_in: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> Response[PulseList]:
    """List pulses

     List pulses

    Args:
        include (str | Unset):
        filtersource (str | Unset):
        filterservices (str | Unset):
        filterenvironments (str | Unset):
        filterlabels (str | Unset):
        filterrefs (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterended_atgt (str | Unset):
        filterended_atgte (str | Unset):
        filterended_atlt (str | Unset):
        filterended_atlte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filtersourceeq (str | Unset):
        filtersourcenot_eq (str | Unset):
        filtersourcein (str | Unset):
        filtersourcenot_in (str | Unset):
        filterserviceseq (str | Unset):
        filterservicesnot_eq (str | Unset):
        filterservicesin (str | Unset):
        filterservicesnot_in (str | Unset):
        filterenvironmentseq (str | Unset):
        filterenvironmentsnot_eq (str | Unset):
        filterenvironmentsin (str | Unset):
        filterenvironmentsnot_in (str | Unset):
        filterlabelseq (str | Unset):
        filterlabelsnot_eq (str | Unset):
        filterlabelsin (str | Unset):
        filterlabelsnot_in (str | Unset):
        filterrefseq (str | Unset):
        filterrefsnot_eq (str | Unset):
        filterrefsin (str | Unset):
        filterrefsnot_in (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PulseList]
    """

    kwargs = _get_kwargs(
        include=include,
        filtersource=filtersource,
        filterservices=filterservices,
        filterenvironments=filterenvironments,
        filterlabels=filterlabels,
        filterrefs=filterrefs,
        filterstarted_atgt=filterstarted_atgt,
        filterstarted_atgte=filterstarted_atgte,
        filterstarted_atlt=filterstarted_atlt,
        filterstarted_atlte=filterstarted_atlte,
        filterended_atgt=filterended_atgt,
        filterended_atgte=filterended_atgte,
        filterended_atlt=filterended_atlt,
        filterended_atlte=filterended_atlte,
        filtercreated_atgt=filtercreated_atgt,
        filtercreated_atgte=filtercreated_atgte,
        filtercreated_atlt=filtercreated_atlt,
        filtercreated_atlte=filtercreated_atlte,
        filtersourceeq=filtersourceeq,
        filtersourcenot_eq=filtersourcenot_eq,
        filtersourcein=filtersourcein,
        filtersourcenot_in=filtersourcenot_in,
        filterserviceseq=filterserviceseq,
        filterservicesnot_eq=filterservicesnot_eq,
        filterservicesin=filterservicesin,
        filterservicesnot_in=filterservicesnot_in,
        filterenvironmentseq=filterenvironmentseq,
        filterenvironmentsnot_eq=filterenvironmentsnot_eq,
        filterenvironmentsin=filterenvironmentsin,
        filterenvironmentsnot_in=filterenvironmentsnot_in,
        filterlabelseq=filterlabelseq,
        filterlabelsnot_eq=filterlabelsnot_eq,
        filterlabelsin=filterlabelsin,
        filterlabelsnot_in=filterlabelsnot_in,
        filterrefseq=filterrefseq,
        filterrefsnot_eq=filterrefsnot_eq,
        filterrefsin=filterrefsin,
        filterrefsnot_in=filterrefsnot_in,
        pagenumber=pagenumber,
        pagesize=pagesize,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    include: str | Unset = UNSET,
    filtersource: str | Unset = UNSET,
    filterservices: str | Unset = UNSET,
    filterenvironments: str | Unset = UNSET,
    filterlabels: str | Unset = UNSET,
    filterrefs: str | Unset = UNSET,
    filterstarted_atgt: str | Unset = UNSET,
    filterstarted_atgte: str | Unset = UNSET,
    filterstarted_atlt: str | Unset = UNSET,
    filterstarted_atlte: str | Unset = UNSET,
    filterended_atgt: str | Unset = UNSET,
    filterended_atgte: str | Unset = UNSET,
    filterended_atlt: str | Unset = UNSET,
    filterended_atlte: str | Unset = UNSET,
    filtercreated_atgt: str | Unset = UNSET,
    filtercreated_atgte: str | Unset = UNSET,
    filtercreated_atlt: str | Unset = UNSET,
    filtercreated_atlte: str | Unset = UNSET,
    filtersourceeq: str | Unset = UNSET,
    filtersourcenot_eq: str | Unset = UNSET,
    filtersourcein: str | Unset = UNSET,
    filtersourcenot_in: str | Unset = UNSET,
    filterserviceseq: str | Unset = UNSET,
    filterservicesnot_eq: str | Unset = UNSET,
    filterservicesin: str | Unset = UNSET,
    filterservicesnot_in: str | Unset = UNSET,
    filterenvironmentseq: str | Unset = UNSET,
    filterenvironmentsnot_eq: str | Unset = UNSET,
    filterenvironmentsin: str | Unset = UNSET,
    filterenvironmentsnot_in: str | Unset = UNSET,
    filterlabelseq: str | Unset = UNSET,
    filterlabelsnot_eq: str | Unset = UNSET,
    filterlabelsin: str | Unset = UNSET,
    filterlabelsnot_in: str | Unset = UNSET,
    filterrefseq: str | Unset = UNSET,
    filterrefsnot_eq: str | Unset = UNSET,
    filterrefsin: str | Unset = UNSET,
    filterrefsnot_in: str | Unset = UNSET,
    pagenumber: int | Unset = UNSET,
    pagesize: int | Unset = UNSET,
) -> PulseList | None:
    """List pulses

     List pulses

    Args:
        include (str | Unset):
        filtersource (str | Unset):
        filterservices (str | Unset):
        filterenvironments (str | Unset):
        filterlabels (str | Unset):
        filterrefs (str | Unset):
        filterstarted_atgt (str | Unset):
        filterstarted_atgte (str | Unset):
        filterstarted_atlt (str | Unset):
        filterstarted_atlte (str | Unset):
        filterended_atgt (str | Unset):
        filterended_atgte (str | Unset):
        filterended_atlt (str | Unset):
        filterended_atlte (str | Unset):
        filtercreated_atgt (str | Unset):
        filtercreated_atgte (str | Unset):
        filtercreated_atlt (str | Unset):
        filtercreated_atlte (str | Unset):
        filtersourceeq (str | Unset):
        filtersourcenot_eq (str | Unset):
        filtersourcein (str | Unset):
        filtersourcenot_in (str | Unset):
        filterserviceseq (str | Unset):
        filterservicesnot_eq (str | Unset):
        filterservicesin (str | Unset):
        filterservicesnot_in (str | Unset):
        filterenvironmentseq (str | Unset):
        filterenvironmentsnot_eq (str | Unset):
        filterenvironmentsin (str | Unset):
        filterenvironmentsnot_in (str | Unset):
        filterlabelseq (str | Unset):
        filterlabelsnot_eq (str | Unset):
        filterlabelsin (str | Unset):
        filterlabelsnot_in (str | Unset):
        filterrefseq (str | Unset):
        filterrefsnot_eq (str | Unset):
        filterrefsin (str | Unset):
        filterrefsnot_in (str | Unset):
        pagenumber (int | Unset):
        pagesize (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PulseList
    """

    return (
        await asyncio_detailed(
            client=client,
            include=include,
            filtersource=filtersource,
            filterservices=filterservices,
            filterenvironments=filterenvironments,
            filterlabels=filterlabels,
            filterrefs=filterrefs,
            filterstarted_atgt=filterstarted_atgt,
            filterstarted_atgte=filterstarted_atgte,
            filterstarted_atlt=filterstarted_atlt,
            filterstarted_atlte=filterstarted_atlte,
            filterended_atgt=filterended_atgt,
            filterended_atgte=filterended_atgte,
            filterended_atlt=filterended_atlt,
            filterended_atlte=filterended_atlte,
            filtercreated_atgt=filtercreated_atgt,
            filtercreated_atgte=filtercreated_atgte,
            filtercreated_atlt=filtercreated_atlt,
            filtercreated_atlte=filtercreated_atlte,
            filtersourceeq=filtersourceeq,
            filtersourcenot_eq=filtersourcenot_eq,
            filtersourcein=filtersourcein,
            filtersourcenot_in=filtersourcenot_in,
            filterserviceseq=filterserviceseq,
            filterservicesnot_eq=filterservicesnot_eq,
            filterservicesin=filterservicesin,
            filterservicesnot_in=filterservicesnot_in,
            filterenvironmentseq=filterenvironmentseq,
            filterenvironmentsnot_eq=filterenvironmentsnot_eq,
            filterenvironmentsin=filterenvironmentsin,
            filterenvironmentsnot_in=filterenvironmentsnot_in,
            filterlabelseq=filterlabelseq,
            filterlabelsnot_eq=filterlabelsnot_eq,
            filterlabelsin=filterlabelsin,
            filterlabelsnot_in=filterlabelsnot_in,
            filterrefseq=filterrefseq,
            filterrefsnot_eq=filterrefsnot_eq,
            filterrefsin=filterrefsin,
            filterrefsnot_in=filterrefsnot_in,
            pagenumber=pagenumber,
            pagesize=pagesize,
        )
    ).parsed
