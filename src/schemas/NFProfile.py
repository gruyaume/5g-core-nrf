from typing import List

from pydantic import BaseModel

from schemas.AmfInfo import AmfInfo
from schemas.AusfInfo import AusfInfo
from schemas.BsfInfo import BsfInfo
from schemas.ChfInfo import ChfInfo
from schemas.DefaultNotificationSubscription import DefaultNotificationSubscription
from schemas.Fqdn import Fqdn
from schemas.NFService import NFService
from schemas.NFStatus import NFStatus
from schemas.NFType import NFType
from schemas.NrfInfo import NrfInfo
from schemas.PcfInfo import PcfInfo
from schemas.PlmnSnssai import PlmnSnssai
from schemas.SmfInfo import SmfInfo
from schemas.UdmInfo import UdmInfo
from schemas.UdrInfo import UdrInfo
from schemas.UpfInfo import UpfInfo
from schemas.common.DateTime import DateTime
from schemas.common.Ipv4Addr import Ipv4Addr
from schemas.common.Ipv6Addr import Ipv6Addr
from schemas.common.NfInstanceId import NfInstanceId
from schemas.common.PlmnId import PlmnId
from schemas.common.Snssai import Snssai


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
