from typing import List

from pydantic import BaseModel

from data_models.AmfInfo import AmfInfo
from data_models.AusfInfo import AusfInfo
from data_models.BsfInfo import BsfInfo
from data_models.ChfInfo import ChfInfo
from data_models.DefaultNotificationSubscription import DefaultNotificationSubscription
from data_models.Fqdn import Fqdn
from data_models.NFService import NFService
from data_models.NFStatus import NFStatus
from data_models.NFType import NFType
from data_models.NrfInfo import NrfInfo
from data_models.PcfInfo import PcfInfo
from data_models.PlmnSnssai import PlmnSnssai
from data_models.SmfInfo import SmfInfo
from data_models.UdmInfo import UdmInfo
from data_models.UdrInfo import UdrInfo
from data_models.UpfInfo import UpfInfo
from data_models.common.DateTime import DateTime
from data_models.common.Ipv4Addr import Ipv4Addr
from data_models.common.Ipv6Addr import Ipv6Addr
from data_models.common.NfInstanceId import NfInstanceId
from data_models.common.PlmnId import PlmnId
from data_models.common.Snssai import Snssai


class NFProfile(BaseModel):
    nfInstanceID: NfInstanceId
    nfType: NFType
    nfStatus: NFStatus
    heartBeatTimer: int = None
    plmnList: List[PlmnId] = None
    sNssais: List[Snssai] = None
    perPlmnSnssaiList: List[PlmnSnssai] = None
    nsiList: List[str] = None
    fqdn: Fqdn = None
    interPlmnFqdn: Fqdn = None
    ipv4Addresses: List[Ipv4Addr] = None
    ipv6Addresses: List[Ipv6Addr] = None
    allowedPlmns: List[PlmnId] = None
    allowedNfTypes: List[NFType] = None
    allowedNfDomains: List[str] = None
    allowedNssais: List[Snssai] = None
    priority: int = None
    capacity: int = None
    load: int = None
    locality: str = None
    udrInfo: UdrInfo = None
    udmInfo: UdmInfo = None
    ausfInfo: AusfInfo = None
    amfInfo: AmfInfo = None
    smfInfo: SmfInfo = None
    upfInfo: UpfInfo = None
    pcfInfo: PcfInfo = None
    bsfInfo: BsfInfo = None
    chfInfo: ChfInfo = None
    nrfInfo: NrfInfo = None
    customInfo: object = None
    recoveryTime: DateTime = None
    nfServicePersistence: bool = None
    nfServices: List[NFService] = None
    nfProfileChangesSupportInd: bool = None
    nfProfileChangesInd: bool = None
    defaultNotificationSubscriptions: List[DefaultNotificationSubscription] = None
