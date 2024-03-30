from app import app

if __name__ == '__main__':
    app.run(debug=False, port=10002, host='0.0.0.0')

# nohup python3 run.py > app.log 2>&1 &
