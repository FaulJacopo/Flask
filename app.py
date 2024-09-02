from flask import Flask

app = Flask(__name__)

@app.route('/<username>')
def home(username):
    return f'Hello, {username}'

if __name__ == '__main__':
    app.run(debug=True)