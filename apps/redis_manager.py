# app/redis_manager.py
import redis

def get_redis_connection():
    return redis.StrictRedis(host='localhost', port=6379, db=0)
