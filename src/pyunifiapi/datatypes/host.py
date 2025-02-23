import json
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
    # elif i is True:
    #     controller = ControllerInstalled
    #     print("installed")
    # elif i is False:
    #     controller = ControllerUninstalled
    # return controller(*args, **kwargs)


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


"""
{
  "data": [
    {
      "hardwareId": "eae0f123-0000-5111-b111-f833f56eade5",
      "id": "900A6F00301100000000074A6BA90000000007A3387E0000000063EC9853:123456789",
      "ipAddress": "192.168.220.114",
      "isBlocked": false,
      "lastConnectionStateChange": "2024-06-23T03:59:52Z",
      "latestBackupTime": "2024-06-22T11:55:10Z",
      "owner": true,
      "registrationTime": "2024-04-17T07:27:14Z",
      "reportedState": {
        "anonid": "c2705509-58a5-40c9-8b2e-d29c8574ff08",
        "apps": [
          {
            "controllerStatus": "READY",
            "name": "users",
            "port": 9080,
            "swaiVersion": 2,
            "type": "app",
            "version": "1.8.42+3695"
          }
        ],
        "availableChannels": [
          "release",
          "beta",
          "release-candidate"
        ],
        "consolesOnSameLocalNetwork": [],
        "controller_uuid": "900A6F00301100000000074A6BA90000000007A3387E0000000063EC9853:123456789",
        "controllers": [
          {
            "abridged": true,
            "controllerStatus": "READY",
            "initialDeviceListSynced": true,
            "installState": "installed",
            "isConfigured": true,
            "isInstalled": true,
            "isRunning": true,
            "name": "network",
            "port": 8081,
            "releaseChannel": "beta",
            "required": true,
            "state": "active",
            "status": "ok",
            "statusMessage": "",
            "swaiVersion": 3,
            "type": "controller",
            "uiVersion": "8.4.20.0",
            "unadoptedDevices": [],
            "updatable": true,
            "updateAvailable": null,
            "version": "8.4.20"
          },
          {
            "abridged": true,
            "controllerStatus": "READY",
            "features": {
              "stackable": false
            },
            "initialDeviceListSynced": true,
            "installState": "installed",
            "installable": true,
            "isConfigured": true,
            "isGeofencingEnabled": false,
            "isInstalled": true,
            "isRunning": true,
            "name": "protect",
            "port": 7080,
            "releaseChannel": "beta",
            "restorePercentage": 100,
            "state": "active",
            "status": "ok",
            "statusMessage": "",
            "swaiVersion": 5,
            "type": "controller",
            "uiVersion": "3.1.22",
            "unadoptedDevices": [],
            "updatable": true,
            "updateAvailable": null,
            "version": "4.0.33"
          },
          {
            "installState": "uninstalled",
            "installable": false,
            "isConfigured": false,
            "isInstalled": false,
            "isRunning": false,
            "name": "access",
            "port": 12080,
            "releaseChannel": "beta",
            "state": "inactive",
            "status": "offline",
            "statusMessage": "",
            "type": "controller",
            "unadoptedDevices": [],
            "updatable": true,
            "version": null
          },
          {
            "installState": "uninstalled",
            "installable": false,
            "isConfigured": false,
            "isInstalled": false,
            "isRunning": false,
            "name": "talk",
            "port": 30080,
            "releaseChannel": "beta",
            "state": "inactive",
            "status": "offline",
            "statusMessage": "",
            "type": "controller",
            "unadoptedDevices": [],
            "updatable": true,
            "version": null
          },
          {
            "installState": "uninstalled",
            "installable": false,
            "isConfigured": false,
            "isInstalled": false,
            "isRunning": false,
            "name": "connect",
            "port": 54480,
            "releaseChannel": "beta",
            "state": "inactive",
            "status": "offline",
            "statusMessage": "",
            "type": "controller",
            "unadoptedDevices": [],
            "updatable": true,
            "version": null
          },
          {
            "installState": "uninstalled",
            "installable": false,
            "isConfigured": false,
            "isInstalled": false,
            "isRunning": false,
            "name": "innerspace",
            "port": 17080,
            "releaseChannel": "beta",
            "state": "inactive",
            "status": "offline",
            "statusMessage": "",
            "type": "controller",
            "unadoptedDevices": [],
            "updatable": true,
            "version": null
          }
        ],
        "country": 840,
        "deviceErrorCode": null,
        "deviceState": "setup",
        "deviceStateLastChanged": 1718804749,
        "directConnectDomain": "f4e2c6c23f1307bc5608082112aa0651cbf10.id.ui.direct",
        "features": {
          "cloud": {
            "applicationEvents": true,
            "applicationEventsHttp": true
          },
          "cloudBackup": true,
          "deviceList": {
            "autolinkDevices": true,
            "partialUpdates": true,
            "ucp4Events": true
          },
          "directRemoteConnection": true,
          "hasGateway": true,
          "hasLCM": true,
          "hasLED": false,
          "infoApis": {
            "firmwareUpdate": true
          },
          "isAutomaticFailoverAvailable": false,
          "mfa": true,
          "notifications": true,
          "sharedTokens": true,
          "supportForm": true,
          "teleport": false,
          "teleportState": "DISABLED",
          "uidService": true
        },
        "firmwareUpdate": {
          "latestAvailableVersion": null
        },
        "hardware": {
          "bom": "113-00917-42",
          "cpu.id": "411fd073-00000000",
          "debianCodename": "bullseye",
          "firmwareVersion": "4.0.6",
          "hwrev": 234794,
          "mac": "F4E2C6C23F13",
          "name": "UniFi Dream Machine SE",
          "qrid": "QwWvUy",
          "reboot": "30",
          "serialno": "f4e2c6c23f13",
          "shortname": "UDMPROSE",
          "subtype": "",
          "sysid": 59948,
          "upgrade": "310",
          "uuid": "eae0f123-0000-5111-b111-f833f56eade5"
        },
        "host_type": 59948,
        "hostname": "unifi.yourdomain.com",
        "internetIssues5min": {
          "periods": [
            {
              "index": 5731574
            }
          ]
        },
        "ip": "192.168.1.226",
        "ipAddrs": [
          "fe80::f6e2:c6ff:fec2:3f15",
          "fe80::f6e2:c6ff:fec2:3f17",
          "192.168.1.226",
          "fe80::f6e2:c6ff:fec2:3f1b",
          "192.168.0.1",
          "fe80::f4e2:c6ff:fec2:3f14"
        ],
        "isStacked": false,
        "location": {
          "lat": 56.9496,
          "long": 24.0978,
          "radius": 200,
          "text": "-----------"
        },
        "mac": "F4E1C6C11F00",
        "mgmt_port": 443,
        "name": "unifi.yourdomain.com",
        "releaseChannel": "beta",
        "state": "connected",
        "timezone": "Europe/Riga",
        "uidb": {
          "guid": "0fd8c390-a0e8-4cb2-b93a-7b3051c83c46",
          "id": "e85485da-54c3-4906-8f19-3cef4116ff02",
          "images": {
            "default": "3008400039c483c496f4ad820242c447",
            "nopadding": "67b553529d0e523ca9dd4826076c5f3f",
            "topology": "8371ecdda1f00f1636a2eefadf0d7d47"
          }
        },
        "unadoptedUnifiOSDevices": [],
        "version": "4.0.180"
      },
      "type": "console",
      "userData": {
        "apps": [
          "users"
        ],
        "consoleGroupMembers": [
          {
            "mac": "F4E2C6C23F13",
            "role": "UNADOPTED",
            "roleAttributes": {
              "applications": {
                "access": {
                  "owned": false,
                  "required": false,
                  "supported": true
                },
                "connect": {
                  "owned": false,
                  "required": false,
                  "supported": true
                },
                "innerspace": {
                  "owned": false,
                  "required": false,
                  "supported": true
                },
                "network": {
                  "owned": false,
                  "required": true,
                  "supported": true
                },
                "protect": {
                  "owned": false,
                  "required": false,
                  "supported": true
                },
                "talk": {
                  "owned": false,
                  "required": false,
                  "supported": true
                }
              },
              "candidateRoles": [
                "PRIMARY"
              ],
              "connectedState": "CONNECTED",
              "connectedStateLastChanged": "2024-04-17T13:27:12.380Z"
            },
            "sysId": 59948
          }
        ],
        "controllers": [
          "network",
          "protect",
          "access",
          "talk",
          "connect",
          "innerspace"
        ],
        "email": "unifi@test-ui.com",
        "features": {
          "deviceGroups": true,
          "floorplan": {
            "canEdit": true,
            "canView": true
          },
          "manageApplications": true,
          "notifications": true,
          "pion": true,
          "webrtc": {
            "iceRestart": true,
            "mediaStreams": true,
            "twoWayAudio": true
          }
        },
        "fullName": "UniFi User",
        "localId": "f537f425-945d-49bf-8b88-e7ed6469b2bb",
        "permissions": {
          "network.management": [
            "admin"
          ],
          "protect.management": [
            "admin"
          ],
          "system.management.location": [
            "admin"
          ],
          "system.management.user": [
            "admin"
          ]
        },
        "role": "owner",
        "roleId": "eb0ac6f9-21d7-4121-98e5-078ae8bacd96",
        "status": "ACTIVE"
      }
    }
  ],
  "httpStatusCode": 200,
  "traceId": "a7dc15e0eb4527142d7823515b15f87d"
}
"""
