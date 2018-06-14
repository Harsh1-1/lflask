from flask import Flask, request, render_template

app = Flask(__name__)

# @ signifies a decorator - way to wrao a function and modifying its behaviour
@app.route('/')   #This decorator is for mapping and routing, that is for mapping a path to a function
@app.route('/<user>')
def index(user=None):
    return render_template('user.html', user=user)

@app.route('/bacon',methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "Most likely you are using GET"

@app.route('/about')
def about():
    return "<h1>This is an about page </h1>"

@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name = name)

@app.route('/post/<int:post_id>')
def post(post_id):
    return "<h2> post id is %s</h2>" %post_id

@app.route('/shopping')
def shopping():
    food = ["cheese","burger","sandwich"]
    return render_template('shopping.html', food=food)



if __name__ == "__main__":
    app.run(debug=True)   #only run this app when this app is directly ran
