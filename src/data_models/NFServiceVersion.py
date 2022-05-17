from pydantic import BaseModel

from data_models.common.DateTime import DateTime


class NFServiceVersion(BaseModel):
    apiVersionInUri: str
    apiFullVersion: str
    expiry: DateTime = None
