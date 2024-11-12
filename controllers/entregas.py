from flask import Blueprint, jsonify
import json

entrega_bp = Blueprint('entregas', __name__)

def ler_dados():
    with open('data.json') as f:
        return json.load(f)

@entrega_bp.route('/', methods=['GET'])
def obter_entregas():
    dados = ler_dados()
    return jsonify(dados['entregas'])

@entrega_bp.route('/<int:id>', methods=['GET'])
def obter_entrega(id):
    dados = ler_dados()
    entrega = next((e for e in dados['entregas'] if e['id'] == id), None)
    if entrega:
        return jsonify(entrega)
    else:
        return jsonify({"erro": "Entrega não encontrada"}), 404
