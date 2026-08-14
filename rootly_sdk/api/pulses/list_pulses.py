from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pulse_list import PulseList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include: Union[Unset, str] = UNSET,
    filtersource: Union[Unset, str] = UNSET,
    filterservices: Union[Unset, str] = UNSET,
    filterenvironments: Union[Unset, str] = UNSET,
    filterlabels: Union[Unset, str] = UNSET,
    filterrefs: Union[Unset, str] = UNSET,
    filterstarted_atgt: Union[Unset, str] = UNSET,
    filterstarted_atgte: Union[Unset, str] = UNSET,
    filterstarted_atlt: Union[Unset, str] = UNSET,
    filterstarted_atlte: Union[Unset, str] = UNSET,
    filterended_atgt: Union[Unset, str] = UNSET,
    filterended_atgte: Union[Unset, str] = UNSET,
    filterended_atlt: Union[Unset, str] = UNSET,
    filterended_atlte: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filtersourceeq: Union[Unset, str] = UNSET,
    filtersourcenot_eq: Union[Unset, str] = UNSET,
    filtersourcein: Union[Unset, str] = UNSET,
    filtersourcenot_in: Union[Unset, str] = UNSET,
    filterserviceseq: Union[Unset, str] = UNSET,
    filterservicesnot_eq: Union[Unset, str] = UNSET,
    filterservicesin: Union[Unset, str] = UNSET,
    filterservicesnot_in: Union[Unset, str] = UNSET,
    filterenvironmentseq: Union[Unset, str] = UNSET,
    filterenvironmentsnot_eq: Union[Unset, str] = UNSET,
    filterenvironmentsin: Union[Unset, str] = UNSET,
    filterenvironmentsnot_in: Union[Unset, str] = UNSET,
    filterlabelseq: Union[Unset, str] = UNSET,
    filterlabelsnot_eq: Union[Unset, str] = UNSET,
    filterlabelsin: Union[Unset, str] = UNSET,
    filterlabelsnot_in: Union[Unset, str] = UNSET,
    filterrefseq: Union[Unset, str] = UNSET,
    filterrefsnot_eq: Union[Unset, str] = UNSET,
    filterrefsin: Union[Unset, str] = UNSET,
    filterrefsnot_in: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
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


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PulseList]:
    if response.status_code == 200:
        response_200 = PulseList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PulseList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include: Union[Unset, str] = UNSET,
    filtersource: Union[Unset, str] = UNSET,
    filterservices: Union[Unset, str] = UNSET,
    filterenvironments: Union[Unset, str] = UNSET,
    filterlabels: Union[Unset, str] = UNSET,
    filterrefs: Union[Unset, str] = UNSET,
    filterstarted_atgt: Union[Unset, str] = UNSET,
    filterstarted_atgte: Union[Unset, str] = UNSET,
    filterstarted_atlt: Union[Unset, str] = UNSET,
    filterstarted_atlte: Union[Unset, str] = UNSET,
    filterended_atgt: Union[Unset, str] = UNSET,
    filterended_atgte: Union[Unset, str] = UNSET,
    filterended_atlt: Union[Unset, str] = UNSET,
    filterended_atlte: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filtersourceeq: Union[Unset, str] = UNSET,
    filtersourcenot_eq: Union[Unset, str] = UNSET,
    filtersourcein: Union[Unset, str] = UNSET,
    filtersourcenot_in: Union[Unset, str] = UNSET,
    filterserviceseq: Union[Unset, str] = UNSET,
    filterservicesnot_eq: Union[Unset, str] = UNSET,
    filterservicesin: Union[Unset, str] = UNSET,
    filterservicesnot_in: Union[Unset, str] = UNSET,
    filterenvironmentseq: Union[Unset, str] = UNSET,
    filterenvironmentsnot_eq: Union[Unset, str] = UNSET,
    filterenvironmentsin: Union[Unset, str] = UNSET,
    filterenvironmentsnot_in: Union[Unset, str] = UNSET,
    filterlabelseq: Union[Unset, str] = UNSET,
    filterlabelsnot_eq: Union[Unset, str] = UNSET,
    filterlabelsin: Union[Unset, str] = UNSET,
    filterlabelsnot_in: Union[Unset, str] = UNSET,
    filterrefseq: Union[Unset, str] = UNSET,
    filterrefsnot_eq: Union[Unset, str] = UNSET,
    filterrefsin: Union[Unset, str] = UNSET,
    filterrefsnot_in: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Response[PulseList]:
    """List pulses

     List pulses

    Args:
        include (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filterrefs (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterended_atgt (Union[Unset, str]):
        filterended_atgte (Union[Unset, str]):
        filterended_atlt (Union[Unset, str]):
        filterended_atlte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filtersourceeq (Union[Unset, str]):
        filtersourcenot_eq (Union[Unset, str]):
        filtersourcein (Union[Unset, str]):
        filtersourcenot_in (Union[Unset, str]):
        filterserviceseq (Union[Unset, str]):
        filterservicesnot_eq (Union[Unset, str]):
        filterservicesin (Union[Unset, str]):
        filterservicesnot_in (Union[Unset, str]):
        filterenvironmentseq (Union[Unset, str]):
        filterenvironmentsnot_eq (Union[Unset, str]):
        filterenvironmentsin (Union[Unset, str]):
        filterenvironmentsnot_in (Union[Unset, str]):
        filterlabelseq (Union[Unset, str]):
        filterlabelsnot_eq (Union[Unset, str]):
        filterlabelsin (Union[Unset, str]):
        filterlabelsnot_in (Union[Unset, str]):
        filterrefseq (Union[Unset, str]):
        filterrefsnot_eq (Union[Unset, str]):
        filterrefsin (Union[Unset, str]):
        filterrefsnot_in (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

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
    include: Union[Unset, str] = UNSET,
    filtersource: Union[Unset, str] = UNSET,
    filterservices: Union[Unset, str] = UNSET,
    filterenvironments: Union[Unset, str] = UNSET,
    filterlabels: Union[Unset, str] = UNSET,
    filterrefs: Union[Unset, str] = UNSET,
    filterstarted_atgt: Union[Unset, str] = UNSET,
    filterstarted_atgte: Union[Unset, str] = UNSET,
    filterstarted_atlt: Union[Unset, str] = UNSET,
    filterstarted_atlte: Union[Unset, str] = UNSET,
    filterended_atgt: Union[Unset, str] = UNSET,
    filterended_atgte: Union[Unset, str] = UNSET,
    filterended_atlt: Union[Unset, str] = UNSET,
    filterended_atlte: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filtersourceeq: Union[Unset, str] = UNSET,
    filtersourcenot_eq: Union[Unset, str] = UNSET,
    filtersourcein: Union[Unset, str] = UNSET,
    filtersourcenot_in: Union[Unset, str] = UNSET,
    filterserviceseq: Union[Unset, str] = UNSET,
    filterservicesnot_eq: Union[Unset, str] = UNSET,
    filterservicesin: Union[Unset, str] = UNSET,
    filterservicesnot_in: Union[Unset, str] = UNSET,
    filterenvironmentseq: Union[Unset, str] = UNSET,
    filterenvironmentsnot_eq: Union[Unset, str] = UNSET,
    filterenvironmentsin: Union[Unset, str] = UNSET,
    filterenvironmentsnot_in: Union[Unset, str] = UNSET,
    filterlabelseq: Union[Unset, str] = UNSET,
    filterlabelsnot_eq: Union[Unset, str] = UNSET,
    filterlabelsin: Union[Unset, str] = UNSET,
    filterlabelsnot_in: Union[Unset, str] = UNSET,
    filterrefseq: Union[Unset, str] = UNSET,
    filterrefsnot_eq: Union[Unset, str] = UNSET,
    filterrefsin: Union[Unset, str] = UNSET,
    filterrefsnot_in: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[PulseList]:
    """List pulses

     List pulses

    Args:
        include (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filterrefs (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterended_atgt (Union[Unset, str]):
        filterended_atgte (Union[Unset, str]):
        filterended_atlt (Union[Unset, str]):
        filterended_atlte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filtersourceeq (Union[Unset, str]):
        filtersourcenot_eq (Union[Unset, str]):
        filtersourcein (Union[Unset, str]):
        filtersourcenot_in (Union[Unset, str]):
        filterserviceseq (Union[Unset, str]):
        filterservicesnot_eq (Union[Unset, str]):
        filterservicesin (Union[Unset, str]):
        filterservicesnot_in (Union[Unset, str]):
        filterenvironmentseq (Union[Unset, str]):
        filterenvironmentsnot_eq (Union[Unset, str]):
        filterenvironmentsin (Union[Unset, str]):
        filterenvironmentsnot_in (Union[Unset, str]):
        filterlabelseq (Union[Unset, str]):
        filterlabelsnot_eq (Union[Unset, str]):
        filterlabelsin (Union[Unset, str]):
        filterlabelsnot_in (Union[Unset, str]):
        filterrefseq (Union[Unset, str]):
        filterrefsnot_eq (Union[Unset, str]):
        filterrefsin (Union[Unset, str]):
        filterrefsnot_in (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

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
    include: Union[Unset, str] = UNSET,
    filtersource: Union[Unset, str] = UNSET,
    filterservices: Union[Unset, str] = UNSET,
    filterenvironments: Union[Unset, str] = UNSET,
    filterlabels: Union[Unset, str] = UNSET,
    filterrefs: Union[Unset, str] = UNSET,
    filterstarted_atgt: Union[Unset, str] = UNSET,
    filterstarted_atgte: Union[Unset, str] = UNSET,
    filterstarted_atlt: Union[Unset, str] = UNSET,
    filterstarted_atlte: Union[Unset, str] = UNSET,
    filterended_atgt: Union[Unset, str] = UNSET,
    filterended_atgte: Union[Unset, str] = UNSET,
    filterended_atlt: Union[Unset, str] = UNSET,
    filterended_atlte: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filtersourceeq: Union[Unset, str] = UNSET,
    filtersourcenot_eq: Union[Unset, str] = UNSET,
    filtersourcein: Union[Unset, str] = UNSET,
    filtersourcenot_in: Union[Unset, str] = UNSET,
    filterserviceseq: Union[Unset, str] = UNSET,
    filterservicesnot_eq: Union[Unset, str] = UNSET,
    filterservicesin: Union[Unset, str] = UNSET,
    filterservicesnot_in: Union[Unset, str] = UNSET,
    filterenvironmentseq: Union[Unset, str] = UNSET,
    filterenvironmentsnot_eq: Union[Unset, str] = UNSET,
    filterenvironmentsin: Union[Unset, str] = UNSET,
    filterenvironmentsnot_in: Union[Unset, str] = UNSET,
    filterlabelseq: Union[Unset, str] = UNSET,
    filterlabelsnot_eq: Union[Unset, str] = UNSET,
    filterlabelsin: Union[Unset, str] = UNSET,
    filterlabelsnot_in: Union[Unset, str] = UNSET,
    filterrefseq: Union[Unset, str] = UNSET,
    filterrefsnot_eq: Union[Unset, str] = UNSET,
    filterrefsin: Union[Unset, str] = UNSET,
    filterrefsnot_in: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Response[PulseList]:
    """List pulses

     List pulses

    Args:
        include (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filterrefs (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterended_atgt (Union[Unset, str]):
        filterended_atgte (Union[Unset, str]):
        filterended_atlt (Union[Unset, str]):
        filterended_atlte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filtersourceeq (Union[Unset, str]):
        filtersourcenot_eq (Union[Unset, str]):
        filtersourcein (Union[Unset, str]):
        filtersourcenot_in (Union[Unset, str]):
        filterserviceseq (Union[Unset, str]):
        filterservicesnot_eq (Union[Unset, str]):
        filterservicesin (Union[Unset, str]):
        filterservicesnot_in (Union[Unset, str]):
        filterenvironmentseq (Union[Unset, str]):
        filterenvironmentsnot_eq (Union[Unset, str]):
        filterenvironmentsin (Union[Unset, str]):
        filterenvironmentsnot_in (Union[Unset, str]):
        filterlabelseq (Union[Unset, str]):
        filterlabelsnot_eq (Union[Unset, str]):
        filterlabelsin (Union[Unset, str]):
        filterlabelsnot_in (Union[Unset, str]):
        filterrefseq (Union[Unset, str]):
        filterrefsnot_eq (Union[Unset, str]):
        filterrefsin (Union[Unset, str]):
        filterrefsnot_in (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

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
    include: Union[Unset, str] = UNSET,
    filtersource: Union[Unset, str] = UNSET,
    filterservices: Union[Unset, str] = UNSET,
    filterenvironments: Union[Unset, str] = UNSET,
    filterlabels: Union[Unset, str] = UNSET,
    filterrefs: Union[Unset, str] = UNSET,
    filterstarted_atgt: Union[Unset, str] = UNSET,
    filterstarted_atgte: Union[Unset, str] = UNSET,
    filterstarted_atlt: Union[Unset, str] = UNSET,
    filterstarted_atlte: Union[Unset, str] = UNSET,
    filterended_atgt: Union[Unset, str] = UNSET,
    filterended_atgte: Union[Unset, str] = UNSET,
    filterended_atlt: Union[Unset, str] = UNSET,
    filterended_atlte: Union[Unset, str] = UNSET,
    filtercreated_atgt: Union[Unset, str] = UNSET,
    filtercreated_atgte: Union[Unset, str] = UNSET,
    filtercreated_atlt: Union[Unset, str] = UNSET,
    filtercreated_atlte: Union[Unset, str] = UNSET,
    filtersourceeq: Union[Unset, str] = UNSET,
    filtersourcenot_eq: Union[Unset, str] = UNSET,
    filtersourcein: Union[Unset, str] = UNSET,
    filtersourcenot_in: Union[Unset, str] = UNSET,
    filterserviceseq: Union[Unset, str] = UNSET,
    filterservicesnot_eq: Union[Unset, str] = UNSET,
    filterservicesin: Union[Unset, str] = UNSET,
    filterservicesnot_in: Union[Unset, str] = UNSET,
    filterenvironmentseq: Union[Unset, str] = UNSET,
    filterenvironmentsnot_eq: Union[Unset, str] = UNSET,
    filterenvironmentsin: Union[Unset, str] = UNSET,
    filterenvironmentsnot_in: Union[Unset, str] = UNSET,
    filterlabelseq: Union[Unset, str] = UNSET,
    filterlabelsnot_eq: Union[Unset, str] = UNSET,
    filterlabelsin: Union[Unset, str] = UNSET,
    filterlabelsnot_in: Union[Unset, str] = UNSET,
    filterrefseq: Union[Unset, str] = UNSET,
    filterrefsnot_eq: Union[Unset, str] = UNSET,
    filterrefsin: Union[Unset, str] = UNSET,
    filterrefsnot_in: Union[Unset, str] = UNSET,
    pagenumber: Union[Unset, int] = UNSET,
    pagesize: Union[Unset, int] = UNSET,
) -> Optional[PulseList]:
    """List pulses

     List pulses

    Args:
        include (Union[Unset, str]):
        filtersource (Union[Unset, str]):
        filterservices (Union[Unset, str]):
        filterenvironments (Union[Unset, str]):
        filterlabels (Union[Unset, str]):
        filterrefs (Union[Unset, str]):
        filterstarted_atgt (Union[Unset, str]):
        filterstarted_atgte (Union[Unset, str]):
        filterstarted_atlt (Union[Unset, str]):
        filterstarted_atlte (Union[Unset, str]):
        filterended_atgt (Union[Unset, str]):
        filterended_atgte (Union[Unset, str]):
        filterended_atlt (Union[Unset, str]):
        filterended_atlte (Union[Unset, str]):
        filtercreated_atgt (Union[Unset, str]):
        filtercreated_atgte (Union[Unset, str]):
        filtercreated_atlt (Union[Unset, str]):
        filtercreated_atlte (Union[Unset, str]):
        filtersourceeq (Union[Unset, str]):
        filtersourcenot_eq (Union[Unset, str]):
        filtersourcein (Union[Unset, str]):
        filtersourcenot_in (Union[Unset, str]):
        filterserviceseq (Union[Unset, str]):
        filterservicesnot_eq (Union[Unset, str]):
        filterservicesin (Union[Unset, str]):
        filterservicesnot_in (Union[Unset, str]):
        filterenvironmentseq (Union[Unset, str]):
        filterenvironmentsnot_eq (Union[Unset, str]):
        filterenvironmentsin (Union[Unset, str]):
        filterenvironmentsnot_in (Union[Unset, str]):
        filterlabelseq (Union[Unset, str]):
        filterlabelsnot_eq (Union[Unset, str]):
        filterlabelsin (Union[Unset, str]):
        filterlabelsnot_in (Union[Unset, str]):
        filterrefseq (Union[Unset, str]):
        filterrefsnot_eq (Union[Unset, str]):
        filterrefsin (Union[Unset, str]):
        filterrefsnot_in (Union[Unset, str]):
        pagenumber (Union[Unset, int]):
        pagesize (Union[Unset, int]):

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
