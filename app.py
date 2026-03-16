from flask import Flask, jsonify
from assistente import AssistenteMaratona

app = Flask(__name__)
assistente = AssistenteMaratona()

@app.route('/')
def index():
    dados = assistente.listar_favoritas()
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True, port=5000)