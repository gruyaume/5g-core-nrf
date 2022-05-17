from pydantic import BaseModel

from data_models.common.Uinteger import Uinteger


class Snssai(BaseModel):
    sst: Uinteger
    sd: str
