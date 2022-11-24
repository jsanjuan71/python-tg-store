
from flask import Flask, jsonify, request
from models.product import Product
from services.products import ProductService
from dotenv import load_dotenv

load_dotenv()

productService = ProductService()

app = Flask(__name__)

@app.route('/')
def health_check():
    return jsonify(name="TG Store API", version="1.0.0")

@app.route('/products', methods=['GET'])
def get_products():
    try:
        keyword = request.args.get("keyword", default=None, type=str)
        found = productService.searchByKeyword( keyword )
        return jsonify( found )
    except Exception as error:
        return jsonify( done=False, error = str(error) )


@app.route('/products', methods=['POST'])
def create_product():
    return jsonify("TODO create product")