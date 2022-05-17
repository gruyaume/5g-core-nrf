from typing import List

from pydantic import BaseModel

from schemas.SupiRange import SupiRange
from schemas.common.NfGroupId import NfGroupId


class AusfInfo(BaseModel):
    groupId: NfGroupId = None
    supiRanges: List[SupiRange] = None
    routingIndicators: List[str] = None
