# pyunifiapi

Python client for the official UniFi Site Manager API v0.1

Example usage


```{python}
a = SiteManagerApiClient(_UNIFI_API_KEY)
hosts = a.list_host_ids()
host_devices = a.list_devices(list(hosts.values()))

for host in host_devices:
    print(f"{host['hostName']}")
    for device in host["devices"]:
        print(f"\t{device['model']}, {device['version']}")
```
