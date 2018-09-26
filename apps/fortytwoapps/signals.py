from django.db.models.signals import post_save, post_delete
from fortytwoapps.models import ObjectLog
from django.dispatch import receiver
from django.conf import settings


@receiver(post_save, dispatch_uid=settings.UID)
def object_log_post_save(sender, instance, created, raw, **kwargs):
    if raw or sender == ObjectLog:
        return

    action = 'created' if created else 'updated'
    ObjectLog.objects.create(appname=instance._meta.app_label,
                             objectname=instance._meta.object_name,
                             action=action)


@receiver(post_delete, dispatch_uid=settings.UID)
def object_log_post_delete(sender, instance, **kwargs):
    if sender == ObjectLog:
        return

    action = 'deleted'
    ObjectLog.objects.create(appname=instance._meta.app_label,
                             objectname=instance._meta.object_name,
                             action=action)
