from typing import Dict

from pydantic import BaseModel

from data_models.AmfInfo import AmfInfo
from data_models.AusfInfo import AusfInfo
from data_models.BsfInfo import BsfInfo
from data_models.ChfInfo import ChfInfo
from data_models.PcfInfo import PcfInfo
from data_models.SmfInfo import SmfInfo
from data_models.UdmInfo import UdmInfo
from data_models.UdrInfo import UdrInfo
from data_models.UpfInfo import UpfInfo
from data_models.common.NfInstanceId import NfInstanceId


class NrfInfo(BaseModel):
    servedUdrInfo: Dict[NfInstanceId, UdrInfo] = None
    servedUdmInfo: Dict[NfInstanceId, UdmInfo] = None
    servedAusfInfo: Dict[NfInstanceId, AusfInfo] = None
    servedAmfInfo: Dict[NfInstanceId, AmfInfo] = None
    servedSmfInfo: Dict[NfInstanceId, SmfInfo] = None
    servedUpfInfo: Dict[NfInstanceId, UpfInfo] = None
    servedPcfInfo: Dict[NfInstanceId, PcfInfo] = None
    servedBsfInfo: Dict[NfInstanceId, BsfInfo] = None
    servedChfInfo: Dict[NfInstanceId, ChfInfo] = None
