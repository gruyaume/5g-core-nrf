from typing import List

from pydantic import BaseModel

from schemas.common.PlmnId import PlmnId
from schemas.common.Snssai import Snssai


class PlmnSnssai(BaseModel):
    plmnId: PlmnId
    sNssaiList: List[Snssai]
