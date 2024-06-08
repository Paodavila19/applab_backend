from flask import Flask, request, jsonify
from flask_cors import CORS

from model.pacientes import (
    get_pacientes,
    get_paciente,
    create_paciente,
    delete_paciente,
    update_paciente,
)

from model.registros import (
    get_registros,
    get_registro,
    create_resgistro,
    update_registro,
    delete_registro
)

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def list_pacientes():
    retorno = get_pacientes()
    return jsonify(retorno)

@app.route('/<int:paciente_id>', methods=['GET'])
def get_pac_by_id(paciente_id):
    return jsonify(get_paciente(paciente_id))


@app.route('/', methods=['POST'])
def create_pac():
    data = request.get_json()
    tipo_id = data['tipo_id']
    nombre = data['nombre']
    email = data['email']
    tipo_sangre = data['tipo_sangre']
    genero = data['genero']
    edad = data['edad']
    fecha_nacimiento = data['fecha_nacimiento']
    dir = data['dir']
    celular = data['celular']
    eps = data['eps']
    return jsonify(create_paciente(tipo_id, nombre, email, tipo_sangre, genero, edad, fecha_nacimiento, dir, celular, eps))

@app.route('/<int:paciente_id>', methods=['PUT'])
def update_pac(paciente_id):
    data = request.get_json()
    tipo_id = data['tipo_id']
    nombre = data['nombre']
    email = data['email']
    tipo_sangre = data['tipo_sangre']
    genero = data['genero']
    edad = data['edad']
    fecha_nacimiento = data['fecha_nacimiento']
    dir = data['dir']
    celular = data['celular']
    eps = data['eps']
    return jsonify(update_paciente(tipo_id, nombre, email, tipo_sangre, genero, edad, fecha_nacimiento, dir, celular, eps, paciente_id))

@app.route('/<int:paciente_id>', methods=['DELETE'])
def delete_pac(paciente_id):
    return jsonify(delete_paciente(paciente_id))

# REGISTROS

@app.route('/registros', methods=['GET'])
def list_registros():
    retorno = get_registros()
    return jsonify(retorno)

@app.route('/registros/<int:registro_id>', methods=['GET'])
def get_reg_by_id(registro_id):
    return jsonify(get_registro(registro_id))


@app.route('/registros', methods=['POST'])
def create_reg():
    data = request.get_json()
    id_paciente = data['id_paciente']
    personal = data['personal']
    cargo = data['cargo']
    prueba = data['prueba']
    valor_resultado = data['valor_resultado']
    unidad_resultado = data['unidad_resultado']
    return jsonify(create_resgistro(id_paciente, personal, cargo, prueba, valor_resultado, unidad_resultado))

@app.route('/registros/<int:registro_id>', methods=['PUT'])
def update_reg(registro_id):
    data = request.get_json()
    id_paciente = data['id_paciente']
    personal = data['personal']
    cargo = data['cargo']
    prueba = data['prueba']
    valor_resultado = data['valor_resultado']
    unidad_resultado = data['unidad_resultado']
    return jsonify(update_registro(id_paciente, personal, cargo, prueba, valor_resultado, unidad_resultado, registro_id))

@app.route('/registros/<int:registro_id>', methods=['DELETE'])
def delete_reg(registro_id):
    return jsonify(delete_registro(registro_id))


    