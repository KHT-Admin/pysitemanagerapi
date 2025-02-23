from dataclasses import dataclass
from typing import Optional

from .apirequest import UniFiApiRequest
from .datatypes.host import UniFiApiHost


class UniFiApiClient:
    def __init__(
        self,
        api_key: str,
        early_access: bool = False,
    ):
        self._api = UniFiApiRequest(api_key, early_access)

    def list_hosts(self) -> list[UniFiApiHost]:
        return [self._host_data(i) for i in self._api.get("hosts")]

    def get_host_by_id(self, hostid: str) -> dict:
        return self._host_data(self._api.get(f"hosts/{hostid}"))

    def list_sites(self) -> list[dict]:
        return self._api.get("sites")

    def list_devices(self, hostids: Optional[list[str] | str] = None):
        url = "devices"

        if isinstance(hostids, str):
            hostids = list((hostids,))

        if hostids is not None:
            hostids = [f"hostIds[]={r}" for r in hostids]
            url = f"{url}?{'&'.join(hostids)}"

        return self._api.get(url=url)

    def get_isp_metrics(
        self,
        metric_type: str,
        begin_ts: Optional[str] = None,
        end_ts: Optional[str] = None,
        duration: Optional[str] = None,
    ):
        if metric_type not in {"5m", "1h"}:
            raise TypeError("Invalid type")

        url = f"isp-metrics/{metric_type}"

        if begin_ts is not None:
            pass
        elif duration is not None:
            if (metric_type == "5m" and duration != "24h") or (
                metric_type == "1h" and duration not in {"7d", "30d"}
            ):
                raise TypeError("Invalid duration")

        return self._api.get(url=url)

    ## Private methods
    def _build_query(self):
        pass

    def _host_data(self, response: dict) -> dict:
        ### Cast data to Host structure ###
        return UniFiApiHost(**response)
        # return response

    ## Utility methods
    def list_host_ids(self) -> dict:
        hosts = self._api.get("hosts")
        return {site["reportedState"]["hostname"]: site["id"] for site in hosts}
