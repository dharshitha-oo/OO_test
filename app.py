from flask import Flask, request, jsonify, abort, session, redirect, url_for
import requests 
from datetime import datetime, timedelta
import os
import json
from urllib.parse import urlparse


# Initialize Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a secure secret key

# File to store user details
WRK_DIR = os.getcwd()

vol = "/mnt/testvol"
vol_test = "/mnt/"
if os.path.isdir(vol):
        print(f"The directory '{vol}' exists.")
else:
        print(f"The directory '{vol}' does not exist.")
if os.path.isdir(vol_test):
        print(f"The directory '{vol_test}' exists.")
else:
        print(f"The directory '{vol_test}' does not exist.")
  
file_path = "/mnt/testvol/user_details.json"
if os.path.isfile(file_path):
        print(f"The file '{file_path}' exists.")
  
vol_test = os.path.join("mnt","testvol")
if os.path.isdir(vol_test):
        print(f"The directory '{vol_test}' exists.")
    else:
        print(f"The directory '{vol_test}' does not exist.")
file_name = os.path.join(vol_test, "user_details.json")
if os.path.isfile(file_path):
        print(f"The file '{file_path}' exists. with os path join")

      
@app.route("/user/", methods=["GET"])
def get_user(): 
    with open(file_name, "r") as file:
            data= json.load(file) 
      
   
    return jsonify({"user": data})



# Run the app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
