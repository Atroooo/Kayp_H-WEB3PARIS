from celery import shared_task
from django.contrib.auth.models import User


@shared_task
def delete_account_if_not_activate(user_id):
    try:
        user = User.objects.get(id=user_id)
        if not user.is_active:
            user.delete()

    except User.DoesNotExist:
        pass
