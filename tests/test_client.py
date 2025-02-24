import dataclasses
import json
import os
import pprint

import pytest
from pyunifiapi.apirequest import UniFiApiRequest
from pyunifiapi.client import UniFiApiClient
from pyunifiapi.errors import NotFound, UniFiApiError

_UNIFI_API_KEY = os.environ["UNIFI_API_KEY"]
_N_SITES = 2
_N_HOSTS = 2


def test_client_unifi():
    a = UniFiApiClient("mykey")
    assert isinstance(a, UniFiApiClient)


def test_client_apirequest_init():
    a = UniFiApiRequest("abc")
    assert isinstance(a, UniFiApiRequest)


def test_list_sites():
    a = UniFiApiClient(_UNIFI_API_KEY)
    b = a.list_sites()
    _N_SITES = len(b)
    assert True


def test_client_api_request():
    a = UniFiApiClient(_UNIFI_API_KEY)
    b = a.list_hosts()
    assert len(b) == _N_SITES


def test_bad_hostid():
    a = UniFiApiClient(_UNIFI_API_KEY)
    with pytest.raises(NotFound) as e_info:
        b = a.get_host_by_id("0000")


def test_host_api_request():
    a = UniFiApiClient(_UNIFI_API_KEY)
    b = a.list_hosts()
    assert len(b) == _N_HOSTS


a = UniFiApiClient(_UNIFI_API_KEY)
hosts = a.list_hosts()
pprint.pp(hosts)
