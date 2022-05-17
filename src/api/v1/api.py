from fastapi import APIRouter

from api.v1.endpoints.nnrf_nf_management import nf_instances

api_router = APIRouter()
api_router.include_router(nf_instances.router, prefix="/nf-instances", tags=["nf_instances"])
