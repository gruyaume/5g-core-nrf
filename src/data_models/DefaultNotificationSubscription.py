from pydantic import BaseModel

from data_models.NotificationType import NotificationType
from data_models.common.N1MessageClass import N1MessageClass
from data_models.common.N2InformationClass import N2InformationClass
from data_models.common.Uri import Uri


class DefaultNotificationSubscription(BaseModel):
    notificationType: NotificationType
    callbackUri: Uri
    n1MessageClass: N1MessageClass = None
    n2InformationClass: N2InformationClass = None
