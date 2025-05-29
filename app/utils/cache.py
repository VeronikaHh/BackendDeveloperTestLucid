from cachetools import TTLCache

post_cache = TTLCache(maxsize=100, ttl=300)
