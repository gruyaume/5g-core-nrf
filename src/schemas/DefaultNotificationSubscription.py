from pydantic import BaseModel

from schemas.NotificationType import NotificationType
from schemas.common.N1MessageClass import N1MessageClass
from schemas.common.N2InformationClass import N2InformationClass
from schemas.common.Uri import Uri


class DefaultNotificationSubscription(BaseModel):
    notificationType: NotificationType
    callbackUri: Uri
    n1MessageClass: N1MessageClass = None
    n2InformationClass: N2InformationClass = None
