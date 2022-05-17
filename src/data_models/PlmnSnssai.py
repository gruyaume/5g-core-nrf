from typing import List

from pydantic import BaseModel

from data_models.common.PlmnId import PlmnId
from data_models.common.Snssai import Snssai


class PlmnSnssai(BaseModel):
    plmnId: PlmnId
    sNssaiList: List[Snssai]
