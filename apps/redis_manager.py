# app/redis_manager.py
import redis

def get_redis_connection():
    return redis.StrictRedis(host='ws', port=8000, db=0)
