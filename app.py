from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'name': 'John',
        'phone': '555-555-5555',
        'id': 1
    },
    {
        'name': 'Mary',
        'phone': '555-555-5556',
        'id': 2
    },
    {
        'name': 'Bob',
        'phone': '555-555-5557',
        'id': 3
    },
    {
        'name': 'Mike',
        'phone': '555-555-5558',
        'id': 4
    }
]

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify({'contacts': contacts})

@app.route('/contacts/<int:id>', methods=['GET'])
def get_contact_by_id(id):
    contact = [contact for contact in contacts if contact['id'] == id]
    return jsonify({'contact': contact[0]})

@app.route('/contacts', methods=['POST'])
def add_contact():
    contact = {
        'name': request.json['name'],
        'phone': request.json['phone'],
        'id': len(contacts) + 1
    }
    contacts.append(contact)
    return jsonify({'contact': contact})

    if not request.json or not 'name' in request.json:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True)
