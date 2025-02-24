from dataclasses import asdict, dataclass
from typing import List, Optional, Union

from . import controller


@dataclass
class ReportedState:
    anonid: str
    apps: List[dict]
    autoUpdate: dict
    availableChannels: List
    consolesOnSameLocalNetwork: List
    controller_uuid: str
    controllers: List[controller.Controller]
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
        self.controllers = [
            controller.controller_factory(**c) for c in self.controllers
        ]

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
