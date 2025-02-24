from dataclasses import asdict, dataclass
from typing import List, Optional, Union


@dataclass
class Controller:
    installState: str
    isConfigured: bool
    isInstalled: bool
    isRunning: bool
    name: str
    port: int
    releaseChannel: str
    state: str
    status: str
    statusMessage: str
    type: str
    unadoptedDevices: List
    updatable: bool
    version: str


@dataclass
class Installed(Controller):
    controllerStatus: str
    initialDeviceListSynced: bool
    swaiVersion: int
    uiVersion: str
    updateAvailable: str
    updateProgress: int


@dataclass
class Required(Controller):
    controllerStatus: str
    initialDeviceListSynced: bool
    swaiVersion: int
    uiVersion: str
    updateAvailable: str
    updateProgress: int
    required: bool
    uiVersion: str
    abridged: Optional[bool] = None
    integrationApis: Optional[str] = None


@dataclass
class Protect(Controller):
    installable: bool
    isGeofencingEnabled: bool
    controllerStatus: str
    initialDeviceListSynced: bool
    restorePercentage: int
    swaiVersion: int
    tcpBridgeUri: str
    uiVersion: str
    updateAvailable: str
    updateProgress: int
    features: Optional[dict] = None
    integrationApis: Optional[str] = None
    updateProgress: Optional[int] = None
    abridged: Optional[bool] = None


@dataclass
class Network(Controller):
    controllerStatus: str
    initialDeviceListSynced: bool
    swaiVersion: int
    uiVersion: str
    updateAvailable: str
    updateProgress: int
    installable: bool
    integrationApis: Optional[str] = None
    abridged: Optional[bool] = None


@dataclass
class Uninstalled(Controller):
    installable: bool


def controller_factory(*args, **kwargs):
    if kwargs.get("installState") == "uninstalled":
        return Uninstalled(*args, **kwargs)

    if kwargs.get("required") is True:
        return Required(*args, **kwargs)

    if kwargs.get("isInstalled") and kwargs.get("name") == "protect":
        return Protect(*args, **kwargs)

    if kwargs.get("isInstalled") and kwargs.get("name") == "network":
        return Network(*args, **kwargs)
