from pydantic import BaseModel

from data_models.common.Dnn import Dnn


class DnnSmfInfoItem(BaseModel):
    dnn: Dnn
