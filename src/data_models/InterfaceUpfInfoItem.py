from typing import List

from pydantic import BaseModel

from data_models.Fqdn import Fqdn
from data_models.UPInterfaceType import UPInterfaceType
from data_models.common.Ipv4Addr import Ipv4Addr
from data_models.common.Ipv6Addr import Ipv6Addr


class InterfaceUpfInfoItem(BaseModel):
    interfaceType: UPInterfaceType
    ipv4EndpointAddresses: List[Ipv4Addr] = None
    ipv6EndpointAddresses: List[Ipv6Addr] = None
    endpointFqdn: Fqdn = None
    networkInstance: str = None
