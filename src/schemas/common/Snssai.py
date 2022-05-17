from pydantic import BaseModel

from schemas.common.Uinteger import Uinteger


class Snssai(BaseModel):
    sst: Uinteger
    sd: str
