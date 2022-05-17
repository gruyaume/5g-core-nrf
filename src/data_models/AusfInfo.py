from typing import List

from pydantic import BaseModel

from data_models.SupiRange import SupiRange
from data_models.common.NfGroupId import NfGroupId


class AusfInfo(BaseModel):
    groupId: NfGroupId = None
    supiRanges: List[SupiRange] = None
    routingIndicators: List[str] = None
