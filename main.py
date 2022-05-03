from flask import Flask, request, make_response, abort, redirect, render_template

app = Flask(__name__)
a = [{'name': 'Alex', 'id': 1, 'surname': 'Turner', 'age': 33},
{'name': 'Thom', 'id': 2, 'surname': 'Yorke', 'age': 50},
{'name': 'Jane', 'id': 3, 'surname': 'Porter', 'age': 17}]

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def userdata():
    surnid = ""
    for i in a:
        s = i['surname']
        e = i['id']
        surnid += f'<h1><a href = "/user/{s}"> {e}. {s} </a></h1><hr style="border: 1px solid pink;">'
    return surnid

@app.route('/error')
def error():
    abort(404)

@app.route('/home')
def home():
    return redirect('/')

@app.route('/user/<surname>')
def user(surname):
    for i in a:
        if surname == i['surname']:
            response = make_response('<h1>Hello, %s</h1>'% i['name'])
            return response
    return error()

if __name__ == '__main__':
    app.run(debug=True)


