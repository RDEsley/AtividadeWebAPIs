from flask import Flask, jsonify
from controllers.clientes import cliente_bp
from controllers.produtos import produto_bp
from controllers.pedidos import pedido_bp
from controllers.estoque import estoque_bp
from controllers.entregas import entrega_bp
from controllers.pagamentos import pagamento_bp

app = Flask(__name__)

# Registrando os blueprints (controllers) para cada entidade
app.register_blueprint(cliente_bp, url_prefix='/api/clientes')
app.register_blueprint(produto_bp, url_prefix='/api/produtos')
app.register_blueprint(pedido_bp, url_prefix='/api/pedidos')
app.register_blueprint(estoque_bp, url_prefix='/api/estoque')
app.register_blueprint(entrega_bp, url_prefix='/api/entregas')
app.register_blueprint(pagamento_bp, url_prefix='/api/pagamentos')

if __name__ == '__main__':
    app.run(debug=True)
