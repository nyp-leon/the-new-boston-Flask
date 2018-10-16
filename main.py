from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Home page'

@app.route('/cat')
def cat():
    return '<h1>Meow</h1>'

@app.route('/food/<food>')
def food(food):
    return "Go eat some %s" %food

@app.route('/prisoner/<int:id>')
def prisoner(id):
    return "You are prisoner %s" %id

if __name__ == "__main__":
    app.run(debug=True)