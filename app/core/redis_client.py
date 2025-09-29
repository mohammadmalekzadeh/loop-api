import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")
REDIS_TTL = os.getenv("REDIS_TTL")

redis_client = None

async def get_redis():
    global redis_client
    
    if not REDIS_URL:
        return None

    import redis.asyncio as redis
    
    if not redis_client:
        redis_client = redis.from_url(REDIS_URL, decode_responses=True)
    
    return redis_client
