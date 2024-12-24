from flask import Flask, request, jsonify
from app.services.product_service import ProductService
from app.models.product import Product  # Import the Product model

app = Flask(__name__)
product_service = ProductService()

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = product_service.create_product(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        category_id=data['category_id'],
        brand_id=data['brand_id']
    )
    return jsonify(product.__dict__), 201

@app.route('/products', methods=['GET'])
def get_all_products():
    products = product_service.get_all_products()
    return jsonify([product.__dict__ for product in products]), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = product_service.get_product(product_id)
    if product:
        return jsonify(product.__dict__), 200
    return jsonify({'error': 'Product not found'}), 404

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    updated_product = product_service.update_product(product_id, Product(
        None, data['name'], data['description'], data['price'], data['category_id'], data['brand_id']
    ))
    if updated_product:
        return jsonify(updated_product.__dict__), 200
    return jsonify({'error': 'Product not found'}), 404

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_service.delete_product(product_id):
        return jsonify({'message': 'Product deleted'}), 204
    return jsonify({'error': 'Product not found'}), 404