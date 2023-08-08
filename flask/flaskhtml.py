from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>This is a title</h1>"

@app.route("/postoption", methods=["GET", "POST"])
def posto():
    response = request.method
    return f"Method is {response}"

# Every single app will have the following 2 lines of code exactly
if __name__ == "__main__":
    app.run(debug=True, host ="0.0.0.0", port=5000)