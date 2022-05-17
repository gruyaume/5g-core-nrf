from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch
import os

BASE_URL = f"nnrf-nfm/v1"
NF_INSTANCE_ENDPOINT = f"{BASE_URL}/nf-instances"
CORRECT_UUID = "bab530a7-1ede-413e-8437-ca07797e258e"
CORRECT_NF_TYPE = "AMF"
CORRECT_NF_STATUS = "REGISTERED"


@patch.dict(os.environ, {"PROJECT_NAME": "ROUGE"})
def test_given_bad_instance_id_format_when_register_nf_then_400_error_is_thrown():
    client = TestClient(app)
    instance_id = "abcdef"
    nf_instance = {
        "nfInstanceID": instance_id,
        "nfType": CORRECT_NF_TYPE,
        "nfStatus": CORRECT_NF_STATUS
    }
    aa = f"{NF_INSTANCE_ENDPOINT}/{instance_id}"
    print(aa)
    response = client.put(f"{NF_INSTANCE_ENDPOINT}/{instance_id}", json=nf_instance)

    assert response.status_code == 400


# def test_given_nfinstance_contains_bad_nf_type_when_register_nf_then_400_error_is_thrown():
#     client = TestClient(app)
#     bad_nf_type = "whatever"
#     nf_instance = {
#         "nfInstanceID": CORRECT_UUID,
#         "nfType": bad_nf_type,
#         "nfStatus": CORRECT_NF_STATUS
#     }
#
#     response = client.put(f"{NF_INSTANCE_ENDPOINT}/{CORRECT_UUID}", json=nf_instance)
#
#     assert response.status_code == 400
#
#
# def test_given_nfinstance_contains_bad_nfstatus_when_register_nf_then_400_error_is_thrown():
#     client = TestClient(app)
#     bad_nf_status = "whatever"
#
#     nf_instance = {
#         "nfInstanceID": CORRECT_UUID,
#         "nfType": CORRECT_NF_TYPE,
#         "nfStatus": bad_nf_status
#     }
#
#     response = client.put(f"{NF_INSTANCE_ENDPOINT}/{CORRECT_UUID}", json=nf_instance)
#
#     assert response.status_code == 400
#
#
# def test_given_correct_nfinstance_when_register_nf_then_201_created_is_returned():
#     client = TestClient(app)
#
#     nf_instance = {
#         "nfInstanceID": CORRECT_UUID,
#         "nfType": CORRECT_NF_TYPE,
#         "nfStatus": CORRECT_NF_STATUS
#     }
#
#     response = client.put(f"{NF_INSTANCE_ENDPOINT}/{CORRECT_UUID}", json=nf_instance)
#
#     assert response.status_code == 201
#
#
# def test_given_correct_nfinstance_when_register_nf_then_content_location_is_returned_in_http_header():
#     client = TestClient(app)
#
#     nf_instance = {
#         "nfInstanceID": CORRECT_UUID,
#         "nfType": CORRECT_NF_TYPE,
#         "nfStatus": CORRECT_NF_STATUS
#     }
#
#     response = client.put(f"{NF_INSTANCE_ENDPOINT}/{CORRECT_UUID}", json=nf_instance)
#
#     assert response.headers["location"] == f"/nf-instances/{CORRECT_UUID}"
