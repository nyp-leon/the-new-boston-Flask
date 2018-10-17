from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template("user.html", user=user)

@app.route('/cat')
def cat():
    return '<h1>Meow</h1>'

@app.route('/food/<food>')
def food(food):
    return "Go eat some %s" %food

@app.route('/prisoner/<int:id>')
def prisoner(id):
    return "You are prisoner %s" %id

@app.route('/get')
def get():
    return "Method used: %s" % request.method

@app.route("/bacon", methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "u are using post"
    else:
        return "probably a get"

@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)