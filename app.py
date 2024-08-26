from flask import Flask, render_template, request
from project import generate_response, load_data

app = Flask(__name__)

data = load_data()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    return generate_response(user_input, data)

if __name__ == "__main__":
    app.run(debug=True)
