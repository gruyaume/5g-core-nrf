from typing import List

from pydantic import BaseModel

from schemas.N2InterfaceAmfInfo import N2InterfaceAmfInfo
from schemas.common.AmfRegionId import AmfRegionId
from schemas.common.AmfSetId import AmfSetId
from schemas.common.Guami import Guami
from schemas.common.Tai import Tai


class AmfInfo(BaseModel):
    amfRegionId: AmfRegionId
    amfSetId: AmfSetId
    guamiList: List[Guami]
    taiList: List[Tai] = None
    backupInfoAmfFailure: List[Guami] = None
    backupInfoAmfRemoval: List[Guami] = None
    n2InterfaceAmfInfo: N2InterfaceAmfInfo = None
