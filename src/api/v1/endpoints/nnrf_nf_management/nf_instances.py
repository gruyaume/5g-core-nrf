from uuid import UUID

from fastapi import APIRouter, Response

from data_models.NFProfile import NFProfile

router = APIRouter()


@router.put(
    path="/{instance_id}",
    tags=["Nnrf_NFManagement"],
    status_code=201,
    response_model=NFProfile
)
async def register_nf(instance_id: UUID, nf_instance: NFProfile, response: Response):
    """
    This service operation is used:
        - to register an NF in the NRF by providing the NF profile of the requesting NF to the NRF,
        and the NRF marks the requesting NF as available to be discovered by other NFs;
        - to register services associated to an existing NF Instance;
        - to register NRF information in another NRF, and this information is used for forwarding
        or redirecting service discovery request.

    Note: For now, it only allows registering standard nf types (no custom ones)

    """
    response.headers["Location"] = f"/nf-instances/{instance_id}"
    return nf_instance


@router.patch(
    path="/{instance_id}",
    tags=["Nnrf_NFManagement"],
    status_code=201,
    response_model=NFProfile
)
async def register_nf(instance_id: UUID, nf_instance: NFProfile, response: Response):
    """
    This service operation updates the profile of a Network Function previously registered in the
    NRF by providing the updated NF profile of the requesting NF to the NRF. The update operation
    may **only** apply to a subset of the parameters of the profile (including
    adding/deleting/replacing services to the NF profile).

    """
    return "Not implemented"
