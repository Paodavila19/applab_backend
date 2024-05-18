from flask import Flask, request, jsonify
from flask_cors import CORS

from model.company import (
    get_companies,
    get_company,
    create_company,
    get_company_by_name,
    update_company,
    delete_company,
)

from model.users import (
    get_users,
    get_user,
    create_user,
    update_user,
    delete_user,
)

app = Flask(__name__)
CORS(app)

@app.route('/companies', methods=['GET'])
def list_companies():
    retorno = get_companies()
    return jsonify(retorno)

@app.route('/companies/<int:company_id>', methods=['GET'])
def get_company_by_id(company_id):
    return jsonify(get_company(company_id))

@app.route('/companies/by_name/<company_name>', methods=['GET'])
def get_company_by_name(company_name):
    return jsonify(get_company_by_name(company_name))

@app.route('/companies', methods=['POST'])
def create_company():
    data = request.get_json()
    name = data['name']
    description = data['description']
    return jsonify(create_company(name, description))

@app.route('/companies/<int:company_id>', methods=['PUT'])
def update_company(company_id):
    data = request.get_json()
    name = data['name']
    description = data['description']
    return jsonify(update_company(name, description, company_id))

@app.route('/companies/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    return jsonify(delete_company(company_id))

@app.route('/users', methods=['GET'])
def list_users():
    retorno = get_users()
    return jsonify(retorno)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_users(user_id):
    return jsonify(get_user(user_id))

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data['name']
    lastname = data['lastname']
    return jsonify(create_user(name, lastname))

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data['name']
    lastname = data['lastname']
    return jsonify(update_user(name, lastname, user_id))

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return jsonify(delete_user(user_id))
