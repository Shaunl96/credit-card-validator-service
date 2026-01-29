from flask import Flask, request, render_template
from validator import is_valid_credit_card

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/validate")
def validate():
    card_number = request.args.get("cardNumber", "")
    if not card_number.isdigit():
        return {"error": "Invalid input"}, 400

    result = is_valid_credit_card(card_number)
    return {"cardNumber": card_number, "valid": result}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
