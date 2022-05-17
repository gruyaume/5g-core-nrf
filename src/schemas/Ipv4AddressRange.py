from pydantic import BaseModel

from schemas.common.Ipv4Addr import Ipv4Addr


class Ipv4AddressRange(BaseModel):
    start: Ipv4Addr
    end: Ipv4Addr
