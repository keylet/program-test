from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/procesar', methods=['POST'])
def procesar():
    dato = request.form['dato']
    resultado = f"Dato recibido: {dato.upper()}"
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
