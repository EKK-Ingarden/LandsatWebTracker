import asyncio
from datetime import date
from enum import Enum

import resend

from backend.database import get_db
from backend.models import PixelWatch


class Notification(Enum):
    EMAIL = 1
    PUSH = 2


async def run_every_hour():
    while True:
        print("Sending notifications processing...")

        db = next(get_db())

        today = date.today()

        user_pixel_watches = db.query(PixelWatch).all()

        for watch in user_pixel_watches:
            if watch.datetime.date() == today:
                NotificationService.sendEmailNotification(
                    watch.user, {"coordinates": [watch.latitude, watch.longitude], "time_left": "today"}
                )
                db.delete(watch)

        db.commit()

        await asyncio.sleep(3600)


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
            "to": [f"{user.email}"],
            "subject": "Landsat notification",
            "html": f"{content}",
        }
        resend.Emails.send(params)
        return

    @staticmethod
    def sendPushNotification(user, message):
        raise NotImplementedError("Push notification not implemented")
