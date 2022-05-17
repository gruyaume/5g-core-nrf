from pydantic import BaseModel

from schemas.common.Dnn import Dnn


class DnnSmfInfoItem(BaseModel):
    dnn: Dnn
