from .utils import getting_notifications

def unseen_notifications(request):
    return {'unseen_notifications': getting_notifications(request.user)}