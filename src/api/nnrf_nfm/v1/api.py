from fastapi import APIRouter

from api.nnrf_nfm.v1.endpoints import nf_instances

api_router = APIRouter()
api_router.include_router(nf_instances.router, prefix="/nnrf-nfm/v1/nf-instances", tags=["nf_instances"])
