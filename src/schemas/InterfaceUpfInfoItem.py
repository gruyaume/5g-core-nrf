from typing import List

from pydantic import BaseModel

from schemas.Fqdn import Fqdn
from schemas.UPInterfaceType import UPInterfaceType
from schemas.common.Ipv4Addr import Ipv4Addr
from schemas.common.Ipv6Addr import Ipv6Addr


class InterfaceUpfInfoItem(BaseModel):
    interfaceType: UPInterfaceType
    ipv4EndpointAddresses: List[Ipv4Addr] = None
    ipv6EndpointAddresses: List[Ipv6Addr] = None
    endpointFqdn: Fqdn = None
    networkInstance: str = None
