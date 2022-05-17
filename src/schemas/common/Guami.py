from pydantic import BaseModel

from schemas.common.AmfId import AmfId
from schemas.common.PlmnId import PlmnId


class Guami(BaseModel):
    plmnId: PlmnId
    amfId: AmfId
