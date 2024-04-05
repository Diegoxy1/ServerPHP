from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.php')

@app.route('/verificar_descricao', methods=['POST'])
def verificar_descricao():
    descricao = request.form.get('descricao')

    if descricao:
        # Aqui você pode adicionar qualquer lógica adicional de validação
        return jsonify({'status': 'success', 'message': 'Descrição preenchida com sucesso!'})
    else:
        return jsonify({'status': 'error', 'message': 'A descrição não foi preenchida!'})

if __name__ == '__main__':
    app.run(debug=True)