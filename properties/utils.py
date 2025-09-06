import logging
from django_redis import get_redis_connection

from properties.models import Property
from django.core.cache import cache

logger = logging.getLogger(__name__)


def get_redis_cache_metrics():
    """
    Retrieve and analyze Redis cache metrics including hits, misses, and hit
    ratio.

    Returns:
        dict: Dictionary containing cache metrics:
            - hits (int): Number of successful key lookups
            - misses (int): Number of failed key lookups
            - hit_ratio (float): Ratio of hits to total requests
             (hits / (hits + misses))
    """

    try:
        redis_conn = get_redis_connection("default")
        info = redis_conn.info("stats")

        hits = info.get("keyspace_hits", 0)
        misses = info.get("keyspace_misses", 0)
        total_requests = hits + misses
        hit_ratio = (hits / total_requests) if total_requests > 0 else 0.0

        logger.info(
            f"Cache metrics - Hits: {hits}, Misses: {misses}, "
            f"Hit Ratio: {hit_ratio:.2%}"
        )

        return {
            "hits": hits,
            "misses": misses,
            "hit_ratio": hit_ratio,
        }
    except Exception as e:
        logger.error(f"Error retrieving Redis cache metrics: {e}")
        return {
            "hits": 0,
            "misses": 0,
            "hit_ratio": 0.0,
        }


def get_all_properties():
    """
    Retrieve all properties from cache if available, otherwise fetch from
    database.
    Caches the queryset for 1 hour (3600 seconds).

    Returns:
        QuerySet: A queryset of all Property objects
    """

    cache_key = "all_properties"
    properties = cache.get(cache_key)

    if properties is None:
        properties = Property.objects.all()
        cache.set(cache_key, properties, timeout=3600)  # Cache for 1 hour

    return properties
