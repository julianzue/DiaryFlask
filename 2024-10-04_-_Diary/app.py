from flask import Flask, render_template, request
import time


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():

    if request.method == "POST":
        if "add" in request.form:
            text = request.form.get("text")
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")

            with open("static/data.txt", "a") as file:
                file.write(current_time + " | " + text + "\n")

    try:
        with open("static/data.txt", "r") as file:
            lines = file.readlines()
    except Exception:
        lines = []


    return render_template("home.html", lines=lines)


if __name__ == "__main__":
    app.run(debug=True)