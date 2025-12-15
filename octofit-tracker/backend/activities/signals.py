from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Activity

@receiver(post_save, sender=Activity)
def update_profile_points(sender, instance, created, **kwargs):
    if created:
        profile = instance.user.profile
        profile.total_points += instance.points
        profile.save()