from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/procesar', methods=['POST'])
def procesar():
    datos = request.get_json() or {}
    entrada = datos.get('entrada', '')
    
    # Lógica de procesamiento
    resultado = f"Resultado procesado: {entrada.upper()}"
    
    return jsonify({'status': 'ok', 'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)