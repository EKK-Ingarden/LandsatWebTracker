from enum import Enum


class Notification(Enum):
    EMAIL = 1
    PUSH = 2


class NotificationService:
    @staticmethod
    def sendNotification(user, message, notificationType: Notification):
        match notificationType:
            case Notification.EMAIL:
                NotificationService.sendEmailNotification(user, message)
                return

            case Notification.PUSH:
                NotificationService.sendPushNotification(user, message)
                return

    @staticmethod
    def sendEmailNotification(user, message):
        raise NotImplementedError("Email notification not implemented")
        return

    @staticmethod
    def sendPushNotification(user, message):
        raise NotImplementedError("Push notification not implemented")
        return