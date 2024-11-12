from flask import Blueprint, jsonify
import json

estoque_bp = Blueprint('estoque', __name__)

def ler_dados():
    with open('data.json') as f:
        return json.load(f)

@estoque_bp.route('/', methods=['GET'])
def obter_estoque():
    dados = ler_dados()
    return jsonify(dados['estoque'])

@estoque_bp.route('/<int:id>', methods=['GET'])
def obter_estoque_produto(id):
    dados = ler_dados()
    estoque = next((e for e in dados['estoque'] if e['produto_id'] == id), None)
    if estoque:
        return jsonify(estoque)
    else:
        return jsonify({"erro": "Estoque não encontrado"}), 404
