from typing import List

from pydantic import BaseModel

from data_models.TacRange import TacRange
from data_models.common.PlmnId import PlmnId


class TaiRange(BaseModel):
    plmnId: PlmnId
    tacRangeList: List[TacRange]
