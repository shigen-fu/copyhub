from datetime import datetime
from app import app, redis_client
from flask import jsonify, render_template, request

REDIS_KEY_PREFIX = 'clip:'
REDIS_KEY_EXPIRE_SES = 3600 * 10


def format_current_time(format='%m%d%H%M%S'):
    """
    默认格式化当前时间为 'MMDDhhmmss'
    :return: 格式化后的时间字符串
    """
    current_time = datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new', methods=['POST'])
def clipboard():
    data = request.form['data']
    # 将数据存储到 Redis 中
    tms = format_current_time()
    key = REDIS_KEY_PREFIX + tms
    redis_client.set(key, data, REDIS_KEY_EXPIRE_SES)
    return jsonify({'data': tms, 'success': True})


@app.route('/get', methods=['GET'])
def get():
    tms = request.args.get('code')
    key = REDIS_KEY_PREFIX + tms
    value = redis_client.get(key)
    if not value:
        return jsonify({'data': None, 'success': False})
    else:
        return jsonify({'data': value, 'success': True})
