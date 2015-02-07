import os
import datetime

import requests as r

from comod_bea import patterns

URL = "http://bea.gov/api/data/"
DATA_REQUEST_DEFAULTS = ("method", "getData"), ("ResultFormat", "json")

API_KEY = None

# built through module
PATTERN_HANDLERS = {}


class BeaFailure(ValueError):
    pass


class BeaSession(r.Session):
    SESSION_EXCEPTIONS = r.RequestException, BeaFailure

    def get_data(self, params, **kwargs):
        params.update(DATA_REQUEST_DEFAULTS)
        response = self.get(URL, params=params, **kwargs)
        response.raise_for_status()
        bea_api_response = response.json()["BEAAPI"]

        if "Error" in bea_api_response["Results"]:
            raise BeaFailure(bea_api_response)

        return bea_api_response["Results"]

    def get(self, url, **kwargs):
        params = kwargs.setdefault("params", {})
        params["UserId"] = _resolve_api_key()
        return super(BeaSession, self).get(url, **kwargs)


def _resolve_api_key():
    global API_KEY
    if API_KEY is None:
        API_KEY = os.environ.get("BEA_API_KEY")
        if API_KEY is None:
            raise ValueError("No API key found.")
    return API_KEY


def query_single_year(session, year, geo_fips, key_code):
    return query(session, geo_fips, key_code, years=[year])


def query_start_end(session, start_year, end_year, geo_fips, key_code):
    start_year = normalize_year_to_int(start_year)
    end_year = normalize_year_to_int(end_year)

    return query(session, geo_fips, key_code,
                 years=map(str, range(start_year, end_year + 1)))


def normalize_year_to_int(year):
    year = int(year)
    if year > 100:
        return year

    in_2000s = year + 2000

    if in_2000s > datetime.date.today().year:  # assume 1900s
        return 1900 + year

    return in_2000s


def query(session, geo_fips, key_code, years=None):
    """
    :type session: BeaSession
    :type geo_fips: str
    :type key_code: str
    :type years: list[str]
    :rtype: dict
    """
    params = {"datasetname": "RegionalData", "KeyCode": key_code,
              "GeoFips": geo_fips}

    if years is not None:
        params["Year"] = years

    results = session.get_data(params)
    data = results.pop("Data")
    return {"data": data, "meta_data": results}

PATTERN_HANDLERS[patterns.STATE_GDP] = \
    query_single_year, {"geo_fips": "STATE", "key_code": "GDP_SP"}, \
    "thousands_of_dollars.html"

PATTERN_HANDLERS[patterns.COUNTY_PERSONAL_INCOME] = \
    query_single_year,  {"geo_fips": "COUNTY", "key_code": "TPI_CI"}, \
    "thousands_of_dollars.html"

PATTERN_HANDLERS[patterns.STATE_PERSONAL_INCOME] = \
    query_single_year,  {"geo_fips": "STATE", "key_code": "TPI_SI"}, \
    "thousands_of_dollars.html"
