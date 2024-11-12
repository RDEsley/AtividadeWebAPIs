from flask import Blueprint, jsonify
import json

pedido_bp = Blueprint('pedidos', __name__)

def ler_dados():
    with open('data.json') as f:
        return json.load(f)

@pedido_bp.route('/', methods=['GET'])
def obter_pedidos():
    dados = ler_dados()
    return jsonify(dados['pedidos'])

@pedido_bp.route('/<int:id>', methods=['GET'])
def obter_pedido(id):
    dados = ler_dados()
    pedido = next((p for p in dados['pedidos'] if p['id'] == id), None)
    if pedido:
        return jsonify(pedido)
    else:
        return jsonify({"erro": "Pedido não encontrado"}), 404
