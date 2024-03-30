from flask import Flask
from redis import StrictRedis, ConnectionPool

app = Flask(__name__)

# 配置 Redis 连接池
redis_pool = ConnectionPool(host='localhost', port=6379, decode_responses=True)
redis_client = StrictRedis(connection_pool=redis_pool)

from app import views
