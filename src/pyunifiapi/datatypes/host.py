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
    version: Optional[str]


@dataclass
class ControllerRequired(Controller):
    """
    "controllerStatus": "READY",
                "initialDeviceListSynced": True,
                "installState": "installed",
                "isConfigured": True,
                "isInstalled": True,
                "isRunning": True,
                "name": "network",
                "port": 8081,
                "releaseChannel": "beta",
                "required": True,
                "state": "active",
                "status": "ok",
                "statusMessage": "",
                "swaiVersion": 3,
                "type": "controller",
                "uiVersion": "8.5.1.0",
                "unadoptedDevices": [],
                "updatable": True,
                "updateAvailable": None,
                "version": "8.5.1",
            },
    """

    abridged: bool
    controllerStatus: str
    initialDeviceListSynced: bool
    restorePercentage: int
    swaiVersion: int
    uiVersion: str
    updateAvailable: str
    required: Optional[bool] = None


@dataclass
class ControllerInstalled(Controller):
    abridged: bool
    controllerStatus: str
    initialDeviceListSynced: bool
    installable: bool
    swaiVersion: int
    uiVersion: str
    updateAvailable: str
    updateProgress: Optional[int]
    features: Optional[dict] = None


@dataclass
class ControllerUninstalled(Controller):
    installable: bool


def controller_factory(*args, **kwargs):
    if kwargs.get("installState") == "uninstalled":
        return ControllerUninstalled(*args, **kwargs)

    if kwargs.get("required") is True and kwargs.get("installable"):
        return ControllerRequired(*args, **kwargs)


@dataclass
class ReportedState:
    anonid: str
    apps: List[dict]
    autoUpdate: dict
    availableChannels: List
    consolesOnSameLocalNetwork: List
    controller_uuid: str
    controllers: List[Controller]
    country: int
    deviceErrorCode: str
    deviceState: str
    deviceStateLastChanged: str
    directConnectDomain: str
    features: dict
    firmwareUpdate: dict
    hardware: dict
    host_type: str
    hostname: str
    internetIssues5min: dict
    ip: str
    ipAddrs: List[str]
    isStacked: bool
    location: dict[str]
    mac: str
    mgmt_port: int
    name: str
    releaseChannel: str
    state: str
    timezone: str
    ucareState: Optional[bool]
    uidb: dict
    unadoptedUnifiOSDevices: List
    version: str

    def __post_init__(self):
        self.controllers = [controller_factory(**c) for c in self.controllers]

    def __iter__(self):
        yield from asdict(self)


@dataclass
class UniFiApiHost:
    hardwareId: str = None
    id: str = None
    ipAddress: int = None
    isBlocked: bool = None
    lastConnectionStateChange: str = None
    latestBackupTime: str = None
    owner: bool = None
    registrationTime: str = None
    reportedState: ReportedState = None
    type: str = None
    userData: dict = None

    def __post_init__(self):
        self.reportedState = ReportedState(**self.reportedState)

    def __iter__(self):
        yield from asdict(self)
