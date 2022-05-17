from typing import List

from pydantic import BaseModel

from schemas.ChfServiceInfo import ChfServiceInfo
from schemas.DefaultNotificationSubscription import DefaultNotificationSubscription
from schemas.Fqdn import Fqdn
from schemas.IpEndPoint import IpEndPoint
from schemas.NFServiceStatus import NFServiceStatus
from schemas.NFServiceVersion import NFServiceVersion
from schemas.NFType import NFType
from schemas.ServiceName import ServiceName
from schemas.common.DateTime import DateTime
from schemas.common.PlmnId import PlmnId
from schemas.common.Snssai import Snssai
from schemas.common.SupportedFeatures import SupportedFeatures
from schemas.common.UriScheme import UriScheme


class NFService(BaseModel):
    serviceInstanceID: str
    serviceName: ServiceName
    versions: List[NFServiceVersion]
    scheme: UriScheme
    nfServiceStatus: NFServiceStatus
    fqdn: Fqdn = None
    interPlmnFqdn: Fqdn = None
    ipEndPoints: List[IpEndPoint] = None
    apiPrefix: str = None
    defaultNotificationSubscriptions: List[DefaultNotificationSubscription] = None
    allowedPlmns: List[PlmnId] = None
    allowedNfTypes: List[NFType] = None
    allowedNfDomains: List[str] = None
    allowedNssais: List[Snssai] = None
    priority: int = None
    capacity: int = None
    load: int = None
    recoveryTime: DateTime = None
    chfServiceInfo: ChfServiceInfo = None
    supportedFeatures: SupportedFeatures = None
