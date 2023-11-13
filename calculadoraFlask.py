from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/budget', methods=['POST'])
def budget():
    valor_placa = 1000
    request_json = request.get_json()
    valor_pacote = request_json.get('valorPacote', None)
    placas_adicionais = request_json.get('placasAdicionais', None)

    if valor_pacote is not None and placas_adicionais is not None:
        valor_budget = int(valor_pacote) + (int(placas_adicionais) * int(valor_placa))
        return jsonify(valorBudget=valor_budget)
    else:
        response = {
            'error': 'Parâmetros inválidos. Certifique-se de que valorPacote e placasAdicionais sejam números válidos e não nulos.'
        }
        return jsonify(response), 400

@app.route('/economy', methods=['POST'])
def economy():
    preco_kwh = 0.75
    geracao_placa = 90
    request_json = request.get_json()

    quantidade_placas = request_json.get('quantidadePlacas', None)
    quantidade_placas_adicionais = request_json.get('quantidadePlacasAdicionais', None)
    uso_cliente = request_json.get('usoCliente', None)

    if quantidade_placas is not None and quantidade_placas_adicionais is not None and uso_cliente is not None:
        total_placas = int(quantidade_placas) + int(quantidade_placas_adicionais)
        geracao_total = total_placas * geracao_placa
        uso_total_cliente = int(uso_cliente) * preco_kwh
        economia_total = geracao_total - uso_total_cliente

        return jsonify(economiaTotal=economia_total, custoUsoCliente=uso_total_cliente, QuantoPlacaGera=geracao_total)
    else:
        response = {
            'error': 'Parâmetros inválidos. Certifique-se de que quantidadePlacas, quantidadePlacasAdicionais e usoCliente sejam números válidos.'
        }
        return jsonify(response), 400

@app.route('/investment', methods=['POST'])
def investment():
    consumo_diario = request.json.get('consumo_diario', None)
    numero_placas = request.json.get('numero_placas', None)

    if consumo_diario is not None and numero_placas is not None and isinstance(consumo_diario, (int, float)) and isinstance(numero_placas, (int, float)):
        kwh_gerados_por_mes = numero_placas * 120
        custo_placas = numero_placas * 1000
        custo_mensal = consumo_diario * 30 * 0.75
        tempo_recuperacao_meses = round(custo_placas / (kwh_gerados_por_mes - consumo_diario * 30))

        return jsonify(custoPlacas=custo_placas, custoMensal=custo_mensal, tempoRecuperacaoMeses=tempo_recuperacao_meses)
    else:
        response = {
            'error': 'Parâmetros inválidos. Certifique-se de que consumo_diario e numero_placas sejam números válidos.'
        }
        return jsonify(response), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
