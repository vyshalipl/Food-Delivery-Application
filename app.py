from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Food Delivery Backend Running"})

@app.route("/menu")
def menu():
    return jsonify({"items": ["Pizza", "Burger", "Pasta"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
