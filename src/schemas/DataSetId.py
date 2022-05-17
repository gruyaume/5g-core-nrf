from enum import Enum


class DataSetId(str, Enum):
    subscription = "SUBSCRIPTION"
    policy = "POLICY"
    exposure = "EXPOSURE"
    application = "APPLICATION"
