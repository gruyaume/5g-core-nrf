from typing import List

from pydantic import BaseModel

from data_models.ChfServiceInfo import ChfServiceInfo
from data_models.DefaultNotificationSubscription import DefaultNotificationSubscription
from data_models.Fqdn import Fqdn
from data_models.IpEndPoint import IpEndPoint
from data_models.NFServiceStatus import NFServiceStatus
from data_models.NFServiceVersion import NFServiceVersion
from data_models.NFType import NFType
from data_models.ServiceName import ServiceName
from data_models.common.DateTime import DateTime
from data_models.common.PlmnId import PlmnId
from data_models.common.Snssai import Snssai
from data_models.common.SupportedFeatures import SupportedFeatures
from data_models.common.UriScheme import UriScheme


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
