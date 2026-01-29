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

if __name__ == "__main__":
    app.run(debug=True)