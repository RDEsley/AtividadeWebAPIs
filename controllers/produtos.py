from flask import Blueprint, jsonify
import json

produto_bp = Blueprint('produtos', __name__)

def ler_dados():
    with open('data.json') as f:
        return json.load(f)

@produto_bp.route('/', methods=['GET'])
def obter_produtos():
    dados = ler_dados()
    return jsonify(dados['produtos'])

@produto_bp.route('/<int:id>', methods=['GET'])
def obter_produto(id):
    dados = ler_dados()
    produto = next((p for p in dados['produtos'] if p['id'] == id), None)
    if produto:
        return jsonify(produto)
    else:
        return jsonify({"erro": "Produto não encontrado"}), 404
