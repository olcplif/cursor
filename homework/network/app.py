from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello World!"


@app.route('/hello', methods=["GET", "POST"])
def hello():
    return 'Hello again!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
