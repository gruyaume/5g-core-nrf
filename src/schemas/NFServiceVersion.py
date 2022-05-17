from pydantic import BaseModel

from schemas.common.DateTime import DateTime


class NFServiceVersion(BaseModel):
    apiVersionInUri: str
    apiFullVersion: str
    expiry: DateTime = None
