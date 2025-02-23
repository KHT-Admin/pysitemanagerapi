class UniFiApiError(Exception):
    """Errors raise by UniFi API Endpoint"""


class InvalidParameter(UniFiApiError):
    """400 Invalid Parameter"""


class Unauthorised(UniFiApiError):
    """401 Authorisation failed"""


class NotFound(UniFiApiError):
    """404 Not Found"""


class RateLimited(UniFiApiError):
    """429 Rated limiting exceeded"""


class ServerError(UniFiApiError):
    """500 Failed to List Hosts"""


class BadGateway(UniFiApiError):
    """502 Bad Gateway"""
