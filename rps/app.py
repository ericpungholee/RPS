from flask import Flask, render_template, request, flash
import random

app = Flask(__name__)
app.secret_key = ""

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/rps", methods=["POST", "GET"])
def rps():
    choices = ["✊", "✋", "✌️"]
    computer = random.choice(choices)
    user = request.form.get("user")

    if user == computer:
        flash(f"Computer: {computer} | You: {user} | Tie!🥱")
        return render_template("index.html")
    elif (computer == "✊" and user == "✋") or (computer == "✋" and user == "✌️") or (computer == "✌️" and user == "✊"):
        flash(f"Computer: {computer} | You: {user} | You've won!🎊")
        return render_template("index.html")
    else:
        flash(f"Computer: {computer} | You: {user} | You've lost!👎")
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

