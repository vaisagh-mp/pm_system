from django.core.cache import cache
from django.conf import settings


def cache_data(key, data, timeout=settings.CACHE_TTL):
    cache.set(key, data, timeout)


def get_cached_data(key):
    return cache.get(key)


def delete_cached_data(key):
    cache.delete(key)
