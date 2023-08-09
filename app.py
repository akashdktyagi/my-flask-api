from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

app.config['DEBUG'] = True

# Create some data
# This is a list of dictionaries
# Each dictionary represents a single todo item
books = [
    { 'id': 0,
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'published': '1992'
    },
    { 'id': 1,
        'title': 'The Ones Who Walk Away From Omelas',
        'author': 'Ursula K. Le Guin',
        'published': '1973'
    },
    { 'id': 2,
        'title': 'Dhalgren',
        'author': 'Samuel R. Delany',
        'published': '1975'
    }
]

# this route will return the welcome page
@app.route('/')
def index():
    return render_template('index.html')

# This route will return all of the data
@app.route('/books', methods=['GET'])
def returnAll():
    return jsonify({'books': books})

# This route will return a single item
@app.route('/books/<int:id>', methods=['GET'])
def returnOne(id):
    return jsonify({'book': books[id]})

# This route will create a new item
@app.route('/books',methods=['POST'])
def addOne():
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author'],
        'published': request.json['published']
    }
    books.append(book)
    return jsonify({'books': books})

# This route will update an existing item
@app.route('/books/<int:id>', methods=['PUT'])
def editOne(id):
    book = books[id]
    book['title'] = request.json['title']
    book['author'] = request.json['author']
    book['published'] = request.json['published']
    return jsonify({'book': book})

# This route will delete an item
@app.route('/books/<int:id>', methods=['DELETE'])
def deleteOne(id):
    books.remove(books[id])
    return jsonify({'books': books})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)