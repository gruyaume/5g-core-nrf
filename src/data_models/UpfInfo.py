from typing import List

from pydantic import BaseModel

from data_models.InterfaceUpfInfoItem import InterfaceUpfInfoItem
from data_models.common.PduSessionType import PduSessionType
from data_models.sNssaiSmfInfoItem import sNssaiSmfInfoItem


class UpfInfo(BaseModel):
    sNssaiSmfInfoList: List[sNssaiSmfInfoItem]
    smfServingArea: List[str] = None
    interfaceUpfInfoList: List[InterfaceUpfInfoItem] = None
    iwkEpsInd: bool = None
    pduSessionTypes: List[PduSessionType] = None
