from flask import Flask, request, jsonify, abort, session, redirect, url_for, render_template

from datetime import datetime, timedelta
import os
import json



# Initialize Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a secure secret key

# File to store user details
WRK_DIR = os.getcwd()

vol = "/mnt/testvol"
vol_test = "/mnt/"
file_name = os.path.join(vol_test, "user_details.json")
if os.path.isfile(file_name):
        print(f"The file '{file_name}' exists. with os path join")
file_name = "/mnt/user_details.json"
if os.path.isfile(file_name):
        print(f"The file '{file_name}' exists. with os path join")
        
if os.path.isdir(vol):
        print(f"The directory '{vol}' exists.")
else:
        print(f"The directory '{vol}' does not exist.")
if os.path.isdir(vol_test):
        print(f"The directory '{vol_test}' exists.")
else:
        print(f"The directory '{vol_test}' does not exist.")
  
file_path = "/mnt/test/user_details.json"
if os.path.isfile(file_path):
        print(f"The file '{file_path}' exists.")
  
vol_test = os.path.join("mnt","testvol")
if os.path.isdir(vol_test):
        print(f"The directory '{vol_test}' exists.")
else:
        print(f"The directory '{vol_test}' does not exist.")
file_name = os.path.join(vol_test, "user_details.json")
if os.path.isfile(file_name):
        print(f"The file '{file_name}' exists. with os path join")

      
@app.route("/user/", methods=["GET"])
def get_user(): 
    file_name = "/mnt/user_details.json"
    with open(file_name, "r") as file:
            data= json.load(file) 
    return jsonify({"user": data})

@app.route("/chat/", methods=["POST])
def chat_res(): 
    req = request.get_json()
    
    # Extract parameters from Dialogflow request
    intent_name = req["queryResult"]["intent"]["displayName"]
    parameters = req["queryResult"]["parameters"]
    subject = parameters.get("subject", "")
    user_query = parameters.get("user_query", "")
    answer = f"ansewr to {user_query} and intent {intent_name}"
    
    return jsonify({"fulfillmentText": "answer"})

@app.route("/")
def home():
    return render_template("home.html")  



# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
