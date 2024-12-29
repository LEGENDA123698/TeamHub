from .models import Notification

def getting_notifications(user):
    if user.is_authenticated:
        unseen_notifications = Notification.objects.exclude(seen_users=user)
        return unseen_notifications
    else:
        return None