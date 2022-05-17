from typing import List

from pydantic import BaseModel

from schemas.DnnSmfInfoItem import DnnSmfInfoItem
from schemas.common.Snssai import Snssai


class sNssaiSmfInfoItem(BaseModel):
    sNssai: Snssai
    dnnSmfInfoList: List[DnnSmfInfoItem]
