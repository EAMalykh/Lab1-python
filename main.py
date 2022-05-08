from flask import Flask, make_response, abort, redirect, render_template

app = Flask(__name__)
userslist = [{'name': 'Alex', 'id': 1, 'surname': 'Turner', 'age': 33},
{'name': 'Thom', 'id': 2, 'surname': 'Yorke', 'age': 50},
{'name': 'Jane', 'id': 3, 'surname': 'Porter', 'age': 17}]

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def userdata():
    return render_template('templates.html', users = userslist)

@app.route('/error')
def error():
    abort(404)

@app.route('/home')
def home():
    return redirect('/')

@app.route('/user/<surname>')
def user(surname):
    for user in userslist:
        if surname == user['surname']:
            return render_template('template2.html', user = user)
    return error()

if __name__ == '__main__':
    app.run(debug=True)


