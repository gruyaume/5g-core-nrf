from pydantic import BaseModel

from data_models.TransportProtocol import TransportProtocol
from data_models.common.Ipv4Addr import Ipv4Addr
from data_models.common.Ipv6Addr import Ipv6Addr


class IpEndPoint(BaseModel):
    ipv4Address: Ipv4Addr = None
    ipv6Address: Ipv6Addr = None
    transport: TransportProtocol = None
    port: int = None
