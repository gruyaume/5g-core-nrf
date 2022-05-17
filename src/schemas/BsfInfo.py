from typing import List

from pydantic import BaseModel

from schemas.Ipv4AddressRange import Ipv4AddressRange
from schemas.Ipv6PrefixRange import Ipv6PrefixRange
from schemas.common.Dnn import Dnn


class BsfInfo(BaseModel):
    ipv4AddressRanges: List[Ipv4AddressRange] = None
    dnnList: List[Dnn] = None
    ipDomainList: List[str] = None
    ipv6PrefixRanges: List[Ipv6PrefixRange] = None
