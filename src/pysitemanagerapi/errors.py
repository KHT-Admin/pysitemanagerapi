class SiteManagerApiError(Exception):
    """Errors raise by UniFi API Endpoint"""


class InvalidParameter(SiteManagerApiError):
    """400 Invalid Parameter"""


class Unauthorised(SiteManagerApiError):
    """401 Authorisation failed"""


class NotFound(SiteManagerApiError):
    """404 Not Found"""


class RateLimited(SiteManagerApiError):
    """429 Rated limiting exceeded"""


class ServerError(SiteManagerApiError):
    """500 Failed to List Hosts"""


class BadGateway(SiteManagerApiError):
    """502 Bad Gateway"""
