from typing import List

from pydantic import BaseModel

from data_models.IdentityRange import IdentityRange
from data_models.SupiRange import SupiRange
from data_models.common.NfGroupId import NfGroupId


class UdmInfo(BaseModel):
    groupId: NfGroupId = None
    supiRanges: List[SupiRange] = None
    gpsiRanges: List[IdentityRange] = None
    externalGroupIdentifiersRanges: List[IdentityRange] = None
    routingIndicators: List[str] = None
