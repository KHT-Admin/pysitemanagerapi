import http.client
import json
from dataclasses import dataclass

from . import errors

API_HOST = "api.ui.com"
API_VERSION = "0.1"


@dataclass
class UniFiApiResponse:
    code: str = None
    data: dict = None
    httpStatusCode: int = None
    message: str = None
    traceId: str = None


class api_request_cm:
    """Context manager for API requests."""

    def __init__(self, connection, method: str, url: str, headers: dict):
        self.conn = connection
        self.conn.request(method, url, headers=headers)

    def __enter__(self):
        return self.conn

    def __exit__(self, exception_type, exception, traceback):
        self.conn.close()


class UniFiApiRequest:
    def __init__(self, api_key: str):
        self._headers: dict = {
            "X-API-KEY": api_key,
            "Accept": "application/json",
        }

        self._base_path = "/ea"

        try:
            self.conn = http.client.HTTPSConnection(API_HOST)

        except Exception as e:
            raise e

    def _api_request(self, method, url):
        with api_request_cm(self.conn, method, url, self._headers) as r:
            resp = r.getresponse()
            response = UniFiApiResponse(**json.loads(resp.read()))

        match response.httpStatusCode:
            case 200:
                return response.data
            case 400:
                raise errors.InvalidParameter(response.message)
            case 401:
                raise errors.Unauthorised(response.message)
            case 404:
                raise errors.NotFound(response.message)
            case 429:
                raise errors.RateLimited(response.message)
            case 500:
                raise errors.ServerError(response.message)
            case 502:
                raise errors.BadGateway(response.message)

    def get(self, url: str):
        return self._api_request("GET", f"{self._base_path}/{url}")
