from typing import List

from pydantic import BaseModel

from schemas.TacRange import TacRange
from schemas.common.PlmnId import PlmnId


class TaiRange(BaseModel):
    plmnId: PlmnId
    tacRangeList: List[TacRange]
