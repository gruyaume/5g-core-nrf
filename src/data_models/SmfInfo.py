from typing import List

from pydantic import BaseModel

from data_models.Fqdn import Fqdn
from data_models.TaiRange import TaiRange
from data_models.common.AccessType import AccessType
from data_models.common.Tai import Tai
from data_models.sNssaiSmfInfoItem import sNssaiSmfInfoItem


class SmfInfo(BaseModel):
    sNssaiSmfInfoList: List[sNssaiSmfInfoItem]
    taiList: List[Tai] = None
    taiRangeList: List[TaiRange] = None
    pgwFqdn: Fqdn = None
    accessType: List[AccessType] = None
