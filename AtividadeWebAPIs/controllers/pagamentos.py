from flask import Blueprint, jsonify
import json

pagamento_bp = Blueprint('pagamentos', __name__)

def ler_dados():
    with open('data.json') as f:
        return json.load(f)

@pagamento_bp.route('/', methods=['GET'])
def obter_pagamentos():
    dados = ler_dados()
    return jsonify(dados['pagamentos'])

@pagamento_bp.route('/<int:id>', methods=['GET'])
def obter_pagamento(id):
    dados = ler_dados()
    pagamento = next((p for p in dados['pagamentos'] if p['id'] == id), None)
    if pagamento:
        return jsonify(pagamento)
    else:
        return jsonify({"erro": "Pagamento não encontrado"}), 404
