import unittest
from flask import json
from app import app, db, Person

class APITestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use a test database
        self.app = app.test_client()
        with app.app_context():
            db.create_all()
        
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_person(self):
        data = {'name': 'John Doe'}
        response = self.app.post('/api/', json=data)
        self.assertEqual(response.status_code, 201)

    def test_create_person_by_name(self):
        name = 'Dave'
        data = {'name': name}
        response = self.app.post(f'/api/{name}', json=data)
        self.assertEqual(response.status_code, 201)

    def test_get_person(self):
        with app.app_context():
            person = Person(name='James')
            
            db.session.add(person)
            db.session.commit()

            response = self.app.get(f'/api/{person.id}')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(data['id'], person.id)

    def test_get_person_by_name(self):
        name = 'John Doe'
        person = Person(name=name)
        with app.app_context():
            db.session.add(person)
            db.session.commit()

            response = self.app.get(f'/api/{name}')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(data['name'], name)

    def test_update_person(self):
        with app.app_context():
            person = Person(name='Joe')
            db.session.add(person)
            db.session.commit()

            new_name = 'Jane'
            data = {'name': new_name}
            response = self.app.put(f'/api/{person.id}', json=data)
            self.assertEqual(response.status_code, 200)

    def test_update_person_by_name(self):
        name = 'John Doe'
        person = Person(name=name)
        with app.app_context():
            db.session.add(person)
            db.session.commit()

            new_name = 'Jane Doe'
            data = {'new_name': new_name}
            response = self.app.put(f'/api/{name}', json=data)
            self.assertEqual(response.status_code, 200)

    def test_delete_person(self):
        person = Person(name='Jerry')
        with app.app_context():
            db.session.add(person)
            db.session.commit()

            response = self.app.delete(f'/api/{person.id}')
            self.assertEqual(response.status_code, 200)

    def test_delete_person_by_name(self):
        name = 'John Doe'
        person = Person(name=name)
        with app.app_context():
            db.session.add(person)
            db.session.commit()

            response = self.app.delete(f'/api/{name}')
            self.assertEqual(response.status_code, 200)

    def test_get_all_persons(self):
        person1 = Person(name='John Doe')
        person2 = Person(name='Jane Smith')
        with app.app_context():
            db.session.add(person1)
            db.session.add(person2)
            db.session.commit()

            response = self.app.get('/api/persons')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode('utf-8'))
            self.assertEqual(len(data), 2)

if __name__ == '__main__':
    unittest.main()
