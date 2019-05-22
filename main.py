"""
from flask import Flask
app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route('/') # decorator
def index():
    return 'This is the home page'

@app.route('/about') # decorator
def about():
    return '<h2>This is the about page</h2>'

@app.route('/profile/<username>') # decorator
def profile(username):
    return '<h3>Hey there %s</h3>' % username

@app.route('/post/<int:post_id>') # decorator
def show_post(post_id):
    return '<h4>Post ID is %s</h4>' % post_id

if __name__ == "__main__":
    app.run(debug=True)

#########

from flask import Flask, request
app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route('/') # decorator
def index():
    return 'Method used: %s' % request.method

@app.route('/about', methods=['GET', 'POST']) # decorator
def about():
    if request.method == 'POST':
        return 'You are using POST'
    else:
        return 'You are using GET'

if __name__ == "__main__":
    app.run(debug=True)

#########

from flask import Flask, render_template
app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route('/profile/<name>') # decorator
def profile(name):
    return render_template("profile.html", name=name)

if __name__ == "__main__":
    app.run()

"""

from flask import Flask, render_template
app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route('/') # decorator
@app.route('/<user>') # decorator
def profile(user=None):
    return render_template("user.html", user=user)

@app.route('/shopping') # decorator
def shopping():
    food = ["Butter", "Curd", "Sweets"]
    return render_template("shopping.html", food=food)

if __name__ == "__main__":
    app.run()

