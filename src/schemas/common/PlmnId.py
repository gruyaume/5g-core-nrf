from pydantic import BaseModel

from schemas.common.Mcc import Mcc
from schemas.common.Mnc import Mnc


class PlmnId(BaseModel):
    mcc: Mcc
    mnc: Mnc
