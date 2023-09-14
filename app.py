from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///person.db'
db.init_app(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

with app.app_context():
    db.create_all()

# create a user
@app.route('/api/', methods=['POST'])
def create_person():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'message': 'Name is required'}), 400

    person = Person(name=name)
    db.session.add(person)
    db.session.commit()

    return jsonify({'message': 'Person created successfully',
                    "id": person.id}), 201

# create a user with name
@app.route('/api/<string:name>', methods=['POST'])
def create_person_by_name(name):
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'message': 'Name is required'}), 400

    person = Person(name=name)
    db.session.add(person)
    db.session.commit()

    return jsonify({'message': 'Person created successfully',
                    'id': person.id}), 201

# Get a person by ID
@app.route('/api/<int:id>', methods=['GET'])
def get_person(id):
    person = Person.query.get(id)

    if not person:
        return jsonify({'message': 'Person not found'}), 404

    person_data = {
        'id': person.id,
        'name': person.name,
    }

    return jsonify(person_data)

# Get a person by name
@app.route('/api/<string:name>', methods=['GET'])
def get_person_by_name(name):
    person = Person.query.filter_by(name=name).first()

    if not person:
        return jsonify({'message': 'Person not found'}), 404

    person_data = {
        'id': person.id,
        'name': person.name,
    }

    return jsonify(person_data), 200

# Update a person by ID
@app.route('/api/<int:id>', methods=['PUT'])
def update_person(id):
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'message': 'Name is required'}), 400

    person = db.session.get(id)

    if not person:
        return jsonify({'message': 'Person not found'}), 404

    person.name = name
    db.session.commit()

    return jsonify({'message': 'Person updated successfully'}), 200

# Update a person by name
@app.route('/api/<string:name>', methods=['PUT'])
def update_person_by_name(name):
    data = request.get_json()
    new_name = data.get('new_name')  # The updated name

    if not new_name:
        return jsonify({'message': 'New Name is required'}), 400
    
    if new_name is not None and not isinstance(new_name, str):
        return jsonify({'message': 'New name should be a string'}), 400

    person = Person.query.filter_by(name=name).first()

    if not person:
        return jsonify({'message': 'Person not found'}), 404
    
    person.name = new_name if new_name else person.name

    db.session.commit()

    return jsonify({'message': 'Person updated successfully'}), 200

# Delete a person by ID
@app.route('/api/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = Person.query.get(id)

    if not person:
        return jsonify({'message': 'Person not found'}), 404

    db.session.delete(person)
    db.session.commit()

    return jsonify({'message': 'Person deleted successfully'})

# Delete a person by name
@app.route('/api/<string:name>', methods=['DELETE'])
def delete_person_by_name(name):
    if not name:
        return jsonify({'message': 'Name is required'}), 400

    person = Person.query.filter_by(name=name).first()

    if not person:
        return jsonify({'message': 'Person not found'}), 404

    db.session.delete(person)
    db.session.commit()

    return jsonify({'message': 'Person deleted successfully'})

# Get all persons
@app.route('/api/persons', methods=['GET'])
def get_all_persons():
    persons = Person.query.all()
    person_list = [{'id': person.id, 'name': person.name} for person in persons]
    return jsonify(person_list)

if __name__ == "__main__":
    app.run(debug=True)
