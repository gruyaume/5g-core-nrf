from typing import List

from pydantic import BaseModel

from data_models.SupiRange import SupiRange
from data_models.common.DiameterIdentity import DiameterIdentity
from data_models.common.Dnn import Dnn


class PcfInfo(BaseModel):
    dnnList: List[Dnn] = None
    supiRanges: List[SupiRange] = None
    rxDiamHost: DiameterIdentity = None
    rxDiamRealm: DiameterIdentity = None
