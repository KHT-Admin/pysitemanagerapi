import csv
import os

from pysitemanagerapi.client import SiteManagerApiClient

_UNIFI_API_KEY = os.environ["UNIFI_API_KEY"]

# Read devices for all sites from Site Manager
a = SiteManagerApiClient(_UNIFI_API_KEY)
hosts = a.list_host_ids()
hostids = list(hosts.values())
host_devices = a.list_devices(hostids)

# uidb contains metadata about icons so exclude from the results.
exclude_fields = {"uidb"}

d = {
    host["hostName"]: [
        {k: v for k, v in device.items() if k not in exclude_fields}
        for device in host["devices"]
    ]
    for host in host_devices
}

# Sitename is the key for the device list of dicts
# {"sitename": [{device details}, {device details}]}

for site, device_list in d.items():
    # extract column headers from first device
    fieldnames = list(device_list[0].keys())

    # create csv per site
    with open(f"{site}.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(device_list)
