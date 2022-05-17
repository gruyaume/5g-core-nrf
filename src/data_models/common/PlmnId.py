from pydantic import BaseModel

from data_models.common.Mcc import Mcc
from data_models.common.Mnc import Mnc


class PlmnId(BaseModel):
    mcc: Mcc
    mnc: Mnc
