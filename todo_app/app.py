import os
from flask import Flask
app = Flask(__name__)

port = int(os.getenv('PORT', 3000))

@app.route('/')
def hello():
    return 'Server started'

if __name__ == '__main__':
    print(f"Server started in port {port}")
    app.run(host='0.0.0.0', port=port)
