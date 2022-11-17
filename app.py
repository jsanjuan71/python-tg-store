import requests
from flask import Flask, jsonify

from dotenv import load_dotenv
import os

load_dotenv()
print(os.environ["ML_API_URL"])

app = Flask(__name__)

@app.route('/')
def health_check():
    return jsonify(name="TG Store API", version="1.0.0")