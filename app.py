from flask import Flask, render_template

app = Flask(__name__)

# Define routes for each HTML file
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/groups/')
def groups():
    return render_template('groups.html')

@app.route('/error/')
def error():
    return render_template('error.html')

@app.route('/success/')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(host ='0.0.0.0', debug=True )
