import os
import redis.asyncio as redis

REDIS_URL = os.getenv("REDIS_URL")
REDIS_TTL = os.getenv("REDIS_TTL")

redis_client = redis.from_url(REDIS_URL, decode_responses=True)

async def get_redis():
    return redis_client
