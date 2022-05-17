from pydantic import BaseModel

from schemas.common.PlmnId import PlmnId
from schemas.common.Tac import Tac


class Tai(BaseModel):
    plmnId: PlmnId
    tac: Tac
