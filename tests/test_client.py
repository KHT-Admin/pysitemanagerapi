import dataclasses
import os

import pytest
from pysitemanagerapi.apirequest import SiteManagerApiRequest
from pysitemanagerapi.client import SiteManagerApiClient
from pysitemanagerapi.errors import NotFound, SiteManagerApiError

_UNIFI_API_KEY = os.environ["UNIFI_API_KEY"]
_N_SITES = 2
_N_HOSTS = 2


def test_client_unifi():
    a = SiteManagerApiClient("mykey")
    assert isinstance(a, SiteManagerApiClient)


def test_client_apirequest_init():
<<<<<<< HEAD
    a = UniFiApiRequest("abc")
    assert isinstance(a, UniFiApiRequest)
=======
    a = SiteManagerApiRequest("abc")
    assert isinstance(a, SiteManagerApiRequest)
>>>>>>> main


def test_list_sites():
    a = SiteManagerApiClient(_UNIFI_API_KEY)
    b = a.list_sites()
    _N_SITES = len(b)
    assert True


def test_client_api_request():
<<<<<<< HEAD
    a = UniFiApiClient(_UNIFI_API_KEY)
=======
    a = SiteManagerApiClient(_UNIFI_API_KEY)
>>>>>>> main
    b = a.list_hosts()
    assert len(b) == _N_SITES


def test_bad_hostid():
    a = SiteManagerApiClient(_UNIFI_API_KEY)
    with pytest.raises(NotFound) as e_info:
        b = a.get_host_by_id("0000")


def test_host_api_request():
<<<<<<< HEAD
    a = UniFiApiClient(_UNIFI_API_KEY)
    b = a.list_hosts()
    assert len(b) == _N_HOSTS


a = UniFiApiClient(_UNIFI_API_KEY)
hosts = a.list_hosts()
pprint.pp(hosts)
=======
    a = SiteManagerApiClient(_UNIFI_API_KEY)
    b = a.list_hosts()
    assert len(b) == _N_HOSTS
>>>>>>> main
