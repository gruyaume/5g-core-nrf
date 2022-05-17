from pydantic import BaseModel

from data_models.common.AmfId import AmfId
from data_models.common.PlmnId import PlmnId


class Guami(BaseModel):
    plmnId: PlmnId
    amfId: AmfId
