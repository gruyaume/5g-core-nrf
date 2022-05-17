from typing import List

from pydantic import BaseModel

from data_models.DnnSmfInfoItem import DnnSmfInfoItem
from data_models.common.Snssai import Snssai


class sNssaiSmfInfoItem(BaseModel):
    sNssai: Snssai
    dnnSmfInfoList: List[DnnSmfInfoItem]
