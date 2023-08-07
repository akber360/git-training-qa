from flask import Flask

app =Flask(__name__)
@app.route("/")
def home():
    return "something"

@app.route("/number/<int:number>")
def number(number):
    number = number *number 
    return number

@app.route('/about')
def about():
    return 'This is the about page'


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)