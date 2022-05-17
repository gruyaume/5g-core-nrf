from typing import List

from pydantic import BaseModel

from data_models.Ipv4AddressRange import Ipv4AddressRange
from data_models.Ipv6PrefixRange import Ipv6PrefixRange
from data_models.common.Dnn import Dnn


class BsfInfo(BaseModel):
    ipv4AddressRanges: List[Ipv4AddressRange] = None
    dnnList: List[Dnn] = None
    ipDomainList: List[str] = None
    ipv6PrefixRanges: List[Ipv6PrefixRange] = None
