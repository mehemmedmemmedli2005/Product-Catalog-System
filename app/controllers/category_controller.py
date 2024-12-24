from flask import Flask, request, jsonify
from app.services.category_service import CategoryService

app = Flask(__name__)
category_service = CategoryService()

@app.route('/categories', methods=['POST'])
def create_category():
    data = request.json
    category = category_service.create_category(name=data['name'])
    return jsonify(category.__dict__), 201

@app.route('/categories', methods=['GET'])
def get_all_categories():
    categories = category_service.get_all_categories()
    return jsonify([category.__dict__ for category in categories]), 200

@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = category_service.get_category(category_id)
    if category:
        return jsonify(category.__dict__), 200
    return jsonify({'error': 'Category not found'}), 404