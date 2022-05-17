from typing import List

from pydantic import BaseModel

from data_models.N2InterfaceAmfInfo import N2InterfaceAmfInfo
from data_models.common.AmfRegionId import AmfRegionId
from data_models.common.AmfSetId import AmfSetId
from data_models.common.Guami import Guami
from data_models.common.Tai import Tai


class AmfInfo(BaseModel):
    amfRegionId: AmfRegionId
    amfSetId: AmfSetId
    guamiList: List[Guami]
    taiList: List[Tai] = None
    backupInfoAmfFailure: List[Guami] = None
    backupInfoAmfRemoval: List[Guami] = None
    n2InterfaceAmfInfo: N2InterfaceAmfInfo = None
