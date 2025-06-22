from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

users = []
services = []

@app.route('/')
def index():
    return render_template('index.html', users=users, services=services)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    users.append({'username': username, 'rating': 0})
    return redirect(url_for('index'))

@app.route('/add_service', methods=['POST'])
def add_service():
    service = {
        'user': request.form['username'],
        'description': request.form['description'],
        'price': request.form['price']
    }
    services.append(service)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
