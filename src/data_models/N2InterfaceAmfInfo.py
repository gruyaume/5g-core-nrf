from typing import List

from pydantic import BaseModel

from data_models.common.AmfName import AmfName
from data_models.common.Ipv4Addr import Ipv4Addr
from data_models.common.Ipv6Addr import Ipv6Addr


class N2InterfaceAmfInfo(BaseModel):
    ipv4EndpointAddress: List[Ipv4Addr]
    ipv6EndpointAddress: List[Ipv6Addr]
    amfName: AmfName
