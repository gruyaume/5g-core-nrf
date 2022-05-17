from pydantic import BaseModel

from data_models.common.PlmnId import PlmnId
from data_models.common.Tac import Tac


class Tai(BaseModel):
    plmnId: PlmnId
    tac: Tac
