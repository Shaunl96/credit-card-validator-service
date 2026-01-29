from flask import Flask, render_template, request
from validator import is_valid_credit_card

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        card_number = request.form.get("card_number")
        if card_number:
            result = "Valid" if is_valid_credit_card(card_number) else "Invalid"

    return render_template("index.html", result=result)

@app.route("/health", methods=["GET"])
def health():
    return "OK", 200    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)