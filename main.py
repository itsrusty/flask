from flask import Flask, jsonify
import os
# from config import config

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "testing_message"})

@app.route("/testing")
def testing():
    return "testing web app"
    
@app.route("/add/<string:product_name>", methods=['POST'])
def add(product_name):
    # pass
    if product_name == "hiram":
        return jsonify({"message": "testeando app"})
    else:
        return jsonify({"message": "test"})

if __name__ == "__main__":
    # app.run(debug=True)
     app.run(debug=True, port=os.getenv("PORT", default=5000))
