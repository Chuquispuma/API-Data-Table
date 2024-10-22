from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Cargar los datos desde el archivo JSON
def load_data():
    with open('datos.json', 'r') as file:
        return json.load(file)

# Guardar los datos en el archivo JSON
def save_data(data):
    with open('datos.json', 'w') as file:
        json.dump(data, file, indent=4)

# Ruta para obtener los datos con paginación
@app.route('/api/data', methods=['GET'])
def get_data():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    data = load_data()
    start = (page - 1) * per_page
    end = start + per_page
    return jsonify(data[start:end])

# Ruta para agregar un nuevo usuario
@app.route('/api/data', methods=['POST'])
def add_data():
    new_user = request.get_json()
    data = load_data()
    new_user['id'] = len(data) + 1  # Asignar un ID único
    data.append(new_user)
    save_data(data)
    return jsonify(new_user), 201

# Ruta para eliminar un usuario por ID
@app.route('/api/data/<int:user_id>', methods=['DELETE'])
def delete_data(user_id):
    data = load_data()
    data = [user for user in data if user['id'] != user_id]
    save_data(data)
    return jsonify({"message": "User deleted"}), 200

# Permitir peticiones CORS
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE'
    return response

if __name__ == '__main__':
    app.run(debug=True)
