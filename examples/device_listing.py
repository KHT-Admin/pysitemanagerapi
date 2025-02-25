import os
import pprint

from pysitemanagerapi.client import SiteManagerApiClient

_UNIFI_API_KEY = os.environ["UNIFI_API_KEY"]

a = SiteManagerApiClient(_UNIFI_API_KEY)
hosts = a.list_host_ids()
host_devices = a.list_devices(list(hosts.values()))


exclude_fields = {"mac", "id", "uidb"}

d = {
    host["hostName"]: [
        {k: v for k, v in device.items() if k not in exclude_fields}
        for device in host["devices"]
    ]
    for host in host_devices
}

pprint.pp(d)
