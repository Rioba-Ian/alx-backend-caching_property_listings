from .models import Property
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver([post_save, post_delete], sender=Property)
def invalidate_properties_cache(sender, **kwargs):
    """
    Invalidate the cache for all properties when a Property instance is saved
    or deleted.
    """

    cache.delete("all_properties_cache")
