from typing import List

from pydantic import BaseModel

from data_models.IdentityRange import IdentityRange
from data_models.PlmnRange import PlmnRange
from data_models.SupiRange import SupiRange


class ChfInfo(BaseModel):
    supiRangeList: List[SupiRange] = None
    gpsiRangeList: List[IdentityRange] = None
    plmnRangeList: List[PlmnRange] = None
