from flask import Blueprint, jsonify
import json

cliente_bp = Blueprint('clientes', __name__)

# Função que lê os dados do arquivo JSON
def ler_dados():
    with open('data.json') as f:
        return json.load(f)

# Rota para obter todos os clientes
@cliente_bp.route('/', methods=['GET'])
def obter_clientes():
    dados = ler_dados()
    return jsonify(dados['clientes'])

# Rota para obter um cliente específico pelo ID
@cliente_bp.route('/<int:id>', methods=['GET'])
def obter_cliente(id):
    dados = ler_dados()
    cliente = next((c for c in dados['clientes'] if c['id'] == id), None)
    if cliente:
        return jsonify(cliente)
    else:
        return jsonify({"erro": "Cliente não encontrado"}), 404
