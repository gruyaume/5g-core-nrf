from pydantic import BaseModel

from schemas.common.Ipv6Prefix import Ipv6Prefix


class Ipv6PrefixRange(BaseModel):
    start: Ipv6Prefix
    end: Ipv6Prefix
