from typing import List

from pydantic import BaseModel

from schemas.Fqdn import Fqdn
from schemas.TaiRange import TaiRange
from schemas.common.AccessType import AccessType
from schemas.common.Tai import Tai
from schemas.sNssaiSmfInfoItem import sNssaiSmfInfoItem


class SmfInfo(BaseModel):
    sNssaiSmfInfoList: List[sNssaiSmfInfoItem]
    taiList: List[Tai] = None
    taiRangeList: List[TaiRange] = None
    pgwFqdn: Fqdn = None
    accessType: List[AccessType] = None
