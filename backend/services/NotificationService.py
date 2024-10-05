from enum import Enum

import resend

from backend.settings import settings


class Notification(Enum):
    EMAIL = 1
    PUSH = 2


resend.api_key = settings.resend_api_key


class NotificationService:
    @staticmethod
    def sendNotification(user, message, notification_type: Notification):
        match notification_type:
            case Notification.EMAIL:
                NotificationService.sendEmailNotification(user, message)
                return

            case Notification.PUSH:
                NotificationService.sendPushNotification(user, message)
                return

    @staticmethod
    def sendEmailNotification(user, message):
        with open("backend/assets/email/template.html") as template:
            content = template.read()
            content = content.replace("{{ message.coordinates }}", f"{message['coordinates']}")
            content = content.replace("{{ message.time_left }}", f"{message['time_left']}")

        params: resend.Emails.SendParams = {
            "from": "Notifications staff <notifications@landsat.wyniki.zip>",
            "to": [f"{user['email']}"],
            "subject": "Landsat notification",
            "html": f"{content}",
        }
        email = resend.Emails.send(params)
        print(email)
        return

    @staticmethod
    def sendPushNotification(user, message):
        raise NotImplementedError("Push notification not implemented")
        return
