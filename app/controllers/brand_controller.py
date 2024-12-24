from flask import Flask, request, jsonify
from app.services.brand_service import BrandService

app = Flask(__name__)
brand_service = BrandService()

@app.route('/brands', methods=['POST'])
def create_brand():
    data = request.json
    brand = brand_service.create_brand(name=data['name'])
    return jsonify(brand.__dict__), 201

@app.route('/brands', methods=['GET'])
def get_all_brands():
    brands = brand_service.get_all_brands()
    return jsonify([brand.__dict__ for brand in brands]), 200

@app.route('/brands/<int:brand_id>', methods=['GET'])
def get_brand(brand_id):
    brand = brand_service.get_brand(brand_id)
    if brand:
        return jsonify(brand.__dict__), 200
    return jsonify({'error': 'Brand not found'}), 404