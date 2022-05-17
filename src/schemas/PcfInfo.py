from typing import List

from pydantic import BaseModel

from schemas.SupiRange import SupiRange
from schemas.common.DiameterIdentity import DiameterIdentity
from schemas.common.Dnn import Dnn


class PcfInfo(BaseModel):
    dnnList: List[Dnn] = None
    supiRanges: List[SupiRange] = None
    rxDiamHost: DiameterIdentity = None
    rxDiamRealm: DiameterIdentity = None
