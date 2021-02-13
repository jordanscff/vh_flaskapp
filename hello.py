from flask import Flask, request
import sys

app = Flask(__name__)


@app.route('/licence', methods=['POST'])
def hello():
    print(request.get_json(), flush=True)
    return "hello"

if __name__ == '__main__':
    app.run(port=5001)
